from abc import ABC

from src.eval.controlled_git.tool_example import ToolExample


class DeleteFile(ToolExample, ABC):
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
        return ['Delete_File', 'Get_files_from_a_directory', 'Create_a_new_branch', 'Set_active_branch',
                'List_branches_in_this_repository', 'Overview_of_existing_files_in_Main_branch',
                'Overview_of_files_in_current_working_branch']


class DeleteFileExample1(DeleteFile):
    def __init__(self):
        super().__init__("I need to delete a file from my GitHub repository. Can you please delete the helpers.py file")

    def validate(self):
        file_to_delete = 'src/utils/helpers.py'
        files = self.ghub.get_files(self.get_new_branch())
        print(files)
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'


class DeleteFileExample2(DeleteFile):
    def __init__(self):
        super().__init__("Please delete the readme file.")

    def validate(self):
        file_to_delete = 'README.md'
        files = self.ghub.get_files(self.get_new_branch())
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'


class DeleteFileExample3(DeleteFile):
    def __init__(self):
        super().__init__("Please delete the .md file in the root directory.")

    def validate(self):
        file_to_delete = 'README.md'
        files = self.ghub.get_files(self.get_new_branch())
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'


class DeleteFileExample4(DeleteFile):
    def __init__(self):
        super().__init__(
            "Remove all the docs we have at the moment from the repository as they are incorrect as of now.")

    def validate(self):
        file_to_delete = 'docs/api.md'
        files = self.ghub.get_files(self.get_new_branch())
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'


class DeleteFileExample5(DeleteFile):
    def __init__(self):
        super().__init__("Remove all the tests we have as we are moving them to separate project with new repository.")

    def validate(self):
        file_to_delete = 'tests/test_main.py'
        files = self.ghub.get_files(self.get_new_branch())
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'


class DeleteFileExample6(DeleteFile):
    def __init__(self):
        super().__init__("Please remove the sample_image file")

    def validate(self):
        file_to_delete = 'assets/images/sample_image.md'
        files = self.ghub.get_files(self.get_new_branch())
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'


class DeleteFileExample7(DeleteFile):
    def __init__(self):
        super().__init__("We no longer need the css styles, remove the ones we have.")

    def validate(self):
        file_to_delete = 'assets/styles.css'
        files = self.ghub.get_files(self.get_new_branch())
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'


class DeleteFileExample8(DeleteFile):
    def __init__(self):
        super().__init__(
            "The modules script is no longer need as in python 3.10 we found a better way of loading them.")

    def validate(self):
        file_to_delete = 'src/modules/module.py'
        files = self.ghub.get_files(self.get_new_branch())
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'


class DeleteFileExample9(DeleteFile):
    def __init__(self):
        super().__init__("We've moved the servies logic to the modules script, please remove the service.py file.")

    def validate(self):
        file_to_delete = 'src/services/service.py'
        files = self.ghub.get_files(self.get_new_branch())
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'


class DeleteFileExample9(DeleteFile):
    def __init__(self):
        super().__init__("Now we start the app in the django way so no more need of the main script please remove it.")

    def validate(self):
        file_to_delete = 'src/main.py'
        files = self.ghub.get_files(self.get_new_branch())
        assert file_to_delete not in files, f'File "{file_to_delete}" still exists in {files}.'
