import unittest
from unittest.mock import patch

from composio_langchain import ComposioToolSet, App
from langchain_community.tools import ShellTool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

from src.eval.buggy_tools.open_street_map import open_street_map_search
from src.toolfuzz.agent_executors.agent_executor import AgentResponse
from src.toolfuzz.agent_executors.langchain.react_new import ReactAgentNew

messages = {
    "open_street_map_search": {'messages': [HumanMessage(
        content='Where can I find the restaurant named Shirikiklamankdatalukudikusdachdestrogenzdddddddddddzdasdadiopswagmagdseas near the Zurich Airport named Ablughafen?',
        additional_kwargs={}, response_metadata={}, id='83ad9b66-1ad4-489e-9506-196a424378b2'),
        AIMessage(content='', additional_kwargs={'tool_calls': [
            {'id': 'call_sKfNiCIpdBqhw2h6TjXYBaM4', 'function': {
                'arguments': '{"query":"Shirikiklamankdatalukudikusdachdestrogenzdddddddddddzdasdadiopswagmagdseas near Ablughafen, Zurich Airport"}',
                'name': 'open-street-map-search'}, 'type': 'function'}],
            'refusal': None},
                  response_metadata={
                      'token_usage': {'completion_tokens': 51,
                                      'prompt_tokens': 161,
                                      'total_tokens': 212,
                                      'completion_tokens_details': {
                                          'accepted_prediction_tokens': 0,
                                          'audio_tokens': 0,
                                          'reasoning_tokens': 0,
                                          'rejected_prediction_tokens': 0},
                                      'prompt_tokens_details': {
                                          'audio_tokens': 0,
                                          'cached_tokens': 0}},
                      'model_name': 'gpt-4o-mini-2024-07-18',
                      'system_fingerprint': 'fp_06737a9306',
                      'finish_reason': 'tool_calls', 'logprobs': None},
                  id='run-a34978fa-e497-4d25-aea4-e14c6ffd132a-0',
                  tool_calls=[{'name': 'open-street-map-search', 'args': {
                      'query': 'Shirikiklamankdatalukudikusdachdestrogenzdddddddddddzdasdadiopswagmagdseas near Ablughafen, Zurich Airport'},
                               'id': 'call_sKfNiCIpdBqhw2h6TjXYBaM4',
                               'type': 'tool_call'}],
                  usage_metadata={'input_tokens': 161, 'output_tokens': 51,
                                  'total_tokens': 212,
                                  'input_token_details': {'audio': 0,
                                                          'cache_read': 0},
                                  'output_token_details': {'audio': 0,
                                                           'reasoning': 0}}),
        ToolMessage(
            content="Error: AssertionError('Query is too long. Query must be less than 100 characters')\n Please fix your mistakes.",
            name='open-street-map-search',
            id='795ef25a-d307-47d8-b5b3-7fc744769c64',
            tool_call_id='call_sKfNiCIpdBqhw2h6TjXYBaM4', status='error')]},
    "terminal": {'messages': [
        HumanMessage(content='Where is my main file in the python project I have?', additional_kwargs={},
                     response_metadata={}, id='845db5df-fb17-4c27-8386-b7f67d1edba2'),
        AIMessage(
            content='In a typical Python project, the main file is usually the one that serves as the entry point for the application. Here are some common conventions to identify the main file:\n\n1. **File Name**: Look for a file named `main.py`, `app.py`, or similar. \n\n2. **`__main__` Block**: Check for a file that contains the following block of code:\n   ```python\n   if __name__ == "__main__":\n       ...\n   ```\n\n3. **Project Structure**: In a well-structured project, the main file is often located in the root directory or in a `src` or `app` folder.\n\n4. **Documentation**: If the project has a README file, it may specify which file to run.\n\nIf you can provide the directory structure of your project or the names of the files, I can help you identify the main file more accurately.',
            additional_kwargs={'refusal': None}, response_metadata={
                'token_usage': {'completion_tokens': 187, 'prompt_tokens': 133, 'total_tokens': 320,
                                'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0,
                                                              'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
                                'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
                'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_06737a9306', 'finish_reason': 'stop',
                'logprobs': None}, id='run-77a94e2c-965b-4e71-95ff-6f0f7e4e97cd-0',
            usage_metadata={'input_tokens': 133, 'output_tokens': 187, 'total_tokens': 320,
                            'input_token_details': {'audio': 0, 'cache_read': 0},
                            'output_token_details': {'audio': 0, 'reasoning': 0}})]},
    "weather": {'messages': [
        HumanMessage(content='What is the weather in Zurich atm?', additional_kwargs={}, response_metadata={},
                     id='5bb8e179-e4ea-454b-bb05-465c338de096'),
        AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_gLcsrPqquWdu0E0V6VdiuM6Q',
                                                                 'function': {'arguments': '{"location":"Zurich"}',
                                                                              'name': 'WEATHERMAP_WEATHER'},
                                                                 'type': 'function'}], 'refusal': None},
                  response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 113, 'total_tokens': 133,
                                                     'completion_tokens_details': {'accepted_prediction_tokens': 0,
                                                                                   'audio_tokens': 0,
                                                                                   'reasoning_tokens': 0,
                                                                                   'rejected_prediction_tokens': 0},
                                                     'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
                                     'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_06737a9306',
                                     'finish_reason': 'tool_calls', 'logprobs': None},
                  id='run-557d4dc8-5e98-4b42-be92-51bf127c32e5-0', tool_calls=[
                {'name': 'WEATHERMAP_WEATHER', 'args': {'location': 'Zurich'}, 'id': 'call_gLcsrPqquWdu0E0V6VdiuM6Q',
                 'type': 'tool_call'}], usage_metadata={'input_tokens': 113, 'output_tokens': 20, 'total_tokens': 133,
                                                        'input_token_details': {'audio': 0, 'cache_read': 0},
                                                        'output_token_details': {'audio': 0, 'reasoning': 0}}),
        ToolMessage(
            content='{"data": {"coord": {"lon": 8.55, "lat": 47.3667}, "weather": [{"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"}], "base": "stations", "main": {"temp": 278.97, "feels_like": 276.88, "temp_min": 277.61, "temp_max": 280.09, "pressure": 1022, "humidity": 63, "sea_level": 1022, "grnd_level": 963}, "visibility": 10000, "wind": {"speed": 2.68, "deg": 321, "gust": 3.58}, "rain": {"1h": 0.15}, "clouds": {"all": 100}, "dt": 1740756382, "sys": {"type": 2, "id": 2003379, "country": "CH", "sunrise": 1740722892, "sunset": 1740762528}, "timezone": 3600, "id": 2657896, "name": "Zurich", "cod": 200}, "error": null, "successfull": true, "successful": true}',
            name='WEATHERMAP_WEATHER', id='8ad0296c-e59e-4ca0-a2a8-ab862cdddaf2',
            tool_call_id='call_gLcsrPqquWdu0E0V6VdiuM6Q'),
        AIMessage(
            content="The current weather in Zurich is as follows:\n\n- **Condition**: Light rain\n- **Temperature**: 6.82°C (feels like 3.73°C)\n- **Humidity**: 63%\n- **Wind Speed**: 2.68 m/s\n- **Cloud Cover**: 100%\n- **Rainfall**: 0.15 mm in the last hour\n\nOverall, it's a rainy and cool day in Zurich.",
            additional_kwargs={'refusal': None}, response_metadata={
                'token_usage': {'completion_tokens': 96, 'prompt_tokens': 420, 'total_tokens': 516,
                                'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0,
                                                              'reasoning_tokens': 0, 'rejected_prediction_tokens': 0},
                                'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}},
                'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_06737a9306', 'finish_reason': 'stop',
                'logprobs': None}, id='run-990ea232-8496-491d-a441-ab011b9fa951-0',
            usage_metadata={'input_tokens': 420, 'output_tokens': 96, 'total_tokens': 516,
                            'input_token_details': {'audio': 0, 'cache_read': 0},
                            'output_token_details': {'audio': 0, 'reasoning': 0}})]}

}


class MockedAgent:
    def __init__(self, tool):
        if tool.name == 'open-street-map-search':
            self.message = messages['open_street_map_search']
        elif tool.name == 'terminal':
            self.message = messages['terminal']
        else:
            self.message = messages['weather']

    def invoke(self, *args, **kwargs):
        return self.message


class TestReactAgentNew(unittest.TestCase):
    @patch('langgraph.prebuilt.create_react_agent')
    def test_open_street_map(self, mocked_create_agent):
        mocked_langchain_agent = MockedAgent(tool=open_street_map_search)
        mocked_create_agent.return_value = mocked_langchain_agent

        agent = ReactAgentNew(tool=open_street_map_search, model='gpt-4o')
        result = agent('Where can I find the restaurant named Shirikiklama near the Zurich Airport named Ablughafen?')

        self.assertEqual(AgentResponse(
            agent_response='Error: AssertionError(\'Query is too long. Query must be less than 100 characters\')\n Please fix your mistakes.',
            trace=[{
                'content': 'Where can I find the restaurant named Shirikiklamankdatalukudikusdachdestrogenzdddddddddddzdasdadiopswagmagdseas near the Zurich Airport named Ablughafen?',
                'role': 'user'}, {'content': '', 'role': 'assistant', 'tool_calls': [{'function': {
                'arguments': '{"query":"Shirikiklamankdatalukudikusdachdestrogenzdddddddddddzdasdadiopswagmagdseas near Ablughafen, Zurich Airport"}',
                'name': 'open-street-map-search'}, 'id': 1, 'type': 'function'}]}, {
                'content': "Error: AssertionError('Query is too long. Query must be less than 100 characters')\n Please fix your mistakes.",
                'role': 'tool', 'tool_call_id': 1}],
            is_tool_invoked=True,
            is_raised_exception=True,
            exception="AssertionError('Query is too long. Query must be less than 100 characters')",
            tool_output='Error: AssertionError(\'Query is too long. Query must be less than 100 characters\')\n Please fix your mistakes.',
            tool_args='{"query":"Shirikiklamankdatalukudikusdachdestrogenzdddddddddddzdasdadiopswagmagdseas near Ablughafen, Zurich Airport"}'
        ), result)

    @patch('langgraph.prebuilt.create_react_agent')
    def test_terminal(self, mocked_create_agent):
        mocked_agent = MockedAgent(tool=ShellTool())
        mocked_create_agent.return_value = mocked_agent

        agent = ReactAgentNew(tool=ShellTool(), model='gpt-4o')
        result = agent('Where is my main file in the python project I have?')

        self.assertEqual(AgentResponse(
            agent_response='In a typical Python project, the main file is usually the one that serves as the entry point for the application. Here are some common conventions to identify the main file:\n\n1. **File Name**: Look for a file named `main.py`, `app.py`, or similar. \n\n2. **`__main__` Block**: Check for a file that contains the following block of code:\n   ```python\n   if __name__ == "__main__":\n       ...\n   ```\n\n3. **Project Structure**: In a well-structured project, the main file is often located in the root directory or in a `src` or `app` folder.\n\n4. **Documentation**: If the project has a README file, it may specify which file to run.\n\nIf you can provide the directory structure of your project or the names of the files, I can help you identify the main file more accurately.',
            trace=[{'content': 'Where is my main file in the python project I have?', 'role': 'user'}, {
                'content': 'In a typical Python project, the main file is usually the one that serves as the entry point for the application. Here are some common conventions to identify the main file:\n\n1. **File Name**: Look for a file named `main.py`, `app.py`, or similar. \n\n2. **`__main__` Block**: Check for a file that contains the following block of code:\n   ```python\n   if __name__ == "__main__":\n       ...\n   ```\n\n3. **Project Structure**: In a well-structured project, the main file is often located in the root directory or in a `src` or `app` folder.\n\n4. **Documentation**: If the project has a README file, it may specify which file to run.\n\nIf you can provide the directory structure of your project or the names of the files, I can help you identify the main file more accurately.',
                'role': 'assistant', 'tool_calls': []}],
            is_tool_invoked=False,
            is_raised_exception=False,
            exception='',
            tool_output='No tool output found',
            tool_args=None
        ),
            result)

    @patch('langgraph.prebuilt.create_react_agent')
    def test_weather(self, mocked_create_agent):
        tool = ComposioToolSet().get_tools(apps=[App.WEATHERMAP])[0]
        mocked_agent = MockedAgent(tool=tool)
        mocked_create_agent.return_value = mocked_agent

        agent = ReactAgentNew(tool, 'gpt-4o')
        result = agent('What is the weather in Zurich atm?')

        self.assertEqual(AgentResponse(
            agent_response="The current weather in Zurich is as follows:\n\n- **Condition**: Light rain\n- **Temperature**: 6.82°C (feels like 3.73°C)\n- **Humidity**: 63%\n- **Wind Speed**: 2.68 m/s\n- **Cloud Cover**: 100%\n- **Rainfall**: 0.15 mm in the last hour\n\nOverall, it's a rainy and cool day in Zurich.",
            trace=[{'content': 'What is the weather in Zurich atm?',
                    'role': 'user'},
                   {'content': '',
                    'role': 'assistant',
                    'tool_calls': [{'function': {'arguments': '{"location":"Zurich"}',
                                                 'name': 'WEATHERMAP_WEATHER'},
                                    'id': 1,
                                    'type': 'function'}]},
                   {'content': '{"data": {"coord": {"lon": 8.55, "lat": '
                               '47.3667}, "weather": [{"id": 500, "main": '
                               '"Rain", "description": "light rain", "icon": '
                               '"10d"}], "base": "stations", "main": '
                               '{"temp": 278.97, "feels_like": 276.88, '
                               '"temp_min": 277.61, "temp_max": 280.09, '
                               '"pressure": 1022, "humidity": 63, '
                               '"sea_level": 1022, "grnd_level": 963}, '
                               '"visibility": 10000, "wind": {"speed": 2.68, '
                               '"deg": 321, "gust": 3.58}, "rain": {"1h": '
                               '0.15}, "clouds": {"all": 100}, "dt": '
                               '1740756382, "sys": {"type": 2, "id": '
                               '2003379, "country": "CH", "sunrise": '
                               '1740722892, "sunset": 1740762528}, '
                               '"timezone": 3600, "id": 2657896, "name": '
                               '"Zurich", "cod": 200}, "error": null, '
                               '"successfull": true, "successful": true}',
                    'role': 'tool',
                    'tool_call_id': 1},
                   {'content': 'The current weather in Zurich is as '
                               'follows:\n'
                               '\n'
                               '- **Condition**: Light rain\n'
                               '- **Temperature**: 6.82°C (feels like '
                               '3.73°C)\n'
                               '- **Humidity**: 63%\n'
                               '- **Wind Speed**: 2.68 m/s\n'
                               '- **Cloud Cover**: 100%\n'
                               '- **Rainfall**: 0.15 mm in the last hour\n'
                               '\n'
                               "Overall, it's a rainy and cool day in "
                               'Zurich.',
                    'role': 'assistant',
                    'tool_calls': []}],
            is_tool_invoked=True,
            is_raised_exception=False,
            exception='',
            tool_output='{"data": {"coord": {"lon": 8.55, "lat": 47.3667}, "weather": [{"id": 500, "main": "Rain", "description": "light rain", "icon": "10d"}], "base": "stations", "main": {"temp": 278.97, "feels_like": 276.88, "temp_min": 277.61, "temp_max": 280.09, "pressure": 1022, "humidity": 63, "sea_level": 1022, "grnd_level": 963}, "visibility": 10000, "wind": {"speed": 2.68, "deg": 321, "gust": 3.58}, "rain": {"1h": 0.15}, "clouds": {"all": 100}, "dt": 1740756382, "sys": {"type": 2, "id": 2003379, "country": "CH", "sunrise": 1740722892, "sunset": 1740762528}, "timezone": 3600, "id": 2657896, "name": "Zurich", "cod": 200}, "error": null, "successfull": true, "successful": true}',
            tool_args='{"location":"Zurich"}'
        ), result)
