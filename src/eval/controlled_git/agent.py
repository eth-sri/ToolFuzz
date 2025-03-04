from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from src.eval.tool_fixing.github_toolkit_fixer import ToolFix

from tqdm import tqdm
from time import sleep

from argparse import ArgumentParser

from src.eval import EvaluateResult
from src.eval.controlled_git.examples import get_all_examples
from src.eval.controlled_git.examples.comment_on_issue import CommentOnIssue
from src.eval.controlled_git.examples.create_file import CreateFile
from src.eval.controlled_git.examples.create_pr import CreatePullRequest
from src.eval.controlled_git.examples.new_branch import CreateNewBranchExample
from src.eval.controlled_git.examples.delete_file import DeleteFile
from src.eval.controlled_git.examples.update_files import UpdateFile
from src.eval.toolfuzz.loaders.langchain_toolkit_loaders import GithubToolkitLoader
from src.toolfuzz.utils import save_test_results


def get_args():
    parser = ArgumentParser(description="Evaluation on docker container environment")
    parser.add_argument('-p', dest='prompt_file')
    parser.add_argument('-o', dest='out_postfix')
    parser.add_argument('-m', dest='mode')
    return parser.parse_args()


cl_args = get_args()


def setup(clazz):
    model = ChatOpenAI(model='gpt-4o-mini', temperature=0)
    tools = GithubToolkitLoader().get_tools()
    tools_to_test = clazz.get_tools_names()
    tools = [t for t in tools if t.name in tools_to_test]
    tools = {tool.name: tool for tool in tools}

    with open(cl_args.prompt_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line.strip()) != 0:
                tool_fix = ToolFix.model_validate_json(line)
                if tool_fix.name not in tools:
                    continue
                tools[tool_fix.name].description = tool_fix.description
                fields = tools[tool_fix.name].args_schema.__fields__
                for k, v in tool_fix.fields.items():
                    if k not in fields:
                        continue
                    fields[k].description = tool_fix.fields[k]['description']
    return create_react_agent(model, tools=list(tools.values()), debug=True)


def run_prompts(clazz):
    agent = setup(clazz)
    issue_comments = get_all_examples(clazz)
    if cl_args.mode == 'train':
        train = len(issue_comments) * 0.1
        if (train < 1):
            train = 1
        issue_comments = issue_comments[:int(train)]
    else:
        train = len(issue_comments) * 0.1
        if (train < 1):
            train = 1
        issue_comments = issue_comments[int(train):]
    evals = []

    for c in tqdm(issue_comments, f'Running prompts {clazz}'):
        eval_res = EvaluateResult(success=True, prompt=c.prompt, output='', env_setup='', prompt_file='', env_gt_dir='',
                                  field=clazz.__name__)
        try:
            result = agent.invoke({'messages': [
                SystemMessage(content="You are an AI agent which can work with GitHub Repository"),
                HumanMessage(content=c.prompt)]})
            eval_res.output = str(result['messages'][-1].content)  # Just in case cast to string
            c.validate()
        except AssertionError as e:
            print("Assertion ERROR", e)
            eval_res.success = False
            eval_res.env_setup = f'AssertionError: {e}'
        except TypeError as e:
            print("Type ERROR", e)
            eval_res.success = False
            eval_res.env_setup = f'TypeError: {e}'
        except Exception as e:
            print(f"UNKNOWN EXCEPTION {e}")
            eval_res.success = False
            eval_res.env_setup = f'Exception: {e}'
        finally:
            c.revert_state()
            sleep(3)  # Wait for 3 seconds so that we don't get timed out...
        evals.append(eval_res)

    save_test_results(evals, f'ghub_eval_gpt4o-mini_{cl_args.out_postfix}.json')


def main():
    run_prompts(CommentOnIssue)
    run_prompts(UpdateFile)
    run_prompts(CreatePullRequest)
    run_prompts(CreateFile)
    run_prompts(DeleteFile)
    run_prompts(CreateNewBranchExample)


if __name__ == '__main__':
    main()
