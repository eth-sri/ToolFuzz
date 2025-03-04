from src.eval.tool_fixing import ToolFixer
from src.eval.toolfuzz.loaders.langchain_toolkit_loaders import FileManagementToolkitLoader


def main():
    examples_base = "/home/ivan/ETH/MasterThesis/code/Thesis/src/test/results/file_toolkit"

    tools = FileManagementToolkitLoader().get_tool()
    print([tool.name for tool in tools])
    for i in range(20):
        with open(f'./fixed_description_toolkit_TD_SRC_{i}.txt', 'a') as f:
            for tool in tools:
                try:
                    fixer = ToolFixer(tool)
                    # Get the bad examples
                    new_desc = fixer.fix_src()
                    print(new_desc)
                    f.write(f"{tool.name}:" + new_desc.description.strip() + '\n')
                    print(f'{tool.name}-----------------------------------{i}')
                except Exception as e:
                    f.write('\n')
                    print(f"Exception encountered: {e}")


if __name__ == '__main__':
    main()
