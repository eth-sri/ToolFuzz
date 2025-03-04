import argparse
import json
import random

from pydantic import BaseModel
from tqdm import tqdm

from src.eval.toolfuzz.utils.setup import init_model
from src.eval.toolfuzz.utils.tools import get_correctness_tool_loaders
from src.toolfuzz.agent_executors.langchain.react_new import ReactAgentNew
from src.toolfuzz.agent_executors.langchain.react_old import ReactAgentOld
from src.toolfuzz.dataclasses import PromptSetTestResults
from src.toolfuzz.utils import save_test_results


class CrossCallsResult(BaseModel):
    tool: str
    prompt: str
    generated_for_tool: str
    invoked: bool
    invocation_params: str


#   -j /local/home/imilev/agent-tool-testing/src/test/results/result_correctness_all copy.json
def args():
    parser = argparse.ArgumentParser(description="Evaluation with cross tool calling")
    parser.add_argument('-j', dest='output_json_files', nargs='+')
    parser.add_argument('-t', dest='tools', nargs='+')
    return parser.parse_args()


cli_args = args()


def read_prompts():
    prompt_data = []
    for file in cli_args.output_json_files:
        with open(file, 'r') as f:
            data = json.loads(f.read())
            for d in data:
                prompt_data.append(PromptSetTestResults.parse_obj(d))
    return prompt_data


def get_agent(model, tool_name):
    tools = get_correctness_tool_loaders()
    tool = [tool for tool in tools if tool.name == tool_name]
    assert len(tool) == 1, f'only one tool can be tested at a time = {tool}'
    tool = tool[0]
    agent_exec = ReactAgentNew(tool, model)
    if not agent_exec.heartbeat():
        agent_exec = ReactAgentOld(tool, model)
    return agent_exec


def tool_groups():
    groups = [
        set(['Dall-E-Image-Generator']),
        set(['Get Nasa Image and Video Library media metadata manifest',
             'Get NASA Image and Video Library media metadata location', 'Search NASA Image and Video Library media',
             'Get NASA Image and Video Library video captions location']),
        set(['wikidata', 'wikipedia']),
        set(['arxiv', 'semanticscholar', 'pubmed']),
        set(['duckduckgosearch', 'duckduckgosearchresult']),
        set(['file_search', 'list_directories', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['file_delete', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['move_file', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['open-street-map-search']),
        set(['read_file', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['copy_file', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['requests_delete', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['requests_get', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['requests_patch', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['requests_post', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['requests_put', 'terminal', 'python_repl', 'python_repl_ast']),
        set(['stack_exchange']),
        set(['json_spec_list_keys', 'json_spec_get_value']),
        set(['youtube_search']),
        set(['open-street-map-distance']),
        set(['query_graphql'])
    ]

    return groups


def test_tool(tool):
    tool_invocation_result = []

    model = init_model('gpt-4o-mini')
    prompt_data = read_prompts()
    # Test a tool:
    # 1. Initialize the tool with the setup we have.
    agent = get_agent(model, tool)
    # 2. Filter out prompts for this tool
    groups = tool_groups()
    group = set()
    for g in groups:
        if tool in g:
            group.update(g)
            break

    prompts = [p for p in prompt_data if p.tool not in group]
    transformed_prompts = []
    for p in prompts:
        for prompt in p.template_prompts:
            transformed_prompts.append((prompt, p.tool))
    # 3. Randomly sample 100 examples from other tools i.e. 
    sampled_prompts = random.sample(transformed_prompts, 50)
    # 4. Run against and see how many times the tool is invoked!
    for prompt, og_tool in tqdm(sampled_prompts, desc=f'Testing tool {tool}'):
        try:
            agent_out, tool_out, trace, tool_args = agent(prompt)
        except:
            continue
        if tool_out != None and tool_args != None:
            tool_invocation_result.append(CrossCallsResult(tool=tool, prompt=prompt,
                                                           generated_for_tool=og_tool,
                                                           invoked=True, invocation_params=tool_args))
        else:
            tool_invocation_result.append(CrossCallsResult(tool=tool, prompt=prompt,
                                                           generated_for_tool=og_tool,
                                                           invoked=False, invocation_params=""))

    save_test_results(tool_invocation_result, f'cross_calling_{tool}.json')


def main():
    tools = get_correctness_tool_loaders()
    if len(cli_args.tools) == 2:
        tools = [tool.name for tool in tools][:25]
    else:
        tools = [tool.name for tool in tools][25:]
    for tool in tqdm(tools, desc='Testing tools.'):
        try:
            test_tool(tool)
        except:
            print(f"Found exception for {tool}")


if __name__ == '__main__':
    main()
