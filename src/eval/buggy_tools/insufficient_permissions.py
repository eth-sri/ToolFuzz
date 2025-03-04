import os
import re

from langchain_core.tools import tool
from langchain.pydantic_v1 import BaseModel, Field

from src.eval.buggy_tools.decorators import tool_description, valid_prompt, breaking_prompt
from src.eval.toolfuzz.utils.assert_lambdas import assert_contains


class FileInput(BaseModel):
    directory: str = Field(description="The directory in which the file should be found")
    filename: str = Field(description="The name of the file we want to read")
    content: str = Field(description="The content which has to be append to the directory/file")


@valid_prompt("Could you please write down for me the message: 'Tomorrow you have to study as exams are coming' in my "
              "exams.txt file in the resources dir ",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                      "tomorrow you have"))
@breaking_prompt(
    "Could you please write down for me the message: 'App doesn't have permissions to write to this file' in"
    "insufficient_write_access.txt file in the resources dir ",
    lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                            "App doesn't have"))
@tool_description("Tool which will break because of insufficient permissions on the tool itself.")
@tool("append-to-file", args_schema=FileInput, return_direct=True)
def append_to_file(directory: str, filename: str, content: str):
    """
    This tool is useful when someone wants to write a message into a file. Or if someone wants to log information to
    a file - append to a file

    Below are several task description and param examples:

    Task: Please write down for me "Ping the guys tomorrow on the deadline" to important_message.txt!
    Tool call: append_file(directory='./', filename='important_message.txt')

    Task: Write a note to myself: "I need to buy milk, eggs and bread for home!" in my notes.txt in resources/! Thanks
    Tool call: append_file(directory='./resources/', filename='notes.txt')
    """

    absolute_path = f"{os.getcwdb().decode().split('src')[0]}/src/buggy_tools/{directory}"
    file_path = f"{absolute_path}/{filename}"
    with open(file_path, "w") as f:
        f.write(content)

    return f"Successfully wrote '{content}' to {file_path}"


class JiraIssueInput(BaseModel):
    issue_key: str = Field(description="The issue key which will be modified in the format PROJECT-Number i.e. MKY-12")
    modification_type: str = Field(description="What kind of modification are we applying to the issue. "
                                               "Valid modifications are: [ISSUE_TYPE_TRANSITION, USER_ASSIGN, "
                                               "ESCALATE, CLOSE]\n"
                                               "note that ESCALATE is allowed only for users who are admin - username "
                                               "starts with admin_")
    new_value: str = Field(description="The new value of the issue under modification")
    old_value: str = Field(description="The old value of the issue under modification")
    username: str = Field(description="The username of the user which will execute the operation. Note there are 2 "
                                      "types of users, admin and normal. All Admin users have prefix of admin on "
                                      "their username.")


@valid_prompt("Change the issue type of IK-12 from Bug to User Story from user123",
              lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params, "successfully"))
@breaking_prompt("I want to escalate issue IK-12 from normal to PRIORITY1 with my user: ivanmi",
                 lambda test_self, agent_invoke, params: assert_contains(test_self, agent_invoke, params,
                                                                         "successfully"))
@tool_description("Tool which aims to show that LLM cannot handle dependency constraints between fields")
@tool('jira-issue-work', args_schema=JiraIssueInput, return_direct=True)
def jira_issue_work(issue_key: str, modification_type: str, old_value: str, new_value: str, username: str):
    """
    Tool which gives the functionality to work with Jira issues and transition them and escalate them.

    Below are few examples of tasks and the tool usage:
    Task: Can you reassign am issue IK-34 from Ivan to Navi from my user mitko123
    Tool usage: jira_issue_work(issue_key='IK-34', modification_type='USER_ASSIGN', old_value='Ivan', new_value='Navi', username='mitko123')

    Task: Escalate ticket MT-1 from normal to urgent with my user admin_marc
    Tool usage: jira_issue_work(issue_key='MT-1', modification_type='ESCALATE', old_value='normal', new_value='urgent', username='admin_marc')

    Task: Change the issue type from User Story to PoC for issue SemProj-12 with my user ivanmilev
    Tool usage: jira_issue_work(issue_key='SemProj-12', modification_type='ISSUE_TYPE_TRANSITION', old_value='User Story', new_value='PoC', username='ivanmilev')
    """
    assert re.match(r"\w+-\d+", issue_key), f'Invalid IssueKey format: {issue_key}'
    assert modification_type.upper() in ['ISSUE_TYPE_TRANSITION', 'USER_ASSIGN', 'ESCALATE',
                                         'CLOSE'], f"Unknown modification type {modification_type}"
    if modification_type == 'ESCALATE':
        assert username.startswith('admin'), f"Cannot escalate if username doesn't start with admin {username}"

    assert old_value != new_value, f"Update value has to be different from old value {old_value} == {new_value}"
    return f"Successfully did a {modification_type} for {issue_key} from {old_value} to {new_value} by {username}"


if __name__ == '__main__':
    from langchain_openai import ChatOpenAI
    from src.utils import ask
    from src.utils import agent_from_tool

    model = ChatOpenAI(model="gpt-4", temperature=0)
    model_with_tool, agent = agent_from_tool(model, append_to_file)
    print(ask(agent,
              "Could you please write down for me the message: 'App doesn't have permissions to write to this file' in"
              "insufficient_write_access.txt file in the resources dir "))
