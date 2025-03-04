from langchain_openai import ChatOpenAI

from src.toolfuzz.agent_executors.crewai.agent import CrewAIAgent
from src.toolfuzz.correctness.correctness_fuzzer import CorrectnessTester
from src.toolfuzz.runtime.runtime_fuzzer import RuntimeErrorTester


def example_runtime_failure_fuzzing():
    from crewai_tools.tools.serper_dev_tool.serper_dev_tool import SerperDevTool

    llm = ChatOpenAI(model='gpt-4o-mini', temperature=1)
    tool = SerperDevTool()
    agent = CrewAIAgent(tool, llm)

    tester = RuntimeErrorTester(llm=llm,
                                tool=tool,
                                agent=agent,
                                fuzzer_iters=5000)
    tester.test()
    tester.save('crewai_runtime_results')


def example_correctness_usage():
    from crewai_tools.tools.file_read_tool.file_read_tool import FileReadTool

    llm = ChatOpenAI(model='gpt-4o-mini', temperature=1)
    tool = FileReadTool()
    agent = CrewAIAgent(tool, llm)

    tester = CorrectnessTester(llm=llm,
                               tool=tool,
                               agent=agent,
                               additional_context='')
    tester.test()
    tester.save('crewai_correctness_results')


if __name__ == '__main__':
    example_runtime_failure_fuzzing()
    example_correctness_usage()
