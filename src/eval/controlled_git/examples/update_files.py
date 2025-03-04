from abc import ABC

from src.eval.controlled_git.tool_example import ToolExample


class UpdateFile(ToolExample, ABC):
    def __init__(self, prompt):
        super().__init__(prompt)
        self.init_branches = [b.name for b in self.ghub.list_branches()]

    def revert_state(self):
        self.ghub.reset_git_history()

    def get_new_branch(self):
        new_branches = [b for b in self.ghub.list_branches() if b.name not in self.init_branches]
        assert len(new_branches) == 1, f'Expected 1 new branch, got {len(new_branches)}'
        return new_branches[0].name

    @classmethod
    def get_tools_names(cls):
        return ['Update_File', 'Get_files_from_a_directory', 'Create_a_new_branch', 'Set_active_branch',
                'Overview_of_files_in_current_working_branch', 'Get_files_from_a_directory',
                'List_branches_in_this_repository', 'Overview_of_existing_files_in_Main_branch',
                'Overview_of_files_in_current_working_branch']


class UpdateFileExample1(UpdateFile):
    def __init__(self):
        super().__init__(
            "Update the README.md\n\n Put the new heading of the README to 'We enter 2025 with version 1.0'")

    def validate(self):
        new_content = 'We enter 2025 with version 1.0'
        fcontent = self.ghub.read_file_from_repo(self.get_new_branch(), 'README.md')
        assert new_content in fcontent, f'Expected {new_content} but got {fcontent}'


class UpdateFileExample2(UpdateFile):
    def __init__(self):
        super().__init__(
            "Please update the README.md file to include a new section titled 'Setup Instructions' with the following content:\nNEW <<<<\n## Setup Instructions\n\nTo set up the project, follow these steps:\n1. Clone the repository.\n2. Navigate to the project directory.\n3. Run `npm install` to install dependencies.\n4. Run `npm start` to start the application.\n\n>>>> NEW")

    def validate(self):
        new_content = '## Setup Instructions'
        fcontent = self.ghub.read_file_from_repo(self.get_new_branch(), 'README.md')
        assert new_content in fcontent, f'Expected {new_content} but got {fcontent}'


class UpdateFileExample3(UpdateFile):
    def __init__(self):
        super().__init__(
            "I need to update the project description in the README.md file. The current description is 'This project is a simple web app.' and I want to change it to 'This project is a complex web application with advanced features.' Can you help me with that?")

    def validate(self):
        new_content = 'This project is a complex web application with advanced features.'
        fcontent = self.ghub.read_file_from_repo(self.get_new_branch(), 'README.md')
        assert new_content in fcontent, f'Expected {new_content} but got {fcontent}'


class UpdateFileExample4(UpdateFile):
    def __init__(self):
        super().__init__(
            "Can you please update the main file to ```Python\nif __name__ == '__main__':\n    print('Hello world!')```")

    def validate(self):
        new_content = "if __name__ == '__main__':\n    print('Hello world!')"
        fcontent = self.ghub.read_file_from_repo(self.get_new_branch(), 'src/main.py')
        assert new_content in fcontent, f'Expected {new_content} but got {fcontent}'


class UpdateFileExample5(UpdateFile):
    def __init__(self):
        super().__init__("Add a function called read_file to my utils/helpers.py")

    def validate(self):
        new_content = "def read_file"
        fcontent = self.ghub.read_file_from_repo(self.get_new_branch(), 'src/utils/helpers.py')
        assert new_content in fcontent, f'Expected {new_content} but got {fcontent}'


class UpdateFileExample6(UpdateFile):
    def __init__(self):
        super().__init__("Prepend the services file with `from django.http import HttpResponse`")

    def validate(self):
        new_content = "from django.http import HttpResponse"
        fcontent = self.ghub.read_file_from_repo(self.get_new_branch(), 'src/services/serivce.py')
        assert new_content in fcontent, f'Expected {new_content} but got {fcontent}'


class UpdateFileExample7(UpdateFile):
    def __init__(self):
        super().__init__(
            "To my modules.py extend with a new function def load_module(module_name):\n    return f'Loading {module_name}...'")

    def validate(self):
        new_content = "def load_module(module_name)"
        fcontent = self.ghub.read_file_from_repo(self.get_new_branch(), 'src/modules/module.py')
        assert new_content in fcontent, f'Expected {new_content} but got {fcontent}'


class UpdateFileExample8(UpdateFile):
    def __init__(self):
        super().__init__("I want to add a new test to our test suite: def test_categories():\n    assert 'a' == 'b'")

    def validate(self):
        new_content = 'def test_categories'
        fcontent = self.ghub.read_file_from_repo(self.get_new_branch(), 'tests/test_main.py')
        assert new_content in fcontent, f'Expected {new_content} but got {fcontent}'


class UpdateFileExample9(UpdateFile):
    def __init__(self):
        super().__init__("I want to add a new test to our test suite: def test_categories():\n    assert 'a' == 'b'")

    def validate(self):
        new_content = 'def test_categories'
        fcontent = self.ghub.read_file_from_repo(self.get_new_branch(), 'tests/test_main.py')
        assert new_content in fcontent, f'Expected {new_content} but got {fcontent}'
