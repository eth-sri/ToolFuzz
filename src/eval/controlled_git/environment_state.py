from src.eval.controlled_git.state import issues, pull_requests
from src.eval.toolfuzz.utils.git_utils import GitHubUtils


def reset_state(issues, pull_requests):
    # Call a hard git push --force so that the repo is in the state it is currently.
    github = GitHubUtils(local_repo='./ThesisTestForGitApp')
    github.reset_git_history()

    github.close_all_issues()

    for issue in issues:
        github.create_issue(issue.title, issue.body)

    for pr in pull_requests:
        github.create_pull_request(pr.title, pr.body, pr.base, pr.head)


if __name__ == '__main__':
    reset_state(issues, pull_requests)
