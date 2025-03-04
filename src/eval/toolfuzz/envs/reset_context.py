import os
import subprocess
from time import sleep
from abc import abstractmethod

from src.eval.controlled_git.state import PullRequest, Issue
from src.eval.toolfuzz.utils.git_utils import GitHubUtils


class ResetContext:
    @abstractmethod
    def reset_context(self): raise NotImplementedError


class DummyResetContext(ResetContext):

    def reset_context(self):
        pass


class DelayResetContext(ResetContext):
    def reset_context(self):
        sleep(3)


class ResetFileContext(ResetContext):
    def __init__(self, src_root_dir):
        super().__init__()
        self.src_root_dir = src_root_dir

    def reset_context(self):
        dir_name = f'{self.src_root_dir}/src/test/envs/file_context/ThesisTesting'
        context_file = f"{self.src_root_dir}/src/test/envs/file_context/create_context.sh"

        subprocess.run(['rm', '-rf', dir_name], check=True)
        subprocess.run(["bash", context_file, dir_name], check=True)


class ResetGitContext(ResetContext):
    def __init__(self, src_root_dir):
        super().__init__()
        self.src_root_dir = src_root_dir

    def reset_context(self):
        context_file = f"{self.src_root_dir}/src/test/envs/git/ThesisTesting"
        ghub = GitHubUtils(local_repo=context_file,
                           owner='',
                           token=os.environ["GITHUB_PAT"],
                           repo="ThesisTesting")
        ghub.reset_git_history()
        ghub.close_all_issues()

        prs = [PullRequest(title='Feature 1 done', body='PR for feature 1', head='feature_branch_1', base='main'),
               PullRequest(title='Feature 2 done', body='PR for feature 2', head='feature_branch_2', base='main'),
               PullRequest(title='Feature 3 done', body='PR for feature 3', head='feature_branch_3', base='main'),
               PullRequest(title='Feature 4 done', body='Dummy test feature 4', head='feature_branch_4', base='main'),
               PullRequest(title='Feature 5 done', body='Dummy test feature 5', head='feature_branch_5', base='main')]
        issues = [
            Issue(title='Java 11', body='Java 7 is very old version can you migrate the project to newer version'),
            Issue(title='Update dependencies', body='Update the dependencies to latest versions')]

        for issue in issues:
            ghub.create_issue(issue.title, issue.body)

        for pr in prs:
            ghub.create_pull_request(pr.title, pr.body, pr.head, pr.base)


if __name__ == '__main__':
    ResetGitContext(src_root_dir='/').reset_context()
