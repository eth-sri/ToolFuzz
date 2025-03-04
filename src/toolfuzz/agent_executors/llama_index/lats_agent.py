from src.toolfuzz.agent_executors.llama_index.llama_index_agent import LlamaIndexAgent


class LanguageAgentTreeSearchExecutor(LlamaIndexAgent):
    def _import_environment(self):
        try:
            from llama_index.packs.agents_lats import LATSPack
        except ImportError as e:
            raise ImportError(
                f"The llama_index.packs.agent_lats package is not installed. Please install it using 'pip install llama-index-packs-agents-lats'. {e}")

    def __init__(self, tool, model, **kwargs):
        from llama_index.packs.agents_lats import LATSPack

        agent = LATSPack([tool], llm=model, verbose=True, **kwargs)
        super().__init__(agent.agent, tool, model)

    def get_name(self) -> str:
        return 'llama_index_language_agent_tree_search'

    def heartbeat(self) -> bool:
        return True
