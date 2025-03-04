import argparse
import json
import os
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import seaborn.objects as so
from tqdm import tqdm

from src.eval.toolfuzz.loaders.module_tool_loader import ToolLoader as OurToolsLoader
from src.eval.toolfuzz.utils.tool_loader import ToolLoader
from src.toolfuzz.runtime.fuzz.fuzzer import Fuzzer

grouped_tools = [
    ('Image and Media Tools',
     {"Dall-E-Image-Generator",
      "Get NASA Image and Video Library media metadata location",
      "Get NASA Image and Video Library media metadata manifest",
      "Search NASA Image and Video Library media"}
     ),
    ('Academic and Research Tools',
     {"Wikidata", "arxiv", "pub_med", "semanticscholar"}),

    ('Search and Discovery Tools',
     {"duckduckgo_results_json",
      "duckduckgo_search",
      "open-street-map-search",
      "stack_exchange",
      "youtube_search"}),

    ('HTTP Request Methods (API Communication)',
     {"requests_delete", "requests_get", "requests_patch", "requests_post", "requests_put"}),

    ('File Management Tools',
     {"copy_file", "file_delete", "file_search", "move_file", "read_file", "write_file", "list_directory"}),
]


def args():
    parser = argparse.ArgumentParser(description="Test agent tools.")
    parser.add_argument('-j', dest='json_file')
    return parser.parse_args()


cl_args = args()


def stats_for_tool(tool_data):
    tool_data = [i for i in tool_data]
    fuzzer_exception = set([tr['expected_exception'] for tr in tool_data])
    test_results = [tr for tr in tool_data if tr['successful_trigger']]
    agent_exception = set([tr['exception'].split('>')[0] for tr in test_results])

    return len(fuzzer_exception), fuzzer_exception, len(agent_exception), agent_exception


def stats_for_correctness(tool_data):
    success = 0
    failed_answer = 0
    for data in tool_data:
        if data['is_tool_failure'] == False and data['is_correct_answer'] == False:
            failed_answer += 1
        if data['is_tool_failure'] == False and data['is_correct_answer'] == True:
            success += 1

    return failed_answer, success


def confusion_matrix(data, tool_name):
    axes = ['TP', 'TN', 'FP', 'FN']
    res = []
    tool_data = [sample for sample in data if sample['tool_label'] == tool_name]
    for axis in axes:
        res.append(
            (f'arg_inconsistency: {axis}', len([l for l in tool_data if l['argument_consistency'].upper() == axis])))

    for axis in axes:
        res.append(
            (f'out_inconsistency: {axis}', len([l for l in tool_data if l['output_consistency'].upper() == axis])))

    for axis in axes:
        failures = []
        for l in tool_data:
            failures += l['tool_failures']
        res.append((f'tool_failures: {axis}', len([l for l in failures if l == axis])))

    for axis in axes:
        llm_outs = []
        for l in tool_data:
            llm_outs += l['unexpected_output']
        res.append((f'unexpected_out: {axis}', len([l for l in llm_outs if l == axis])))

    for axis in axes:
        relevent = []
        for l in tool_data:
            relevent += l['not_relevant']
        res.append((f'not_relevant: {axis}', len([l for l in relevent if l == axis])))

    res.append(('Bugs: ', len([l for l in tool_data if l['has_bug']])))

    return res


def label_stats(file):
    with open(file, 'r') as f:
        data = json.loads(f.read())
    tools = set([sample['tool_label'] for sample in data])
    for tool in tools:
        print(tool, confusion_matrix(data, tool))
        print()


def main():
    print(os.getcwd())
    file = cl_args.json_file
    label_stats(file)


def text_stats(text):
    word_count = len(text.split())

    # Count the number of characters (including spaces)
    character_count = len(text)

    # Count the number of sentences (assuming sentences end with '.', '!', or '?')
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    return character_count, word_count, sentence_count


def documentation_stats():
    tools = ToolLoader('langchain_community.tools').get_tools()

    word_count = []
    char_count = []
    sentence_count = []

    for tool in tools:
        pg = PromptGenerator(tool)
        tool_docs = pg.tool_prompt
        cc, wc, sc = text_stats(tool_docs)
        print(cc, wc, sc)
        word_count.append(wc)
        char_count.append(cc)
        sentence_count.append(sc)

    bins_cc = [0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400]
    bins_wc = [0, 100, 200, 300, 400, 500, 750, 1000, 1500, 2000, 3000]
    bins_sc = [0, 1, 2, 3, 4, 5, 7, 10, 15, 20, 25, 30]
    plt.hist(sentence_count, bins=bins_sc, edgecolor='black')
    plt.xlabel('Range')
    plt.ylabel('Number of tools')
    plt.title('Histogram of the number of sentences per tool documentation')
    plt.savefig('sc.png')
    plt.cla()
    plt.clf()

    plt.hist(char_count, bins=bins_cc, edgecolor='black')
    plt.xlabel('Range')
    plt.ylabel('Number of tools')
    plt.title('Histogram of the number of characters per tool documentation')
    plt.savefig('cc.png')
    plt.cla()
    plt.clf()

    plt.hist(word_count, bins=bins_wc, edgecolor='black')
    plt.xlabel('Range')
    plt.ylabel('Number of tools')
    plt.title('Histogram of the number of words per tool documentation')
    plt.savefig('wc.png')
    plt.cla()
    plt.clf()


def parameter_stats():
    tool_loader = ToolLoader('langchain_community.tools')
    tools = tool_loader.get_tools()

    num_of_params = []
    type_of_params = {}
    skip_params = ['typing.Optional[langchain_core.callbacks.manager.CallbackManagerForToolRun]',
                   'Optional[CallbackManagerForToolRun]']
    arg_strs = {
        'string': 'string',
        'str': 'string',
        "<class 'str'>": 'string',
        'boolean': 'boolean',
        'typing.Optional[int]': "Optional['int']",
        "<class 'int'>": 'int',
        "<class 'bool'>": 'bool',
    }

    for tool in tqdm(tools, desc="Analyzing tools"):
        fuzzer = Fuzzer(tool)
        args = fuzzer.tool_args
        num_args = 0
        used_arg_types = set()
        for arg in args:
            if arg.name == 'self':
                continue
            elif arg.type.name in arg_strs:
                arg_str = arg_strs[arg.type.name]
            elif 'enum' in arg.type.name.lower():
                arg_str = 'enum'
            elif 'union' in arg.type.name.lower():
                arg_str = 'union'
            elif 'list' in arg.type.name.lower():
                arg_str = 'list'
            elif 'dict' in arg.type.name.lower():
                arg_str = 'dict'

            if arg_str in skip_params:
                continue

            used_arg_types.add(arg_str)
            num_args += 1

        for arg_str in used_arg_types:
            if arg_str in type_of_params:
                type_of_params[arg_str] += 1
            else:
                type_of_params[arg_str] = 1
        num_of_params.append(num_args)

    # Data for the first plot (parameter type usage)
    categories = list(type_of_params.keys())
    frequencies = list(type_of_params.values())

    # Create the first histogram using Seaborn
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=categories, y=frequencies, palette="viridis")

    # Add labels and title
    plt.xlabel('Parameter type', fontsize=12)
    plt.ylabel('Number of tools', fontsize=12)
    plt.title('Histogram of Parameter Type Usage', fontsize=14)
    # plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the first plot
    plt.savefig('param_type_usage.png')
    plt.clf()

    # Data for the second plot (number of parameters used by tools)
    tool_w_params = Counter(num_of_params)
    categories = [str(i) for i in list(tool_w_params.keys())]
    frequencies = list(tool_w_params.values())

    # Create the second histogram using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x=categories, y=frequencies, palette="rocket")

    # Add labels and title
    plt.xlabel('Number of parameters', fontsize=12)
    plt.ylabel('Number of tools', fontsize=12)
    plt.title('Histogram of Number of Parameters Used by Tools', fontsize=14)
    plt.tight_layout()

    # Save the second plot
    plt.savefig('param_num_usage.png')
    plt.clf()


def failure_stats(file):
    with open(file, 'r') as f:
        failure_res = json.loads(f.read())

    # Group by tool -> How many failed attempts, how many different excpetions I got
    tools = set([t['tool'] for t in failure_res])
    print(f"Number of tested tools {len(tools)}, {tools}")
    print("==================================================================")
    for tool in tools:
        print(f"TOOL: '{tool}'")
        tool_res = [t for t in failure_res if t['tool'] == tool]
        # number of found errors and the errors:
        exceptions = set([t['exception'] for t in tool_res])
        print("Triggered exceptions:", len(exceptions), exceptions)
        # Some counts:
        print("Number of succ triggers: ", len([x for x in tool_res if x['successful_trigger']]), "out of",
              len(tool_res))

        print(Counter([x['exception'] for x in tool_res]))

        print("==================================================================")


def correctness_stats(file):
    with open(file, 'r') as f:
        res = json.loads(f.read())
    tools = set([t['tool'] for t in res])
    tools = sorted(list(tools))
    print(f"Number of tested tools: {len(tools)}, {tools}")

    total_bugs, total_prompts, total_prompt_sets = 0, 0, 0

    for tool in tools:
        print("====================================================")
        print(tool)
        tool_run = [t for t in res if t['tool'] == tool]
        prompt_runs = 0
        bucket_inp_cons = 0
        bucket_outp_cons = 0
        tool_failures = 0
        bugs = 0
        buggy_prompts = []

        for run in tool_run:
            prompt_runs += len(run['template_prompts'])
            bucket_inp_cons += 1 if run['tool_arguments_inconsistency'] else 0
            bucket_outp_cons += 1 if run['tool_output_inconsistency'] else 0
            for indi_run in run['individual_run_test_results']:
                tool_failures += 1 if indi_run['tool_failure'] else 0
                if run['tool_arguments_inconsistency'] and run['tool_output_inconsistency'] and indi_run[
                    'unexpected_agent_output'] <= 5:
                    bugs += 1
                    buggy_prompts.append(indi_run['prompt'])
        print(f'Correctness bugs: {bugs}, {buggy_prompts}')
        print(f"Total prompts: {prompt_runs}, Prompt sets: {len(tool_run)}")
        print(f"Tool failures: {tool_failures}")
        print(f"Inconsistent inputs: {bucket_inp_cons}, Outputs: {bucket_outp_cons}")

        total_prompt_sets += len(tool_run)
        total_prompts += prompt_runs
        total_bugs += bugs

    print(f"Total bugs found: {total_bugs}. Total prompts set: {total_prompt_sets}. Total prompts: {total_prompts}.")


def baseline_stats(json_file):
    with open(json_file, 'r') as f:
        baseline_stat = json.loads(f.read())
    print(f"Number of baseline test runs: {len(baseline_stat)}")
    tools = set([t['tool'] for t in baseline_stat])
    tools = sorted(list(tools))
    total_incorrect = 0
    print(f"Tested tools: {len(tools)} {tools}")
    print("")
    print("Per tool info")
    for tool in tools:
        print('===========================================')
        print(tool)
        tool_runs = [t for t in baseline_stat if t['tool'] == tool]
        incorrects = len([t for t in tool_runs if t['successful_trigger']])
        print(f"Incorrects found: {incorrects} out of {len(tool_runs)}")
        total_incorrect += incorrects
    print(f"Total incorrect: {total_incorrect}")


def add(map, item, tool):
    if item not in map:
        map[item] = {tool}
    else:
        map[item].add(tool)


def transform_exceptions(synth_tools_excepts):
    res = {}
    for exception, tool in synth_tools_excepts:
        if 'valueerror' in exception.lower():
            if 'an output parsing error' in exception.lower():
                add(res, '<class \'ValueError\'>An output parsing error occurred.', tool)
            elif 'Error code: 400':
                add(res, 'HTTP related error', tool)
            else:
                print(exception)
        elif 'http' in exception.lower():
            add(res, 'HTTP related error', tool)
        elif 'modulenotfounderror' in exception.lower():
            add(res, "<class 'ModuleNotFoundError'>", tool)
        elif "'attributeerror'>'nonetype' object has no attribute 'invoke" in exception.lower():
            add(res, exception, tool)
        elif "'attributeerror'>'str' object has no attribute 'keys'" in exception.lower():
            add(res, 'Tool specific error', tool)
        elif 'assertionerror' in exception.lower():
            add(res, 'Input grammar assertion error', tool)
        elif 'jsondecodeerror' in exception.lower():
            add(res, 'Input grammar assertion error', tool)
        elif 'pydantic' in exception.lower() and 'validationerror' in exception.lower():
            add(res, 'Input grammar types assertion error', tool)
        elif 'toolexception' in exception.lower() and 'arguments' in exception.lower():
            add(res, 'Input grammar types assertion error', tool)
        elif 'typeerror' in exception.lower():
            add(res, 'Input grammar assertion error', tool)
        elif 'duckduckgo' in exception.lower() and 'exception' in exception.lower():
            add(res, 'Tool specific error', tool)
        elif 'retryerror' in exception.lower() and 'connectionrefused' in exception.lower():
            add(res, 'HTTP related error', tool)
        elif 'keyerror' in exception.lower():
            add(res, 'Tool specific error', tool)
        elif "GraphQLError'>Cannot query field".lower() in exception.lower():
            add(res, 'Input grammar assertion error', tool)
        elif "GraphQLSyntaxError'>Syntax Error".lower() in exception.lower():
            add(res, 'Input grammar assertion error', tool)
        elif "GraphRecursionError'>Recursion limit".lower() in exception.lower():
            add(res, 'Langgraph error', tool)
        elif 'requests.exceptions' in exception.lower() and 'connection' in exception.lower():
            add(res, 'HTTP related error', tool)
        elif 'openai.badrequesterror' in exception.lower() and (
                'string too long' in exception.lower() or "model's maximum context length" in exception):
            add(res, 'Invalid tool output for the model', tool)
        elif 'zerodivision' in exception.lower():
            add(res, 'Tool specific error', tool)
        elif 'invalidurl' in exception.lower():
            add(res, 'Tool specific error', tool)
        else:
            print(exception)

    return res


def exception_groups(json_file):
    with open(json_file, 'r') as f:
        data = json.loads(f.read())
    # Now lets look at the exceptions I have
    # Firstly group them in our and community tools:
    regrouped_data = {}
    for d in data:
        prompt = d['prompt']
        if prompt not in regrouped_data:
            regrouped_data[prompt] = d
        elif (not regrouped_data[prompt]['successful_trigger']) and d['successful_trigger']:
            regrouped_data[prompt] = d
    data = list(regrouped_data.values())

    our_tools = OurToolsLoader('src.buggy_tools').load_tools()
    our_tools = [t.name for t in our_tools]

    synthetic_tools = [d for d in data if d['tool'] in our_tools]

    print('Tested synth tools: ', len(set([d['tool'] for d in synthetic_tools])))

    langchain_tools = [d for d in data if d['tool'] not in our_tools]

    print('Langchain tools: ', len(set([d['tool'] for d in langchain_tools])))

    print(len(synthetic_tools), len(langchain_tools))
    langc_excepts = [(d['exception'], d['tool']) for d in langchain_tools if d['successful_trigger']]
    synth_tools_excepts = [(d['exception'], d['tool']) for d in synthetic_tools if d['successful_trigger']]
    # Now try to group them:
    langc_excepts = transform_exceptions(langc_excepts)
    synth_tools_excepts = transform_exceptions(synth_tools_excepts)
    print('======Langchain=======')
    for k, v in langc_excepts.items():
        print(k, len(v))
    print('======Synthetic=======')
    for k, v in synth_tools_excepts.items():
        print(k, len(v))


def stacked_barchart(white_json, gray_json, tf_json):
    # Load data from JSON files
    with open(white_json, 'r') as f:
        white_data = json.load(f)

    with open(gray_json, 'r') as f:
        gray_data = json.load(f)

    with open(tf_json, 'r') as f:
        tf_data = json.load(f)

    # Define the valid toolset
    toolset = {
        'Dall-E-Image-Generator', 'Get NASA Image and Video Library media metadata location',
        'Get NASA Image and Video Library media metadata manifest',
        'Search NASA Image and Video Library media', 'Wikidata', 'arxiv',
        'duckduckgo_results_json', 'duckduckgo_search', 'json_spec_list_keys',
        'open-street-map-search', 'pub_med', 'python_repl_ast', 'requests_delete',
        'requests_get', 'requests_patch', 'requests_post', 'requests_put', 'semanticscholar',
        'stack_exchange', 'youtube_search', 'copy_file', 'file_delete', 'file_search',
        'move_file', 'read_file', 'write_file', 'list_directory'
    }

    # Filter data based on the toolset
    white_data = [d for d in white_data if d['tool'] in toolset]
    gray_data = [d for d in gray_data if d['tool'] in toolset]
    tf_data = [d for d in tf_data if d['tool'] in toolset]

    # Prepare data for plotting
    plot_data = []
    for tool in toolset:
        white_count = len([d for d in white_data if d['tool'] == tool])
        gray_count = len([d for d in gray_data if d['tool'] == tool])

        # Extract ToolFuzz counts
        tfd = [d['individual_run_test_results'] for d in tf_data if d['tool'] == tool]
        tfd = [item for sublist in tfd for item in sublist]  # Flatten the list
        toolfuzz_count = len(tfd)

        # Append data in long format
        plot_data.append({'Tool': tool, 'Category': 'Whitebox', 'Count': white_count})
        plot_data.append({'Tool': tool, 'Category': 'Greybox', 'Count': gray_count})
        plot_data.append({'Tool': tool, 'Category': 'ToolFuzz', 'Count': toolfuzz_count})

    # Convert to DataFrame
    df = pd.DataFrame(plot_data)

    # Create a stacked bar chart using `sns.objects`
    p = (
        so.Plot(df, x="Category", y="Count", color="Tool")
        .add(so.Bar(), so.Stack())
        .layout(size=(10, 6))
        .label(x="Category", y="Count", color="Tool")
    )

    # Save the plot
    p.save("stacked_bar_chart.png")


def bar_chart(white_json, gray_json, tf_json):
    with open(white_json, 'r') as f:
        white_data = json.loads(f.read())

    with open(gray_json, 'r') as f:
        gray_data = json.loads(f.read())

    with open(tf_json, 'r') as f:
        tf_data = json.loads(f.read())

    # First filter out the :
    toolset = {'Dall-E-Image-Generator', 'Get NASA Image and Video Library media metadata location',
               'Get NASA Image and Video Library media metadata manifest',
               'Search NASA Image and Video Library media', 'Wikidata', 'arxiv',
               'duckduckgo_results_json', 'duckduckgo_search',
               'open-street-map-search', 'pub_med', 'requests_delete',
               'requests_get', 'requests_patch', 'requests_post', 'requests_put', 'semanticscholar',
               'stack_exchange', 'youtube_search', 'copy_file', 'file_delete', 'file_search',
               'move_file', 'read_file', 'write_file', 'list_directory'}

    white_data = [d for d in white_data if d['tool'] in toolset]
    gray_data = [d for d in gray_data if d['tool'] in toolset]
    tf_data = [d for d in tf_data if d['tool'] in toolset]

    plot_data = []
    for group_name, tool_group in grouped_tools:
        white_count = len([d for d in white_data if d['tool'] in tool_group])
        gray_count = len([d for d in gray_data if d['tool'] in tool_group])

        # Extract ToolFuzz counts
        tfd = [d['individual_run_test_results'] for d in tf_data if d['tool'] in tool_group]
        tfd = [item for sublist in tfd for item in sublist]
        toolfuzz_count = len(tfd)

        # Append data in long format
        plot_data.append({'Tool': group_name, 'Category': 'Whitebox', 'Count': white_count})
        plot_data.append({'Tool': group_name, 'Category': 'Greybox', 'Count': gray_count})
        plot_data.append({'Tool': group_name, 'Category': 'ToolFuzz', 'Count': toolfuzz_count})

        # Convert to DataFrame
        df = pd.DataFrame(plot_data)

        # Create a stacked bar chart using Seaborn
        plt.figure(figsize=(12, 8))
        sns.barplot(data=df, x='Category', y='Count', hue='Tool', ci=None)

        # Customize the plot
        plt.title('Stacked Bar Chart Example', fontsize=16)
        plt.ylabel('Count', fontsize=14)
        plt.xlabel('Category', fontsize=14)
        # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Tool')
        plt.tight_layout()
        plt.savefig(f'bar_chart.png')
        # Save the plot
        plt.show()


def barchart_per_tool(labels_white, labels_grey, labels_tf):
    with open(labels_white, 'r') as f:
        res_white = json.loads(f.read())
    with open(labels_grey, 'r') as f:
        res_grey = json.loads(f.read())
    with open(labels_tf, 'r') as f:
        res_tf = json.loads(f.read())
    data = {}
    for title, group in grouped_tools:
        white = [val for tool, val in res_white.items() if tool in group]
        tp_white = [d[1] - d[0] for d in white]
        gray = [val for tool, val in res_grey.items() if tool in group]
        tp_gray = [d[1] - d[0] for d in gray]

        tf = [val for tool, val in res_tf.items() if tool in group]
        tp_tf = [d[1] - d[0] for d in tf]
        data[title] = {'ToolFuzz White-box': sum(tp_white), 'ToolFuzz Gray-box': sum(tp_gray), 'ToolFuzz': sum(tp_tf)}

    # Convert the data into a DataFrame
    df = pd.DataFrame(data).reset_index().melt(id_vars='index', var_name='Toolkit', value_name='Value')
    df.rename(columns={'index': 'Method'}, inplace=True)

    # Create the grouped bar chart
    plt.figure(figsize=(10, 6))
    barplot = sns.barplot(data=df, x='Toolkit', y='Value', hue='Method', palette='Set2')

    for p in barplot.patches:
        barplot.annotate(
            format(p.get_height(), '.0f'),  # Format the value (e.g., 1 decimal place)
            (p.get_x() + p.get_width() / 2., p.get_height()),  # Position (x, y)
            ha='center', va='center',  # Alignment
            fontsize=10, color='black', xytext=(0, 5), textcoords='offset points'  # Styling and offset
        )
    # Add labels and title
    plt.title('Performance of Methods Across Toolkits', fontsize=16)
    plt.xlabel('Toolkit', fontsize=14)
    plt.ylabel('Value', fontsize=14)
    plt.legend(title='Method', fontsize=12)
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig('barchart_per_tool_category.png')
    # Show the plot
    plt.show()


def stacked_grouped_barchart(labels_white, labels_grey, labels_tf):
    with open(labels_white, 'r') as f:
        res_white = json.loads(f.read())
    with open(labels_grey, 'r') as f:
        res_grey = json.loads(f.read())
    with open(labels_tf, 'r') as f:
        res_tf = json.loads(f.read())

    data = {}
    for title, group in grouped_tools:
        white = [val for tool, val in res_white.items() if tool in group]
        tp_white = [d[1] - d[0] for d in white]
        fp_white = [d[0] for d in white]
        gray = [val for tool, val in res_grey.items() if tool in group]
        tp_gray = [d[1] - d[0] for d in gray]
        fp_gray = [d[0] for d in gray]

        tf = [val for tool, val in res_tf.items() if tool in group]
        tp_tf = [d[1] - d[0] for d in tf]
        fp_tf = [d[0] for d in tf]
        data[title] = {
            'ToolFuzz White-box': [sum(fp_white), sum(tp_white)],
            'ToolFuzz Gray-box': [sum(fp_gray), sum(tp_gray)],
            'ToolFuzz': [sum(fp_tf), sum(tp_tf)]
        }

    categories = list(data.keys())
    tools = ["ToolFuzz White-box", "ToolFuzz Gray-box", "ToolFuzz"]

    x = np.arange(len(categories))
    bar_width = 0.25

    fig, ax = plt.subplots(figsize=(10, 6))

    for i, tool in enumerate(tools):
        fp_vals = [data[cat][tool][0] for cat in categories]
        tp_vals = [data[cat][tool][1] for cat in categories]

        offset = (i - 1) * bar_width

        # Always give each bar a legend label = tool
        bottom_bars = ax.bar(
            x + offset,
            fp_vals,
            bar_width,
            label=tool  # <--- changed to tool
        )

        # For the top segment, no separate legend label (unless you want one)
        top_bars = ax.bar(
            x + offset,
            tp_vals,
            bar_width,
            bottom=fp_vals,
            color=bottom_bars[0].get_facecolor(),
            alpha=0.6
        )

        # Optionally add multiline text at the top of each stacked bar
        for j, cat in enumerate(categories):
            top_height = fp_vals[j] + tp_vals[j]  # total stacked height
            label_str = f"TP: {tp_vals[j]}\nFP: {fp_vals[j]}"  # newline between FP and TP
            x_center = (x[j] + offset) + bar_width / 2
            ax.text(
                x_center - 0.125,
                top_height + 1,  # shift upward by 1
                label_str,
                ha="center",
                va="bottom",
                multialignment="center"  # ensures each line is centered
            )

    ax.set_xticks(x)
    ax.set_xticklabels(categories, rotation=30, ha="right")
    ax.set_ylabel("Value")
    ax.set_title("Grouped + Stacked Bars with Full Legend")
    ax.legend()  # Now you'll see labels for all three tools
    plt.tight_layout()
    plt.savefig('stacked_grouped_barchart.png')
    plt.show()


if __name__ == '__main__':
    stacked_grouped_barchart(
        '/home/ivan/ETH/MasterThesis/code/Thesis/src/test/results/finals/baseline_labels_white.json',
        '/home/ivan/ETH/MasterThesis/code/Thesis/src/test/results/finals/baseline_labels_gray.json',
        '/home/ivan/ETH/MasterThesis/code/Thesis/src/test/results/finals/toolfuzz_labels.json')
