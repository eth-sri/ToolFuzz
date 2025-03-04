from src.toolfuzz.agent_executors.langchain.react_new import ReactAgentNew
from src.toolfuzz.correctness.correctness_fuzzer import CorrectnessTester
from src.toolfuzz.runtime.runtime_fuzzer import RuntimeErrorTester


def example_runtime_failure_fuzzing():
    from composio_langchain import ComposioToolSet, App
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model='gpt-4o-mini')

    composio_toolset = ComposioToolSet()
    tools = composio_toolset.get_tools(apps=[App.SHELLTOOL])
    tool = tools[0]
    agent = ReactAgentNew(tool, llm)

    tester = RuntimeErrorTester(llm=llm,
                                tool=tool,
                                agent=agent,
                                fuzzer_iters=50)
    tester.test()
    tester.save('composio_runtime_results')


def example_correctness_usage():
    from composio_langchain import ComposioToolSet, App
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model='gpt-4o')

    composio_toolset = ComposioToolSet()
    tools = composio_toolset.get_tools(apps=[App.SHELLTOOL])
    tool = tools[0]
    agent = ReactAgentNew(tool, llm)

    tester = CorrectnessTester(llm=llm,
                               tool=tool,
                               agent=agent,
                               additional_context='')
    tester.test()
    tester.save('composio_correctness_results')


if __name__ == '__main__':
    example_runtime_failure_fuzzing()
    example_correctness_usage()
