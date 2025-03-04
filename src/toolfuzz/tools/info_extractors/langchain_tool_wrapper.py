import inspect

from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument, ArgumentType
from src.toolfuzz.tools.info_extractors.tool_wrapper import ToolWrapper


class LangchainToolWrapper(ToolWrapper):

    def _import_environment(self):
        pass

    def invoke_tool(self, kwargs):
        if dir(self.tool).__contains__('invoke'):
            result = self.tool.invoke(kwargs)
        elif dir(self.tool).__contains__('run'):
            result = self.tool.run(**kwargs)
        else:
            raise AttributeError(f"Tool {self.tool} does not have an invoke or run method")
        if isinstance(result, dict) and not result['successful']:
            # Handling composio tools
            raise Exception(result['error'])
        return result

    def get_tool_args(self):
        tool_args = []
        if 'args_schema' in dir(self.tool) and self.tool.args_schema is not None:
            schema = self.tool.args_schema.schema()
            assert 'properties' in schema
            schema = schema['properties']
            for key, value in schema.items():
                tool_args.append(ToolArgument(name=key, type=self.__get_type(value), default=None, has_default=False,
                                              description=value.get('description', None)))
        elif 'func' in self.tool.__dict__:
            schema = inspect.signature(self.tool.func).parameters
            for _, value in schema.items():
                tool_args.append(
                    ToolArgument(name=value.name,
                                 type=ArgumentType(self.__type_to_str(str(value.annotation))),
                                 default=value.default if value.default != inspect._empty else None,
                                 description=self.__get_annotation_doc(value.annotation),
                                 has_default=value.default != inspect._empty))
        else:
            schema = inspect.signature(self.tool._run).parameters
            for _, value in schema.items():
                tool_args.append(
                    ToolArgument(name=value.name,
                                 type=ArgumentType(self.__type_to_str(value.annotation)),
                                 description=self.__get_annotation_doc(value.annotation),
                                 default=value.default if value.default != inspect._empty else None,
                                 has_default=value.default != inspect._empty))

        return tool_args

    @staticmethod
    def __get_annotation_doc(annotation):
        if annotation.__doc__ in [str.__doc__, int.__doc__, dict.__doc__, list.__doc__, bool.__doc__]:
            # Explicit handling for basic types
            return None

        return annotation.__doc__

    def get_tool_src(self):
        if 'source_code' in dir(self.tool):
            return self.tool.source_code
        if 'func' in dir(self.tool) and inspect.isfunction(self.tool.func):
            return inspect.getsource(self.tool.func)
        elif 'func' in dir(self.tool) and inspect.ismethod(self.tool.func):
            return inspect.getsource(type(self.tool.func.__self__))
        try:
            return inspect.getsource(self.tool)
        except:
            return inspect.getsource(type(self.tool))

    def get_tool_name(self):
        return self.tool.name

    def get_tool_declaration_name(self):
        if 'composio_crewai' in inspect.getmodule(self.tool).__name__:
            return self.tool.name
        if 'func' in dir(self.tool) and inspect.isfunction(self.tool.func):
            return self.tool.func.__name__
        elif 'func' in dir(self.tool) and inspect.ismethod(self.tool.func):
            return self.tool.func.__self__.__class__.__name__
        return self.tool.__class__.__name__

    def get_tool_docs(self):
        format = "Tool Name: {name}\nTool Arguments: {args}\nTool Description: {desc}"
        description = self.tool.description
        args = [str(arg) for arg in self.get_tool_args()]
        args = "[" + ", ".join(args) + "]"
        return format.format(name=self.get_tool_name(), args=args, desc=description)

    def __get_type(self, value):
        if type(value) == dict and len(value) == 0:
            # Any types so we can't infer the type - default is string
            return ArgumentType(name='string')
        if 'type' in value:
            if value['type'] == 'object':
                # Dict value is referred to object in schema
                return ArgumentType(name='dict')
            if value['type'] != 'array':
                # If the type is not array, we can return the type directly (it is not container type)
                return ArgumentType(name=value['type'])
            else:
                return ArgumentType(name=value['type'], sub_types=[self.__get_type(value['items'])], has_subtype=True)
        elif 'anyOf' in value:
            subtypes = []
            for item in value['anyOf']:
                subtypes.append(self.__get_type(item))
            return ArgumentType(name='Union', sub_types=subtypes, has_subtype=True)
        raise ValueError(f"Couldn't parse argument type for {value}")

    @staticmethod
    def __type_to_str(type_annotation):
        type_to_str = {
            str: 'string',
            int: 'int',
            dict: 'dict',
            list: 'array',
            bool: 'boolean'
        }
        if type_annotation in type_to_str:
            return type_to_str[type_annotation]
        return str(type_annotation)
