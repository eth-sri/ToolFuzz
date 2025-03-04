from abc import abstractmethod, ABC

from langchain_openai import ChatOpenAI

from src.toolfuzz.agent_executors.langchain.react_new import ReactAgentNew
from src.toolfuzz.agent_executors.langchain.react_old import ReactAgentOld


class LangChainToolLoader(ABC):
    @abstractmethod
    def get_tool(self): raise NotImplementedError()

    @abstractmethod
    def can_load(self, tool: str) -> bool: raise NotImplementedError()

    @abstractmethod
    def get_agent(self): raise NotImplementedError()


class ReactNewAgentLoader(LangChainToolLoader, ABC):
    def get_agent(self):
        TESTED_MODEL = ChatOpenAI(model='gpt-4o-mini', temperature=0)

        return ReactAgentNew(self.get_tool(), TESTED_MODEL)


class ReactOldAgentLoader(LangChainToolLoader, ABC):
    def get_agent(self):
        TESTED_MODEL = ChatOpenAI(model='gpt-4o-mini', temperature=0)
        return ReactAgentOld(self.get_tool(), TESTED_MODEL)
