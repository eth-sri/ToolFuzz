import json
from datetime import datetime
from typing import Optional
from src.eval.buggy_tools.decorators import valid_prompt, breaking_prompt, tool_description

from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field

from src.eval.toolfuzz.utils.assert_lambdas import assert_contains


# class WorkDayInput(BaseModel):
#     name: str = Field(description="The name of the worker doing the report")
#     hours_worked: int = Field(description="The number of hours that have been worked today.")
#     department_id: str = Field(description="The department id you work in.")
#     paired_with: List[str] = Field(description="The people with who the work was done.")
#     finished_tasks: List[str] = Field(description="The tasks that have been completed today.")
#     work_in_progress_tasks: List[str] = Field(description="The tasks that are still in progress.")


# @tool_description("NOT WORKING. Tool which wanted to show error when optional param is no longer optional")
# @tool("report_workday_tool", args_schema=WorkDayInput, return_direct=True)
# def report_workday(name, hours_worked, department_id, paired_with, finished_tasks, work_in_progress_tasks):
#     """
#     Tool to submit report daily work reports. This tool should be used when one wants to report their work for the day.
#     The tool will give a summary of the done report.
#
#     Below are several task description and param examples:
#
#     Task: Today I - Ivan Milev worked from home for 2 hours, synced with Jamie Hopper, Petar Petrov and Ivan Ivanov on the Marketing Campaign for conference X, however didn't manage to finish any tasks
#     Params: name='Ivan Milev', hours_worked=2, paired_with=["J. Hopper", "P. Petrov", "I. Ivanov"], finished_tasks=[], work_in_progress_tasks=["Marketing Campaign for conference X"]
#
#     Task: Mitko doing the daily report, today I worked from the office for 5 hours, worked alone the whole time and managed to finish the Gmail/Jira integration
#     Params: name='Mitko', hours_worked=5, paired_with=[], finished_tasks=["Gmail/Jira integration"], work_in_progress_tasks=[]
#     """
#     report = (f"Report for {name}. "
#               f"Today I finished {finished_tasks} and am still working on {work_in_progress_tasks}.\n"
#               f"I synced and worked with {paired_with}. In total I managed to do my work in {hours_worked} hours."
#               f"I worked from {department_id}"
#               f"This report is issued on: 26.06.2024")
#     return report


class JiraAccountCreatorInput(BaseModel):
    name: str = Field(description="The full name of the user")
    email: str = Field(description="The email with which the account should be created")
    username: str = Field(description="Username, the username should not contain any special characters and spaces.")
    description: str = Field(description="Personal description, should be shorter than 10 words")


@valid_prompt(
    "Please create new Jira account for Ivan Milev with username ivanmilev and mail imilev@ethz.ch, description is 'student'",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "_atlassian_id"))
@breaking_prompt(
    "Can you create a new Jira account for Martin Vechev and mail mtv@gmail.com, description is 'ETH Professor'",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "_atlassian_id"))
@tool_description(
    "Tool to showcase change in field constraints (username), not reflected in the examples (username has underscore)")
@tool("jira-account-creator", args_schema=JiraAccountCreatorInput, return_direct=True)
def jira_acc_creator(name: str, email: str, username: str, description: str) -> str:
    """
    Tool which can create new Jira Accounts. It can be used when a new user has to be created or existing user wants a new account.
    It will return the atlassian Id of the new user:

    Below are several task description and param examples:

    Task: Create for a new user for Dimitar Stoyanov and description: "I am the new lead software engineer of the department for Psychology" with mitko123@gmail.com
    tool usage: jira_acc_creator(name="Dimitar Stoyanov", username="dimitar_stoyanov", description="I am the new lead software engineer of the department for Psychology", email="mitko123@gmail.com")


   Task: Create for a new user for Ivan Milev and description: "Student doing his MSc Thesis in the company" with ivan_milev@gmail.com
    tool usage: jira_acc_creator(name="Ivan Milev", username="ivan_milev", description="Student doing his MSc Thesis in the company", email="ivan_milev@gmail.com")

    """
    assert username.isalpha(), f'Username should have only alpa {username}'
    assert len(description.split(' ')) <= 10, f'Description should be with less than 10 words: {description}'

    return f"{username}_{email}_atlassian_id"


class SearchDocumentsInput(BaseModel):
    keywords: str = Field(description="Keywords to search for")
    doc_type: str = Field(description="The type of the document. One of ['taxes', 'real estate', 'kids', 'picture']")
    file_extension: Optional[str] = Field(
        description="Optional filtering by file extension one of: [docx, xlsx, txt, ps, png]")


@valid_prompt("Can you list me all the pictures I have from switzerland?",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "Lauterbrunnen"))
@breaking_prompt("Can you find a document which mentions the square footage of our flat, should be a pdf?",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         "no such file"))
@breaking_prompt("Can you find a document for the kids, it is a python code file so it is py??",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         "no such file"))
@breaking_prompt("Can you list me all the images I have from switzerland?",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         "Lauterbrunnen"))
@tool_description(
    "Tool which shows how changing the enum values (doctype: picture) is not reflected in the examples breaks it")
@tool("search-documents", args_schema=SearchDocumentsInput, return_direct=True)
def search_documents(keywords, doc_type, file_extension: Optional[str] = None) -> str:
    """
    Tool to search for documents on your PC. Use this to find the name of a file which contains keywords.

    Below are a several task descriptions and param examples:
    Task: Search for the pictures with my grant parents
    tool usage: search_documents(doc_type='image', keywords='grant parents', file_extensions='pdf')

    Task: Can you list all the files related to our apartment.
    tool usage: search_documents(doc_type='flat', keywords='')

    Task: Can you list me all my taxes files, just the pdfs?
    tool usage: search_documents(doc_type='taxes', keywords='', file_extension='pdf')

    Task: Can you find the picture of our family from the first day of school?
    tool usage: search_documents(doc_type='image', keywords='first day of school')
    """
    docs = [
        {'keywords': ['school trip'], 'topic': ['kids'], 'extension': ['pdf'], 'description': 'Trip to Amsterdam'},
        {'keywords': ['ownership'], 'topic': ['real estate'], 'extension': ['pdf'], 'description': 'House in Como'},
        {'keywords': ['tax report for 2022'], 'topic': ['taxes'], 'extension': ['txt'], 'description': '1M in revenue'},
        {'keywords': ['owner'], 'topic': ['real estate'], 'extension': ['pdf'], 'description': 'Apartment in Zurich'},
        {'keywords': ['tax report for 2025'], 'topic': ['taxes'], 'extension': ['pdf'],
         'description': 'tax report for 2025'},
        {'keywords': ['switzerland'], 'topic': ['picture'], 'extension': ['png'], 'description': 'Lauterbrunnen'},
    ]

    assert doc_type in ['taxes', 'real estate', 'kids', 'picture'], f'Unknown doctype: {doc_type}'
    docs = [doc for doc in docs if doc_type in doc['topic']]

    if file_extension is not None:
        assert file_extension in ['docx', 'xlsx', 'txt', 'ps'], f'Unknown file extension: {file_extension}'
        docs = [doc for doc in docs if file_extension == doc['extension']]

    if keywords is not None and keywords != '':
        docs = [doc for doc in docs if keywords.lower() in doc['keywords']]
    return str(docs)


class NewsInput(BaseModel):
    date: str = Field(
        description="Date for which we want to get the news. The string must be in the format of MM/dd/YYYY")
    category: str = Field(
        description="Category of news. One of [US, World, Politics, Business, Opinion, Health, Entertainment, Sport, "
                    "Fashion, Science]")


@valid_prompt("What has happened on the 25th of June 2024?",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      "The Bear"))
@breaking_prompt("What is happening today in the world of entertainment?",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         "The Bear"))
@breaking_prompt("Today is 2024/12/30 what's up with the news in politics",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         "No relevant"))
@tool_description(
    "Tool which shows the problem of having different type templates in the field description and the examples (date)")
@tool("daily-news-search", args_schema=NewsInput, return_direct=True)
def daily_news_search(date: str, category: str) -> str:
    """
    Tool to search the news by date. Use this tool to find the hot, latest headlines on different topics like politics,
    business, entertainment, sports etc.

    Below are a several task descriptions and param examples:
    Task: What was the biggest sports news on the 2nd of July 2023?
    Tool usage: daily_news(date='06/02/2023', category='sports')

    Task: What new is happening in the politics scene today 26.06.2024?
    Tool usage: daily_news(date='26/06/2024', category='politics')

    Task: I want to know all about Business today - (2024/05/23)?
    Tool usage: daily_news(date='23/05/2024', category='politics')
    """

    date = datetime.strptime(date, '%m/%d/%Y')

    assert category.lower() in ["us", "world", "politics", "business", "opinion", "health", "entertainment", "sport",
                                "fashion", "science"], f'Unknown category: {category}'

    return ("‘The Bear’ Season 3 premiere in L.A.\nStars attend the premiere of 'The Bear' season 3 at the El Capitan "
            f"Theatre on Tuesday, June 25, 2024, in Hollywood, Calif. for {date}")


class DatabaseQueryInput(BaseModel):
    table: str = Field(
        description="The name of the table which is part of the above schema for which the query will be executed."
                    "Must either clothing or shoes")
    column: str = Field(description="The column which is of interest for the query")
    filter: str = Field(description="Filtering statement i.e. less than 5 or contains the word hello")


@valid_prompt("Is there a green Vans' shoe model?",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      "Vans high-top old school"))
@breaking_prompt("Can you list me all T-shirts names in ascending order?",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         "Vans high-top old school"))
@breaking_prompt("What is the biggest size in shoes for Vans that I can buy?",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         "Vans high-top old school"))
@tool_description("Tool which shows how a missing argument which still exists in the examples can be added from the LLM"
                  "Note: I couldn't reproduce this behavior with the DatabseQueryInput(BaseModel) - this way the LLM "
                  "never halucinated")
@tool("vans-database-query-engine", return_direct=True)
def vans_query_db(db_query_inp: str) -> str:
    """
    Tool which can be used for querying the database of the Institute of Van's Annotated Names. This tool has few
    table such as: Old school, Knu Skul, Authentic etc.
    Each of those has a columns which show the different models of shoes there are with their specifics.

    The parameter db_query_inp has the following props:
        table#string#The name of the table which is part of the above schema for which the query will be executed. Must either clothing or shoes
        column#str#The column which is of interest for the query"
        filter#filtering statement i.e. less than 5 or contains the word hello

    Here are several examples of the usage of the tool given task description:
    Task: I was wondering what are the different names of the Van's old schools models starting with 'X'?
    Tool usage: {"table"="Shoes", "column":"name", "filter":"name starting with 'X'")

    Task: Can you list all T-Shirt Van's has ever produced in ascending order?
    db_query_inp: {"table":"Clothing", "column":"price", "filter":"", "sort":"asc")
    """
    params = json.loads(db_query_inp)
    assert 'table' in params, f'Expected "table" in {params}'
    assert 'column' in params, f'Expected "column" in {params}'
    assert 'filter' in params, f'Expected "filter" in {params}'
    assert 'sort' not in params, f'Parameter unknown "sort" in {params}'
    return 'Vans high-top old school'
