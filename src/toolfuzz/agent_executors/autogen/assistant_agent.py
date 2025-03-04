import ast
import asyncio
import json
from json import JSONDecodeError
from typing import Dict, List

from src.toolfuzz.agent_executors.agent_executor import TestingAgentExecutor, AgentResponse


class AssistantAgentExecutor(TestingAgentExecutor):
    def _import_environment(self):
        try:
            from autogen_agentchat.agents import AssistantAgent
            from autogen_agentchat.messages import ToolCallExecutionEvent, ToolCallRequestEvent, TextMessage
            from autogen_core import FunctionCall
            from autogen_core.models import FunctionExecutionResult
        except ImportError as e:
            raise ImportError(
                f"The autogen package is not installed. Please install it using 'pip install -U 'autogen-agentchat'. {e}")

    def __init__(self, tool, model, **kwargs):
        super().__init__(tool, model)

        from autogen_agentchat.agents import AssistantAgent
        self.agent = AssistantAgent(name='AssistantAgent',
                                    model_client=model,
                                    tools=[tool],
                                    system_message='You are a helpful AI assistant.',
                                    reflect_on_tool_use=True,
                                    **kwargs)

    def __call__(self, prompt: str, *args, **kwargs) -> AgentResponse:
        from autogen_agentchat.messages import ToolCallExecutionEvent

        agent_response = asyncio.run(self.agent.run(task=prompt))
        tool_output = self.get_tool_output(agent_response.messages)
        args = self.get_tool_arguments(agent_response.messages)

        trace = self.get_trace(agent_response.messages)
        is_raised_exception, exception = self.extract_error(agent_response.messages)
        agent_answer = agent_response.messages[-1].content
        is_tool_invoked = any([isinstance(msg, ToolCallExecutionEvent) for msg in agent_response.messages])
        return AgentResponse(agent_response=agent_answer, trace=trace, is_tool_invoked=is_tool_invoked,
                             is_raised_exception=is_raised_exception, exception=exception, tool_output=tool_output,
                             tool_args=args)

    def extract_error(self, agent_result):
        from autogen_agentchat.messages import ToolCallExecutionEvent, FunctionExecutionResult

        for message in reversed(agent_result):
            if isinstance(message, ToolCallExecutionEvent):
                for item in message.content:
                    if isinstance(item, FunctionExecutionResult):
                        try:
                            result = json.loads(item.content)
                            if not result['successful']:
                                return True, result['error']
                        except JSONDecodeError:
                            try:
                                result = ast.literal_eval(item.content)
                                if not result['successful']:
                                    return True, result['error']
                            except Exception:
                                pass
                        # In this case we cannot extract the exception itself.
                        if item.is_error:
                            return True, item.content
        return False, None

    def get_tool_output(self, agent_result):
        from autogen_agentchat.messages import ToolCallExecutionEvent, FunctionExecutionResult

        tool_outs = []
        for message in reversed(agent_result):
            if isinstance(message, ToolCallExecutionEvent):
                for item in message.content:
                    if isinstance(item, FunctionExecutionResult):
                        tool_outs.append(item.content)
        if len(tool_outs) > 0:
            return "\n".join(tool_outs)
        return "No tool output found"

    def get_tool_arguments(self, trace) -> str:
        from autogen_agentchat.messages import ToolCallRequestEvent, FunctionCall

        for message in reversed(trace):
            if isinstance(message, ToolCallRequestEvent):
                for item in message.content:
                    if isinstance(item, FunctionCall):
                        return item.arguments
        return "No tool invocation found"

    def get_trace(self, agent_result) -> List[Dict]:
        from autogen_agentchat.messages import ToolCallRequestEvent, TextMessage, ToolCallExecutionEvent, FunctionCall, \
            FunctionExecutionResult

        trace = []
        for message in agent_result:
            if isinstance(message, TextMessage):
                trace.append({'role': message.source, 'content': message.content})
            elif isinstance(message, ToolCallRequestEvent):
                tool_calls = []
                for tool_call in message.content:
                    if isinstance(tool_call, FunctionCall):
                        tool_calls.append({'id': tool_call.id,
                                           "type": "function",
                                           "function": {"name": tool_call.name,
                                                        "arguments": tool_call.arguments}})
                trace.append({'role': 'assistant', "content": '', "tool_calls": tool_calls})
            elif isinstance(message, ToolCallExecutionEvent):
                for item in message.content:
                    if isinstance(item, FunctionExecutionResult):
                        trace.append({"role": "tool", "tool_call_id": item.call_id, "content": item.content})
        return trace

    def heartbeat(self) -> bool:
        return True

    def get_name(self) -> str:
        return "AssistantAgentExecutor"
