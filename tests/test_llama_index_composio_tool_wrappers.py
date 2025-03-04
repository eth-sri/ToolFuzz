import unittest

from composio_llamaindex import ComposioToolSet, App
from parameterized import parameterized

from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument, ArgumentType
from src.toolfuzz.tools.info_extractors.llama_index_tool_wrapper import LLamaIndexToolWrapper

FILE_TOOL = ComposioToolSet().get_tools(apps=[App.FILETOOL])[0]
FILE_DOCS = '''Tool Name: FILETOOL_OPEN_FILE
Tool Arguments: [{'file_manager_id': {'description': 'None', 'type': 'string'}}, {'file_path': {'description': 'None', 'type': 'string'}}, {'line_number': {'description': 'None', 'type': 'integer'}}]
Tool Description: Opens a file in the editor based on the provided file path, if line number is provided, the window will be moved after that line. (i.e. 100 lines after the line number will be displayed) can result in: - valueerror: if file path is not a string or if the file does not exist. - filenotfounderror: if the file does not exist. - ioerror: if there's an issue reading the file. - permissionerror: if the user doesn't have permission to read the file. - isadirectoryerror: if the provided path is a directory.'''

HACKER_NEWS_TOOL = [tool for tool in ComposioToolSet().get_tools(apps=[App.HACKERNEWS]) if
                    tool.metadata.name == 'HACKERNEWS_SEARCH_POSTS'][0]
HACKER_NEWS_DOCS = '''Tool Name: HACKERNEWS_SEARCH_POSTS
Tool Arguments: [{'query': {'description': 'None', 'type': 'string'}}, {'tags': {'description': 'None', 'type': 'array'}}, {'page': {'description': 'None', 'type': 'integer'}}]
Tool Description: Get Relevant Posts From Hacker News Based On A Full Text Query And Optional Filters.'''

WEATHER_MAP_TOOL = ComposioToolSet().get_tools(apps=[App.WEATHERMAP])[0]
WEATHER_MAP_DOCS = '''Tool Name: WEATHERMAP_WEATHER
Tool Arguments: [{'location': {'description': 'None', 'type': 'string'}}]
Tool Description: Tool For Querying The Open Weather Map Api.'''


class TestLlamaIndexComposioToolWrapper(unittest.TestCase):
    @parameterized.expand([
        (FILE_TOOL, "FILETOOL_OPEN_FILE"),
        (HACKER_NEWS_TOOL, "HACKERNEWS_SEARCH_POSTS"),
        (WEATHER_MAP_TOOL, "WEATHERMAP_WEATHER")
    ])
    def test_get_tool_name(self, tool, tool_name):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(tool_name, tool_wrapper.get_tool_name())

    @parameterized.expand([
        (FILE_TOOL, FILE_DOCS),
        (HACKER_NEWS_TOOL, HACKER_NEWS_DOCS),
        (WEATHER_MAP_TOOL, WEATHER_MAP_DOCS)
    ])
    def test_get_tool_docs(self, tool, expected_docs):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(expected_docs, tool_wrapper.get_tool_docs())

    @parameterized.expand([
        (FILE_TOOL, "FILETOOL_OPEN_FILE"),
        (HACKER_NEWS_TOOL, "HACKERNEWS_SEARCH_POSTS"),
        (WEATHER_MAP_TOOL, "WEATHERMAP_WEATHER")
    ])
    def test_get_tool_declaration_name(self, tool, expected_declaration_name):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(expected_declaration_name, tool_wrapper.get_tool_declaration_name())

    @parameterized.expand([
        (FILE_TOOL, [
            ToolArgument(name='file_manager_id', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                         default='',
                         has_default=True,
                         description=None),
            ToolArgument(name='file_path', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                         default=None,
                         has_default=False,
                         description=None),
            ToolArgument(name='line_number', type=ArgumentType(name='integer', sub_types=None, has_subtype=False),
                         default=0,
                         has_default=True,
                         description=None)]),
        (HACKER_NEWS_TOOL, [
            ToolArgument(name='query', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                         default=None,
                         has_default=False,
                         description=None),
            ToolArgument(name='tags', type=ArgumentType(name='array',
                                                        sub_types=[
                                                            ArgumentType(name='string', sub_types=None,
                                                                         has_subtype=False)],
                                                        has_subtype=True),
                         default=None,
                         has_default=True,
                         description=None),
            ToolArgument(name='page', type=ArgumentType(name='integer', sub_types=None, has_subtype=False),
                         default=0,
                         has_default=True,
                         description=None),
        ]),
        (WEATHER_MAP_TOOL, [
            ToolArgument(name='location', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                         default=None,
                         has_default=False,
                         description=None)
        ])
    ])
    def test_get_tool_args(self, tool, args):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(args, tool_wrapper.get_tool_args())

    @unittest.skip("Skipping composio tool source code test for now.")
    # @parameterized.expand([
    #     (FILE_TOOL, "filetool"),
    #     (HACKER_NEWS_TOOL, "hackernews"),
    #     (WEATHER_MAP_TOOL, "weathermap")
    # ])
    def test_get_tool_src(self, tool, src):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        self.assertEqual(src, tool_wrapper.get_tool_src())

    @parameterized.expand([
        (FILE_TOOL, None, {'file_manager_id': '', 'file_path': '', 'line_number': 13333333}),
        (HACKER_NEWS_TOOL, None, {'query': 'query', 'tags': ['tags'], 'page': 1}),
        (WEATHER_MAP_TOOL, None, {'location': 'Zurich'}),
    ])
    def test_tool_invoke(self, tool, expected_exception, parameters):
        tool_wrapper = LLamaIndexToolWrapper(tool)
        if expected_exception is None:
            tool_wrapper.invoke_tool(parameters)
        else:
            self.assertRaises(expected_exception, tool_wrapper.invoke_tool, parameters)
