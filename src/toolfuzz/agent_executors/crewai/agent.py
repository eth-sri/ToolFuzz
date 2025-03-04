import ast
from typing import List

from src.toolfuzz.agent_executors.agent_executor import TestingAgentExecutor, AgentResponse


class CrewAIAgent(TestingAgentExecutor):

    def _import_environment(self):
        try:
            from crewai import Agent, Task, Crew, Process
            from crewai.agents.crew_agent_executor import ToolResult
            from crewai.agents.parser import AgentAction, AgentFinish
        except ImportError as e:
            raise ImportError(
                f"The crewai package is not installed. Please install it using \"pip install -U 'crewai'\". {e}")

    def __init__(self, tool, model, **kwargs):
        super().__init__(tool, model)

        from crewai import Agent

        self.agent = Agent(
            role='Conversational Assistant',
            llm=model,
            goal=f'Based on the context provided, answer using the tools available to you',
            backstory='You are a knowledgeable AI assistant, skilled in answering user queries based on your tools.',
            verbose=True,
            allow_delegation=False,
            tools=[tool],
            step_callback=self.steps_collector,
            **kwargs
        )
        self.steps = []

    def steps_collector(self, info):
        self.steps.append(info)

    def heartbeat(self) -> bool:
        return True

    def __call__(self, prompt: str, *args, **kwargs) -> AgentResponse:
        from crewai import Task, Crew, Process
        from crewai.agents.parser import AgentAction

        self.steps = []
        task = Task(description=prompt, tools=[self.tool], agent=self.agent,
                    expected_output="A clear and informative response to the user's question.")
        crew = Crew(agents=[self.agent], tasks=[task], process=Process.sequential)
        result = crew.kickoff()
        tool_output = self.get_tool_output(result)
        trace = self.get_trace(prompt)
        args = self.get_tool_arguments(trace)
        is_raised_exception, exception = self.extract_correctness()
        is_tool_invoked = any([isinstance(item, AgentAction) for item in self.steps])
        return AgentResponse(agent_response=result.raw, trace=trace, is_tool_invoked=is_tool_invoked,
                             is_raised_exception=is_raised_exception, exception=exception, tool_output=tool_output,
                             tool_args=args)

    def extract_correctness(self):
        from crewai.agents.parser import AgentAction
        from crewai.agents.crew_agent_executor import ToolResult

        for item in reversed(self.steps):
            if isinstance(item, AgentAction):
                if 'encountered an error while trying to use the tool' in item.text:
                    return True, item.text.split("This was the error:")[1].split('\n')[0]
            elif isinstance(item, ToolResult):
                if 'encountered an error while trying to use the tool' in item.result:
                    return True, item.result.split("This was the error:")[1].split('\n')[0]
                try:
                    # Composio tooling handling.
                    item_content = ast.literal_eval(item.result)
                    if isinstance(item_content, dict) and not item_content['successful']:
                        return True, item_content['error']
                except:
                    pass
        return False, None

    def get_name(self) -> str:
        return 'CrewAI_agent'

    def get_tool_output(self, agent_result) -> str:
        from crewai.agents.parser import AgentAction

        tool_outs = []

        for item in reversed(self.steps):
            if isinstance(item, AgentAction):
                tool_outs.append(item.result)
        if len(tool_outs) > 0:
            return "\n".join(tool_outs)
        return "No tool output found"

    def get_trace(self, prompt) -> List[dict]:
        from crewai.agents.parser import AgentAction, AgentFinish
        from crewai.agents.crew_agent_executor import ToolResult

        trace = [{'role': 'user', 'content': prompt}]
        for item in self.steps:
            if isinstance(item, ToolResult):
                trace.append({'role': 'assistant', 'content': item.result})
            elif isinstance(item, AgentFinish):
                trace.append({'role': 'assistant', 'content': item.text})
            elif isinstance(item, AgentAction):
                trace.append({'id': '',
                              "type": "function",
                              "function": {"name": item.tool,
                                           "arguments": item.tool_input}})
                trace.append({'role': 'tool', "tool_call_id": '', 'content': item.result})
        return trace

    def get_tool_arguments(self, trace) -> str:
        from crewai.agents.parser import AgentAction

        for item in reversed(self.steps):
            if isinstance(item, AgentAction):
                return item.tool_input

        return "No tool output found"
