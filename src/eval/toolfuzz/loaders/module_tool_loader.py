import importlib
import inspect
import pkgutil

from langchain_community.tools import BaseTool
from langchain_core.tools import StructuredTool


class ToolLoader:
    def __init__(self, package):
        self.tools_package_location = package
        self.tools = self.load_tools()

    def load_tools(self):
        langchain_tools_pkg = importlib.import_module(self.tools_package_location)

        available_tools = []

        for importer, modname, ispkg in pkgutil.iter_modules(langchain_tools_pkg.__path__):
            module_name = f'{self.tools_package_location}.{modname}'

            # Import:
            module = importlib.import_module(module_name)
            for name, obj in inspect.getmembers(module):
                if type(obj) is StructuredTool:
                    available_tools.append(obj)
                elif (inspect.isclass(obj) and obj.__module__.startswith(module_name) and self.inherits_base_tool(obj)):
                    available_tools.append(obj())

        return available_tools

    def inherits_base_tool(self, class_obj):
        if len(class_obj.__bases__) == 0:
            return False
        for base_class in class_obj.__bases__:
            if base_class == BaseTool:
                return True
            if self.inherits_base_tool(base_class):
                return True
        return False

    def map_to_parameterized_test_input(self):
        assert len(self.tools) != 0
        parameterized_tools = []
        for tool in self.tools:
            if inspect.isclass(tool):
                tool = tool()
            if 'valid_prompt' in tool.__dict__:
                for valid_prompt in tool.valid_prompt:
                    parameterized_tools.append(
                        (f"{tool.name}_valid", tool, valid_prompt.prompt, valid_prompt.assert_lambda))
            if 'breaking_prompt' in tool.__dict__:
                for breaking_prompt in tool.breaking_prompt:
                    parameterized_tools.append(
                        (f"{tool.name}_breaking", tool, breaking_prompt.prompt, breaking_prompt.assert_lambda))
        return parameterized_tools
