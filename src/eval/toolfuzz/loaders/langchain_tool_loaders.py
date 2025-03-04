from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.tools import Tool

from src.eval.toolfuzz.loaders.langchain_loader import ReactNewAgentLoader


class ShellToolLoader(ReactNewAgentLoader):

    def get_tool(self):
        """
        Initialization taken from: https://python.langchain.com/v0.2/docs/integrations/tools/bash/
        """
        from langchain_community.tools import ShellTool
        shell_tool = ShellTool()
        shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
            "{", "{{"
        ).replace("}", "}}")
        return shell_tool

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'shell' or tool.lower() == 'shelltool'


class ChatGPTPluginLoader(ReactNewAgentLoader):
    def get_tool(self):
        from langchain_community.tools import AIPluginTool
        return AIPluginTool.from_plugin_url("https://www.klarna.com/.well-known/ai-plugin.json")

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'chatgptplugin'


class DalleMockedToolLoader(ReactNewAgentLoader):
    def get_tool(self):
        from langchain_community.agent_toolkits.load_tools import load_tools
        tool = load_tools(['dalle-image-generator'])
        assert len(tool) == 1
        tool = tool[0]
        tool.func.__self__.client = MockedDalEEClient()
        return tool

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'dalle-image-generator'


class DuckDuckGoSearchToolLoader(ReactNewAgentLoader):

    def get_tool(self):
        from langchain_community.tools import DuckDuckGoSearchRun
        return DuckDuckGoSearchRun()

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'duckduckgosearch'


class DuckDuckGoSearchResultToolLoader(ReactNewAgentLoader):

    def get_tool(self):
        from langchain_community.tools import DuckDuckGoSearchResults
        return DuckDuckGoSearchResults()

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'duckduckgosearchresult'


class GraphQLLoader(ReactNewAgentLoader):

    def get_tool(self):
        tools = load_tools(
            ["graphql"],
            graphql_endpoint="https://swapi-graphql.netlify.app/.netlify/functions/index",
        )
        assert len(tools) == 1
        return tools[0]

    def can_load(self, tool: str) -> bool:
        return tool == 'graphql'


class HuggingFaceHubToolLoader(ReactNewAgentLoader):

    def get_tool(self):
        from langchain_community.agent_toolkits.load_tools import load_huggingface_tool

        return load_huggingface_tool("lysandre/hf-model-downloads")

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'huggingfacehubtool'


class IonicToolLoader(ReactNewAgentLoader):

    def get_tool(self):
        from ionic_langchain.tool import IonicTool
        ionic_tool = IonicTool().tool()
        return ionic_tool

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'ionic'


class PubMedLoader(ReactNewAgentLoader):

    def get_tool(self):
        from langchain_community.tools.pubmed.tool import PubmedQueryRun
        return PubmedQueryRun()

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'pubmed'


class PythonReplLoader(ReactNewAgentLoader):

    def get_tool(self):
        from langchain_experimental.utilities import PythonREPL
        repl = PythonREPL()
        return Tool(
            name="python_repl",
            description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
            func=repl.run,
        )

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'pythonrepl'


class SemanticScholarLoader(ReactNewAgentLoader):

    def get_tool(self):
        from langchain_community.tools.semanticscholar.tool import SemanticScholarQueryRun
        return SemanticScholarQueryRun()

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'semanticscholar'


class WikiToolLoader(ReactNewAgentLoader):

    def get_tool(self):
        from langchain_community.tools.wikidata.tool import WikidataAPIWrapper, WikidataQueryRun

        wikidata = WikidataQueryRun(api_wrapper=WikidataAPIWrapper())
        return wikidata

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'wikidata'


class WikipediaToolLoader(ReactNewAgentLoader):

    def get_tool(self):
        from langchain_community.tools import WikipediaQueryRun
        from langchain_community.utilities import WikipediaAPIWrapper

        wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
        return wikipedia

    def can_load(self, tool: str) -> bool:
        return tool.lower() == 'wikipedia'


class YoutubeSearchToolLoader(ReactNewAgentLoader):

    def get_tool(self):
        from langchain_community.tools import YouTubeSearchTool
        tool = YouTubeSearchTool()
        return tool

    def can_load(self, tool: str) -> bool:
        return tool == 'youtube_search'


class GenericToolLoader(ReactNewAgentLoader):
    def can_load(self, tool: str) -> bool:
        return tool.lower() == self.tool_name.lower()

    def __init__(self, tool_name):
        self.tool_name = tool_name

    def get_tool(self):
        tools = load_tools([self.tool_name], allow_dangerous_tools=True)
        assert len(tools) == 1
        return tools[0]


class MockResponse:
    def __init__(self, data):
        class MockData:
            def __init__(self, url):
                self.url = url

        self.data = [MockData(data)]


class MockedDalEEClient:

    def generate(self, prompt, n, size, model, quality):
        if len(prompt) == 0:
            raise ValueError(
                "Mocked Error code: 400 - {'error': {'code': None, 'message': 'You must provide a prompt.', 'param': None, 'type': 'invalid_request_error'}}")
        return MockResponse('https://oaidalleapiprodscus.blob.core.windows.net')

    def create(self, prompt, n, size, model):
        if len(prompt) == 0:
            raise ValueError(
                "Mocked Error code: 400 - {'error': {'code': None, 'message': 'You must provide a prompt.', 'param': None, 'type': 'invalid_request_error'}}")
        return MockResponse('https://oaidalleapiprodscus.blob.core.windows.net')
