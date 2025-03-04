import argparse
import json
import pprint
from typing import List

from pydantic import BaseModel, Field


def get_args():
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', dest='file', help='File to grade')
    return ap.parse_args()


args = get_args()


class LabeledToolOutput(BaseModel):
    tool_label: str = Field()
    argument_consistency: str = Field()
    output_consistency: str = Field()
    tool_failures: List[str] = Field()
    unexpected_output: List[str] = Field()
    not_relevant: List[str] = Field()
    has_bug: bool = Field()


def populate_label(sample):
    print(sample['tool'])
    pprint.pp(sample['same_arguments_buckets'], width=250)
    print(sample['tool_arguments_inconsistency'])
    argument_consistency = input('[TP/TN/FP/FN]: ')
    pprint.pp(sample['same_output_buckets'], width=250)
    print(sample['tool_output_inconsistency'])
    output_consistency = input('[TP/TN/FP/FN]: ')

    # LLM output eval:
    tool_failures = []
    output_expected = []
    not_relevant = []
    for indx, test_res in enumerate(sample['individual_run_test_results']):
        print(f"[{indx}/{len(sample['individual_run_test_results'])}]")
        print(test_res['tool_output'])
        print(test_res['tool_failure'])
        tool_failures.append(input('tool failure [TP/TN/FP/FN]: '))
        print('LLM expect: ' + sample['llm_output_expectation'])
        print('Tool out:   ' + test_res['tool_output'])
        print('Agent out:  ' + test_res['agent_output'])
        print(test_res['unexpected_agent_output'])
        print('Reason:     ' + test_res['llm_agent_out_reason'])
        output_expected.append(input('[TP/TN/FP/FN]: '))
        print(test_res['agent_output_not_relevant'])
        not_relevant.append(input('Agent output relevancy: [TP/TN/FP/FN]: '))
    overall = input('Does the set have bug or not [Y/N]:')
    return LabeledToolOutput(tool_label=sample['tool'], argument_consistency=argument_consistency,
                             output_consistency=output_consistency, tool_failures=tool_failures,
                             unexpected_output=output_expected, not_relevant=not_relevant,
                             has_bug=True if overall.upper() == 'Y' else False)


def main():
    with open(args.file) as f:
        content_to_grade = json.loads(f.read())
    labels = []
    last_tool = ''
    skipping = False
    for indx, sample in enumerate(content_to_grade):
        print(f'[{indx}/{len(content_to_grade)}]')
        if skipping and sample['tool'] == last_tool:
            continue
        if sample['tool'] != last_tool:
            last_tool = sample['tool']
            skip = input(f'Skip tool {last_tool} [Y/N]:')
            if skip == 'Y':
                skipping = True
                continue
        # label time:
        label = populate_label(sample)
        labels.append(label)
    print(labels)
    with open('./labels_correctness.json', 'w') as f:
        f.write(json.dumps([label.model_dump() for label in labels]))


def baseline_labeler(file):
    with open(file, 'r') as f:
        data = json.loads(f.read())
    print(len(data))
    # Regroup data:
    regrouped_data = {}
    for d in data:
        prompt = d['prompt']
        if prompt not in regrouped_data:
            regrouped_data[prompt] = d
        elif (not regrouped_data[prompt]['successful_trigger']) and d['successful_trigger']:
            regrouped_data[prompt] = d
    data = list(regrouped_data.values())
    print('All prompts:', len(data))
    data = [d for d in data if d['successful_trigger']]
    results = {}

    plot_tools = {'Dall-E-Image-Generator', 'Get NASA Image and Video Library media metadata location',
                  'Get NASA Image and Video Library media metadata manifest',
                  'Search NASA Image and Video Library media', 'Wikidata', 'arxiv',
                  'duckduckgo_results_json', 'duckduckgo_search',
                  'open-street-map-search', 'pub_med', 'requests_delete',
                  'requests_get', 'requests_patch', 'requests_post', 'requests_put', 'semanticscholar',
                  'stack_exchange', 'youtube_search', 'copy_file', 'file_delete', 'file_search',
                  'move_file', 'read_file', 'write_file', 'list_directory'}
    data = [d for d in data if d['tool'] in plot_tools]
    for tool in plot_tools:
        print(tool, len([d for d in data if d['tool'] == tool]))
    print(len(data))

    for i in range(len(data)):
        sample = data[i]
        tool_name = sample['tool']
        print(f"Sample #{i}, {tool_name}")
        print(f'Prompt: {sample["prompt"]}')
        print(f'Answer: {sample["expected_exception"]}')
        print(f'Reason: {sample["exception"]}')
        is_bug = input("Is bug Y/N?:")
        is_bug = True if is_bug.lower() == 'y' else False
        if tool_name in results:
            fp = 0 if is_bug else 1
            results[tool_name] += fp
        else:
            results[tool_name] = 0 if is_bug else 1

        print(results)
    with open('baseline_labels.json', 'w') as f:
        f.write(json.dumps(results))


def correctness_stats(file):
    with open(file, 'r') as f:
        res = json.loads(f.read())
    tools = set([t['tool'] for t in res])
    print(f"Number of tested tools: {len(tools)}, {tools}")

    total_bugs = 0
    results = {}
    i = 0
    r = 0
    for tool in tools:
        print("====================================================")
        tool_run = [t for t in res if t['tool'] == tool]
        for run in tool_run:
            print(len(run), f'{r}/{len(tool_run)}')
            r += 1
            for indi_run in run['individual_run_test_results']:
                if run['tool_arguments_inconsistency'] and run['tool_output_inconsistency'] and indi_run[
                    'unexpected_agent_output'] <= 5:
                    i += 1
                    print(f'{i}/842 Tool:{tool}')
                    print(f'Prompt: {indi_run["prompt"]}')
                    print(f'args: {indi_run["tool_arguments"]}')
                    print(f'Answer: {indi_run["agent_output"]}')
                    print(f'Reason: {indi_run["llm_agent_out_reason"]}')
                    print(f'Expectation: {run["llm_output_expectation"]}')
                    total_bugs += 1
                    is_bug = input("Is bug Y/N?:")
                    is_bug = True if is_bug.lower() == 'y' else False

                    if tool in results:
                        fp = 0 if is_bug else 1
                        results[tool] += fp
                    else:
                        results[tool] = 0 if is_bug else 1
                    print(f"Results: {results}")
                    print(f"Detected bugs: {total_bugs}")
                    if i % 5 == 0:
                        # save results:
                        with open('correctness_stats.json', 'w') as f:
                            f.write(json.dumps(results))
    with open('correctness_stats.json', 'w') as f:
        f.write(json.dumps(results))
    print(i)


if __name__ == '__main__':
    baseline_labeler('/src/eval/baseline/baseline_greybox_correctness.json')
