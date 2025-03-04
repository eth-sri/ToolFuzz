import json

from src.toolfuzz.agent_executors.llama_index.openai_agent import OpenAIAgentExecutor
from src.toolfuzz.correctness.correctness_fuzzer import CorrectnessTester
from src.toolfuzz.runtime.runtime_fuzzer import RuntimeErrorTester


def get_weather(location: str) -> str:
    """Useful for getting the weather for a given location."""
    loc = json.loads(location)
    assert 'name' in loc
    place = loc['name']
    return f"The weather in {place} is sunny"


def example_runtime_failure_fuzzing():
    from llama_index.llms.openai import OpenAI
    from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec

    llm = OpenAI('gpt-4o-mini')
    tool = DuckDuckGoSearchToolSpec().to_tool_list()[0]
    agent = OpenAIAgentExecutor(tool, llm)

    tester = RuntimeErrorTester(llm=llm,
                                tool=tool,
                                agent=agent,
                                fuzzer_iters=50)
    tester.test()
    tester.save('llamaindex_runtime_results')


### Example of correctness usage:
def example_correctness_usage():
    from llama_index.core.tools import FunctionTool
    from llama_index.llms.openai import OpenAI

    llm = OpenAI('gpt-4o-mini')
    tool = FunctionTool.from_defaults(get_weather)
    agent = OpenAIAgentExecutor(tool, llm)

    tester = CorrectnessTester(llm=llm,
                               tool=tool,
                               agent=agent,
                               additional_context='')
    tester.test()
    tester.save('llamaindex_correctness_results')


if __name__ == '__main__':
    example_runtime_failure_fuzzing()
    example_correctness_usage()
