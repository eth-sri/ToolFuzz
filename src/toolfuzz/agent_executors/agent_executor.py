from abc import abstractmethod
from dataclasses import dataclass
from typing import List

from src.toolfuzz.environment_import import EnvironmentImportMixin


@dataclass
class AgentResponse:
    agent_response: str
    trace: List[dict]
    is_tool_invoked: bool
    is_raised_exception: bool
    exception: str
    tool_output: str
    tool_args: str


class TestingAgentExecutor(EnvironmentImportMixin):
    def __init__(self, tool, model, **kwargs):
        """
        :param tool: The tool which will be used for the agent
        :param model: The models which will be used for the agent. Has to instance of the model not just name.
        :param kwargs: Additional KWARGS which will be passed to the agent construction.
        """
        self._import_environment()
        self.tool = tool
        self.model = model

    @abstractmethod
    def heartbeat(self) -> bool:
        """
        The method which checks if the agent is working properly with a test call.
        :return: True if the agent is initialized and works properly, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def __call__(self, prompt: str, *args, **kwargs) -> AgentResponse:
        """
        The method which executes the agent call.
        In langchain this is the .invoke() method.
        :param prompt: the prompt with which the agent is called.
        :param args: additional arguments for the agent invocation.
        :param kwargs: additional keyword arguments for the agent invocation.
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_name(self) -> str:
        """
        The name of the agent, it is used for identification in the fuzzing reports.
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_tool_output(self, agent_result) -> str:
        """
        Given the output of the __call__ method, this method should return the output of the tool.
        :param agent_result:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_trace(self, trace) -> List[dict]:
        """
        Given the output of the __call__ method, this method should return the trace of the agent.
        :param trace:
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def get_tool_arguments(self, trace) -> str:
        """
        Given the trace from the @get_trace method, this method should return the arguments of the tool call.
        :param trace:
        :return:
        """
        raise NotImplementedError
