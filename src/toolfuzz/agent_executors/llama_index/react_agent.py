from src.toolfuzz.agent_executors.llama_index.llama_index_agent import LlamaIndexAgent


class ReactAgentExecutor(LlamaIndexAgent):

    def _import_environment(self):
        try:
            from llama_index.core.agent import ReActAgent
        except ImportError as e:
            raise ImportError(
                f"The llama_index package is not installed. Please install it using 'pip install -U 'llama_index'. {e}")

    def __init__(self, tool, model, **kwargs):
        from llama_index.core.agent import ReActAgent
        super().__init__(ReActAgent.from_tools([tool], llm=model, verbose=True, **kwargs), tool, model)

    def heartbeat(self) -> bool:
        return True

    def get_name(self) -> str:
        return "llama_index_react_agent"
