from abc import abstractmethod

from src.eval.toolfuzz.utils.git_utils import GitHubUtils


class ToolExample:

    def __init__(self, prompt):
        self.ghub = GitHubUtils(local_repo='./ThesisTestForGitApp')
        self.prompt = prompt

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def revert_state(self):
        pass

    def can_handle(self, prompt):
        return self.prompt.lower().strip() == prompt.lower().strip()
