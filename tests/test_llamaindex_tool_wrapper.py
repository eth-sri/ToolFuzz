import inspect
import json
import unittest

from duckduckgo_search.exceptions import DuckDuckGoSearchException
from llama_index.core.tools import FunctionTool
from llama_index.tools.wikipedia import WikipediaToolSpec
from parameterized import parameterized

from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument, ArgumentType
from src.toolfuzz.tools.info_extractors.llama_index_tool_wrapper import LLamaIndexToolWrapper

wiki_spec = WikipediaToolSpec()
WIKI_TOOL = wiki_spec.to_tool_list()[1]
WIKI_DOCS = '''Tool Name: search_data
Tool Arguments: [{'query': {'description': 'None', 'type': 'string'}}, {'lang': {'description': 'None', 'type': 'string'}}]
Tool Description: search_data(query: str, lang: str = 'en') -> str

        Search Wikipedia for a page related to the given query.
        Use this tool when `load_data` returns no results.

        Args:
            query (str): the string to search for
        '''
WIKI_SRC = inspect.getsource(WIKI_TOOL.fn)

from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec

DUCKDUCK_TOOL = DuckDuckGoSearchToolSpec().to_tool_list()[0]
DUCKDUCK_DOCS = '''Tool Name: duckduckgo_instant_search
Tool Arguments: [{'query': {'description': 'None', 'type': 'string'}}]
Tool Description: duckduckgo_instant_search(query: str) -> List[Dict]

        Make a query to DuckDuckGo api to receive an instant answer.

        Args:
            query (str): The query to be passed to DuckDuckGo.
        '''
DUCKDUCK_SRC = inspect.getsource(DUCKDUCK_TOOL.fn)


def get_weather(location: str) -> str:
    """Useful for getting the weather for a given location."""
    loc = json.loads(location)
    assert 'name' in loc
    place = loc['name']
    return f"The weather in {place} is sunny"


GET_WEATHER_TOOL = FunctionTool.from_defaults(get_weather)
GET_WEATHER_DOCS = '''Tool Name: get_weather
Tool Arguments: [{'location': {'description': 'None', 'type': 'string'}}]
Tool Description: get_weather(location: str) -> str
Useful for getting the weather for a given location.'''
GET_WEATHER_SRC = inspect.getsource(GET_WEATHER_TOOL.fn)


class TestLangchainToolWrapper(unittest.TestCase):
    @parameterized.expand([
        (WIKI_TOOL, None, {"query": "LLM agents"}),
        (DUCKDUCK_TOOL, DuckDuckGoSearchException, {"query": "too long message" * 100}),
        (GET_WEATHER_TOOL, json.JSONDecodeError, {"location": "Not a json"})])
    def test_invoke_tool(self, tool, expected_exception, parameters):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        if expected_exception is None:
            try:
                tool_wrapper.invoke_tool(parameters)
            except Exception as e:
                self.fail(f"{tool} raised an exception: {e} when it should not have.")
        else:
            self.assertRaises(expected_exception, tool_wrapper.invoke_tool, parameters)

    @parameterized.expand([
        (WIKI_TOOL, [ToolArgument(name='query', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                                  default=None,
                                  has_default=False,
                                  description=None),
                     ToolArgument(name='lang', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                                  default="en",
                                  has_default=True,
                                  description=None)]),
        (DUCKDUCK_TOOL,
         [ToolArgument(name='query', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                       default=None,
                       has_default=False,
                       description=None)]),
        (GET_WEATHER_TOOL,
         [ToolArgument(name='location', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                       default=None,
                       has_default=False,
                       description=None)]),
    ])
    def test_get_tool_args(self, tool, expected_args):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(expected_args, tool_wrapper.get_tool_args())

    @parameterized.expand([
        (WIKI_TOOL, WIKI_SRC),
        (DUCKDUCK_TOOL, DUCKDUCK_SRC),
        (GET_WEATHER_TOOL, GET_WEATHER_SRC),
    ])
    def test_get_tool_src(self, tool, src):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(tool_wrapper.get_tool_src(), src)

    @parameterized.expand([
        (WIKI_TOOL, "search_data"),
        (DUCKDUCK_TOOL, "duckduckgo_instant_search"),
        (GET_WEATHER_TOOL, "get_weather"),
    ])
    def test_get_tool_name(self, tool, expected_name):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(expected_name, tool_wrapper.get_tool_name())

    @parameterized.expand([
        (WIKI_TOOL, "search_data"),
        (DUCKDUCK_TOOL, "duckduckgo_instant_search"),
        (GET_WEATHER_TOOL, "get_weather"),
    ])
    def test_get_tool_declaration_name(self, tool, expected_name):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(expected_name, tool_wrapper.get_tool_declaration_name())

    @parameterized.expand([
        (WIKI_TOOL, WIKI_DOCS),
        (DUCKDUCK_TOOL, DUCKDUCK_DOCS),
        (GET_WEATHER_TOOL, GET_WEATHER_DOCS),
    ])
    def test_get_tool_docs(self, tool, expected_docs):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(expected_docs, tool_wrapper.get_tool_docs())
