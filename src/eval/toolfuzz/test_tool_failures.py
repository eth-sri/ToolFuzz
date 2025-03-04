import argparse

from langchain_core.exceptions import LangChainException
from tqdm import tqdm

from src.eval.toolfuzz.agent_executor import CsvAgent, JsonAgent
from src.eval.toolfuzz.loaders.langchain_tool_loaders import GenericToolLoader, DuckDuckGoSearchToolLoader, \
    IonicToolLoader, PubMedLoader, DuckDuckGoSearchResultToolLoader, ShellToolLoader, PythonReplLoader, WikiToolLoader, \
    YoutubeSearchToolLoader, SemanticScholarLoader, GraphQLLoader, DalleMockedToolLoader
from src.eval.toolfuzz.loaders.langchain_toolkit_loaders import NasaToolkitLoader, FileManagementToolkitLoader, \
    RequestsAllToolkitLoader
from src.eval.toolfuzz.loaders.module_tool_loader import ToolLoader
from src.eval.toolfuzz.utils.setup import init_model
from src.toolfuzz.agent_executors.langchain.react_new import ReactAgentNew
from src.toolfuzz.runtime.runtime_fuzzer import RuntimeErrorTester
from src.toolfuzz.tools.info_extractors.langchain_tool_wrapper import LangchainToolWrapper


def args():
    parser = argparse.ArgumentParser(description="Test agent tools.")
    parser.add_argument('-t', dest='tool')
    return parser.parse_args()


cl_args = args()


def toolkits_test(model):
    toolkit_loaders = [NasaToolkitLoader(), FileManagementToolkitLoader(), RequestsAllToolkitLoader()]
    loader = [loader for loader in toolkit_loaders if loader.can_load(cl_args.tool)]
    if len(loader) != 1:
        print("No toolkit found")
        return
    loader = loader[0]
    for tool in tqdm(loader.get_tool(), desc='Toolkits test'):
        try:
            tester = RuntimeErrorTester(model, tool, loader.get_agent(),
                                        LangchainToolWrapper(tool))
            tester.test()
            tester.save()
        except Exception as e:
            print(f"Global level error for {tool}: {e}")


def special_toolkits_test(model):
    agent = CsvAgent("src/eval/buggy_tools/resources/test.csv", model)
    tools = agent.agent.tools
    tools = [tool for tool in tools if tool.name == cl_args.tool]

    for tool in tqdm(tools, desc='Special toolkits'):
        try:
            tester = RuntimeErrorTester(model, tool, agent, LangchainToolWrapper(tool))
            tester.test()
            tester.save(f'./result_failures_special_toolkits{cl_args.tool}.json')
        except Exception as e:
            print(f"Global level error for {tool}: {e}")

    agent = JsonAgent('src/eval/buggy_tools/resources/open_ai.yml', model)
    tools = agent.agent.tools
    tools = [tool for tool in tools if tool.name == cl_args.tool]
    for tool in tqdm(tools, desc='Special toolkits'):
        try:
            tester = RuntimeErrorTester(model, tool, agent, LangchainToolWrapper(tool))
            tester.test()
            tester.save(f'./result_failures_special_toolkits{cl_args.tool}.json')
        except Exception as e:
            print(f"Global level error for {tool}: {e}")


def tool_test(model):
    tool_loaders = [GenericToolLoader('arxiv'), ShellToolLoader(), DalleMockedToolLoader(),
                    DuckDuckGoSearchToolLoader(), DuckDuckGoSearchResultToolLoader(), GraphQLLoader(),
                    IonicToolLoader(), PubMedLoader(), PythonReplLoader(), SemanticScholarLoader(),
                    GenericToolLoader('stackexchange'), WikiToolLoader(), YoutubeSearchToolLoader()]
    tool_loader = ToolLoader('src.eval.buggy_tools')
    tools = tool_loader.load_tools()

    tools = [tool for tool in tools if tool.name == cl_args.tool]
    for tool in tqdm(tools, desc='Tools'):
        try:
            tester = RuntimeErrorTester(model, tool, ReactAgentNew(tool, model), LangchainToolWrapper(tool))
            tester.test()
            tester.save(f'./result_failures_{cl_args.tool}.json')
        except IndexError as e:
            print(f"Global level error for {tool}: {e}")

    for loader in tool_loaders:
        extractor = LangchainToolWrapper(loader.get_tool())
        if extractor.get_tool_name().lower() == cl_args.tool.lower():
            try:
                tester = RuntimeErrorTester(model, loader.get_tool(), loader.get_agent(), extractor)
                tester.test()
                tester.save(f'./result_failures_{cl_args.tool}.json')
            except LangChainException as e:
                print(f"Global level error for {loader.get_tool()}: {e}")


def main():
    model = init_model('gpt-4o-mini')
    # tool_test(model)
    # toolkits_test(model)
    special_toolkits_test(model)


if __name__ == '__main__':
    main()
