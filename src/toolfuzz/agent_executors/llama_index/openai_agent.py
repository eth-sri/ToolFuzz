from src.toolfuzz.agent_executors.llama_index.llama_index_agent import LlamaIndexAgent


class OpenAIAgentExecutor(LlamaIndexAgent):

    def _import_environment(self):
        try:
            from llama_index.agent.openai import OpenAIAgent
        except ImportError as e:
            raise ImportError(
                f"The llama_index package is not installed. Please install it using 'pip install -U 'llama_index'. {e}")

    def __init__(self, tool, model, **kwargs):
        from llama_index.agent.openai import OpenAIAgent
        super().__init__(OpenAIAgent.from_tools([tool], llm=model, verbose=True, **kwargs), tool, model)

    def get_name(self) -> str:
        return 'llama_index_openai_agent'

    def heartbeat(self) -> bool:
        return self.agent is not None
