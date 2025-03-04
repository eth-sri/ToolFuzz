# Configuration
import subprocess


class GitHubUtils:
    def __init__(self, token, owner, repo, local_repo):
        from github import Github
        g = Github(token)
        self.repo = g.get_repo(f"{owner}/{repo}")
        self.local_repo = local_repo

    # Create an Issue
    def create_issue(self, title, body):
        issue = self.repo.create_issue(title=title, body=body)
        print(f"Issue created: {issue.html_url}")
        return issue.number

    # Create a Pull Request
    def create_pull_request(self, title, body, head, base):
        print(f"PR from {head} to {base}")
        pr = self.repo.create_pull(title=title, body=body, head=head, base=base)
        print(f"Pull request created: {pr.html_url}")
        return pr.number

    # Close an Issue
    def close_issue(self, issue_number):
        issue = self.repo.get_issue(number=issue_number)
        issue.edit(state="closed")
        print(f"Issue #{issue_number} closed.")

    # Delete a Branch
    def delete_branch(self, branch_name):
        ref = self.repo.get_git_ref(f"heads/{branch_name}")
        ref.delete()
        print(f"Branch '{branch_name}' deleted.")

    def close_all_issues(self):
        open_issues = self.repo.get_issues(state="open")  # Get all open issues
        for issue in open_issues:
            issue.edit(state="closed")
            print(f"Issue #{issue.number} closed: {issue.title}")

    def reset_git_history(self):
        try:
            result = subprocess.run(
                ["git", "-C", self.local_repo, "fetch", "origin", "--prune"],
                check=True,
                text=True,
                capture_output=True)
            print("Git fetch origin result stdout:", result.stdout, " stderr: ", result.stderr)

            command = """for branch in $(git -C %s branch -r | grep -v '\\->' | grep -v "$(git -C %s rev-parse --abbrev-ref HEAD)"); do
    git -C %s push origin --delete "${branch#origin/}"
done""" % (self.local_repo, self.local_repo, self.local_repo)

            result = subprocess.run(command, shell=True, check=True, capture_output=True)
            print("Success stdout:", result.stdout, "stderr:", result.stderr)

            result = subprocess.run(
                ["git", "-C", self.local_repo, "fetch", "origin", "--prune"],
                check=True,
                text=True,
                capture_output=True)
            print("Git fetch origin result stdout:", result.stdout, " stderr: ", result.stderr)

            # Run the git push command
            result = subprocess.run(
                ["git", "-C", self.local_repo, "push", "--all", "--force"],
                check=True,  # Raise an exception if the command fails
                text=True,  # Capture output as text
                capture_output=True  # Capture stdout and stderr
            )
            print("Success stdout:", result.stdout, "stderr:", result.stderr)
        except subprocess.CalledProcessError as e:
            print("Error:", e.stderr)

    def list_branches(self):
        return self.repo.get_branches()

    def list_issues(self):
        return self.repo.get_issues(state="all")

    def list_prs(self):
        return self.repo.get_pulls(state="all")

    def list_comments(self, issue_number):
        issue = self.repo.get_issue(number=issue_number)
        comments = issue.get_comments()
        return comments

    def delete_branch(self, branch_name):
        ref = self.repo.get_git_ref(f"heads/{branch_name}")
        ref.delete()

    def get_files(self, branch):
        files = []
        contents = self.repo.get_contents("", ref=branch)
        for content_file in contents:
            # If the content is a directory, fetch its contents for the branch
            if content_file.type == "dir":
                sub_contents = self.repo.get_contents(content_file.path, ref=branch)
                for sub_file in sub_contents:
                    files.append(f'{sub_file.path}')
        return files

    def read_file_from_repo(self, branch_name, file_path):
        try:
            # Get the file content
            contents = self.repo.get_contents(file_path, ref=branch_name)

            # Decode the content (if encoded) and return it
            file_content = contents.decoded_content.decode("utf-8")
            print(f"File '{file_path}' content from branch '{branch_name}':\n")
            return file_content
        except Exception as e:
            print(f"Error reading file: {e}")
            return None
