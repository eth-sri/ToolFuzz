import inspect
import json
import unittest

from langchain_community.agent_toolkits import NasaToolkit
from langchain_community.tools import WikipediaQueryRun
from langchain_community.tools.nasa.prompt import NASA_SEARCH_PROMPT
from langchain_community.utilities import WikipediaAPIWrapper, NasaAPIWrapper
from parameterized import parameterized

from src.eval.buggy_tools.open_street_map import open_street_map_search
from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument, ArgumentType
from src.toolfuzz.tools.info_extractors.langchain_tool_wrapper import LangchainToolWrapper

WIKI_TOOL = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
WIKIPEDIA_DOCS = '''Tool Name: wikipedia
Tool Arguments: [{'query': {'description': 'query to look up on wikipedia', 'type': 'string'}}]
Tool Description: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.'''
WIKI_TOOL_SRC = inspect.getsource(type(WIKI_TOOL))

OPEN_STREET_MAP_DOCS = '''Tool Name: open-street-map-search
Tool Arguments: [{'query': {'description': 'Search query for locating places on a map. The query can be a place directly like Zurich, Sofia and so on or a query like libraries in Zurich or coffee shops in San Francisco', 'type': 'string'}}]
Tool Description: Tool to query a map. This tool can locate places by name and simple queries such as: libraries in San Francisco.
The idea of the tool is to locate places like coffe shops offices etc.'''
OPEN_STREET_MAP_SRC = inspect.getsource(open_street_map_search.func)

NASA_TOOL = NasaToolkit.from_nasa_api_wrapper(NasaAPIWrapper()).get_tools()[0]
NASA_SEARCH_DOCS = '''Tool Name: Search NASA Image and Video Library media
Tool Arguments: [{'instructions': {'description': 'None', 'type': 'string'}}, {'run_manager': {'description': 'None', 'type': 'typing.Optional[langchain_core.callbacks.manager.CallbackManagerForToolRun]'}}]
Tool Description: ''' + NASA_SEARCH_PROMPT
NASA_TOOL_SRC = inspect.getsource(type(NASA_TOOL))


class TestLangchainToolWrapper(unittest.TestCase):
    @parameterized.expand([
        (WIKI_TOOL, None, "LLM agents"),
        (open_street_map_search, AssertionError, "too long message" * 100),
        (NASA_TOOL, json.JSONDecodeError, "telescope hubble"),
    ])
    def test_invoke_tool(self, tool, expected_exception, parameters):
        tool_wrapper = LangchainToolWrapper(tool)
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
                                  description='query to look up on wikipedia',
                                  has_default=False)]),
        (open_street_map_search,
         [ToolArgument(name='query', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                       default=None,
                       description='Search query for locating places on a map. The query can be a place directly like Zurich, Sofia and so on or a query like libraries in Zurich or coffee shops in San Francisco',
                       has_default=False)]),
        (NASA_TOOL,
         [ToolArgument(name='instructions', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                       default=None,
                       description=None,
                       has_default=False),
          ToolArgument(name='run_manager', type=ArgumentType(
              name='typing.Optional[langchain_core.callbacks.manager.CallbackManagerForToolRun]', sub_types=None,
              has_subtype=False),
                       description=None,
                       default=None,
                       has_default=True)]),
    ])
    def test_get_tool_args(self, tool, expected_args):
        tool_wrapper = LangchainToolWrapper(tool)
        self.assertEqual(expected_args, tool_wrapper.get_tool_args())

    @parameterized.expand([
        (WIKI_TOOL, WIKI_TOOL_SRC),
        (open_street_map_search, OPEN_STREET_MAP_SRC),
        (NASA_TOOL, NASA_TOOL_SRC),
    ])
    def test_get_tool_src(self, tool, src):
        tool_wrapper = LangchainToolWrapper(tool)
        self.assertEqual(tool_wrapper.get_tool_src(), src)

    @parameterized.expand([
        (WIKI_TOOL, "wikipedia"),
        (open_street_map_search, "open-street-map-search"),
        (NASA_TOOL, "Search NASA Image and Video Library media"),
    ])
    def test_get_tool_name(self, tool, expected_name):
        tool_wrapper = LangchainToolWrapper(tool)
        self.assertEqual(tool_wrapper.get_tool_name(), expected_name)

    @parameterized.expand([
        (WIKI_TOOL, "WikipediaQueryRun"),
        (open_street_map_search, "open_street_map_search"),
        (NASA_TOOL, "NasaAction"),
    ])
    def test_get_tool_declaration_name(self, tool, expected_name):
        tool_wrapper = LangchainToolWrapper(tool)
        self.assertEqual(tool_wrapper.get_tool_declaration_name(), expected_name)

    @parameterized.expand([
        (WIKI_TOOL, WIKIPEDIA_DOCS),
        (open_street_map_search, OPEN_STREET_MAP_DOCS),
        (NASA_TOOL, NASA_SEARCH_DOCS),
    ])
    def test_get_tool_docs(self, tool, expected_docs):
        tool_wrapper = LangchainToolWrapper(tool)
        self.assertEqual(expected_docs, tool_wrapper.get_tool_docs())
