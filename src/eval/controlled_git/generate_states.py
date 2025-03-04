from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

from src.eval.controlled_git.prompts import pull_requests, issues
from src.eval.toolfuzz.loaders.langchain_toolkit_loaders import GithubToolkitLoader
from src.eval.toolfuzz.utils.setup import init_model
from src.toolfuzz.utils import save_test_results


class PromptResult(BaseModel):
    task: str = Field(description='The task that should be performed')
    user_prompt: str = Field(description='The user prompt that should be used to perform the task')
    code_snippet: str = Field(description='The code snippet that validates the task complitio')


generate_task = """
You are an developer and want are working with your GitHub Web repository, now you get access to  the tool: {tool_description}.

Here is some context information on what you can do with that tool: {context}

Generate a task that a developer or support engineer might want to do in GitHub.
Please generate a user prompt which is basically the user interacting with the agent to perform the task.
Generate code snippet of validating the task:
you have access to repo methods of repo.list_branches(), repo.list_issues(), repo.list_prs(), repo.list_comments(issue_number)
i.e. if you are adding a comment something like: `assert len(repo.list_comments(issue_number)) == 1` 

{format_instructions}
"""


def main():
    llm = init_model('gpt-4o', temperature=0.7)
    tools = GithubToolkitLoader().get_tools()
    tools = {tool.name: tool for tool in tools if 'pull_request' in tool.name.lower()}
    print(tools.keys())

    parser = PydanticOutputParser(pydantic_object=PromptResult)
    template = PromptTemplate(template=generate_task,
                              input_variables=['tool_description', 'context'],
                              partial_variables={"format_instructions": parser.get_format_instructions()})
    chain = template | llm | parser

    res = {}
    for i in range(10):
        try:
            for tool_name, tool in tools.items():
                context = 'Just use the tool description'
                # if 'pr' in tool_name.lower():
                context = '\n'.join(pull_requests)
                # if 'issue' in tool_name.lower():
                context = '\n'.join(issues)
                # if 'file' in tool_name.lower():
                # context = 'You can work with files'
                result = chain.invoke({'tool_description': tool.description, 'context': context})
                if tool_name not in res:
                    res[tool_name] = [result]
                else:
                    res[tool_name].append(result)
                print(result)
        except Exception as e:
            print(e)
            continue
    for k, v in res.items():
        save_test_results(v, f'{k}_tasks.json')


if __name__ == '__main__':
    main()
