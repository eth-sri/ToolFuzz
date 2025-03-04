import argparse

from src.eval.toolfuzz.env_prompts import docker_env_context, ghub_context
from src.eval.toolfuzz.utils.setup import init_model
from src.eval.toolfuzz.utils.tools import get_correctness_tool_loaders
from src.toolfuzz.correctness.correctness_fuzzer import CorrectnessTester

"""
One test is one prompt template -> This are a bunch of questions
1. Evaluate all the questions
2. Put them in buckets for output (output bucket)
3. Put them in buckets for input arguments (argument bucket)

For now save each record
"""


def args():
    parser = argparse.ArgumentParser(description="Test agent tools.")
    parser.add_argument('-t', dest='tool')
    return parser.parse_args()


cl_args = args()


def tools_test(loaders, model):
    loader = [loader for loader in loaders if loader.can_load(cl_args.tool)][0]
    tool = loader.get_tool()
    if isinstance(tool, list):
        tool = [t for t in tool if t.name == cl_args.tool][0]
    context = ''

    if tool.name in ['copy_file', 'file_delete', 'file_search', 'move_file', 'read_file', 'write_file',
                     'list_directory', 'terminal']:
        context = docker_env_context
    elif tool.name in ['Get_Issues', 'Get_Issue', 'Comment_on_Issue', 'List_open_pull_requests__PRs_',
                       'Get_Pull_Request', 'Overview_of_files_included_in_PR', 'Create_Pull_Request',
                       'List_Pull_Requests_Files', 'Create_File', 'Read_File', 'Update_File',
                       'Delete_File',
                       'Overview_of_existing_files_in_Main_branch',
                       'Overview_of_files_in_current_working_branch',
                       'List_branches_in_this_repository', 'Set_active_branch', 'Create_a_new_branch',
                       'Get_files_from_a_directory', 'Search_issues_and_pull_requests', 'Search_code',
                       'Create_review_request']:
        context = ghub_context
    else:
        context = ''
    tester = CorrectnessTester(model, tool, loader.get_agent(), additional_context=context)
    tester.test()
    tester.save(f'result_{cl_args.tool}.json')


def main():
    model = init_model('gpt-4o-mini')
    loaders = get_correctness_tool_loaders()
    tools_test(loaders, model)  # Now test all tools.


if __name__ == '__main__':
    main()
