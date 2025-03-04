####################################################################################
# The idea of this file is to load and setup all the tools that are available in the
# langchain community, and then potentially test if they work or not :)
####################################################################################

import importlib
import inspect
import pkgutil

from langchain_community.tools import BaseTool


class ToolLoader:
    def __init__(self, tools_package_location: str):
        self.tools_package_location = tools_package_location

    def get_tools(self):
        langchain_tools_pkg = importlib.import_module(self.tools_package_location)

        available_tools = []

        for importer, modname, ispkg in pkgutil.iter_modules(langchain_tools_pkg.__path__):
            module_name = f'{self.tools_package_location}.{modname}'

            # Import:
            module = importlib.import_module(module_name)
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and obj.__module__.startswith(module_name) and self.inherits_base_tool(obj):
                    available_tools.append(obj)

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


def main():
    tool_loader = ToolLoader('langchain_community.tools')
    print(tool_loader.get_tools())


if __name__ == '__main__':
    main()
