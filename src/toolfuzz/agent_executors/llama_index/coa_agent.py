from src.toolfuzz.agent_executors.llama_index.llama_index_agent import LlamaIndexAgent


class ChainOfAbstractionAgentExecutor(LlamaIndexAgent):
    def _import_environment(self):
        try:
            from llama_index.agent.coa import CoAAgentWorker
        except ImportError as e:
            raise ImportError(
                f"The llama_index.agent.coa package is not installed. Please install it using 'pip install llama-index-agent-coa'. {e}")

    def __init__(self, tool, model, **kwargs):
        from llama_index.agent.coa import CoAAgentWorker

        agent = CoAAgentWorker.from_tools([tool], llm=model, verbose=True, **kwargs)
        agent = agent.as_agent()
        super().__init__(agent, tool, model)

    def heartbeat(self) -> bool:
        return True

    def get_name(self) -> str:
        return 'llama_index_coa_agent'
