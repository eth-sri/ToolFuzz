import inspect
import unittest

from crewai.tools import tool
from crewai.tools.structured_tool import CrewStructuredTool
from crewai_tools.tools.directory_read_tool.directory_read_tool import DirectoryReadTool
from crewai_tools.tools.llamaindex_tool.llamaindex_tool import LlamaIndexTool
from duckduckgo_search.exceptions import DuckDuckGoSearchException
from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from parameterized import parameterized
from pydantic import BaseModel

from src.toolfuzz.tools.info_extractors.crew_ai_tool_wrapper import CrewAIToolWrapper
from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument, ArgumentType


class APICallInput(BaseModel):
    endpoint: str
    parameters: dict


# Wrapper function to execute the API calls, it uses APICallInput as the input schema
def tool_wrapper(*args, **kwargs):
    # Here, you would typically call the API using the parameters
    # For demonstration, we'll return a placeholder string
    return f"Call the API at {kwargs['endpoint']} with parameters {kwargs['parameters']}"


API_CALLING_TOOL = CrewStructuredTool.from_function(
    name='Wrapper API',
    description="A tool to wrap API calls with structured input.",
    args_schema=APICallInput,
    func=tool_wrapper,
)

API_CALLING_SRC = inspect.getsource(tool_wrapper)

API_CALLING_DOCS = '''Tool Name: Wrapper API
Tool Arguments: {'endpoint': {'description': None, 'type': 'str'}, 'parameters': {'description': None, 'type': 'dict'}}
Tool Description: A tool to wrap API calls with structured input.'''

DIRECTORY_READ_TOOL = DirectoryReadTool()
DIRECTORY_READ_DOCS = DIRECTORY_READ_TOOL.description
DIRECTORY_READ_SRC = inspect.getsource(DirectoryReadTool)

llama_tool = DuckDuckGoSearchToolSpec().to_tool_list()[0]
DUCKDUCK_SRC = inspect.getsource(llama_tool.fn)
DUCKDUCK_TOOL = LlamaIndexTool.from_tool(llama_tool)
DUCKDUCK_DOCS = DUCKDUCK_TOOL.description


@tool("WebSearch")
def web_search(question: str) -> str:
    """A tool to search the web for your random questions."""
    # Function logic here
    assert len(question) <= 50, 'the search query is too long'
    return "Result from your custom tool"


WEB_SEARCH_DOCS = 'Tool Name: WebSearch\nTool Arguments: {\'question\': {\'description\': None, \'type\': \'str\'}}\nTool Description: A tool to search the web for your random questions.'
WEB_SEARCH_SRC = inspect.getsource(web_search.func)


class TestCrewAIToolWrapper(unittest.TestCase):
    @parameterized.expand([
        (API_CALLING_TOOL, None, {"endpoint": "test input", "parameters": {"param1": "value1"}}),
        (DIRECTORY_READ_TOOL, None, {"directory": "current directory"}),
        (web_search, AssertionError, {"question": "too long message" * 100}),
        (DUCKDUCK_TOOL, DuckDuckGoSearchException, {"query": "too long message" * 100}),
    ])
    def test_invoke_tool(self, tool, expected_exception, parameters):
        tool_wrapper = CrewAIToolWrapper(tool)
        if expected_exception is None:
            try:
                tool_wrapper.invoke_tool(parameters)
            except Exception as e:
                self.fail(f"{tool} raised an exception: {e} when it should not have.")
        else:
            self.assertRaises(expected_exception, tool_wrapper.invoke_tool, parameters)

    @parameterized.expand([
        (API_CALLING_TOOL,
         [ToolArgument(name='endpoint', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                       default=None,
                       description=None,
                       has_default=False),
          ToolArgument(name='parameters', type=ArgumentType(name='dict', sub_types=None, has_subtype=False),
                       default=None,
                       description=None,
                       has_default=False)]),
        (DIRECTORY_READ_TOOL,
         [ToolArgument(name='directory', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                       default=None,
                       description='Mandatory directory to list content',
                       has_default=False)]),
        (web_search,
         [ToolArgument(name='question', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                       default=None,
                       description=None,
                       has_default=False)]),
        (DUCKDUCK_TOOL,
         [ToolArgument(name='query', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                       default=None,
                       description=None,
                       has_default=False)]),
    ])
    def test_get_tool_args(self, tool, expected_args):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(expected_args, tool_wrapper.get_tool_args())

    @parameterized.expand([
        (API_CALLING_TOOL, API_CALLING_SRC),
        (DIRECTORY_READ_TOOL, DIRECTORY_READ_SRC),
        (web_search, WEB_SEARCH_SRC),
        (DUCKDUCK_TOOL, DUCKDUCK_SRC),
    ])
    def test_get_tool_src(self, tool, src):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(src, tool_wrapper.get_tool_src())

    @parameterized.expand([
        (API_CALLING_TOOL, "Wrapper API"),
        (DIRECTORY_READ_TOOL, "List files in directory"),
        (web_search, "WebSearch"),
        (DUCKDUCK_TOOL, "duckduckgo_instant_search"),
    ])
    def test_get_tool_name(self, tool, expected_name):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(expected_name, tool_wrapper.get_tool_name())

    @parameterized.expand([
        (API_CALLING_TOOL, "tool_wrapper"),
        (DIRECTORY_READ_TOOL, "DirectoryReadTool"),
        (web_search, "web_search"),
        (DUCKDUCK_TOOL, "LlamaIndexTool"),
    ])
    def test_get_tool_declaration_name(self, tool, expected_name):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(expected_name, tool_wrapper.get_tool_declaration_name())

    @parameterized.expand([
        (API_CALLING_TOOL, API_CALLING_DOCS),
        (DIRECTORY_READ_TOOL, DIRECTORY_READ_DOCS),
        (web_search, WEB_SEARCH_DOCS),
        (DUCKDUCK_TOOL, DUCKDUCK_DOCS),
    ])
    def test_get_tool_docs(self, tool, expected_docs):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(expected_docs, tool_wrapper.get_tool_docs())
