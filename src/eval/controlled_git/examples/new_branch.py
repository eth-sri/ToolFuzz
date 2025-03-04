from abc import ABC

from src.eval.controlled_git.tool_example import ToolExample


class CreateNewBranchExample(ToolExample, ABC):
    def __init__(self, prompt):
        super().__init__(prompt)
        self.target = None

    def revert_state(self):
        if self.target is None:
            return

        self.ghub.delete_branch(self.target)

    def get_branches(self):
        return [b for b in self.ghub.list_branches()]

    @classmethod
    def get_tools_names(cls):
        return ['Create_a_new_branch', 'List_branches_in_this_repository', 'Set_active_branch']


class CreateNewBranchExample1(CreateNewBranchExample):
    def __init__(self):
        super().__init__("Create a new branch called 'feature/new-payment-gateway' in the repository.")

    def validate(self):
        branches = self.get_branches()
        branch_names = [b.name for b in branches]
        assert 'feature/new-payment-gateway' in branch_names, f'Expected "feature/new-payment-gateway" in {branch_names}'

        new_branch_commit_id = [b.commit.sha for b in branches if b.name == 'feature/new-payment-gateway'][0]
        main_branc_id = [b.commit.sha for b in branches if b.name == 'main'][0]
        assert new_branch_commit_id == main_branc_id, f'Expected new branch to be at the same commit as main branch'

        self.target = 'feature/new-payment-gateway'


class CreateNewBranchExample2(CreateNewBranchExample):
    def __init__(self):
        super().__init__("Create a new branch called 'feature-update' in the repository.")

    def validate(self):
        new_branch_name = 'feature-update'
        branches = self.get_branches()
        branch_names = [b.name for b in branches]
        assert new_branch_name in branch_names, f'Expected "{new_branch_name}" in {branch_names}'

        new_branch_commit_id = [b.commit.sha for b in branches if b.name == new_branch_name][0]
        main_branc_id = [b.commit.sha for b in branches if b.name == 'main'][0]
        assert new_branch_commit_id == main_branc_id, f'Expected new branch to be at the same commit as main branch'
        self.target = new_branch_name


class CreateNewBranchExample3(CreateNewBranchExample):
    def __init__(self):
        super().__init__(
            "Create a new branch names CI-coverage-integration, it has to be based on the test coverage branch.")

    def validate(self):
        new_branch_name = 'CI-coverage-integration'
        branches = self.get_branches()
        branch_names = [b.name for b in branches]
        assert new_branch_name in branch_names, f'Expected "{new_branch_name}" in {branch_names}'

        new_branch_commit_id = [b.commit.sha for b in branches if b.name == new_branch_name][0]
        test_coverage_branch_id = [b.commit.sha for b in branches if b.name == 'feature-test-coverage'][0]
        assert new_branch_commit_id == test_coverage_branch_id, f'Expected new branch to be at the same commit as test coverage branch'

        self.target = new_branch_name


class CreateNewBranchExample4(CreateNewBranchExample):
    def __init__(self):
        super().__init__("Create branch from the enhanced ui called new-ui-doc-update.")

    def validate(self):
        new_branch_name = 'new-ui-doc-update'
        branches = self.get_branches()
        branch_names = [b.name for b in branches]
        assert new_branch_name in branch_names, f'Expected "{new_branch_name}" in {branch_names}'

        new_branch_commit_id = [b.commit.sha for b in branches if b.name == new_branch_name][0]
        enhanced_ui_branch_id = [b.commit.sha for b in branches if b.name == 'feature-enhanced-ui'][0]
        assert new_branch_commit_id == enhanced_ui_branch_id, f'Expected new branch to be at the same commit as enhanced ui branch'

        self.target = new_branch_name


class CreateNewBranchExample5(CreateNewBranchExample):
    def __init__(self):
        super().__init__(
            "I need to create a new branch called 'api-integration-docs' in my GitHub repository. Base that branch on top of the api integration one.")

    def validate(self):
        new_branch_name = 'api-integration-docs'
        branches = self.get_branches()
        branch_names = [b.name for b in branches]
        assert new_branch_name in branch_names, f'Expected "{new_branch_name}" in {branch_names}'

        new_branch_commit_id = [b.commit.sha for b in branches if b.name == new_branch_name][0]
        api_integration_branch_id = [b.commit.sha for b in branches if b.name == 'feature-api-integration'][0]
        assert new_branch_commit_id == api_integration_branch_id, f'Expected new branch to be at the same commit as api integration branch'

        self.target = new_branch_name


class CreateNewBranchExample6(CreateNewBranchExample):
    def __init__(self):
        super().__init__("Please create a new branch named 'feature/new-ui' in the GitHub repository.")

    def validate(self):
        new_branch_name = 'feature/new-ui'
        branches = self.get_branches()
        branch_names = [b.name for b in branches]
        assert new_branch_name in branch_names, f'Expected "{new_branch_name}" in {branch_names}'

        new_branch_commit_id = [b.commit.sha for b in branches if b.name == new_branch_name][0]
        main_branch_id = [b.commit.sha for b in branches if b.name == 'main'][0]
        assert new_branch_commit_id == main_branch_id, f'Expected new branch to be at the same commit as main branch'

        self.target = new_branch_name


class CreateNewBranchExample7(CreateNewBranchExample):
    def __init__(self):
        super().__init__("I need to create a new branch called 'feature/add-login' in my GitHub repository.")

    def validate(self):
        new_branch_name = 'feature/add-login'
        branch_names = [b.name for b in self.get_branches()]
        assert new_branch_name in branch_names, f'Expected "{new_branch_name}" in {branch_names}'
        self.target = new_branch_name


class CreateNewBranchExample8(CreateNewBranchExample):
    def __init__(self):
        super().__init__(
            "We need new branch based on the loggin branch for the integrations - 'feature/logging-integration'")

    def validate(self):
        new_branch_name = 'feature/logging-integration'
        branches = self.get_branches()
        branch_names = [b.name for b in branches]
        assert new_branch_name in branch_names, f'Expected "{new_branch_name}" in {branch_names}'

        new_branch_commit_id = [b.commit.sha for b in branches if b.name == new_branch_name][0]
        logging_branch_commit_id = [b.commit.sha for b in branches if b.name == 'feature-add-logging'][0]
        assert new_branch_commit_id == logging_branch_commit_id, f'Expected new branch to be at the same commit as logging branch'

        self.target = new_branch_name


class CreateNewBranchExample9(CreateNewBranchExample):
    def __init__(self):
        super().__init__("Please create a new branch named 'feature-update' in the GitHub repository.")

    def validate(self):
        new_branch_name = 'feature-update'
        branch_names = [b.name for b in self.get_branches()]
        assert new_branch_name in branch_names, f'Expected "{new_branch_name}" in {branch_names}'
        self.target = new_branch_name


class CreateNewBranchExample10(CreateNewBranchExample):
    def __init__(self):
        super().__init__(
            "Please create a new feature branch named 'feature/add-login-functionality' in the repository.")

    def validate(self):
        new_branch_name = 'feature/add-login-functionality'
        branch_names = [b.name for b in self.get_branches()]
        assert new_branch_name in branch_names, f'Expected "{new_branch_name}" in {branch_names}'
        self.target = new_branch_name


def get_all_branch_examples():
    examples = []
    for ex in CreateNewBranchExample.__subclasses__():
        examples.append(ex())

    return examples
