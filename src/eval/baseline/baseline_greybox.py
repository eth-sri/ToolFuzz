from typing import List

from langchain_core.exceptions import OutputParserException
from pydantic.v1 import BaseModel, Field
from tqdm import tqdm

from src.eval.baseline.prompts import prompt_correctness, prompt_crash, prompt_oracle
from src.eval.toolfuzz.utils.tools import get_correctness_tool_loaders
from src.toolfuzz.agent_executors.langchain.react_new import ReactAgentNew
from src.toolfuzz.agent_executors.langchain.react_old import ReactAgentOld
from src.toolfuzz.correctness.prompt_generation.llm_responses import CorrectnessResponse
from src.toolfuzz.dataclasses import TestFailureResult
from src.toolfuzz.runtime.prompt_generation.prompt_generator import RuntimeFailurePromptGeneration
from src.toolfuzz.tools.info_extractors.langchain_tool_wrapper import LangchainToolWrapper
from src.toolfuzz.utils import save_test_results


class GeneratedPrompt(BaseModel):
    prompts: List[str] = Field(
        description="Multiple prompts which can trigger tool crash")


def failure_test(tools, model):
    """
    Function which will generate the results for the grey box baseline for runtime failures.

    Args:
        tools: The tools which will be evaluated
        model: The model which will be used for generating the prompts
    """
    failures = []

    for tool in tqdm(tools, desc="Testing tools"):
        extractor = LangchainToolWrapper(tool)
        pg = RuntimeFailurePromptGeneration(extractor)
        agent_exec = ReactAgentNew(tool, model)
        if not agent_exec.heartbeat():
            agent_exec = ReactAgentOld(tool, model)
        try:
            tool_docs = pg.tool_prompt
        except Exception as e:
            print(f'Error when getting tool info {tool}, {e}')
            continue

        tool_name = extractor.get_tool_name()

        for iter in range(2):  # 2 iterations
            try:
                prompts = pg._generate_from_template(prompt_crash, ['tool_info'], {'tool_info': tool_docs},
                                                     GeneratedPrompt)
            except OutputParserException as e:
                print(f"Cannot parse output: {e}")
                continue

            for prompt in tqdm(prompts['prompts'], desc='Testing prompts'):
                try:
                    agent_exec(prompt)
                    failures.append(TestFailureResult(tool=tool_name, expected_exception='',
                                                      exception='',
                                                      prompt=prompt, agent_type=agent_exec.get_name(),
                                                      bad_params='', successful_trigger=False, trace=''))
                except Exception as e:
                    print(f"Error {e}")
                    failures.append(TestFailureResult(tool=tool_name, expected_exception=str(e),
                                                      exception=str(type(e)) + str(e),
                                                      prompt=prompt, agent_type=agent_exec.get_name(),
                                                      bad_params='', successful_trigger=True, trace=''))
        save_test_results(failures, 'baseline_greybox_failure_2.json')


def correct_test(loaders):
    """
        Function which will generate the results for the grey box baseline for correctness.

        Args:
            loaders: The tool loaders for the tools which will be evaluated
    """
    failures = []
    for loader in tqdm(loaders, desc="Testing tools"):
        agent_exec = loader.get_agent()
        tools = loader.get_tool()
        if not isinstance(tools, list):
            tools = [tools]

        for tool in tqdm(tools, desc="Testing tools"):
            extractor = LangchainToolWrapper(tool)
            pg = RuntimeFailurePromptGeneration(extractor)

            try:
                tool_docs = pg.tool_prompt
            except Exception as e:
                print(f'Error when getting tool info {tool}, {e}')
                continue
            tool_name = tool_docs
            if 'name' in dir(tool) and tool.name is not None:
                tool_name = str(tool.name)
            for iter in range(2):  # 2 iterations
                try:
                    prompts = pg._generate_from_template(prompt_correctness, ['tool_info'], {'tool_info': tool_docs},
                                                         GeneratedPrompt)
                except OutputParserException as e:
                    print(f"Cannot parse output: {e}")
                    continue
                for prompt in tqdm(prompts['prompts'], desc='Testing prompts'):
                    try:
                        agent_answer, _, _, _ = agent_exec(prompt)
                        resp = pg._generate_from_template(prompt_oracle, ['question', 'answer'],
                                                          {'question': prompt, 'answer': agent_answer},
                                                          CorrectnessResponse)
                        if resp['correctness_degree'] < 5:
                            failures.append(TestFailureResult(tool=tool_name, expected_exception=agent_answer,
                                                              exception=resp['reason'],
                                                              prompt=prompt, agent_type=agent_exec.get_name(),
                                                              bad_params='', successful_trigger=True, trace=''))
                        else:
                            failures.append(TestFailureResult(tool=tool_name, expected_exception=agent_answer,
                                                              exception=resp['reason'],
                                                              prompt=prompt, agent_type=agent_exec.get_name(),
                                                              bad_params='', successful_trigger=False, trace=''))
                    except Exception as e:
                        print(f"Error {e}")

        save_test_results(failures, 'baseline_graybox_correctness.json')


def main():
    correctness_tools = get_correctness_tool_loaders()
    correct_test(correctness_tools)


if __name__ == '__main__':
    main()
