from src.toolfuzz.agent_executors.langchain.react_new import ReactAgentNew
from src.toolfuzz.correctness.correctness_fuzzer import CorrectnessTester
from src.toolfuzz.runtime.runtime_fuzzer import RuntimeErrorTester


def example_runtime_failure_fuzzing():
    from langchain_community.tools import ShellTool
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model='gpt-4o-mini')
    tool = ShellTool()
    agent = ReactAgentNew(tool, llm)

    tester = RuntimeErrorTester(llm=llm,
                                tool=tool,
                                agent=agent,
                                fuzzer_iters=500)
    tester.test()
    tester.save('langchain_runtime_results')


def example_correctness_usage():
    from langchain_community.tools import ShellTool
    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI(model='gpt-4o-mini')
    tool = ShellTool()
    agent = ReactAgentNew(tool, llm)

    tester = CorrectnessTester(llm=llm,
                               tool=tool,
                               agent=agent,
                               additional_context='',
                               prompt_set_iters=5)
    tester.test()
    tester.save('langchain_correctness_results')


if __name__ == '__main__':
    example_runtime_failure_fuzzing()
    example_correctness_usage()
