from abc import ABC

from src.eval.controlled_git.tool_example import ToolExample


class CreatePullRequest(ToolExample, ABC):
    def __init__(self, prompt):
        super().__init__(prompt)
        self.target_pr = None
        self.PRs = self.ghub.list_prs()

    def revert_state(self):
        if self.target_pr:
            self.ghub.close_issue(self.target_pr.number)

    def get_last_pr(self):
        for pr in self.PRs:
            last_pr = pr
            if last_pr.state != 'closed':
                return last_pr
        return None

    @classmethod
    def get_tools_names(cls):
        return ['Create_Pull_Request', 'List_Pull_Requests_Files', 'List_branches_in_this_repository',
                'Search_issues_and_pull_requests', 'Set_active_branch']


class CreatePullRequest1(CreatePullRequest):
    def __init__(self):
        super().__init__("Can you create a PR for the refactor service branch to be merged in main." +
                         " The title should just be refacto service and for description write that now service is using 2x less memory")

    def validate(self):
        last_pr = self.get_last_pr()
        print(last_pr)
        head_ref, base_ref = 'refactor-service', 'main'

        # Now validate the last pr
        assert last_pr.head.ref == head_ref, f'Expected head ref to be {head_ref}, but it is {last_pr.head.ref}'
        assert last_pr.base.ref == base_ref, f'Expected base ref to be {base_ref}, but it is {last_pr.base.ref}'

        self.target_pr = last_pr


class CreatePullRequest3(CreatePullRequest):
    def __init__(self):
        super().__init__(
            "Please create PR's for all branches that don't have PRs open at the moment. Use the name of the branch as the tittle of the PR")

    def validate(self):
        last_pr = self.get_last_pr()
        head_ref, base_ref = 'refactor-service', 'main'

        # Now validate the last pr
        assert last_pr.head.ref == head_ref, f'Expected head ref to be {head_ref}, but it is {last_pr.head.ref}'
        assert last_pr.base.ref == base_ref, f'Expected base ref to be {base_ref}, but it is {last_pr.base.ref}'

        self.target_pr = last_pr


if __name__ == '__main__':
    CreatePullRequest1().validate()
