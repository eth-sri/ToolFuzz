import inspect

from src.toolfuzz.logging_mixin import LoggingMixin
from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument, ArgumentType
from src.toolfuzz.tools.info_extractors.tool_wrapper import ToolWrapper


class LLamaIndexToolWrapper(ToolWrapper, LoggingMixin):
    def _import_environment(self):
        # No need to import anything for LLamaIndexToolWrapper
        pass

    def __init__(self, tool):
        LoggingMixin.__init__(self)
        ToolWrapper.__init__(self, tool)

    def invoke_tool(self, kwargs):
        result = self.tool.call(**kwargs)
        if isinstance(result, dict) and 'successful' in result.raw_input and not result.raw_input['successful']:
            # Handling composio tools
            raise Exception(result.raw_input['error'])
        return result

    def get_tool_args(self):
        tool_args = []
        schema = self.tool.metadata.fn_schema.schema()
        for argument, arg_info in schema['properties'].items():
            if 'kwargs' in argument.lower() and 'type' not in arg_info.keys():
                self.log_info('Generating KWARGS with no type is not supported.')
                continue
            tool_args.append(ToolArgument(
                name=argument,
                type=self._extract_type(arg_info),
                default=arg_info.get('default', None),
                has_default='default' in arg_info,
                description=arg_info.get('description', None)
            ))
        if len(tool_args) == 0 and 'fn' in dir(self.tool):
            schema = inspect.signature(self.tool.fn).parameters
            for argument, arg_info in schema.items():
                if arg_info.kind in [inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD]:
                    continue
                tool_args.append(ToolArgument(
                    name=argument,
                    type=self.__transform_type(arg_info.annotation),
                    default=arg_info.default if arg_info.default != inspect.Parameter.empty else None,
                    has_default=arg_info.default != inspect.Parameter.empty,
                    description=self.__get_annotation_doc(arg_info.annotation)
                ))
        return tool_args

    @staticmethod
    def __get_annotation_doc(annotation):
        if annotation.__doc__ in [str.__doc__, int.__doc__, dict.__doc__, list.__doc__, bool.__doc__]:
            # Explicit handling for basic types
            return None

        return annotation.__doc__

    def get_tool_src(self):
        if 'fn' in dir(self.tool):
            return inspect.getsource(self.tool.fn)
        raise NotImplementedError("Only FunctionTool is supported for now")

    def get_tool_docs(self):
        docs = self.tool.metadata.description
        format = "Tool Name: {name}\nTool Arguments: {args}\nTool Description: {desc}"
        # Do this so that we avoid __repr__ being called and use the __str__ method
        args = [str(arg) for arg in self.get_tool_args()]
        args = "[" + ", ".join(args) + "]"
        return format.format(name=self.get_tool_name(), args=args, desc=docs)

    def get_tool_name(self):
        return self.tool.metadata.name

    def get_tool_declaration_name(self):
        if 'fn' in dir(self.tool):
            return self.tool.fn.__name__
        if 'fn_schema' in dir(self.tool.metadata):
            return self.tool.metadata.fn_schema.__name__

    @staticmethod
    def __transform_type(annotation):
        if hasattr(annotation, '__origin__') and annotation.__origin__ == list:
            return ArgumentType(name='array', sub_types=[ArgumentType(name=annotation.__args__[0].__name__)],
                                has_subtype=True)
        elif hasattr(annotation, '__origin__') and annotation.__origin__ == dict:
            return ArgumentType(name='object', sub_types=[ArgumentType(name='str'),
                                                          ArgumentType(name=annotation.__args__[1].__name__)],
                                has_subtype=True)
        return ArgumentType(name=str(annotation))

    def _extract_type(self, arg_info):
        if type(arg_info) == dict and len(arg_info) == 0:
            # Any types so we can't infer the type - default is string
            return ArgumentType(name='string')
        if 'type' in arg_info:
            # This is a KWARG type, check the WikiPedia tool for reference
            if arg_info['type'] == 'object':
                return ArgumentType(name='dict', sub_types=[ArgumentType(name='str'), ArgumentType(name='str')],
                                    has_subtype=True)
            elif arg_info['type'] != 'array':
                return ArgumentType(name=arg_info['type'])
            else:
                return ArgumentType(name=arg_info['type'], sub_types=[self._extract_type(arg_info['items'])],
                                    has_subtype=True)
        elif 'anyOf' in arg_info:
            subtypes = []
            for item in arg_info['anyOf']:
                subtypes.append(self._extract_type(item))
            return ArgumentType(name='Union', sub_types=subtypes, has_subtype=True)
        elif 'default' in arg_info:
            return ArgumentType(name=type(arg_info['default']).__name__)
        raise ValueError(f"Couldn't parse argument type for {arg_info}")
