from abc import ABC

from src.eval.controlled_git.tool_example import ToolExample


class CreateFile(ToolExample, ABC):
    def __init__(self, prompt):
        super().__init__(prompt)
        self.init_branches = [b.name for b in self.ghub.list_branches()]

    def revert_state(self):
        self.ghub.reset_git_history()

    @classmethod
    def get_tools_names(cls):
        return ['Create_File', 'Overview_of_existing_files_in_Main_branch', 'Create_a_new_branch',
                'Set_active_branch', 'Overview_of_files_in_current_working_branch', 'Get_files_from_a_directory']


class CreateFileExample1(CreateFile):
    def __init__(self):
        super().__init__(
            "Please create a new file called docs/README.md with the following contents:\n\n# Project Title\n\nThis is the initial documentation for the project.")

    def validate(self):
        new_branches = [b for b in self.ghub.list_branches() if b.name not in self.init_branches]
        assert len(new_branches) == 1, f'Expected 1 new branch, got {len(new_branches)}'
        files = self.ghub.get_files(branch=new_branches[0].name)
        assert 'docs/README.md' in files, f'"docs/README.md" not in {files}'


class CreateFileExample2(CreateFile):
    def __init__(self):
        super().__init__(
            "Please create a file called docs/new_feature.md with the following contents: 'This document describes the new feature introduced in version 2.0. It includes setup instructions, usage examples, and troubleshooting tips.'")

    def validate(self):
        find_file = 'docs/new_feature.md'
        new_branches = [b for b in self.ghub.list_branches() if b.name not in self.init_branches]
        assert len(new_branches) == 1, f'Expected 1 new branch, got {len(new_branches)}'
        files = self.ghub.get_files(branch=new_branches[0].name)
        assert find_file in files, f'"{find_file}" not in {files}'


class CreateFileExample3(CreateFile):
    def __init__(self):
        super().__init__(
            "Create a config folder and add settings.json in it: \n{\n  \"setting1\": \"value1\",\n  \"setting2\": \"value2\",\n  \"setting3\": \"value3\"\n}")

    def validate(self):
        find_file = 'config/settings.json'

        new_branches = [b for b in self.ghub.list_branches() if b.name not in self.init_branches]
        assert len(new_branches) == 1, f'Expected 1 new branch, got {len(new_branches)}'
        files = self.ghub.get_files(branch=new_branches[0].name)

        assert find_file in files, f'"{find_file}" not in {files}'


class CreateFileExample4(CreateFile):
    def __init__(self):
        super().__init__(
            "Please create a new file named config/settings.json with the following contents: '{\"setting1\": \"value1\", \"setting2\": \"value2\"}'.'")

    def validate(self):
        find_file = 'config/settings.json'

        new_branches = [b for b in self.ghub.list_branches() if b.name not in self.init_branches]
        assert len(new_branches) == 1, f'Expected 1 new branch, got {len(new_branches)}'
        files = self.ghub.get_files(branch=new_branches[0].name)

        assert find_file in files, f'"{find_file}" not in {files}'


class CreateFileExample5(CreateFile):
    def __init__(self):
        super().__init__(
            "Please create a file called 'docs/README.md' with the contents 'This is the README file for the project.'")

    def validate(self):
        find_file = 'docs/README.md'

        new_branches = [b for b in self.ghub.list_branches() if b.name not in self.init_branches]
        assert len(new_branches) == 1, f'Expected 1 new branch, got {len(new_branches)}'
        files = self.ghub.get_files(branch=new_branches[0].name)

        assert find_file in files, f'"{find_file}" not in {files}'


class CreateFileExample6(CreateFile):
    def __init__(self):
        super().__init__(
            "I need to create a new file in my GitHub repository to keep track of the project's changelog. The file should be named docs/changelog.md and should contain the initial heading 'Changelog'.")

    def validate(self):
        find_file = 'docs/changelog.md'

        new_branches = [b for b in self.ghub.list_branches() if b.name not in self.init_branches]
        assert len(new_branches) == 1, f'Expected 1 new branch, got {len(new_branches)}'

        files = self.ghub.get_files(branch=new_branches[0].name)
        assert find_file in files, f'"{find_file}" not in {files}'
