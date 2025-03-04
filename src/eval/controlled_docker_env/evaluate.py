import subprocess
import argparse

from tqdm import tqdm

from src.eval import EvaluateResult
from src.eval.controlled_docker_env.environment import Environments
from src.toolfuzz.utils import save_test_results


def get_args():
    parser = argparse.ArgumentParser(description="Evaluation on docker container environment")
    parser.add_argument('-c', dest='config_file')
    parser.add_argument('-i', dest='id_index')
    parser.add_argument('-p', dest='file_prefix')
    return parser.parse_args()


args = get_args()


def build_docker_file(setup_file, prompt_file, ground_truth_dir, field):
    # docker build -t eval_container --build-arg SETUP_FILE=./setup.sh --build-arg PROMPT_FILE=./prompt.txt .
    command = ['docker', 'build', '-t',
               f'eval_container_{field}',  # '--no-cache',
               '--build-arg', f'SETUP_FILE={setup_file}',
               '--build-arg', f'PROMPT_FILE={prompt_file}',
               '--build-arg', f'GROUND_TRUTH={ground_truth_dir}',
               '--build-arg', f'AGENT_FILE=./agent_filetoolkit.py',
               '--build-arg',
               f'TOOL_DESC=./tool_descs/baseline_TD_SRC_tkit/fixed_description_toolkit_TD_SRC_{args.id_index}.txt',
               '.']
    output = subprocess.run(command, capture_output=True, text=True, check=True)
    print(f"Building with: '{' '.join(command)}'")
    print(f"DOCKER Build output:\n{output.stdout}")


def run_docker_file(field):
    out = subprocess.run(['docker', 'run', f'eval_container_{field}'], capture_output=True, text=True)
    return out.stdout


def validate_output(output, prompt):
    # parse
    git_output = output.split('On branch master')[-1]
    # validate
    if 'nothing to commit, working tree clean' in git_output:
        print("Test successfully passed")
        return True
    else:
        print(f"Detected differences: {git_output}\n\nFull output: {output}\n\nfor prompt {prompt}")
        return False


def main():
    # 1. read yml with setups:
    envs = Environments.load(args.config_file)
    evals = []
    evals_d = {}
    # 2. Run for each teh build
    for env in tqdm(envs.environments, desc='Running testing on environments'):
        try:
            field = env.setup_file.split('setup_')[-1].split('.sh')[0]
            build_docker_file(env.setup_file, env.prompt_file, env.ground_truth_directory, field)
            output = run_docker_file(field)
            # 3. Validate the result
            with open(env.prompt_file, 'r') as f:
                prompt = f.read()
            is_valid = validate_output(output, prompt)
            evals.append(EvaluateResult(success=is_valid, prompt=prompt, output=output, env_setup=env.setup_file,
                                        prompt_file=env.prompt_file, env_gt_dir=env.ground_truth_directory,
                                        field=field))
            if field in evals_d.keys():
                evals_d[field].append(
                    EvaluateResult(success=is_valid, prompt=prompt, output=output, env_setup=env.setup_file,
                                   prompt_file=env.prompt_file, env_gt_dir=env.ground_truth_directory,
                                   field=field))
            else:
                evals_d[field] = [
                    EvaluateResult(success=is_valid, prompt=prompt, output=output, env_setup=env.setup_file,
                                   prompt_file=env.prompt_file, env_gt_dir=env.ground_truth_directory,
                                   field=field)]
        except Exception as e:
            print(f"ERROR: Something went wrong with the evaluation {e}")
    # 4. Save the results
    for k, v in evals_d.items():
        save_test_results(v, f'eval_{args.file_prefix}_results_{k}.json')
    save_test_results(evals, f'eval_{args.file_prefix}_results.json')


if __name__ == '__main__':
    main()
