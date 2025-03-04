from langchain_community.utilities import WikipediaAPIWrapper

from src.eval.buggy_tools.fixed_tools.pubmed import PubmedQueryRunFixed
from src.eval.buggy_tools.fixed_tools.wikipedia import WikipediaQueryRunFixed
from src.eval.toolfuzz.loaders.custom_tools_loader import CustomToolsLoader
from src.eval.toolfuzz.loaders.langchain_tool_loaders import GenericToolLoader, DuckDuckGoSearchToolLoader, \
    IonicToolLoader, SemanticScholarLoader, YoutubeSearchToolLoader, WikipediaToolLoader, WikiToolLoader, \
    PythonReplLoader, PubMedLoader, DuckDuckGoSearchResultToolLoader, ShellToolLoader, DalleMockedToolLoader, \
    GraphQLLoader
from src.eval.toolfuzz.loaders.langchain_toolkit_loaders import RequestsAllToolkitLoader, FileManagementToolkitLoader, \
    NasaToolkitLoader
from src.eval.toolfuzz.loaders.module_tool_loader import ToolLoader


def get_correctness_tool_loaders():
    tool_loaders = [GenericToolLoader('arxiv'), ShellToolLoader(), DalleMockedToolLoader(),
                    DuckDuckGoSearchToolLoader(), DuckDuckGoSearchResultToolLoader(), GraphQLLoader(),
                    IonicToolLoader(), PubMedLoader(), PythonReplLoader(),
                    SemanticScholarLoader(), GenericToolLoader('stackexchange'), WikiToolLoader(),
                    YoutubeSearchToolLoader(), WikipediaToolLoader(),
                    CustomToolsLoader('open_street_map_distance'), CustomToolsLoader('open_street_map_search')]

    # Now test toolkits:
    toolkit_loaders = [NasaToolkitLoader(), FileManagementToolkitLoader(),
                       RequestsAllToolkitLoader()]  # GithubToolkitLoader())

    return tool_loaders + toolkit_loaders


def get_failure_tools():
    tool_loader = ToolLoader('src.eval.buggy_tools')
    tools = tool_loader.load_tools()
    return tools + get_correctness_tool_loaders()


def get_fixed_tools():
    tools = [
        WikipediaQueryRunFixed(api_wrapper=WikipediaAPIWrapper()), PubmedQueryRunFixed()
    ]
    return tools


if __name__ == '__main__':
    # print([t.name for t in get_failure_tools()])
    print([t.name for t in get_correctness_tool_loaders()])
