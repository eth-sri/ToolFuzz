import os
import json
from src.eval.cross_tool_calling.collect_prompts import CrossCallsResult


def scan_dir(directory, prefix='cross_calling_'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json") and file.startswith(prefix):
                yield file


def generate_markdown_table(tools) -> str:
    """Generate a markdown table from the tools dictionary."""
    # Extract headers
    headers = ['Tool'] + list(next(iter(tools.values())).keys())
    
    # Create markdown table
    table = ['| ' + ' | '.join(headers) + ' |']  # Header row
    table.append('| ' + ' | '.join(['---'] * len(headers)) + ' |')  # Separator row
    
    # Populate rows
    for tool, counts in tools.items():
        row = [tool] + [str(count) for count in counts.values()]
        table.append('| ' + ' | '.join(row) + ' |')
    
    return '\n'.join(table)


def main():
    files = [f for f in scan_dir('./')]
    # Now compute the other stuff!
    # First get table columns and rows:
    columns = ['total']
    columns += [file.split('cross_calling_')[-1][:-5] for file in files]
    init_dict = {col: 0 for col in columns}
    tools = {}
    # Read files now:
    loaded_results = {}
    for file in files:
        print(file)
        with open(file, 'r') as f:
            tool = file.split('cross_calling_')[-1][:-5]
            data = json.loads(f.read())
            loaded_results[tool] = [CrossCallsResult.model_validate(di) for di in data]
    # Now put tehm in the tools dictionary:
    for tool, results in loaded_results.items():
        if tool not in tools:
            tools[tool] = init_dict.copy()
        for result in results:
            if not result.invoked:
                continue
            tools[tool][result.generated_for_tool] += 1
            tools[tool]['total'] += 1
    print(generate_markdown_table(tools))

if __name__ == '__main__':
    main()