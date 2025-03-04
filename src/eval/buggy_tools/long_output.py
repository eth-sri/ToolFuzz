import os

from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field

from src.eval.buggy_tools.decorators import tool_description, valid_prompt, breaking_prompt
from src.eval.toolfuzz.utils.assert_lambdas import assert_contains


class LongFileInput(BaseModel):
    directory: str = Field(description="The directory in which the file should be found")
    filename: str = Field(description="The name of the file we want to read")


@valid_prompt("Can you print out the contents of the file results.txt in resources/?",
              lambda self, agent_invoke, params: assert_contains(self, agent_invoke, params,
                                                                 "These are test result on the agent tools."))
@breaking_prompt("Can you print out the contents of the file TheAdventuresOfSherlockHolmes.txt in resources/",
                 lambda self, agent_invoke, params: assert_contains(self, agent_invoke, params,
                                                                    "The Project Gutenberg EBook of The Adventures of Sherlock Holmes"))
@tool_description("Tool which will break the LLM because of too long return value")
@tool("read-files-from-system", args_schema=LongFileInput, return_direct=True)
def read_file(directory: str, filename: str):
    """
    Tool for reading files from the file system. This tool should be user asks for the contents of a file.

    Below are several task description and param examples:

    Task: Can you read me the result of report.txt?
    Tool call: read_file(directory='./', filename='report.txt')

    Task: Under the directory of resources there is a results.txt what are its contents?
    Tool call: read_file(directory='./resources/', filename='results.txt')
    """
    base_dir = os.getcwd().split('src')[0] + '/src/buggy_tools'
    file_path = f"{base_dir}/{directory}/{filename}"
    if os.path.exists(file_path):
        with open(file_path) as f:
            return "\n".join(f.readlines())

    return f"File {file_path} not found"
