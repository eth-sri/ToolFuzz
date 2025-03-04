import asyncio
from dataclasses import dataclass
from typing import Any, List

from src.toolfuzz.agent_executors.agent_executor import TestingAgentExecutor, AgentResponse


@dataclass
class Message:
    content: str


class RoutedAgentExecutor(TestingAgentExecutor):

    def _import_environment(self):
        try:
            from autogen_core import (
                AgentId,
                RoutedAgent,
                SingleThreadedAgentRuntime,
                message_handler, FunctionCall,
            )
            from autogen_core.models import (SystemMessage, UserMessage, FunctionExecutionResult,
                                             FunctionExecutionResultMessage,
                                             AssistantMessage)
            from autogen_core.tool_agent import ToolAgent, tool_agent_caller_loop
        except ImportError as e:
            raise ImportError(
                f"The autogen package is not installed. Please install it using 'pip install -U 'autogen-core'. {e}")

    def __init__(self, tool, model):
        super().__init__(tool, model)
        from autogen_core import SingleThreadedAgentRuntime

        self.runtime = SingleThreadedAgentRuntime()
        self.tools = tool
        if not isinstance(tool, list):
            self.tools = [tool]
        asyncio.run(self.__register_agent(model))

    async def __register_agent(self, model):
        from autogen_core import AgentId, RoutedAgent, message_handler, MessageContext
        from autogen_core.tools import ToolSchema
        from autogen_core.models import SystemMessage, UserMessage, ChatCompletionClient, LLMMessage
        from autogen_core.tool_agent import ToolAgent, tool_agent_caller_loop

        class ToolUseAgent(RoutedAgent):
            def __init__(self, model_client: ChatCompletionClient, tool_schema: List[ToolSchema],
                         tool_agent_type: str) -> None:
                super().__init__("An agent with tools")
                self._system_messages: List[LLMMessage] = [SystemMessage(content="You are a helpful AI assistant.")]
                self._model_client = model_client
                self._tool_schema = tool_schema
                self._tool_agent_id = AgentId(tool_agent_type, self.id.key)

            @message_handler
            async def handle_user_message(self, message: Message, ctx: MessageContext) -> Any:
                # Create a session of messages.
                session: List[LLMMessage] = self._system_messages + [
                    UserMessage(content=message.content, source="user")]
                # Run the caller loop to handle tool calls.
                messages = await tool_agent_caller_loop(
                    self,
                    tool_agent_id=self._tool_agent_id,
                    model_client=self._model_client,
                    input_messages=session,
                    tool_schema=self._tool_schema,
                    cancellation_token=ctx.cancellation_token,
                )
                return messages

        await ToolAgent.register(self.runtime, "tool_executor_agent",
                                 lambda: ToolAgent("tool executor agent", self.tools))
        await ToolUseAgent.register(self.runtime, "tool_use_agent", lambda: ToolUseAgent(
            model,
            [tool.schema for tool in self.tools],
            "tool_executor_agent"
        ))
        self.runtime.start()
        self.tool_use_agent = AgentId("tool_use_agent", "default")

    def heartbeat(self) -> bool:
        return True

    def __call__(self, prompt, *args, **kwargs):
        from autogen_core.models import FunctionExecutionResultMessage

        user_message = Message(content=prompt)
        agent_response = asyncio.run(self.runtime.send_message(user_message, self.tool_use_agent))
        tool_output = self.get_tool_output(agent_response)
        args = self.get_tool_arguments(agent_response)

        trace = self.get_trace([user_message] + agent_response)
        is_raised_exception, exception = self.extract_error(trace)
        agent_answer = agent_response[-1].content
        is_tool_invoked = any([isinstance(msg, FunctionExecutionResultMessage) for msg in agent_response])

        return AgentResponse(agent_response=agent_answer, trace=trace, is_tool_invoked=is_tool_invoked,
                             is_raised_exception=is_raised_exception, exception=exception, tool_output=tool_output,
                             tool_args=args)

    def get_name(self) -> str:
        return "AutogenAgent"

    def get_tool_output(self, agent_result):
        from autogen_core.models import FunctionExecutionResult, FunctionExecutionResultMessage

        tool_outs = []

        for i in reversed(agent_result):
            if isinstance(i, FunctionExecutionResultMessage):
                for item in i.content:
                    if isinstance(item, FunctionExecutionResult):
                        tool_outs.append(item.content)
        if len(tool_outs) > 0:
            return "\n".join(tool_outs)
        return "No tool output found"

    def get_trace(self, agent_result):
        from autogen_core.models import AssistantMessage, FunctionExecutionResult, FunctionExecutionResultMessage
        from autogen_core import FunctionCall

        transformed_trace = []
        for item in agent_result:
            if isinstance(item, Message):
                transformed_trace.append({'role': 'user', 'content': item.content})
            elif isinstance(item, AssistantMessage):
                tool_calls = []
                if isinstance(item.content, str):
                    transformed_trace.append({'role': 'assistant', "content": item.content, "tool_calls": []})
                else:
                    for tool_call in item.content:
                        if isinstance(tool_call, FunctionCall):
                            tool_calls.append({'id': tool_call.id,
                                               "type": "function",
                                               "function": {"name": tool_call.name, "arguments": tool_call.arguments}})
                    transformed_trace.append({'role': 'assistant', "content": '', "tool_calls": tool_calls})
            elif isinstance(item, FunctionExecutionResultMessage):
                for citem in item.content:
                    if isinstance(item, FunctionExecutionResult):
                        transformed_trace.append(
                            {"role": "tool", "tool_call_id": citem.call_id, "content": item.content})
        return transformed_trace

    def extract_error(self, agent_trace):
        from autogen_core.models import FunctionExecutionResultMessage, FunctionExecutionResult

        for item in agent_trace:
            if isinstance(item, FunctionExecutionResultMessage):
                for citem in item.content:
                    if isinstance(citem, FunctionExecutionResult) and citem.error:
                        return True, citem.content.split('\n')[0].split('Error: ')[1]
        return False, ''

    def get_tool_arguments(self, trace):
        from autogen_core.models import AssistantMessage
        from autogen_core import FunctionCall

        for i in reversed(trace):
            if isinstance(i, AssistantMessage) and isinstance(i.content, list):
                for item in i.content:
                    if isinstance(item, FunctionCall):
                        return item.arguments
        return "No tool invocation found"
