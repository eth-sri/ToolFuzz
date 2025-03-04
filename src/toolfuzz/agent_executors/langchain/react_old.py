import json
from typing import List

from src.toolfuzz.agent_executors.agent_executor import TestingAgentExecutor, AgentResponse


class ReactOldAgentFactory:

    @classmethod
    def create(cls, tools, model, **kwargs):
        from langchain.agents import AgentType, initialize_agent

        try:
            agent = initialize_agent(tools, model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,
                                     return_intermediate_steps=True, handle_parsing_errors=True, **kwargs)
            agent.invoke({'input': "Can you call the available to you tool with random parameters?"})
            return agent
        except:
            return None


class ReactAgentOld(TestingAgentExecutor):
    """"
    This class is a wrapper for the langchain-core agent that uses the old version of the ReactAgent. However, it is out of date and should be replaced with the new version.
    Left just in case someone is still using it, otherwise you are better off with the new version. ReactAgentNew.
    """

    def _import_environment(self):
        try:
            from langchain.agents import AgentType, initialize_agent
            from langchain_core.agents import AgentAction
        except ImportError:
            raise ImportError(
                "Please install langchain-core and langgraph packages to use this agent executor: 'pip install langchain', 'pip install langchain-core' and 'pip install langgraph'")

    def __init__(self, tool, model, factory=ReactOldAgentFactory, **kwargs):
        super().__init__(tool, model)
        if not isinstance(tool, list):
            tool = [tool]
        self.agent = factory.create(tool, model, **kwargs)

    def __call__(self, prompt, *args, **kwargs):
        agent_results = self.agent.invoke({'input': prompt}, **kwargs)
        print(agent_results)
        agent_answer = agent_results['output']
        tool_outputs = self.get_tool_output(agent_results)
        trace = self.get_trace(agent_results)

        is_tool_invoked = any(['tool' in msg.values() for msg in trace])

        raised_exception, error = self.extract_error(trace)

        return AgentResponse(agent_response=agent_answer, trace=trace, is_tool_invoked=is_tool_invoked,
                             is_raised_exception=raised_exception, exception=error, tool_output=tool_outputs,
                             tool_args=self.get_tool_arguments(agent_results))

    def extract_error(self, trace):
        for item in trace:
            if item['role'] == 'tool':
                try:
                    content = json.loads(item['content'])
                    return content['error'] == None, content['error']
                except ValueError:
                    if 'Error: ' in item['content']:
                        return 'Error: ' in item['content'], item['content'].split('\n')[0].split('Error: ')[1]
        return False, ''

    def get_trace(self, trace) -> List[dict]:
        from langchain_core.agents import AgentAction

        transformed_trace = [{'role': 'user', 'content': trace["input"]}]
        for message in trace['intermediate_steps']:
            if isinstance(message, tuple):
                if isinstance(message[0], AgentAction):
                    transformed_trace.append({'role': 'system', 'content': message[0].log})
                    transformed_trace.append({'role': 'assistant',
                                              'content': None,
                                              "tool_calls": [
                                                  {'id': 1,
                                                   'type': 'function',
                                                   'function': {'name': message[0].tool,
                                                                'arguments': message[0].tool_input}}
                                              ]})
                if isinstance(message[1], str):
                    transformed_trace.append({'role': 'tool', 'id': 1, 'content': message[1]})
        transformed_trace.append(f'assistant({trace["output"]}, None)')
        return transformed_trace

    def get_tool_output(self, agent_results):
        from langchain_core.agents import AgentAction

        tool_outputs = []
        for action, output in reversed(agent_results['intermediate_steps']):
            if isinstance(action, AgentAction) and action.tool == self.tool.name:
                tool_outputs.append(output)
        if len(tool_outputs) > 0:
            return "\n".join(tool_outputs)
        return "No tool output found"

    def get_tool_arguments(self, trace):
        from langchain_core.agents import AgentAction

        for message in trace['intermediate_steps']:
            if isinstance(message, tuple):
                if isinstance(message[0], AgentAction):
                    return message[0].tool_input
        return None

    def heartbeat(self) -> bool:
        return self.agent is not None

    def get_name(self) -> str:
        return 'react_old'
