import unittest
from unittest.mock import patch

from autogen_agentchat.base import TaskResult
from autogen_agentchat.messages import TextMessage, ToolCallRequestEvent, ToolCallExecutionEvent
from autogen_core import FunctionCall
from autogen_core.models import FunctionExecutionResult, RequestUsage
from autogen_ext.tools.http import HttpTool
from autogen_ext.tools.langchain import LangChainToolAdapter
from composio_autogen import ComposioToolSet, App
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

from src.toolfuzz.agent_executors.agent_executor import AgentResponse
from src.toolfuzz.agent_executors.autogen.assistant_agent import AssistantAgentExecutor

messages = {
    'http_tool': TaskResult(
        messages=[TextMessage(source='user', models_usage=None, metadata={},
                              content='Can you please decode the following: asdhaksdgajkfdgakjsdgfauiksygdfaiusdfiabfd?',
                              type='TextMessage'),
                  ToolCallRequestEvent(source='AssistantAgent',
                                       models_usage=RequestUsage(
                                           prompt_tokens=93,
                                           completion_tokens=37),
                                       metadata={}, content=[
                          FunctionCall(id='call_Wdgfel2UlQIwmg0eRwbTwWrC',
                                       arguments='{"value":"asdhaksdgajkfdgakjsdgfauiksygdfaiusdfiabfd"}',
                                       name='base64_decode')],
                                       type='ToolCallRequestEvent'),
                  ToolCallExecutionEvent(source='AssistantAgent', models_usage=None, metadata={},
                                         content=[FunctionExecutionResult(
                                             content='Incorrect Base64 data try: SFRUUEJJTiBpcyBhd2Vzb21l',
                                             name='base64_decode',
                                             call_id='call_Wdgfel2UlQIwmg0eRwbTwWrC',
                                             is_error=False)], type='ToolCallExecutionEvent'),
                  TextMessage(source='AssistantAgent',
                              models_usage=RequestUsage(prompt_tokens=107, completion_tokens=82),
                              metadata={},
                              content='The string you provided, "asdhaksdgajkfdgakjsdgfauiksygdfaiusdfiabfd," does not appear to follow any standard encoding or cipher that I can decode. It seems to be a random string of characters.\n\nIf you are looking for a specific type of encoding or a cipher, please provide more details, and I would be happy to help!',
                              type='TextMessage')], stop_reason=None),
    'wikipedia': TaskResult(messages=[
        TextMessage(source='user', models_usage=None, metadata={}, content='Who is Alan Turing?', type='TextMessage'),
        ToolCallRequestEvent(source='AssistantAgent', models_usage=RequestUsage(prompt_tokens=98, completion_tokens=16),
                             metadata={}, content=[
                FunctionCall(id='call_aaH2DjgT3SdO47cakOLsz9A0', arguments='{"query":"Alan Turing"}',
                             name='wikipedia')], type='ToolCallRequestEvent'),
        ToolCallExecutionEvent(source='AssistantAgent', models_usage=None, metadata={}, content=[
            FunctionExecutionResult(
                content='Page: Alan Turing\nSummary: Alan Mathison Turing (; 23 June 1912 – 7 June 1954) was an English mathem',
                name='wikipedia', call_id='call_aaH2DjgT3SdO47cakOLsz9A0', is_error=False)],
                               type='ToolCallExecutionEvent'),
        TextMessage(source='AssistantAgent', models_usage=RequestUsage(prompt_tokens=72, completion_tokens=244),
                    metadata={},
                    content="Alan Turing (23 June 1912 – 7 June 1954) was an English mathematician, logician, computer scientist, and cryptanalyst. He is best known for his pivotal role in the development of theoretical computer science and for his contributions to breaking the German Enigma code during World War II, which significantly aided the Allied forces.\n\nTuring is often regarded as the father of modern computer science for his conceptualization of the Turing machine, a fundamental model of computation that defines algorithms and computation. He also contributed to the fields of artificial intelligence and mathematical biology.\n\nIn addition to his scientific achievements, Turing faced significant personal challenges due to his homosexuality, which was criminalized in the UK at the time. In 1952, he was prosecuted for his sexual orientation, leading to a conviction that subjected him to chemical castration. Turing died in 1954 under circumstances that were ruled a suicide.\n\nHis legacy has been honored posthumously, including a formal apology from the British government in 2009 and a royal pardon in 2013. Turing's life and work have inspired many films, books, and academic studies, highlighting his profound impact on technology and society.",
                    type='TextMessage')], stop_reason=None),
    'weather': TaskResult(messages=[
        TextMessage(source='user', models_usage=None, metadata={}, content='What is the weather in Zurich?',
                    type='TextMessage'),
        ToolCallRequestEvent(source='AssistantAgent', models_usage=RequestUsage(prompt_tokens=75, completion_tokens=25),
                             metadata={}, content=[
                FunctionCall(id='call_uNp6GYlnSWtTWTK4TFcbHHXt', arguments='{"location":"Zurich"}',
                             name='WEATHERMAP_WEATHER_b404817b58')], type='ToolCallRequestEvent'),
        ToolCallExecutionEvent(source='AssistantAgent', models_usage=None, metadata={}, content=[
            FunctionExecutionResult(
                content="{'data': {'coord': {'lon': 8.55, 'lat': 47.3667}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 288.15, 'feels_like': 286.72, 'temp_min': 286.64, 'temp_max': 289.08, 'pressure': 1024, 'humidity': 39, 'sea_level': 1024, 'grnd_level': 965}, 'visibility': 10000, 'wind': {'speed': 1.54, 'deg': 300}, 'clouds': {'all': 0}, 'dt': 1741185556, 'sys': {'type': 1, 'id': 6932, 'country': 'CH', 'sunrise': 1741154320, 'sunset': 1741194973}, 'timezone': 3600, 'id': 2657896, 'name': 'Zurich', 'cod': 200}, 'error': None, 'successfull': True, 'successful': True}",
                name='WEATHERMAP_WEATHER_b404817b58', call_id='call_uNp6GYlnSWtTWTK4TFcbHHXt', is_error=False)],
                               type='ToolCallExecutionEvent'),
        TextMessage(source='AssistantAgent', models_usage=RequestUsage(prompt_tokens=314, completion_tokens=53),
                    metadata={},
                    content='The current weather in Zurich is clear with a temperature of approximately 15°C (288.15 K). The humidity level is at 39%, and there is a light wind blowing at 1.54 m/s from the northwest. Enjoy the beautiful weather!',
                    type='TextMessage')], stop_reason=None)
}


class MockedAgent:
    def __init__(self, tool, **kwargs):
        self.tool = tool

    async def run(self, *args, **kwargs) -> TaskResult:
        if self.tool.name == 'base64_decode':
            return messages['http_tool']
        elif self.tool.name == 'wikipedia':
            return messages['wikipedia']
        elif self.tool.name == 'WEATHERMAP_WEATHER_b404817b58':
            return messages['weather']
        else:
            raise ValueError(f"Tool {self.tool.name} not found")


class TestAutogenAssistant(unittest.TestCase):
    @patch('autogen_agentchat.agents.AssistantAgent')
    def test_http_tool(self, mocked_agent):
        base64_schema = {
            "type": "object",
            "properties": {
                "value": {"type": "string", "description": "The base64 value to decode"},
            },
            "required": ["value"],
        }

        tool = HttpTool(
            name="base64_decode",
            description="base64 decode a value",
            scheme="https",
            host="httpbin.org",
            port=443,
            path="/base64/{value}",
            method="GET",
            json_schema=base64_schema
        )

        mocked_agent.return_value = MockedAgent(tool)
        agent = AssistantAgentExecutor(tool, 'gpt-4o-mini')

        result = agent('Can you please decode the following: asdhaksdgajkfdgakjsdgfauiksygdfaiusdfiabfd?')
        self.assertEqual(AgentResponse(agent_response='The string you provided, '
                                                      '"asdhaksdgajkfdgakjsdgfauiksygdfaiusdfiabfd," '
                                                      'does not appear to follow any standard encoding '
                                                      'or cipher that I can decode. It seems to be a '
                                                      'random string of characters.\n'
                                                      '\n'
                                                      'If you are looking for a specific type of '
                                                      'encoding or a cipher, please provide more '
                                                      'details, and I would be happy to help!',
                                       trace=[{'content': 'Can you please decode the following: '
                                                          'asdhaksdgajkfdgakjsdgfauiksygdfaiusdfiabfd?',
                                               'role': 'user'},
                                              {'content': '',
                                               'role': 'assistant',
                                               'tool_calls': [{'function': {
                                                   'arguments': '{"value":"asdhaksdgajkfdgakjsdgfauiksygdfaiusdfiabfd"}',
                                                   'name': 'base64_decode'},
                                                   'id': 'call_Wdgfel2UlQIwmg0eRwbTwWrC',
                                                   'type': 'function'}]},
                                              {'content': 'Incorrect Base64 data try: '
                                                          'SFRUUEJJTiBpcyBhd2Vzb21l',
                                               'role': 'tool',
                                               'tool_call_id': 'call_Wdgfel2UlQIwmg0eRwbTwWrC'},
                                              {'content': 'The string you provided, '
                                                          '"asdhaksdgajkfdgakjsdgfauiksygdfaiusdfiabfd," '
                                                          'does not appear to follow any standard '
                                                          'encoding or cipher that I can decode. It '
                                                          'seems to be a random string of characters.\n'
                                                          '\n'
                                                          'If you are looking for a specific type of '
                                                          'encoding or a cipher, please provide more '
                                                          'details, and I would be happy to help!',
                                               'role': 'AssistantAgent'}],
                                       is_tool_invoked=True,
                                       is_raised_exception=False,
                                       exception=None,
                                       tool_output='Incorrect Base64 data try: SFRUUEJJTiBpcyBhd2Vzb21l',
                                       tool_args='{"value":"asdhaksdgajkfdgakjsdgfauiksygdfaiusdfiabfd"}'
                                       ), result)

    @patch('autogen_agentchat.agents.AssistantAgent')
    def test_wiki_tool(self, mocked_agent):
        api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
        tool = WikipediaQueryRun(api_wrapper=api_wrapper)
        tool = LangChainToolAdapter(tool)

        mocked_agent.return_value = MockedAgent(tool)
        agent = AssistantAgentExecutor(tool, 'gpt-4o-mini')

        result = agent('Who is Alan Turing?')
        self.assertEqual(AgentResponse(
            agent_response="Alan Turing (23 June 1912 – 7 June 1954) was an English mathematician, logician, computer scientist, and cryptanalyst. He is best known for his pivotal role in the development of theoretical computer science and for his contributions to breaking the German Enigma code during World War II, which significantly aided the Allied forces.\n\nTuring is often regarded as the father of modern computer science for his conceptualization of the Turing machine, a fundamental model of computation that defines algorithms and computation. He also contributed to the fields of artificial intelligence and mathematical biology.\n\nIn addition to his scientific achievements, Turing faced significant personal challenges due to his homosexuality, which was criminalized in the UK at the time. In 1952, he was prosecuted for his sexual orientation, leading to a conviction that subjected him to chemical castration. Turing died in 1954 under circumstances that were ruled a suicide.\n\nHis legacy has been honored posthumously, including a formal apology from the British government in 2009 and a royal pardon in 2013. Turing's life and work have inspired many films, books, and academic studies, highlighting his profound impact on technology and society.",
            trace=[{'role': 'user', 'content': 'Who is Alan Turing?'},
                   {'role': 'assistant',
                    'content': '',
                    'tool_calls': [{'id': 'call_aaH2DjgT3SdO47cakOLsz9A0',
                                    'type': 'function',
                                    'function': {'name': 'wikipedia',
                                                 'arguments': '{"query":"Alan Turing"}'}}]},
                   {'role': 'tool',
                    'tool_call_id': 'call_aaH2DjgT3SdO47cakOLsz9A0',
                    'content': 'Page: Alan Turing\nSummary: Alan Mathison Turing (; 23 June 1912 – 7 June 1954) was an English mathem'},
                   {'role': 'AssistantAgent',
                    'content': "Alan Turing (23 June 1912 – 7 June 1954) was an English mathematician, logician, computer scientist, and cryptanalyst. He is best known for his pivotal role in the development of theoretical computer science and for his contributions to breaking the German Enigma code during World War II, which significantly aided the Allied forces.\n\nTuring is often regarded as the father of modern computer science for his conceptualization of the Turing machine, a fundamental model of computation that defines algorithms and computation. He also contributed to the fields of artificial intelligence and mathematical biology.\n\nIn addition to his scientific achievements, Turing faced significant personal challenges due to his homosexuality, which was criminalized in the UK at the time. In 1952, he was prosecuted for his sexual orientation, leading to a conviction that subjected him to chemical castration. Turing died in 1954 under circumstances that were ruled a suicide.\n\nHis legacy has been honored posthumously, including a formal apology from the British government in 2009 and a royal pardon in 2013. Turing's life and work have inspired many films, books, and academic studies, highlighting his profound impact on technology and society."}],
            tool_output='Page: Alan Turing\nSummary: Alan Mathison Turing (; 23 June 1912 – 7 June 1954) was an English mathem',
            is_tool_invoked=True,
            is_raised_exception=False,
            exception=None,
            tool_args='{"query":"Alan Turing"}',
        ), result)

    @patch('autogen_agentchat.agents.AssistantAgent')
    def test_composio_weather(self, mocked_agent):
        tool = ComposioToolSet().get_tools(apps=[App.WEATHERMAP])[0]

        mocked_agent.return_value = MockedAgent(tool)
        agent = AssistantAgentExecutor(tool, 'gpt-4o-mini')
        result = agent('What is the weather in Zurich?')

        self.assertEqual(AgentResponse(
            agent_response='The current weather in Zurich is clear with a temperature of approximately 15°C (288.15 K). The humidity level is at 39%, and there is a light wind blowing at 1.54 m/s from the northwest. Enjoy the beautiful weather!',
            trace=[{'content': 'What is the weather in Zurich?',
                    'role': 'user'},
                   {'content': '',
                    'role': 'assistant',
                    'tool_calls': [{'function': {'arguments': '{"location":"Zurich"}',
                                                 'name': 'WEATHERMAP_WEATHER_b404817b58'},
                                    'id': 'call_uNp6GYlnSWtTWTK4TFcbHHXt',
                                    'type': 'function'}]},
                   {
                       'content': "{'data': {'coord': {'lon': 8.55, 'lat': 47.3667}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 288.15, 'feels_like': 286.72, 'temp_min': 286.64, 'temp_max': 289.08, 'pressure': 1024, 'humidity': 39, 'sea_level': 1024, 'grnd_level': 965}, 'visibility': 10000, 'wind': {'speed': 1.54, 'deg': 300}, 'clouds': {'all': 0}, 'dt': 1741185556, 'sys': {'type': 1, 'id': 6932, 'country': 'CH', 'sunrise': 1741154320, 'sunset': 1741194973}, 'timezone': 3600, 'id': 2657896, 'name': 'Zurich', 'cod': 200}, 'error': None, 'successfull': True, 'successful': True}",
                       'role': 'tool',
                       'tool_call_id': 'call_uNp6GYlnSWtTWTK4TFcbHHXt'
                   },
                   {
                       'content': 'The current weather in Zurich is clear with a temperature of approximately 15°C (288.15 K). The humidity level is at 39%, and there is a light wind blowing at 1.54 m/s from the northwest. Enjoy the beautiful weather!',
                       'role': 'AssistantAgent'
                   }],
            is_tool_invoked=True,
            is_raised_exception=False,
            exception=None,
            tool_output="{'data': {'coord': {'lon': 8.55, 'lat': 47.3667}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 'main': {'temp': 288.15, 'feels_like': 286.72, 'temp_min': 286.64, 'temp_max': 289.08, 'pressure': 1024, 'humidity': 39, 'sea_level': 1024, 'grnd_level': 965}, 'visibility': 10000, 'wind': {'speed': 1.54, 'deg': 300}, 'clouds': {'all': 0}, 'dt': 1741185556, 'sys': {'type': 1, 'id': 6932, 'country': 'CH', 'sunrise': 1741154320, 'sunset': 1741194973}, 'timezone': 3600, 'id': 2657896, 'name': 'Zurich', 'cod': 200}, 'error': None, 'successfull': True, 'successful': True}",
            tool_args='{"location":"Zurich"}'), result)
