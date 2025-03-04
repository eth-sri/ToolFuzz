import os

from pydantic import BaseModel
from tqdm import tqdm

from src.eval.tool_fixing import ToolFixer
from src.eval.toolfuzz.loaders.langchain_toolkit_loaders import GithubToolkitLoader


class ToolFix(BaseModel):
    name: str
    description: str
    fields: dict


def main():
    examples_base = "/local/home/imilev/agent-tool-testing/src/test/results/git_tkit_3_sleep/"

    tools = GithubToolkitLoader().get_tool()
    # print([tool.name for tool in tools])
    print(tools)
    for i in tqdm(range(10), desc='Generating fixed descriptions.'):
        with open(f'./fixed_description_toolkit_{i}_new_ctx.jsonl', 'a') as f:
            for tool in tools:
                try:
                    fixer = ToolFixer(tool)
                    # Get the bad examples
                    examples_file = f"{examples_base}/result_{tool.name}.json"
                    if not os.path.exists(examples_file):
                        print(f"No examples found for {tool.name}")
                        continue

                    new_desc = fixer.fix_bad_examples(examples_file)
                    fixed_fields = fixer.fix_fields_examples(examples_file)
                    tfix = ToolFix(name=tool.name, description=new_desc.description.strip(), fields=fixed_fields)
                    f.write(tfix.model_dump_json() + '\n')
                except Exception as e:
                    print(f"Exception encountered: {e}")


if __name__ == '__main__':
    main()
