import json
import unittest
from unittest.mock import patch

from composio_llamaindex import App, ComposioToolSet
from llama_index.core.chat_engine.types import AgentChatResponse
from llama_index.core.tools import ToolOutput
from llama_index.core.tools.tool_spec.load_and_search import LoadAndSearchToolSpec
from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from llama_index.tools.wikipedia import WikipediaToolSpec

from src.toolfuzz.agent_executors.agent_executor import AgentResponse
from src.toolfuzz.agent_executors.llama_index.openai_agent import OpenAIAgentExecutor

messages = {'search_data': AgentChatResponse(
    response='Alan Turing was a British mathematician, logician, cryptanalyst, and computer scientist, widely considered to be one of the fathers of computer science and artificial intelligence. He was born on June 23, 1912, and is best known for his role in breaking the German Enigma code during World War II, which significantly contributed to the Allied victory.\n\nTuring developed the concept of the Turing machine, a theoretical construct that forms the basis of modern computing. He also proposed the Turing test, a criterion for determining whether a machine exhibits human-like intelligence.\n\nDespite his monumental contributions, Turing faced persecution due to his homosexuality, which was criminalized in the UK at the time. In 1952, he was convicted of "gross indecency" and underwent chemical castration. Turing died on June 7, 1954, under circumstances that are widely believed to be suicide.\n\nIn recent years, Turing has been posthumously recognized for his contributions to science and society, and he was granted a royal pardon in 2013. His legacy continues to influence the fields of mathematics, computer science, and artificial intelligence.',
    sources=[ToolOutput(content='Content loaded! You can now search the information using read_search_data',
                        tool_name='search_data', raw_input={'args': (), 'kwargs': {'query': 'Alan Turing'}},
                        raw_output='Content loaded! You can now search the information using read_search_data',
                        is_error=False)], source_nodes=[], is_dummy_stream=False, metadata=None),
    'duckduckgo_instant_search': AgentChatResponse(
        response="The safety of LLM (Large Language Model) agents can depend on various factors, including their design, implementation, and the context in which they are used. Here are some considerations regarding their safety:\n\n1. **Bias and Misinformation**: LLMs can inadvertently generate biased or misleading information based on the data they were trained on. This can lead to the propagation of stereotypes or false information.\n\n2. **Privacy Concerns**: If LLMs are trained on sensitive data, there may be risks related to privacy and data security. It's essential to ensure that they do not inadvertently reveal personal information.\n\n3. **Manipulation and Misuse**: LLMs can be used to create convincing fake content, which can be exploited for malicious purposes, such as spreading disinformation or phishing attacks.\n\n4. **Dependence on Technology**: Over-reliance on LLMs for decision-making can lead to a lack of critical thinking and human oversight, which can be dangerous in high-stakes situations.\n\n5. **Ethical Considerations**: The deployment of LLMs raises ethical questions about accountability, transparency, and the potential impact on jobs and society.\n\nTo ensure safety, it's crucial to implement robust guidelines, conduct thorough testing, and maintain human oversight when using LLM agents.",
        sources=[ToolOutput(content='[]', tool_name='duckduckgo_instant_search',
                            raw_input={'args': (), 'kwargs': {'query': 'Are LLM Agents safe?'}}, raw_output=[],
                            is_error=False)], source_nodes=[], is_dummy_stream=False, metadata=None),
    'WEATHERMAP_WEATHER': AgentChatResponse(
        response="The current weather in Zurich is as follows:\n\n- **Condition**: Light rain\n- **Temperature**: Approximately 5.8°C (feels like 1.3°C)\n- **Humidity**: 70%\n- **Wind Speed**: 4.63 m/s from the east\n- **Cloud Cover**: 75%\n- **Rainfall**: 0.15 mm in the last hour\n\nOverall, it's a cool and rainy day in Zurich.",
        sources=[ToolOutput(
            content="{'data': {'coord': {'lon': 8.55, 'lat': 47.3667}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 277.96, 'feels_like': 274.43, 'temp_min': 276.4, 'temp_max': 278.58, 'pressure': 1026, 'humidity': 70, 'sea_level': 1026, 'grnd_level': 966}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 90}, 'rain': {'1h': 0.15}, 'clouds': {'all': 75}, 'dt': 1740848521, 'sys': {'type': 2, 'id': 2019255, 'country': 'CH', 'sunrise': 1740809179, 'sunset': 1740849018}, 'timezone': 3600, 'id': 2657896, 'name': 'Zurich', 'cod': 200}, 'error': None, 'successfull': True, 'successful': True}",
            tool_name='WEATHERMAP_WEATHER', raw_input={'args': (), 'kwargs': {'location': 'Zurich'}}, raw_output={
                'data': {'coord': {'lon': 8.55, 'lat': 47.3667},
                         'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}],
                         'base': 'stations',
                         'main': {'temp': 277.96, 'feels_like': 274.43, 'temp_min': 276.4, 'temp_max': 278.58,
                                  'pressure': 1026, 'humidity': 70, 'sea_level': 1026, 'grnd_level': 966},
                         'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 90}, 'rain': {'1h': 0.15},
                         'clouds': {'all': 75}, 'dt': 1740848521,
                         'sys': {'type': 2, 'id': 2019255, 'country': 'CH', 'sunrise': 1740809179,
                                 'sunset': 1740849018}, 'timezone': 3600, 'id': 2657896, 'name': 'Zurich', 'cod': 200},
                'error': None, 'successfull': True, 'successful': True}, is_error=False)], source_nodes=[],
        is_dummy_stream=False, metadata=None)
}


def get_weather(location: str) -> str:
    """Useful for getting the weather for a given location."""
    loc = json.loads(location)
    assert 'name' in loc
    place = loc['name']
    return f"The weather in {place} is sunny"


class MockedAgent:
    def __init__(self, tool):
        self.tool = tool

    def chat(self, prompt, **kwargs):
        return messages[self.tool.metadata.name]


class TestLlamaIndexOpenai(unittest.TestCase):
    @patch('llama_index.agent.openai.OpenAIAgent.from_tools')
    def test_wiki_tool(self, mocked_agent):
        wiki_spec = WikipediaToolSpec()
        tool = wiki_spec.to_tool_list()[1]
        tool = LoadAndSearchToolSpec.from_defaults(tool).to_tool_list()[0]

        mocked_agent.return_value = MockedAgent(tool)
        agent = OpenAIAgentExecutor(tool, 'gpt-4o-mini')

        result = agent("Who is Alan Turing?")
        self.assertEqual(AgentResponse(
            agent_response='Alan Turing was a British mathematician, logician, cryptanalyst, and computer scientist, widely considered to be one of the fathers of computer science and artificial intelligence. He was born on June 23, 1912, and is best known for his role in breaking the German Enigma code during World War II, which significantly contributed to the Allied victory.\n\nTuring developed the concept of the Turing machine, a theoretical construct that forms the basis of modern computing. He also proposed the Turing test, a criterion for determining whether a machine exhibits human-like intelligence.\n\nDespite his monumental contributions, Turing faced persecution due to his homosexuality, which was criminalized in the UK at the time. In 1952, he was convicted of "gross indecency" and underwent chemical castration. Turing died on June 7, 1954, under circumstances that are widely believed to be suicide.\n\nIn recent years, Turing has been posthumously recognized for his contributions to science and society, and he was granted a royal pardon in 2013. His legacy continues to influence the fields of mathematics, computer science, and artificial intelligence.',
            trace=[{'content': 'Who is Alan Turing?', 'role': 'user'},
                   {'function': {'arguments': "{'args': (), 'kwargs': "
                                              "{'query': 'Alan Turing'}}",
                                 'name': 'search_data'},
                    'id': '',
                    'role': 'function'},
                   {'content': 'Content loaded! You can now search the information using read_search_data',
                    'role': 'tool',
                    'tool_call_id': ''},
                   {
                       'content': 'Alan Turing was a British mathematician, logician, cryptanalyst, and computer scientist, widely considered to be one of the fathers of computer science and artificial intelligence. He was born on June 23, 1912, and is best known for his role in breaking the German Enigma code during World War II, which significantly contributed to the Allied victory.\n\nTuring developed the concept of the Turing machine, a theoretical construct that forms the basis of modern computing. He also proposed the Turing test, a criterion for determining whether a machine exhibits human-like intelligence.\n\nDespite his monumental contributions, Turing faced persecution due to his homosexuality, which was criminalized in the UK at the time. In 1952, he was convicted of "gross indecency" and underwent chemical castration. Turing died on June 7, 1954, under circumstances that are widely believed to be suicide.\n\nIn recent years, Turing has been posthumously recognized for his contributions to science and society, and he was granted a royal pardon in 2013. His legacy continues to influence the fields of mathematics, computer science, and artificial intelligence.',
                       'role': 'assistant',
                       'tool_calls': []}],
            is_tool_invoked=True,
            is_raised_exception=False,
            exception='',
            tool_output='Content loaded! You can now search the information using read_search_data',
            tool_args="{'args': (), 'kwargs': {'query': 'Alan Turing'}}"
        ), result)

    @patch('llama_index.agent.openai.OpenAIAgent.from_tools')
    def test_duckduckgo_tool(self, mocked_agent):
        tool = DuckDuckGoSearchToolSpec().to_tool_list()[0]

        mocked_agent.return_value = MockedAgent(tool)

        agent = OpenAIAgentExecutor(tool, 'gpt-4o-mini')
        result = agent('Are LLM Agent\'s safe?')

        self.assertEqual(AgentResponse(
            agent_response="The safety of LLM (Large Language Model) agents can depend on various factors, including their design, implementation, and the context in which they are used. Here are some considerations regarding their safety:\n\n1. **Bias and Misinformation**: LLMs can inadvertently generate biased or misleading information based on the data they were trained on. This can lead to the propagation of stereotypes or false information.\n\n2. **Privacy Concerns**: If LLMs are trained on sensitive data, there may be risks related to privacy and data security. It's essential to ensure that they do not inadvertently reveal personal information.\n\n3. **Manipulation and Misuse**: LLMs can be used to create convincing fake content, which can be exploited for malicious purposes, such as spreading disinformation or phishing attacks.\n\n4. **Dependence on Technology**: Over-reliance on LLMs for decision-making can lead to a lack of critical thinking and human oversight, which can be dangerous in high-stakes situations.\n\n5. **Ethical Considerations**: The deployment of LLMs raises ethical questions about accountability, transparency, and the potential impact on jobs and society.\n\nTo ensure safety, it's crucial to implement robust guidelines, conduct thorough testing, and maintain human oversight when using LLM agents.",
            trace=[{'role': 'user', 'content': "Are LLM Agent's safe?"},
                   {'role': 'function',
                    'id': '',
                    'function': {'name': 'duckduckgo_instant_search',
                                 'arguments': "{'args': (), 'kwargs': {'query': 'Are LLM Agents safe?'}}"}},
                   {'role': 'tool', 'tool_call_id': '', 'content': '[]'},
                   {'role': 'assistant',
                    'content': "The safety of LLM (Large Language Model) agents can depend on various factors, including their design, implementation, and the context in which they are used. Here are some considerations regarding their safety:\n\n1. **Bias and Misinformation**: LLMs can inadvertently generate biased or misleading information based on the data they were trained on. This can lead to the propagation of stereotypes or false information.\n\n2. **Privacy Concerns**: If LLMs are trained on sensitive data, there may be risks related to privacy and data security. It's essential to ensure that they do not inadvertently reveal personal information.\n\n3. **Manipulation and Misuse**: LLMs can be used to create convincing fake content, which can be exploited for malicious purposes, such as spreading disinformation or phishing attacks.\n\n4. **Dependence on Technology**: Over-reliance on LLMs for decision-making can lead to a lack of critical thinking and human oversight, which can be dangerous in high-stakes situations.\n\n5. **Ethical Considerations**: The deployment of LLMs raises ethical questions about accountability, transparency, and the potential impact on jobs and society.\n\nTo ensure safety, it's crucial to implement robust guidelines, conduct thorough testing, and maintain human oversight when using LLM agents.",
                    'tool_calls': []}],
            is_tool_invoked=True,
            is_raised_exception=False,
            exception='',
            tool_output='[]',
            tool_args="{'args': (), 'kwargs': {'query': 'Are LLM Agents safe?'}}"
        ), result)

    @patch('llama_index.agent.openai.OpenAIAgent.from_tools')
    def test_weather_tool(self, mocked_agent):
        tool = ComposioToolSet().get_tools(apps=[App.WEATHERMAP])[0]

        mocked_agent.return_value = MockedAgent(tool)

        agent = OpenAIAgentExecutor(tool, 'gpt-4o-mini')
        result = agent('What is the weather in Zurich?')

        self.assertEqual(AgentResponse(
            agent_response="The current weather in Zurich is as follows:\n\n- **Condition**: Light rain\n- **Temperature**: Approximately 5.8°C (feels like 1.3°C)\n- **Humidity**: 70%\n- **Wind Speed**: 4.63 m/s from the east\n- **Cloud Cover**: 75%\n- **Rainfall**: 0.15 mm in the last hour\n\nOverall, it's a cool and rainy day in Zurich.",
            trace=[{'content': 'What is the weather in Zurich?',
                    'role': 'user'},
                   {'function': {'arguments': "{'args': (), 'kwargs': "
                                              "{'location': 'Zurich'}}",
                                 'name': 'WEATHERMAP_WEATHER'},
                    'id': '',
                    'role': 'function'},
                   {
                       'content': "{'data': {'coord': {'lon': 8.55, 'lat': 47.3667}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 277.96, 'feels_like': 274.43, 'temp_min': 276.4, 'temp_max': 278.58, 'pressure': 1026, 'humidity': 70, 'sea_level': 1026, 'grnd_level': 966}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 90}, 'rain': {'1h': 0.15}, 'clouds': {'all': 75}, 'dt': 1740848521, 'sys': {'type': 2, 'id': 2019255, 'country': 'CH', 'sunrise': 1740809179, 'sunset': 1740849018}, 'timezone': 3600, 'id': 2657896, 'name': 'Zurich', 'cod': 200}, 'error': None, 'successfull': True, 'successful': True}",
                       'role': 'tool',
                       'tool_call_id': ''},
                   {
                       'content': "The current weather in Zurich is as follows:\n\n- **Condition**: Light rain\n- **Temperature**: Approximately 5.8°C (feels like 1.3°C)\n- **Humidity**: 70%\n- **Wind Speed**: 4.63 m/s from the east\n- **Cloud Cover**: 75%\n- **Rainfall**: 0.15 mm in the last hour\n\nOverall, it's a cool and rainy day in Zurich.",
                       'role': 'assistant',
                       'tool_calls': []}],
            is_tool_invoked=True,
            is_raised_exception=False,
            exception='',
            tool_output="{'data': {'coord': {'lon': 8.55, 'lat': 47.3667}, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'base': 'stations', 'main': {'temp': 277.96, 'feels_like': 274.43, 'temp_min': 276.4, 'temp_max': 278.58, 'pressure': 1026, 'humidity': 70, 'sea_level': 1026, 'grnd_level': 966}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 90}, 'rain': {'1h': 0.15}, 'clouds': {'all': 75}, 'dt': 1740848521, 'sys': {'type': 2, 'id': 2019255, 'country': 'CH', 'sunrise': 1740809179, 'sunset': 1740849018}, 'timezone': 3600, 'id': 2657896, 'name': 'Zurich', 'cod': 200}, 'error': None, 'successfull': True, 'successful': True}",
            tool_args="{'args': (), 'kwargs': {'location': 'Zurich'}}"
        ), result)
