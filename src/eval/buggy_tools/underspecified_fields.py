import json
import time
from datetime import datetime
from urllib.parse import urlparse

from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field

from src.eval.buggy_tools.decorators import tool_description, valid_prompt, breaking_prompt
from src.eval.toolfuzz.utils.assert_lambdas import assert_contains


class SearchMailInput(BaseModel):
    keywords: str = Field(description="Keywords which will be used for filtering (searching) the email inbox.")
    label: str = Field(description="Assigned label to the email.")  # underspecified, this is enum of few labels
    # labels are -> INBOX, SPAM, TRASH, UNREAD, STARRED, IMPORTANT
    sender_email: str = Field(description="The email of the user who sent the email.")


@valid_prompt("What mail did I get in SPAM from royalty@mail.ng about diamonds",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      "I have 10K diamonds which I need to ship to EU"))
@breaking_prompt(
    "Can you find my email with label finance which is related to my taxes?",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                            "label"))
@tool_description("Tool which will break because of underspecified fields descriptions for enum values.")
@tool("search-mail", args_schema=SearchMailInput, return_direct=True)
def search_mail(keywords: str, label: str, sender_email: str):
    """
    This tools can search your email box. Useful when you want to find something from your emails!
    """

    mails = [{'sender': 'test@abv.bg', 'content': 'work mail', 'label': 'INBOX'},
             {'sender': 'royalty@mail.ng', 'content': 'I have 10K diamonds which I need to ship to EU',
              'label': 'SPAM'},
             {'sender': 'admin@eth.ng', 'content': "It's time to do your thesis", 'label': 'SPAM'}]

    # simulate API valdiation:
    assert label in ['INBOX', 'SPAM', 'TRASH', 'UNREAD', 'STARRED', 'IMPORTANT'], f"Invalid label: '{label}'"
    mails = [mail for mail in mails if label.lower() == mail['label'].lower()]
    mails = [mail for mail in mails if keywords.lower() in mail['content']]
    mails = [mail for mail in mails if sender_email.lower() == mail['sender']]
    return mails


class JsonFilterInput(BaseModel):
    query: str = Field(description="The search query for the json to be searched. It should be ThingWorx style query.")


@valid_prompt("""Can you filter a json file with the following query:
{
    "select": [
        {
            "dataShapeName": "PTC.SCA.SCO.JobOrderProcessingResourceRequirement",
            "fieldName": "Name"
        },
        {
            "dataShapeName": "PTC.SCA.SCO.JobOrder",
            "fieldName": "Name"
        },
        {
            "dataShapeName": "PTC.SCA.SCO.JobOrder",
            "fieldName": "ID"
        },
        {
            "dataShapeName": "PTC.SCA.SCO.ProcessingResource",
            "fieldName": "Name"
        }
    ],
    "filters": {
        "filters": [
            {
                "dataShapeName": "PTC.SCA.SCO.ProcessingResource",
                "fieldName": "ID",
                "type": "EQ",
                "value": "WC1"
            }
        ],
        "type": "AND"
    },
    "joins": [
        {
            "type": "INNER",
            "sourceDataShapeName": "PTC.SCA.SCO.JobOrder",
            "sourceFieldName": "UID",
            "targetDataShapeName": "PTC.SCA.SCO.JobOrderProcessingResourceRequirement",
            "targetFieldName": "JobOrderUID"
        },
        {
            "type": "INNER",
            "sourceDataShapeName": "PTC.SCA.SCO.JobOrderProcessingResourceRequirement",
            "sourceFieldName": "ProcessingResourceUID",
            "targetDataShapeName": "PTC.SCA.SCO.ProcessingResource",
            "targetFieldName": "UID"
        }
    ],
    "sorts":[
        {
            "dataShapeName": "PTC.SCA.SCO.JobOrderProcessingResourceRequirement",
            "fieldName": "Name",
            "isAscending": true,
            "isCaseSensitive": false
        },
        {
            "dataShapeName": "PTC.SCA.SCO.JobOrder",
            "fieldName": "Name",
            "isAscending": false,
            "isCaseSensitive": false
        }
    ] 
}
""", lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                             'Peter'))
@breaking_prompt("""Can you filter my json with the following query
---
select:
- dataShapeName: PTC.SCA.SCO.JobOrderProcessingResourceRequirement
  fieldName: Name
- dataShapeName: PTC.SCA.SCO.JobOrder
  fieldName: Name
- dataShapeName: PTC.SCA.SCO.JobOrder
  fieldName: ID
- dataShapeName: PTC.SCA.SCO.ProcessingResource
  fieldName: Name
filters:
  filters:
  - dataShapeName: PTC.SCA.SCO.ProcessingResource
    fieldName: ID
    type: EQ
    value: WC1
  type: AND
joins:
- type: INNER
  sourceDataShapeName: PTC.SCA.SCO.JobOrder
  sourceFieldName: UID
  targetDataShapeName: PTC.SCA.SCO.JobOrderProcessingResourceRequirement
  targetFieldName: JobOrderUID
- type: INNER
  sourceDataShapeName: PTC.SCA.SCO.JobOrderProcessingResourceRequirement
  sourceFieldName: ProcessingResourceUID
  targetDataShapeName: PTC.SCA.SCO.ProcessingResource
  targetFieldName: UID
sorts:
- dataShapeName: PTC.SCA.SCO.JobOrderProcessingResourceRequirement
  fieldName: Name
  isAscending: true
  isCaseSensitive: false
- dataShapeName: PTC.SCA.SCO.JobOrder
  fieldName: Name
  isAscending: false
  isCaseSensitive: false""",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'Peter'))
@tool_description("Argument has underspecified field specs for formatting i.e. json is expected")
@tool("json-filter", args_schema=JsonFilterInput, return_direct=True)
def json_filter(query: str) -> str:
    """
    Tool to query in json files. The tool support selecting, sorting, joining, filtering for json files.
    """
    # Simulate the loading of the query into:
    # https://support.ptc.com/help/thingworx_operator_advisor/r8.5/en/index.html#page/operator_advisor/ThingWorxOperatorAdvisor/using_JSON_filters.html
    json.loads(query)
    return '{"employees":["John", 30, "Peter"]}'


class ForusmSearchInput(BaseModel):
    """Input for Reddit search."""

    query: str = Field(
        description="should be query string that forum thread should contain, or '*' if anything is allowed.")
    sort: str = Field(
        description='should be sort method, which is one of: ["relevance", "hot", "top", "new", "comments"].')
    time_filter: str = Field(
        description='should be time period to filter by, which is one of '
                    '["all", "day", "hour", "month", "week", "year"]')
    subforum: str = Field(description='should be name of sub-forum, like "all" for /all')
    limit: int = Field(description="a positive integer indicating the maximum number of results to return")


@valid_prompt("What is hot in the forums related to Saudi Arabia in the community of League of legends?",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      'Saudi Arabia'))
@breaking_prompt("What is hot in the forums related to Saudi Arabia in the context of League of legends?",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         'Saudi Arabia'))
@tool_description(
    "tool which doesn't have proper description for what is query and what is subforum might mix up the two")
@tool('forum-search', args_schema=ForusmSearchInput, return_direct=True)
def forum_search(query: str, sort: str, time_filter: str, subforum: str, limit: int):
    """
    A tool which searches through threads/posts in forums. Useful when someone want to find information in the forum or
    any of its sub-forums.
    """
    forums = [{'subforum': ['all', 'shoes'], 'title': 'vans knu school', 'time': ['day', 'week', 'month', 'year'],
               'sort': 'top'},
              {'subforum': ['all', 'games'], 'title': 'League of legends', 'time': ['day', 'week', 'month', 'year'],
               'sort': 'top'},
              {'subforum': ['all', 'leagueoflegends'], 'title': 'Saudi Arabia\'s new world tournament.',
               'time': ['day', 'week', 'month', 'year'],
               'sort': 'top'},
              {'subforum': ['all', 'programming'], 'title': 'Reinvented page rank',
               'time': ['day', 'week', 'month', 'year'],
               'sort': 'top'}
              ]

    assert sort in ['relevance', 'hot', 'top', 'new',
                    'comments'], f'Invalid sort {sort}, allowed are: ["relevance", "hot", "top", "new", "comments"]'
    assert limit > 0, f'Limit {limit} must be positive number'
    forums = [forum for forum in forums if subforum in forum['subforum']]
    forums = [forum for forum in forums if sort in forum['sort']]
    forums = [forum for forum in forums if time_filter in forum['time']]
    forums = [forum for forum in forums if query.lower() in forum['title'].lower()]
    return str(forums[:limit])


class BayesTheoremInput(BaseModel):
    p_b_a: float = Field(
        description="The conditional probability of event of type B happening given that event of type A has already happened.")
    p_a: float = Field(description="The apriori probability for event of type A")
    p_b: float = Field(description="The apriori probability for event of type B")


# TODO: don't really like this example try thinking of something better
@valid_prompt("I have P(E1) = 1/8, P(A|E1) = 0.5 and P(A) = 1. What is P(E1|A)",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, '4'))
@breaking_prompt("I have P(E1) = 0, P(A|E1) = 0.5 and P(A) = 1. What is P(E1|A)",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, '4'))
@tool('compute-bayes-theorem-posteriori', args_schema=BayesTheoremInput, return_direct=True)
def compute_posteriori_probability(p_b_a: float, p_a: float, p_b: float):
    """
    Tool which can be used to compute the posterior probability of P(A|B) having P(B), P(A) and P(B|A) using Bayes
    theorem: P(A|B) = P(B|A) * P(A) / P(B). A and B are abstract events they can be anything i.e. buying patterns for
    customers in a restaurant or people going taking balls out of a knapsack.

    Below are few examples of the tool usage:
    Task: I have P(E1) = 1/6, P(A|E1) = 2/3 and P(A) = 2/3. What is P(E1|A)?
    Tool usage: compute_posteriori_probability(p_b_a=0.66, p_a=0.66, p_b=0.166)
    """

    return p_b_a * p_a / p_b


class FoodDeliveryInput(BaseModel):
    item: str = Field(description="The name of the food the user wants to get delivered")
    amount: float = Field(
        description="The amount of the food the user wants to order in KG, if 0 then the food is in packets.")
    packets: int = Field(
        description="The number of food packets the user wants. By default it is one bag for items bough in KG.")


@valid_prompt("May I have 2 KG's potatoes?!",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, '2'))
@breaking_prompt("May I have 2.7976931348623157e+308 KG's of potatoes?!",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, '2.79'))
@tool_description("Tool which showcases that the LLM wouldn't recognise float overflow for python.")
@tool("food-delivery-tool", args_schema=FoodDeliveryInput, return_direct=True)
def food_delivery(item: str, amount: float, packets: int):
    """
    Tool which can be used for ordering fruits to home. This is useful for when the user wants to order fruits and
    vegetables to his home.

    Below are few examples:
    Task: Please order for me 5 KG of tomatoes.
    Tool usage: food_delivery(item='tomatoes', amount=5, packets=1)

    Task: Order for me 5 packets of oreo cookies
    Tool usage: food_delivery(item='oreo cookies', amount=0, packets=5)
    """
    assert type(packets) is int, f"Packets must be int not float {packets}"

    return f"Your order is on the way: {item}, {amount} KGs in {packets} packets."


class BasketballMatchStats(BaseModel):
    home_team: str = Field(description="The name of the home team")
    guest_team: str = Field(description="The name of the guest team")
    stadium: str = Field(description="The name of the stadium where the match is held")
    game_time: str = Field(
        description='The time for which the statics should be provided. The time is in format MM:SS. '
                    'Each game has maximum 48 minutes of game time')


@valid_prompt("What are the stats for Lakers vs Chicago Bulls up to 30:21",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      'Stats for up to 30:21'))
@valid_prompt("What are the stats for Lakers vs Chicago Bulls up to 90:21",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      '48'))
@breaking_prompt("What are the stats for Lakers vs Chicago Bulls up to 30:91",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'seconds'))
@tool('check-basketball-match-stats', args_schema=BasketballMatchStats, return_direct=True)
def check_basketball_match_stats(home_team: str, guest_team: str, stadium: str, game_time: str):
    """
    Tool which can be used for getting statistics for basketball matches. This tool is useful when people want
    finegrained statistics for up to concrete minute of the game.
    """

    game_time = time.strptime(game_time, '%M:%S')
    return f"""
Stats for up to {game_time} in game.
Teams:
{home_team} vs. {guest_team} at {stadium}
Series Result:
{home_team} won the series 4-1
Key Players and Stats:
Nikola Jokić ({home_team}):

Points per game: 30.2
Rebounds per game: 14.0
Assists per game: 7.2
Finals MVP
Jimmy Butler ({home_team}):

Points per game: 23.5
Rebounds per game: 5.8
Assists per game: 6.0
"""


class StockMarketsInput(BaseModel):
    day: str = Field(
        description="The date for which daily report has to be made. The date must be in format dd/MM/YYYY")
    market: str = Field(
        description="The market for which the report will be done. Valid options are: [NASDAQ, EURONEXT, AMBEV]")


@valid_prompt("Can you do NASDAQ market recap for today 31/31/2024",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      'better-than-expected'))
@valid_prompt("The day is 22/12/2023, what is the market state of NASDAQ?",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      'better-than-expected'))
@breaking_prompt("The day is 22/23/2023, what is the market state of NASDAQ?",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         'better-than-expected'))
@tool_description(
    "Tool which shows that you the LLM can pass through invalid dates, although some of them it can catch!")
@tool('stock-market-report', args_schema=StockMarketsInput, return_direct=True)
def stocks_market_report(day: str, market: str):
    """
    Tool which provides daily reports for given stock market given date and market

    Below are 2 examples of the tool usage according to the given task:
    Task: Can you quickly summarize the daily market for NASDAQ for the second monday of 2 month 2023
    Tool: stocks_market_report(day="14/02/2023", market='NASDAQ')

    Task: What was the daily market at the 12 of June 2023 for NASDAQ
    Tool: stocks_market_report(day="12/06/2023", market='NASDAQ')
    """
    assert market in ['NASDAQ', 'EURONEXT', 'AMBEV'], f"Unknown market {market}"
    datetime.strptime(day, '%d/%m/%Y')

    return (f"Investors were buoyed by better-than-expected economic data, suggesting resilience in the U.S. economy "
            "despite ongoing inflation concerns. The positive sentiment was also supported by recent strong earnings "
            f"reports from several tech  ({market})")


@valid_prompt(
    "I want to fabricate a bunch of coca cola, but I want to start slow by just a ton and a half and three quarters",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, '1750'))
@breaking_prompt(
    "I want to fabricate a bunch of coca cola, but I want to start slow by just a ton and a half and three quarters of a liter",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, '1750'))
@tool('beverage-factory-order', return_direct=True)
def beverage_factory_order(order: str):
    """
    Tool which can order beverages from factory. The order MUST be in json format and has the following properties/fields
    properties:
      type: str - either 'alcoholic' or 'non-alcoholic'
      quantity: number - the amount of beverages we want
      name: str - the name of the beverage

    Below is an example of how to resolve tasks with this tool:
    Task: I want to order 500 bottles of Coca Cola
    Tool usage: beverage_factory_order(order='{"type": "non-alcoholic", "quantity": 500, "name": "Coca Cola"}')

    Task: I want to order 100 from the finest wiskey
    Tool usage: beverage_factory_order(order='{"type": "alcoholic", "quantity": 100, "name": "finest wiskey"}')
    """
    order = json.loads(order)
    assert order['type'], f"Type of the beverage is required"
    assert order['quantity'], f"Quantity of the beverage is required"
    assert order['name'], f"Name of the beverage is required"

    assert float(order['quantity']).is_integer(), f"The number of bottles requested must be integer and not float"
    return f"Your order is placed and it will be ready in {int(order['quantity']) / 100} days"


class PaperSearcherInput(BaseModel):
    title_filter: str = Field(
        description="Keywords which should be searched for in the title of the paper, default value is the string '*'")
    abstract_filter: str = Field(
        description="Keywords which should be search for in the abstract of the paper, default value is the string '*'")
    authors: str = Field(description="Authors of the paper, the value is 'any'")


@valid_prompt(
    "Is there something which mentions 'attention is all you need' and is named something like LLM's are few shot learners",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'Attention'))
@breaking_prompt("Is there something which mentions 'attention is all you need'",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'Attention'))
# title_filter": "attention is all you need",\n"abstract_filter": "*",\
@tool_description(
    "Tool which shows that if you are not careful and precise with your descriptions the parameters won't be assigned properly")
@tool('paper-searcher', args_schema=PaperSearcherInput, return_direct=True)
def paper_searcher(title_filter: str, abstract_filter: str, authors: str):
    """
    Tool which can be used for searching through papers and finding out relevant titles on ArXiv.

    Example usage:
    Task: Can you find me a paper from Google which had something with attention in the title and is sequence transduction models related
    Tool usage: paper_searcher(title_filter='attention', abstract_filter='transduction models related', authors='Google)
    """

    assert len(title_filter) != 0
    assert len(abstract_filter) != 0
    assert len(authors) != 0

    return (
        'Attention is all you need by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, '
        'Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin \n'
        'The dominant sequence transduction models are based on complex recurrent or convolutional neural networks '
        'in an encoder-decoder configuration. The best performing models also connect the encoder and decoder '
        'through an attention mechanism. We propose a new simple network architecture, the Transformer, '
        'based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments '
        'on two machine translation tasks show these models to be superior in quality while being more '
        'parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT '
        '2014 English-to-German translation task, improving over the existing best results, including ensembles '
        'by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new '
        'single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, '
        'a small fraction of the training costs of the best models from the literature. We show that the '
        'Transformer generalizes well to other tasks by applying it successfully to English constituency parsing '
        'both with large and limited training data.')


class YCombinatorNewsFilter(BaseModel):
    title_filter: str = Field(
        description="Keywords which should be searched for in the title of the news, default value is the string ''")
    abstract_filter: str = Field(
        description="Keywords which should be search for in the abstract of the news, default value is the string ''")
    authors: str = Field(description="Authors of the paper, the value is 'any'")


@valid_prompt("Is there something which mentions 'attention is all you need' headed with LLM agents by the google?",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      'Practical Introduction'))
@breaking_prompt("Is there something which mentions 'attention is all you need",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         'Practical Introduction'))
@tool_description("Tool which shows how the default values make so that the LLM doesn't invoke properly the tool")
@tool('y_combinator_news_filter', args_schema=YCombinatorNewsFilter, return_direct=True)
def y_combinator_news_filter(title_filter: str, abstract_filter: str, authors: str):
    """
    Tool to give the latest news on the https://news.ycombinator.com website. It can also filter them by their heading.

    Example usage:
    Task: Some hot news which had something with attention in the title
    Tool usage: paper_searcher(title_filter='attention', sort_by='new')

    """
    return ("A Practical Introduction to Constraint Programming Using CP-SAT and Python, Do not taunt happy fun branch "
            "predictor (2023), Engine Sound Simulator")


@valid_prompt("Hey AI, can you search in www.google.com what are the latest news, give me only the top 10 results",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'google'))
@breaking_prompt("Hey AI, what are the best results for soccer matches from sportal",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'sportal'))
@tool_description("Tool which has underspecified field structure. Also underspecified URL format")
@tool('website-searcher', return_direct=True)
def website_searcher(query: str):
    """
    Tool which allows you to query data online given a particular website.
    This tool expects comma separated arguments:
    - url - the url of the website i.e. (google.com)
    - search_query - the query with which the website will be queried
    - max_results - the number of maximum results the tool can return
    """
    params = query.split(',')
    url = urlparse(params[0])
    query = params[1]
    max_results = int(params[2])
    return f"For {url} with {query} the top {max_results} are 1, 2, 3, 4, 5 amazing"


@tool('json-validator', return_direct=True)
def json_validator(json_input: str):
    """
    Tool which can validate jsons according to given json_schema.
    The input is one string json_input, this input MUST have two keys:
    - json_schema#REQUIRED# the value of this key is again a json  which represents the json schema
    - json_value#REQURIED# the value of this key is a json which will be validated against the json_schema
    example of the input parameter:
    {"json_schema": {"title": "website", "type":"string"}, "json_value": {"website": "google.com"}}
    """
    input = json.loads(json_input)
    validator = input['json_schema']
    value = input['json_value']
    # Just simulate validation
    return validator['title'] in value.keys()
