import os
import json
import shutil
from collections import defaultdict
from dataclasses import dataclass
from typing import List
from jinja2 import Environment, PackageLoader, select_autoescape

from src.toolfuzz.dataclasses import PromptSetTestResults, TestFailureResult

from importlib import resources

env = Environment(
    loader=PackageLoader("src", 'templates'),
    autoescape=select_autoescape()
)


@dataclass
class TestResultsHtml:
    prompt: str
    tool_arguments: str
    tool_output: str
    agent_output: str
    tool_failure: bool
    unexpected_agent_output: int
    agent_output_not_relevant: bool
    llm_agent_out_reason: str
    trace: str
    input_bucket_color: str
    input_bucket: int
    output_bucket_color: str
    output_bucket: int


@dataclass
class PromptSetTestResultsHtml:
    tool: str
    template_question: str
    llm_output_expectation: str
    individual_run_test_results: List[TestResultsHtml]


TEXT_COLOR_CLASSES = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'no_invocation']


def save_test_results_html(test_results, file='./results.html'):
    html_file_content = ''
    full_result_file = '.'.join(file.split('.')[:-1]) + ".json"

    if len(test_results) == 0:
        print("No errors found! Omitting html save.")
        return
    if isinstance(test_results[0], TestFailureResult):
        template = env.get_template('runtime_failure_report.html')
        grouped_res = defaultdict(list)
        for tr in test_results:
            tr.trace = json.dumps(json.loads(tr.trace), indent=4)
            grouped_res[tr.tool].append(tr)
        html_file_content = template.render(test_results=grouped_res, full_result_file=full_result_file)
    elif isinstance(test_results[0], PromptSetTestResults):
        template = env.get_template('correctness_failure_report.html')
        test_results = transform_test_results(test_results)
        grouped_res = defaultdict(list)
        for result in test_results:
            grouped_res[result.tool].append(result)
        html_file_content = template.render(test_results=grouped_res, full_result_file=full_result_file)
    with open(file, 'w') as f:
        f.write(html_file_content)
    with resources.path('src.templates', 'toolfuzz.png') as template_path:
        shutil.copy(template_path, './toolfuzz.png')


def transform_test_results(test_results: List[PromptSetTestResults]) -> List[PromptSetTestResultsHtml]:
    result = []
    for tr in test_results:
        runs = []
        for run in tr.individual_run_test_results:
            arg_color = get_index(tr.same_arguments_buckets, run.tool_arguments)
            out_color = get_index(tr.same_output_buckets, run.tool_output)
            runs.append(TestResultsHtml(prompt=run.prompt,
                                        tool_arguments=run.tool_arguments,
                                        tool_output=run.tool_output,
                                        agent_output=run.agent_output,
                                        tool_failure=run.tool_failure,
                                        unexpected_agent_output=run.unexpected_agent_output,
                                        agent_output_not_relevant=run.agent_output_not_relevant,
                                        llm_agent_out_reason=run.llm_agent_out_reason,
                                        trace=json.dumps(json.loads(run.trace), indent=4),
                                        input_bucket_color=TEXT_COLOR_CLASSES[arg_color],
                                        input_bucket=arg_color,
                                        output_bucket_color=TEXT_COLOR_CLASSES[out_color],
                                        output_bucket=out_color))
        result.append(PromptSetTestResultsHtml(tool=tr.tool, template_question=tr.template_question,
                                               llm_output_expectation=tr.llm_output_expectation,
                                               individual_run_test_results=runs))
    return result


def get_index(buckets, value):
    for idx, item in enumerate(buckets):
        if item.bucket_value == value and value is not None and value != 'None':
            return idx
    return -1


def save_test_results(test_results, file='./results.json'):
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read().strip()
            if len(content) == 0:
                data = []
            else:
                data = json.loads(content)
            data += [tr.model_dump() for tr in test_results]
    else:
        data = [tr.model_dump() for tr in test_results]
    with open(file, 'w') as f:
        f.write(json.dumps(data))


if __name__ == '__main__':
    # Load the results_correctness.json
    import os

    with open('../../correctness_results.json', 'r') as f:
        data = json.load(f)
    test_results = [PromptSetTestResults.model_validate(tr) for tr in data]
    save_test_results_html(test_results)
