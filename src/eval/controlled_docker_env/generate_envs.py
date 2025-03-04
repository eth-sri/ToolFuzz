import os
import re
import shutil
import subprocess
from pydantic_yaml import to_yaml_str

from src.eval.controlled_docker_env.environment import Environments, Environment


def get_setups(home_dir):
    home_dir = f"{home_dir}/setups"
    setups = []
    for setup in os.listdir(home_dir):
        if setup.startswith("setup_"):
            tree_file, field = get_tree(home_dir, setup)
            setups.append((setup, tree_file, field))
    return setups


def get_tree(home_dir, setup_file):
    field_name = setup_file.split('setup_')[-1]
    field_name = field_name.split('.sh')[0]
    for file in os.listdir(home_dir):
        if file.startswith("expected_tree") and field_name in file:
            with open(f"{home_dir}/{file}", 'r') as f:
                tree = f.read()
                return tree, field_name
    return None, None


def get_ground_truth_scripts(home_dir, field):
    files = []
    field = field.replace(' ', '_')
    home_dir = f"{home_dir}/ground_truths/setup_{field}"
    for file in os.listdir(home_dir):
        if file.endswith(".sh"):
            files.append(file)
    return files


def tree_to_files(tree):
    """
    Converts a tree string to a list of files, because chatgpt doesn't sort the files in the tree alphabetically
    """
    files = set()
    lines = tree.split('\n')
    for line in lines:
        line = line.strip()
        if len(line) == 0 or line[0].isdigit() or line[0] == '/':
            continue

        file_name = line.replace('├── ', '').replace('└── ', '').replace('│   ', '').replace('│\xa0\xa0', '').replace(
            '    ', '').strip()
        if file_name.startswith("./"):
            continue
        files.add(file_name)
    return files


def run_and_validate_setup(home, setup):
    try:
        setup_script = f"{home}/setups/{setup[0]}"
        tree = setup[1]
        root_dir = f"{home}/ground_truths/{setup[2]}"

        subprocess.run(["bash", setup_script, root_dir], check=True)
        fs_result = subprocess.run(["tree", root_dir], check=True, capture_output=True, text=True)
        fs_files = tree_to_files(fs_result.stdout)
        gpt_files = tree_to_files(tree)
        if fs_files != gpt_files:
            print(f"FAILURE: Setup {setup} failed, difference in files is {fs_files ^ gpt_files}")
            return False
        print(f"SUCCESS: {setup[0]}")
        return True

    except Exception as e:
        print(f"FAILURE: Setup {setup[0]} failed with exception {e}")


def run_and_validate_gt_scripts(home_dir, gt_scripts, field, envs):
    og_home_dir = home_dir
    home_dir = f"{home_dir}/ground_truths/setup_{field.replace(' ', '_').lower()}"
    pattern = r"prompt(\d+)_gt\.sh"
    local_envs = []
    for script in gt_scripts:
        try:
            indx = int(re.search(pattern, script).group(1))
            if os.path.exists(f"{home_dir}/{field}_{indx}"):
                shutil.rmtree(f"{home_dir}/{field}_{indx}")
            subprocess.run(["bash", f"{home_dir}/{script}", f"{home_dir}/{field}_{indx}"], check=True)
            print(f"SUCCESS: {script}")
            envs.append(Environment(setup_file=f"{og_home_dir}/setups/setup_{field}.sh",
                                    prompt_file=f"{og_home_dir}/prompts/{field}/prompt{indx}.txt",
                                    ground_truth_directory=f"{home_dir}/{field}_{indx}"))
            local_envs.append(Environment(setup_file=f"{og_home_dir}/setups/setup_{field}.sh",
                                          prompt_file=f"{og_home_dir}/prompts/{field}/prompt{indx}.txt",
                                          ground_truth_directory=f"{home_dir}/{field}_{indx}"))
        except Exception as e:
            print(f"FAILURE: {script} failed with exception {e}")

    yaml_str = to_yaml_str(Environments(environments=local_envs))
    with open(f'envs/envs_{field}.yml', 'w') as f:
        f.write(yaml_str)


def main():
    home_dir = "."
    setups = get_setups(home_dir)

    environments = []
    for setup in setups:
        if run_and_validate_setup(home_dir, setup):
            gt_scripts = get_ground_truth_scripts(home_dir, setup[2])
            run_and_validate_gt_scripts(home_dir, gt_scripts, setup[2], environments)
    yaml_str = to_yaml_str(Environments(environments=environments))
    with open('envs_all.yml', 'w') as f:
        f.write(yaml_str)


if __name__ == "__main__":
    main()
