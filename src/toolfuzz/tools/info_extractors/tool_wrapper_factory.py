import inspect

from src.toolfuzz.tools.info_extractors.autogen_tool_wrapper import AutogenToolWrapper
from src.toolfuzz.tools.info_extractors.crew_ai_tool_wrapper import CrewAIToolWrapper
from src.toolfuzz.tools.info_extractors.langchain_tool_wrapper import LangchainToolWrapper
from src.toolfuzz.tools.info_extractors.llama_index_tool_wrapper import LLamaIndexToolWrapper
from src.toolfuzz.tools.info_extractors.tool_wrapper import ToolWrapper


class ToolWrapperFactory:
    @classmethod
    def create_extractor(cls, tool) -> ToolWrapper:
        module = inspect.getmodule(tool).__name__
        if module.startswith('langchain') or module.startswith('composio_langchain'):
            return LangchainToolWrapper(tool)
        elif module.startswith('autogen') or module.startswith('composio_autogen'):
            return AutogenToolWrapper(tool)
        elif module.startswith('llama_index') or module.startswith('composio_llama'):
            return LLamaIndexToolWrapper(tool)
        elif module.startswith('crewai') or module.startswith('composio_crewai'):
            return CrewAIToolWrapper(tool)
        raise NotImplementedError(f"Tool extractor for module {module} is not implemented.")
