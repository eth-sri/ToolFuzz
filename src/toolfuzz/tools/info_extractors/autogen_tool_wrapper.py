import asyncio
import inspect

from src.toolfuzz.logging_mixin import LoggingMixin
from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument, ArgumentType
from src.toolfuzz.tools.info_extractors.tool_wrapper import ToolWrapper


class AutogenToolWrapper(ToolWrapper, LoggingMixin):
    def _import_environment(self):
        try:
            from autogen_core.tools import FunctionTool, BaseTool
            from autogen_ext.tools.langchain import LangChainToolAdapter
        except ImportError as e:
            error_msg = f"The autogen package is not installed. Please install it using 'pip install -U 'autogen-agentchat' and 'pip install autogen-ext'. {e}"
            raise ImportError(error_msg)

    def invoke_tool(self, kwargs):
        from autogen_core import CancellationToken
        result = asyncio.run(self.tool.run_json(kwargs, CancellationToken()))
        if not result['successful']:
            raise Exception(result['error'])
        return result['data']

    def get_tool_args(self):
        tool_args = []
        for k, v in self.tool.schema.items():
            if k != 'parameters':
                continue
            if v['type'] != 'object':
                self.log_debug(f"Skipping non-object schema: {v}")
                continue
            for param_name, param_info in v['properties'].items():
                tool_args.append(ToolArgument(
                    name=param_name,
                    type=self.__get_type(param_info),
                    default=param_info.get('default', None),
                    has_default='default' in param_info,
                    description=param_info.get('description', None)
                ))
        return tool_args

    def get_tool_src(self):
        from autogen_core.tools import FunctionTool, BaseTool
        from autogen_ext.tools.langchain import LangChainToolAdapter

        if isinstance(self.tool, LangChainToolAdapter) and hasattr(self.tool, '_langchain_tool'):
            from src.toolfuzz.tools.info_extractors.langchain_tool_wrapper import LangchainToolWrapper
            return LangchainToolWrapper(self.tool._langchain_tool).get_tool_src()
        if isinstance(self.tool, FunctionTool):
            return inspect.getsource(self.tool._func)
        if isinstance(self.tool, BaseTool):
            # Last Chance to get the source code
            return inspect.getsource(type(self.tool))
        raise NotImplementedError("Only FunctionTool is supported for now")

    def get_tool_docs(self):
        format = "Tool Name: {name}\nTool Arguments: {args}\nTool Description: {desc}"
        args = [str(arg) for arg in self.get_tool_args()]
        args = "[" + ", ".join(args) + "]"
        return format.format(name=self.get_tool_name(), args=args, desc=self.tool.description)

    def get_tool_name(self):
        return self.tool.name

    def get_tool_declaration_name(self):
        from autogen_core.tools import FunctionTool, BaseTool
        from autogen_ext.tools.langchain import LangChainToolAdapter

        if isinstance(self.tool, LangChainToolAdapter) and hasattr(self.tool, '_langchain_tool'):
            from src.toolfuzz.tools.info_extractors.langchain_tool_wrapper import LangchainToolWrapper
            return LangchainToolWrapper(self.tool._langchain_tool).get_tool_declaration_name()

        if isinstance(self.tool, FunctionTool):
            return self.tool._func.__name__
        elif isinstance(self.tool, BaseTool):
            return self.tool.__class__.__name__
        raise NotImplementedError(
            f"{self.tool} type is not supported. Supported types are: FunctionTool, LangChainToolAdapter")

    def __get_type(self, arg_info):
        if type(arg_info) == dict and len(arg_info) == 0:
            # Any types so we can't infer the type - default is string
            return ArgumentType(name='string')
        if 'type' in arg_info and arg_info['type'] == 'array':
            return ArgumentType(name=arg_info['type'],
                                sub_types=[self.__get_type(arg_info['items'])],
                                has_subtype=True)
        if 'type' in arg_info:
            return ArgumentType(name=arg_info['type'])
        elif 'anyOf' in arg_info:
            subtypes = []
            for item in arg_info['anyOf']:
                subtypes.append(self.__get_type(item))
            return ArgumentType(name='Union', sub_types=subtypes, has_subtype=True)
        raise ValueError(f"Couldn't parse argument type for {arg_info}")
