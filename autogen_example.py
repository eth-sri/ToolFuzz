import random

from autogen_core.tools import FunctionTool
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.langchain import LangChainToolAdapter
from typing_extensions import Annotated

from src.eval.toolfuzz.loaders.langchain_tool_loaders import ShellToolLoader
from src.toolfuzz.agent_executors.autogen.assistant_agent import AssistantAgentExecutor
from src.toolfuzz.agent_executors.autogen.routed_agent import RoutedAgentExecutor
from src.toolfuzz.correctness.correctness_fuzzer import CorrectnessTester
from src.toolfuzz.runtime.runtime_fuzzer import RuntimeErrorTester


async def get_stock_price(ticker: str, date: Annotated[str, "Date in YYYY/MM/DD"]) -> float:
    # Returns a random stock price for demonstration purposes.
    return random.uniform(10, 200)


def example_fuzzing_test():
    llm = OpenAIChatCompletionClient(model='gpt-4o-mini')
    tool = LangChainToolAdapter(ShellToolLoader().get_tool())
    agent = AssistantAgentExecutor(tool, llm)
    tester = RuntimeErrorTester(llm=llm,
                                tool=tool,
                                agent=agent)
    tester.test()
    tester.save('autogen_runtime_results')


def example_correctness_test():
    llm = OpenAIChatCompletionClient(model='gpt-4o-mini')
    tool = FunctionTool(get_stock_price, description="Get stock price for a given ticker and date.")
    agent = RoutedAgentExecutor(tool, llm)
    tester = CorrectnessTester(llm=llm,
                               tool=tool,
                               agent=agent,
                               additional_context='')
    tester.test()
    tester.save('autogen_correctness_results')


if __name__ == "__main__":
    example_correctness_test()
    example_fuzzing_test()
