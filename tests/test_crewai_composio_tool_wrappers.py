import unittest

from parameterized import parameterized
from composio_crewai import ComposioToolSet, App

from src.toolfuzz.tools.info_extractors.crew_ai_tool_wrapper import CrewAIToolWrapper
from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument, ArgumentType

FILE_TOOL = ComposioToolSet().get_tools(apps=[App.FILETOOL])[0]
FILE_DOCS = '''Tool Name: FILETOOL_OPEN_FILE
Tool Arguments: {'file_manager_id': {'description': 'ID of the file manager where the file will be opened, if not provided the recent file manager will be used to execute the action. Please provide a value of type string.', 'type': 'str'}, 'file_path': {'description': 'file path to open in the editor. This is a relative path to the current directory. Please provide a value of type string. This parameter is required.', 'type': 'str'}, 'line_number': {'description': 'If file-number is given, file will be opened from that line number. Please provide a value of type integer.', 'type': 'int'}}
Tool Description: Opens a file in the editor based on the provided file path, if line number is provided, the window will be moved after that line. (i.e. 100 lines after the line number will be displayed) can result in: - valueerror: if file path is not a string or if the file does not exist. - filenotfounderror: if the file does not exist. - ioerror: if there's an issue reading the file. - permissionerror: if the user doesn't have permission to read the file. - isadirectoryerror: if the provided path is a directory.'''

HACKER_NEWS_TOOL = [tool for tool in ComposioToolSet().get_tools(apps=[App.HACKERNEWS]) if
                    tool.name == 'HACKERNEWS_SEARCH_POSTS'][0]
HACKER_NEWS_DOCS = '''Tool Name: HACKERNEWS_SEARCH_POSTS
Tool Arguments: {'query': {'description': 'Full-text query to filter the posts. Please provide a value of type string. This parameter is required.', 'type': 'str'}, 'tags': {'description': 'Filter on a specific tag. Available tags: story, comment, poll, pollopt, show_hn, ask_hn, front_page, author_<USERNAME>, story_<ID>.', 'type': 'list[str]'}, 'page': {'description': 'Page number for pagination. Please provide a value of type integer.', 'type': 'int'}}
Tool Description: Get Relevant Posts From Hacker News Based On A Full Text Query And Optional Filters.'''

WEATHER_MAP_TOOL = ComposioToolSet().get_tools(apps=[App.WEATHERMAP])[0]
WEATHER_MAP_DOCS = '''Tool Name: WEATHERMAP_WEATHER
Tool Arguments: {'location': {'description': "The location for which weather information is requested (e.g., 'London,GB', 'London').You may specify the country code or not. If you get city not found error, try without country code. Please provide a value of type string. This parameter is required.", 'type': 'str'}}
Tool Description: Tool For Querying The Open Weather Map Api.'''


class TestCrewAIComposioToolWrapper(unittest.TestCase):
    @parameterized.expand([
        (FILE_TOOL, "FILETOOL_OPEN_FILE"),
        (HACKER_NEWS_TOOL, "HACKERNEWS_SEARCH_POSTS"),
        (WEATHER_MAP_TOOL, "WEATHERMAP_WEATHER")
    ])
    def test_get_tool_name(self, tool, tool_name):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(tool_name, tool_wrapper.get_tool_name())

    @parameterized.expand([
        (FILE_TOOL, FILE_DOCS),
        (HACKER_NEWS_TOOL, HACKER_NEWS_DOCS),
        (WEATHER_MAP_TOOL, WEATHER_MAP_DOCS)
    ])
    def test_get_tool_docs(self, tool, expected_docs):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(expected_docs, tool_wrapper.get_tool_docs())

    @parameterized.expand([
        (FILE_TOOL, "FILETOOL_OPEN_FILE"),
        (HACKER_NEWS_TOOL, "HACKERNEWS_SEARCH_POSTS"),
        (WEATHER_MAP_TOOL, "WEATHERMAP_WEATHER")
    ])
    def test_get_tool_declaration_name(self, tool, expected_declaration_name):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(expected_declaration_name, tool_wrapper.get_tool_declaration_name())

    @parameterized.expand([
        (FILE_TOOL, [
            ToolArgument(name='file_manager_id', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                         default=None,
                         has_default=False,
                         description='ID of the file manager where the file will be opened, if not provided the recent file manager will be used to execute the action. Please provide a value of type string.'),
            ToolArgument(name='file_path', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                         default=None,
                         has_default=False,
                         description='file path to open in the editor. This is a relative path to the current directory. Please provide a value of type string. This parameter is required.'),
            ToolArgument(name='line_number', type=ArgumentType(name='integer', sub_types=None, has_subtype=False),
                         default=None,
                         has_default=False,
                         description='If file-number is given, file will be opened from that line number. Please provide a value of type integer.')]),
        (HACKER_NEWS_TOOL, [
            ToolArgument(name='query', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                         default=None,
                         has_default=False,
                         description='Full-text query to filter the posts. Please provide a value of type string. This parameter is required.'),
            ToolArgument(name='tags', type=ArgumentType(name='array',
                                                        sub_types=[
                                                            ArgumentType(name='string', sub_types=None,
                                                                         has_subtype=False)],
                                                        has_subtype=True),
                         default=None,
                         has_default=False,
                         description='Filter on a specific tag. Available tags: story, comment, poll, pollopt, show_hn, ask_hn, front_page, author_<USERNAME>, story_<ID>.'),
            ToolArgument(name='page', type=ArgumentType(name='integer', sub_types=None, has_subtype=False),
                         default=None,
                         has_default=False,
                         description='Page number for pagination. Please provide a value of type integer.'),
        ]),
        (WEATHER_MAP_TOOL, [
            ToolArgument(name='location', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                         default=None,
                         has_default=False,
                         description='The location for which weather information is requested (e.g., \'London,GB\', \'London\').You may specify the country code or not. If you get city not found error, try without country code. Please provide a value of type string. This parameter is required.')
        ])
    ])
    def test_get_tool_args(self, tool, args):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(args, tool_wrapper.get_tool_args())

    @unittest.skip("Skipping composio tool source code test for now.")
    # @parameterized.expand([
    #     (FILE_TOOL, "filetool"),
    #     (HACKER_NEWS_TOOL, "hackernews"),
    #     (WEATHER_MAP_TOOL, "weathermap")
    # ])
    def test_get_tool_src(self, tool, src):
        tool_wrapper = CrewAIToolWrapper(tool)
        self.assertEqual(src, tool_wrapper.get_tool_src())

    @parameterized.expand([
        (FILE_TOOL, Exception, {'file_manager_id': '', 'file_path': '', 'line_number': 13333333}),
        (HACKER_NEWS_TOOL, None, {'query': 'query', 'tags': ['tags'], 'page': 1}),
        (WEATHER_MAP_TOOL, None, {'location': 'Zurich'}),
    ])
    def test_tool_invoke(self, tool, expected_exception, parameters):
        tool_wrapper = CrewAIToolWrapper(tool)
        if expected_exception is None:
            tool_wrapper.invoke_tool(parameters)
        else:
            self.assertRaises(expected_exception, tool_wrapper.invoke_tool, parameters)
