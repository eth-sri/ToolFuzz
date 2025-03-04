import abc
from typing import List

from src.toolfuzz.environment_import import EnvironmentImportMixin
from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument


class ToolWrapper(EnvironmentImportMixin):
    def __init__(self, tool):
        """
        Constructor of the ToolExtractor accepts the tool under test
        :param tool: the tool under test.
        """
        self._import_environment()
        self.tool = tool

    @abc.abstractmethod
    def get_tool_args(self) -> List[ToolArgument]:
        """
        Extracts the input arguments of the tool
        :return: List of ToolArgument, the input arguments of the tool
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_tool_src(self) -> str:
        """
        Extracts the source code of the tool
        :return: the source code of the tool under test
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_tool_docs(self) -> str:
        """
        Extracts the documentation of the tool. This is the documentation which is sent to the LLM Agent.
        :return: the documentation of the tool
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_tool_name(self) -> str:
        """
        Extracts the name of the tool. The name which is sent to the LLM agent.
        :return: the name of the tool
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_tool_declaration_name(self) -> str:
        """
        Extracts the declaration name of the tool. This is the name of the declared name of tool in the source code.
        :return: the declaration name of the tool
        """
        raise NotImplementedError

    @abc.abstractmethod
    def invoke_tool(self, kwargs):
        """
        Invokes the tool with the given arguments
        :param kwargs: the arguments to be passed to the tool
        :return: the output of the tool
        """
        raise NotImplementedError
