import json
import os


def scan_dir(directory, prefix='eval_us_5_results_'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json") and file.startswith(prefix):
                yield file


def files_stats(directory):
    res = []
    for i in range(1, 19):
        files = scan_dir(directory, prefix=f'eval_tkctxt_1_{i}_results_')
        data = []
        for f in files:
            with open(f"{directory}/{f}", 'r') as file:
                data += json.loads(file.read())
        print(f"Results for {i}")
        succ = len([x for x in data if x['success']])
        fails = len([x for x in data if not x['success']])
        res.append((
            len(data),
            succ,
            fails,
            i,
            succ / len(data),
        ))
        print(f"Total number of files: {len(data)}")
        print(f"Number of successful tests: {len([x for x in data if x['success']])}")
        print(f"Number of unsuccessful tests: {len([x for x in data if not x['success']])}")
        print(f"PR: {succ / len(data)}")
        print("=====================================")
    res.sort(key=lambda x: x[1])
    print(res)
    print(sum([pr[-1] for pr in res]) / len(res))


def file_stats(directory):
    files = scan_dir(directory, prefix=f'eval_full11_results_')
    data = []
    for f in files:
        with open(f"{directory}/{f}", 'r') as file:
            fdata = json.loads(file.read())
            data += fdata
            print(file.name, len(fdata), len(data))
    print(f"Total number of files: {len(data)}")
    print(f"Number of successful tests: {len([x for x in data if x['success']])}")
    print(f"Number of unsuccessful tests: {len([x for x in data if not x['success']])}")
    print(f"PR: {len([x for x in data if x['success']]) / len(data)}")
    print("=====================================")


def stats_per_env(directory, prefix=f'eval_fullrun0_results_'):
    files = scan_dir(directory, prefix)
    res_per_env = {}
    for f in files:
        with open(f"{directory}/{f}", 'r') as file:
            env = f.split(prefix)[-1].split('.json')[0]
            fdata = json.loads(file.read())
            passes = len([x for x in fdata if x['success']])
            fails = len([x for x in fdata if not x['success']])
            res_per_env[env] = {"passes": passes, "fails": fails, "total": len(fdata)}

    print('| Category                               | Pass | Fails |')
    print('|----------------------------------------|------|-------|')
    for env, prate in res_per_env.items():
        print(f'| {env: <45} | {prate["passes"]} | {prate["fails"]}|')


if __name__ == '__main__':
    files_stats("./")
