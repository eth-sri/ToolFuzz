from abc import ABC
from typing import List

from llama_index.core.tools import ToolOutput

from src.toolfuzz.agent_executors.agent_executor import TestingAgentExecutor, AgentResponse


class LlamaIndexAgent(TestingAgentExecutor, ABC):

    def __init__(self, agent, tool, model):
        super().__init__(tool, model)
        self.agent = agent

    def extract_error(self, agent_trace):
        for item in agent_trace.sources:
            if isinstance(item, ToolOutput):
                if isinstance(item.raw_output, BaseException):
                    return True, item.raw_output
                if isinstance(item.raw_output, dict) and (not item.raw_output['successful']):
                    # composio handling.
                    return True, item.raw_output['error']
        return False, ''

    def __call__(self, prompt: str, *args, **kwargs) -> AgentResponse:
        agent_result = self.agent.chat(prompt, **kwargs)
        tool_out = self.get_tool_output(agent_result)
        args = self.get_tool_arguments(agent_result)
        trace = self.get_trace((prompt, agent_result))
        is_tool_invoked = any([isinstance(msg, ToolOutput) for msg in agent_result.sources])
        is_raised_exception, exception = self.extract_error(agent_result)

        return AgentResponse(
            agent_response=agent_result.response,
            trace=trace,
            is_tool_invoked=is_tool_invoked,
            is_raised_exception=is_raised_exception,
            exception=exception,
            tool_output=tool_out,
            tool_args=args,
        )

    def get_tool_output(self, agent_result) -> str:
        tool_outs = []
        for source in agent_result.sources:
            if isinstance(source, ToolOutput):
                tool_outs.append(str(source.raw_output))
        if len(tool_outs) > 0:
            return "\n".join(tool_outs)
        return "No tool output found"

    def get_trace(self, trace) -> List[dict]:
        prompt, agent_result = trace
        transformed_trace = [{'role': 'user', 'content': prompt}]
        for source in agent_result.sources:
            if isinstance(source, ToolOutput):
                transformed_trace.append({
                    'role': 'function',
                    'id': '',
                    'function': {'name': source.tool_name, 'arguments': str(source.raw_input)},
                })
                transformed_trace.append({
                    'role': 'tool',
                    'tool_call_id': '',
                    'content': str(source.raw_output),
                })

        transformed_trace.append({'role': 'assistant', 'content': agent_result.response, 'tool_calls': []})
        return transformed_trace

    def get_tool_arguments(self, agent_result) -> str:
        for source in agent_result.sources:
            if isinstance(source, ToolOutput):
                return str(source.raw_input)
        return "No tool invocation found"
