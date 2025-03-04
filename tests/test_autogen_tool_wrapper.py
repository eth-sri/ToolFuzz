import inspect
import unittest
from random import random
from typing import Annotated

from autogen_core.tools import FunctionTool
from parameterized import parameterized

from autogen_ext.tools.langchain import LangChainToolAdapter
from autogen_ext.tools.code_execution import PythonCodeExecutionTool
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
from autogen_ext.tools.http import HttpTool

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from src.toolfuzz.tools.info_extractors.autogen_tool_wrapper import AutogenToolWrapper
from src.toolfuzz.tools.info_extractors.dataclasses import ToolArgument, ArgumentType

base64_schema = {
    "type": "object",
    "properties": {
        "value": {"type": "string", "description": "The base64 value to decode"},
    },
    "required": ["value"],
}

HTTP_TOOL = HttpTool(
    name="base64_decode",
    description="base64 decode a value",
    scheme="https",
    host="httpbin.org",
    port=443,
    path="/base64/{value}",
    method="GET",
    json_schema=base64_schema,
)

HTTP_DOC = '''Tool Name: base64_decode
Tool Arguments: [{'value': {'description': 'The base64 value to decode', 'type': 'string'}}]
Tool Description: base64 decode a value'''

HTTP_SRC = inspect.getsource(type(HTTP_TOOL))

PYTHON_TOOL = PythonCodeExecutionTool(LocalCommandLineCodeExecutor(work_dir="./dd"))
PYTHON_DOC = '''Tool Name: CodeExecutor
Tool Arguments: [{'code': {'description': 'The contents of the Python code block that should be executed', 'type': 'string'}}]
Tool Description: Execute Python code blocks.'''
PYTHON_SRC = inspect.getsource(PythonCodeExecutionTool)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
tool = WikipediaQueryRun(api_wrapper=api_wrapper)
WIKI_TOOL = LangChainToolAdapter(tool)
WIKI_DOC = '''Tool Name: wikipedia
Tool Arguments: [{'query': {'description': 'query to look up on wikipedia', 'type': 'string'}}]
Tool Description: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.'''
WIKI_SRC = inspect.getsource(type(tool))


async def get_stock_price(ticker: str, date: Annotated[str, "Date in YYYY/MM/DD"]) -> float:
    # Returns a random stock price for demonstration purposes.
    return random.uniform(10, 200)


tool = FunctionTool(get_stock_price, description="Get stock price for a given ticker and date.")


class TestAutogenToolWrapper(unittest.TestCase):
    @parameterized.expand([
        (WIKI_TOOL, [ToolArgument(name='query', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                                  default=None,
                                  description='query to look up on wikipedia',
                                  has_default=False)]),
        (PYTHON_TOOL, [ToolArgument(name='code', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                                    default=None,
                                    description='The contents of the Python code block that should be executed',
                                    has_default=False)]),
        (HTTP_TOOL, [ToolArgument(name='value', type=ArgumentType(name='string', sub_types=None, has_subtype=False),
                                  default=None,
                                  description='The base64 value to decode',
                                  has_default=False)]),
    ])
    def test_get_tool_args(self, tool, expected_args):
        tool_wrapper = AutogenToolWrapper(tool)
        self.assertEqual(expected_args, tool_wrapper.get_tool_args())

    @parameterized.expand([
        (HTTP_TOOL, HTTP_SRC),
        (PYTHON_TOOL, PYTHON_SRC),
        (WIKI_TOOL, WIKI_SRC),
    ])
    def test_get_tool_src(self, tool, src):
        tool_wrapper = AutogenToolWrapper(tool)
        self.assertEqual(src, tool_wrapper.get_tool_src())

    @parameterized.expand([
        (HTTP_TOOL, 'base64_decode'),
        (PYTHON_TOOL, 'CodeExecutor'),
        (WIKI_TOOL, 'wikipedia'),
    ])
    def test_get_tool_name(self, tool, expected_name):
        tool_wrapper = AutogenToolWrapper(tool)
        self.assertEqual(expected_name, tool_wrapper.get_tool_name())

    @parameterized.expand([
        (HTTP_TOOL, 'HttpTool'),
        (PYTHON_TOOL, 'PythonCodeExecutionTool'),
        (WIKI_TOOL, 'WikipediaQueryRun'),
    ])
    def test_get_tool_declaration_name(self, tool, expected_name):
        tool_wrapper = AutogenToolWrapper(tool)
        self.assertEqual(expected_name, tool_wrapper.get_tool_declaration_name())

    @parameterized.expand([
        (HTTP_TOOL, HTTP_DOC),
        (PYTHON_TOOL, PYTHON_DOC),
        (WIKI_TOOL, WIKI_DOC),
    ])
    def test_get_tool_docs(self, tool, expected_docs):
        tool_wrapper = AutogenToolWrapper(tool)
        self.assertEqual(expected_docs, tool_wrapper.get_tool_docs())
