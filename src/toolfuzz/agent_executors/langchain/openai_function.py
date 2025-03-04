from langchain import hub
from langchain.agents import create_openai_functions_agent, AgentExecutor

from src.toolfuzz.agent_executors.langchain.react_old import ReactAgentOld


class OpenAIFuncFactory:
    @classmethod
    def create(cls, tool, model):
        try:
            agent = create_openai_functions_agent(model, [tool], hub.pull("hwchase17/openai-tools-agent"))
            agent = AgentExecutor(agent=agent, tools=[tool], verbose=True, return_intermediate_steps=True)
            agent.invoke({'input': "Can you call the available to you tool with random parameters?"})
            return agent
        except:
            return None


class OpenAiFunctionExecutor(ReactAgentOld):
    def __init__(self, tool, model):
        super().__init__(tool, model, OpenAIFuncFactory)
