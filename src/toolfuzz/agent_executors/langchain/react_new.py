import json

from src.eval.buggy_tools.open_street_map import open_street_map_search
from src.toolfuzz.agent_executors.agent_executor import TestingAgentExecutor, AgentResponse


class ReactAgentNew(TestingAgentExecutor):
    def _import_environment(self):
        try:
            from langchain_core.messages import HumanMessage, ToolMessage, AIMessage
            from langgraph.prebuilt import create_react_agent
        except ImportError:
            raise ImportError(
                "Please install langchain-core and langgraph packages to use this agent executor: 'pip install langchain', 'pip install langchain-core' and 'pip install langgraph'")

    def __init__(self, tool, model, **kwargs):
        super().__init__(tool, model)
        from langgraph.prebuilt import create_react_agent
        try:
            if not isinstance(tool, list):
                tool = [tool]
            self.agent = create_react_agent(model, tool, **kwargs)
        except:
            self.agent = None

    def __call__(self, prompt, *args, **kwargs):
        from langchain_core.messages import HumanMessage

        agent_result = self.agent.invoke({'messages': [HumanMessage(content=prompt)]}, **kwargs)
        agent_answer = agent_result['messages'][-1].content
        tool_output = self.get_tool_output(agent_result)
        trace = self.get_trace(agent_result)

        is_tool_invoked = any(['tool' in msg.values() for msg in trace])
        runtime_failure, error = self.extract_error(trace)

        return AgentResponse(agent_response=agent_answer, trace=trace, is_tool_invoked=is_tool_invoked,
                             is_raised_exception=runtime_failure, exception=error, tool_output=tool_output,
                             tool_args=self.get_tool_arguments(agent_result))

    def extract_error(self, trace):
        for item in trace:
            if item['role'] == 'tool':
                try:
                    content = json.loads(item['content'])
                    error = content['error']
                    return error is not None, '' if not error else error
                except ValueError:
                    if 'Error: ' in item['content']:
                        return 'Error: ' in item['content'], item['content'].split('\n')[0].split('Error: ')[1]
        return False, ''

    def heartbeat(self) -> bool:
        try:
            if self.agent is not None:
                self(f"Please come up with parameters for a test run and do a test call to: {self.tool.name}")
                return True
        except:
            return False
        return False

    def get_tool_output(self, agent_result):
        from langchain_core.messages import ToolMessage

        messages = agent_result['messages'].copy()
        messages.reverse()
        tool_messages = []
        for message in messages:
            if isinstance(message, ToolMessage):
                tool_messages.append(message.content)
        if len(tool_messages) > 0:
            return "\n".join(tool_messages)
        return "No tool output found"

    def get_trace(self, trace):
        from langchain_core.messages import HumanMessage, ToolMessage, AIMessage

        transformed_trace = []
        for item in trace['messages']:
            if isinstance(item, HumanMessage):
                transformed_trace.append({'role': 'user', 'content': item.content})
            if isinstance(item, AIMessage):
                tool_calls = []
                if 'tool_calls' in item.additional_kwargs:
                    tool_call = item.additional_kwargs['tool_calls'][0]  # We have only one function
                    tool_calls.append({'id': 1,
                                       "type": "function",
                                       "function": {"name": tool_call["function"]["name"],
                                                    "arguments": tool_call["function"]["arguments"]
                                                    }})
                transformed_trace.append({'role': 'assistant', "content": item.content, "tool_calls": tool_calls})
            if isinstance(item, ToolMessage):
                transformed_trace.append({"role": "tool", "tool_call_id": 1, "content": item.content})

        return transformed_trace

    def get_tool_arguments(self, trace):
        from langchain_core.messages import AIMessage

        for item in trace['messages']:
            if isinstance(item, AIMessage):
                if 'tool_calls' in item.additional_kwargs:
                    tool_call = item.additional_kwargs['tool_calls'][0]  # We have only one function
                    return tool_call["function"]["arguments"]
        return None

    def get_name(self) -> str:
        return 'react_new'
