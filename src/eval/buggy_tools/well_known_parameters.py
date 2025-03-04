from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field

from src.eval.buggy_tools.decorators import valid_prompt, breaking_prompt
from src.eval.toolfuzz.utils.assert_lambdas import assert_contains


class FileReaderInput(BaseModel):
    file_extension: str = Field(
        description="File extension of the file, the allowed extensions are [docx, docm, docx, dotx, txt]")
    file_name: str = Field(description="The name of the file to be read")


@valid_prompt("Can you read me the main.docx file",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      'Some file content'))
@breaking_prompt("Please type out what is inside main.py",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         'Some file content'))
@breaking_prompt("Can you find a document of mine names types it is in a .ts file",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         'Some file content'))
@breaking_prompt("Can you find a document of mine and give me it's contents: types.ts",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         'Some file content'))
@tool("file_reader", args_schema=FileReaderInput, return_direct=True)
def file_reader(file_name: str, file_extension: str):
    """
    Tool for reading the content of a file given the name and extension of the file.
    Supported types are the ones from MS Word.

    Below are few examples on how to use this tool:

    Task: Can you find and read the taxes.docx file?
    Tool usage: file_reader(file_name='taxes', file_extension='docx')

    Task: Print me the contents of SherlockHolmes.txt
    Tool usage: file_reader(file_name='SherlockHolmes', file_extension='txt')
    """
    assert file_extension.lower() in ['docx', 'docm', 'docx', 'dotx',
                                      'txt'], f'Unknown file extension: {file_extension}'
    return "Some file content, this is just a bunch of text, which is very random and I wrote myself"


class NewsInput(BaseModel):
    topic: str = Field(
        description="The topic in which we want to collect the news. Available topics are: ['politics', 'business', 'entertainment', 'sports']")
    day: str = Field(description="The day for which the news will be fetched - in format of dd/MM/YYYY")


@valid_prompt("What are some new things in entertainment today 28 of June 2024",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      'Person A'))
@breaking_prompt("Can you tell me what is new in the field of science as of 2024, 13th of April",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         'Person A'))
@tool("search-news-topics", args_schema=NewsInput)
def search_news_topics(topic: str, day: str):
    """
    Tool to fetch the news for a concreate topic and day. To be used when the person is interested in the leading news of
    topics for concrete date.

    Below are few examples on how ot use this tool:

    Task: What were the hot news in sports for 22 of June 2023
    Tool usage: search_news_topics(topic='sports', day='22/07/2023')

    Task: What was hot in politics on the 13 of April 2022
    Tool usage: search_news_topics(topic='politics', day='13/04/2022')
    """
    assert topic in ['politics', 'business', 'entertainment', 'sports'], f'Unknown topic: {topic}'

    return "Person A did action A and person B did action B"


class SystemInput(BaseModel):
    processor: str = Field(description="The processor of the system. For now it can be only INTEL")
    architecture: str = Field(description="The architecture of the system. Valid values: [X64, X86, risc].")
    ram: int = Field(description="The amount of RAM that the system has")
    gpu: str = Field(description="The brand of the GPU. Valid values: [NVIDIA, AMD].")


@valid_prompt(
    "Bought this new PC which is cuttin edge the architecure is RISC, 128 gigs of ram, the brand new, polished RTX 5090 from Nvidia and the brand new CPU from the company named AMD",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'installed'))
@breaking_prompt(
    "Bought this new PC which is cuttin edge the architecure is RISC, 128 gigs of ram, the brand new, polished RTX 5090 from Nvidia and the brand new CPU from the company name amd",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'installed'))
@valid_prompt(
    "Bought this new PC which is cuttin edge the architecure is RISC, 128 gigs of ram, the brand new, polished RTX 5090 from Nvidia and the brand new CPU from the company name intel",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'installed'))
@breaking_prompt(
    "Bought this new PC which is cuttin edge the architecure is RISC, 128 gigs of ram, the brand new, polished RTX 5090 from Nvidia and the brand new CPU from the company named intelchips",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, 'installed'))
@tool('personal_computer_system_builder', args_schema=SystemInput, return_direct=True)
def system_builder(processor: str, architecture: str, ram: int, gpu: str):
    """
    Tool which would setup a system with its drivers given the processor and architecture as well as the gpu brand
    """

    assert processor.lower() == 'intel', f'Unknown processor: {processor}'
    assert architecture.lower() in ['x64', 'x86', 'risc'], f'Unknown architecture: {architecture}'
    assert gpu.lower() in ['nvidia', 'amd'], f'Unknown GPU {gpu}'

    return f'Your PC is installed with {processor} drivers and Linux for {architecture}, the {ram} gigs of ram are utilized and {gpu} drivers are installed'
