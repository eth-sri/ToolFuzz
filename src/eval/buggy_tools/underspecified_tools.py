import json
import math
from typing import List, Optional

from src.eval.toolfuzz.information_provider import TestInformationProvider
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import tool, BaseTool
from langchain.pydantic_v1 import BaseModel, Field

from src.eval.buggy_tools.decorators import tool_description, valid_prompt, breaking_prompt
from src.eval.toolfuzz.utils.assert_lambdas import assert_contains, assert_tool_call


class ClothingSorterInput(BaseModel):
    sizes: List[int] = Field(description="The size of the item.")
    designer: str = Field(description="The designer of the item.")  # brand
    colors: List[str] = Field(description="The email of the user who sent the email.")
    min_budget: int = Field(description="The minimum budget you have for this item")  # min_price
    max_budget: int = Field(description="The maximum budget you have for this item")  # max_price
    template: str = Field(description="Some template (figures or shapes or items) that is in search")  # pattern
    collection: str = Field(description="From which collection the item has to be")
    type: str = Field(description="The type of the item i.e. clothing piece, shoes, hats etc.")


@valid_prompt(
    "Can you find me T-shirt for at least 10 usd but max 50 usd, I would like it to have one of few patterns i.e. "
    "first square pattern, second traditional bulgarian pattern or just a casual flower pattern, be from the brand "
    "Quick Silver, also from the autumn collection please",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                            'T-shirt'))
@breaking_prompt("I want to buy shoes in size 23 with price range of 100 to 250 usd.",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         'T-shirt'))
@tool_description("Tool which is underspecified and this leads to misuse of the parameters of the function")
@tool("find-clothing", return_direct=True)
def find_clothes(sizes: List[int], designer: str, colors: List[str], min_budget: int, max_budget: int, template: str,
                 collection: str, type: str):
    """
    This tool is useful for filtering clothing items.
    """
    return (f"There is {type} in size {sizes} from {designer} with colors: {colors}\n"
            f"The items is within your budget of {min_budget} - {max_budget} and has a pattern of {template}"
            f"It is the Nike Hoodie from {collection} collection.")


@breaking_prompt(
    "Using the compute-law-of-cosines tool which can compute side c with the law of cosines can you compute C knowing "
    "the angle between two sides is 36 degrees and the sides are 2",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'missing param'))
@tool_description(
    "Tool works only for right triangles but doesn't specify it! Note that you cannot make the llm to hallucinate new "
    "parameters as the langchain framework will parse the output according to the pydantic model")
@tool("compute-law-of-cosines", return_direct=True)
def compute_law_of_cosines(json_parameters: str):
    """
    Tool which can compute side c with the law of cosines.

    parameters:
        {'side_a': one side of the triangle, 'side_b': another side of the triangle}
    """

    params = json.loads(json_parameters)
    # Assert that there are no additional parameters:
    # Maybe this is not the case in another frameworks not sure.
    assert len(params.keys()) == 2, params
    assert 'side_a' in params, params
    assert 'side_b' in params, params
    # The tool doesn't say that it actually works only for 90 degree triangles
    return math.sqrt(int(params['side_a']) ** 2 + int(params['side_b']) ** 2)


class ContentInput(BaseModel):
    content: str = Field("The content of a fairy tale which will be summarized")


@breaking_prompt("""Can you shorten this message:
And then, all of a sudden, he said "Pop!" just as if a cork were coming out of a bottle.

And Christopher Robin and Rabbit and all Rabbit's friends and relations went head-over-heels backwards ... and on the top of them came Winnie-the-Pooh—free!

So, with a nod of thanks to his friends, he went on with his walk through the forest, humming proudly to himself. But, Christopher Robin looked after him lovingly, and said to himself, "Silly old Bear!"
""",
                 lambda test_self, agent_invoke, params: assert_tool_call(test_self, agent_invoke, params))
@tool_description(
    "The tool has too concrete description on a common LLM task which will result in the LLM not being able to "
    "recognise when to call it")
@tool('summarize-fairy-tale-content', args_schema=ContentInput, return_direct=True)
def summarize_fairy_tale_content(content: str) -> str:
    """
    Tool to summarize fairy tales given their content. This tool can summarize the likes of: Hansel and Gretel,
    Snow White, The Golden Fish, Rapunzel, The little Mermaid and so on.
    """

    return f"{content[:100]}"


# This tool is inspired by PubMed's and Merriam-Webster's tools
class ApiWrapper(BaseModel):
    api_key: Optional[str] = None

    def run(self, query: str) -> str:
        return f"result for {query}: 'The weather today is 25 degrees'"


class WeatherQueryRun(BaseTool):
    """Tool that searches the Weather API."""

    name: str = "weather_tool"
    description: str = (
        "A wrapper around Weather API. "
        "Useful for when you need to get the Weather for the day."
        "Input should be the day for which you want to know the weather."
    )
    api_wrapper: ApiWrapper = ApiWrapper()

    valid_prompt: List[TestInformationProvider] = [TestInformationProvider('', lambda _, __, ___: True)]
    breaking_prompt: List[TestInformationProvider] = [TestInformationProvider('What will be the weather today?',
                                                                              lambda test_self, agent_invoke,
                                                                                     params: assert_contains(test_self,
                                                                                                             agent_invoke,
                                                                                                             params,
                                                                                                             "25"))]

    def _run(
            self,
            query: str,
            run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the Weather tool."""
        return self.api_wrapper.run(query)


class TranslateInput(BaseModel):
    text: str = Field(description="The text to be translated")
    from_lang: str = Field(
        description="The language from which the text has to be translated. Available languages are ['french', "
                    "'english', 'german]")
    to_lang: str = Field(
        description="The language to which the text has to be translated. Available languages are ['french', "
                    "'english', 'german']")


@valid_prompt("Can you translate me the short sentence 'Hello my name is Ivan' to the language spoken in Monaco?",
              lambda test_self, agent_invoke, params: assert_tool_call(test_self, agent_invoke, params))
@breaking_prompt(
    "Can you translate me the text 'Hello my name is Ivan' to the language spoken in Monaco?",
    lambda test_self, agent_invoke, params: assert_tool_call(test_self, agent_invoke, params))
@tool_description("The tool is used for a common task and the LLM doesn't recognise it always")
@tool('translate-paragraphs', args_schema=TranslateInput, return_direct=True)
def translate_paragraphs(text: str, from_lang: str, to_lang: str):
    """
    Tool for specifically translating long paragraphs of texts. This tool is useful in the case one wants to translate a whole book or few articles at a time
    """
    if to_lang == 'french':
        return 'Voici un texte simple à traduire'
    elif to_lang == 'german':
        return 'Hey, dies ist ein einfacher zu übersetzender Text'
    elif to_lang == 'english':
        return 'Hey this is a simple text to be translated'


class PersonalTrainerInput(BaseModel):
    question: str = Field(description="The user's question related to fitness routines, diet etc.")
    height: float = Field(description="The height of the user asking in KG")
    weight: float = Field(description="The weight of the user asking in cm")


@valid_prompt(
    "I am a small guy 150 cm tall, who is super skinny - 45 kilos. People bully me, I want them to know I can protect myself",
    lambda test_self, agent_invoke, params: assert_tool_call(test_self, agent_invoke, params))
@breaking_prompt("I am a small guy, who is super skinny. People bully me quite a lot because I seem vulnerable ("
                 "physically). I am wondering if it is possible for a short guy 150, who is weighing less than a well "
                 "fed dog (45 killos) to make it such that people know I can protect myself",
                 lambda test_self, agent_invoke, params: assert_tool_call(test_self, agent_invoke, params))
@tool_description(
    "personal trainer is a tool which has too broad of a description which sometimes prevents the LLM of calling it")
@tool('personal-trainer', args_schema=PersonalTrainerInput, return_direct=True)
def personal_trainer(question: str, height: float, weight: float):
    """
    Tool which gives general health advice.
    """

    if 'food' in question:
        return (f'For your height {height} and weight{weight}, you should reduce your calories intake to 1500 calories '
                f'per day.')
    else:
        return (f'For your height {height} and weight{weight}, you should do 5 series of 5 pull ups followed by 5 '
                f'series of 15 push ups.')


class KBSearchInput(BaseModel):
    query: str = Field(description="Search query for the knowledge base of TchaikaPharma")


@valid_prompt("What drugs use mRNA?",
              lambda test_self, agent_invoke, params: assert_tool_call(test_self, agent_invoke, params))
@breaking_prompt("Where is mRNA used?",
                 lambda test_self, agent_invoke, params: assert_tool_call(test_self, agent_invoke, params))
@tool_description(
    "Tool which is quite specific and sometimes might not be called from the LLM, but rather the llm will answer directly")
@tool('knowledge-base-search', args_schema=KBSearchInput, return_direct=True)
def knowledge_base_search(query: str):
    """
    Tool to search through TchaikaPharma's knowledge base. Can be used whenever we are looking for some information related to TchaikaPharma's medicines.
    """

    return (
        "Remifentanil-Tchaikapharma contains a medicine called remifentanil. This belongs to a group of medicines known as opioids.\n"
        "Levor tablets contain a medicine called levofloxacin. It belongs to a group of medicines called quinolone antimicrobials and works by killing the bacteria that cause infections.")


class ExersiceInput(BaseModel):
    text: str = Field(description="The open close exersice. Sentence which contains ____")


@valid_prompt("I am writing a novel, can you help me finish the last sentence of it 'This is what I need the most '",
              lambda test_self, agent_invoke, params: assert_tool_call(test_self, agent_invoke, params))
@breaking_prompt(
    "I am writting a novel, can you help me finish the last sentence of it 'This is what I need the most '",
    lambda test_self, agent_invoke, params: assert_tool_call(test_self, agent_invoke, params))
@tool('ivanovices_open_close_solver', args_schema=ExersiceInput, return_direct=True)
def ivanovices_open_close_solver(text: str):
    """
    Tool which solves open close exercises typically found in the Reading and Use of English paper in English exams.
    The exercise text should contain blanks (e.g., '_____') that need to be filled in.
    """

    return text
