"""GitHub Toolkit."""
from typing import Dict, List

# from langchain_core import BaseModel, Field
from langchain_core.tools import BaseToolkit

from typing import Any, Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field

from langchain_community.utilities.github import GitHubAPIWrapper

from langchain_community.tools import BaseTool
from langchain_community.tools.github.prompt import (
    COMMENT_ON_ISSUE_PROMPT,
    CREATE_BRANCH_PROMPT,
    CREATE_FILE_PROMPT,
    CREATE_PULL_REQUEST_PROMPT,
    CREATE_REVIEW_REQUEST_PROMPT,
    DELETE_FILE_PROMPT,
    GET_FILES_FROM_DIRECTORY_PROMPT,
    GET_ISSUE_PROMPT,
    GET_ISSUES_PROMPT,
    GET_PR_PROMPT,
    LIST_BRANCHES_IN_REPO_PROMPT,
    LIST_PRS_PROMPT,
    LIST_PULL_REQUEST_FILES,
    OVERVIEW_EXISTING_FILES_BOT_BRANCH,
    OVERVIEW_EXISTING_FILES_IN_MAIN,
    READ_FILE_PROMPT,
    SEARCH_CODE_PROMPT,
    SEARCH_ISSUES_AND_PRS_PROMPT,
    SET_ACTIVE_BRANCH_PROMPT,
    UPDATE_FILE_PROMPT,
)
from pydantic import BaseModel, Field


class NoInput(BaseModel):
    """Schema for operations that do not require any input."""

    instructions: str = Field("", description="No input required, e.g. `` (empty string).")


class GetIssue(BaseModel):
    """Schema for operations that require an issue number as input."""

    instructions: int = Field(0, description="Issue number as an integer, e.g. `42`")


class CommentOnIssue(BaseModel):
    """Schema for operations that require a comment as input."""

    instructions: str = Field(..., description="Follow the required formatting.")
    # instructions: str = Field(..., description="Pass a string in the following format:  Parameters:comment_query(str): a string which contains the issue number, two newlines, and the comment.for example: '1\n\nWorking on it now' adds the comment 'working on it now' to issue 1")


class GetPR(BaseModel):
    """Schema for operations that require a PR number as input."""

    instructions: int = Field(0, description="The PR number as an integer, e.g. `12`")


class CreatePR(BaseModel):
    """Schema for operations that require a PR title and body as input."""

    instructions: str = Field(..., description="Follow the required formatting.")


class CreateFile(BaseModel):
    """Schema for operations that require a file path and content as input."""

    instructions: str = Field(..., description="Follow the required formatting.")


class ReadFile(BaseModel):
    """Schema for operations that require a file path as input."""

    instructions: str = Field(
        ...,
        description=(
            "The full file path of the file you would like to read where the "
            "path must NOT start with a slash, e.g. `some_dir/my_file.py`."
        ),
    )


class UpdateFile(BaseModel):
    """Schema for operations that require a file path and content as input."""

    instructions: str = Field(
        ..., description="Strictly follow the provided rules."
    )


class DeleteFile(BaseModel):
    """Schema for operations that require a file path as input."""

    instructions: str = Field(
        ...,
        description=(
            "The full file path of the file you would like to delete"
            " where the path must NOT start with a slash, e.g."
            " `some_dir/my_file.py`. Only input a string,"
            " not the param name."
        ),
    )


class DirectoryPath(BaseModel):
    """Schema for operations that require a directory path as input."""

    instructions: str = Field(
        "",
        description=(
            "The path of the directory, e.g. `some_dir/inner_dir`."
            " Only input a string, do not include the parameter name."
        ),
    )


class BranchName(BaseModel):
    """Schema for operations that require a branch name as input."""

    instructions: str = Field(
        ..., description="The name of the branch, e.g. `my_branch`."
    )


class SearchCode(BaseModel):
    """Schema for operations that require a search query as input."""

    instructions: str = Field(
        ...,
        description=(
            "A keyword-focused natural language search"
            "query for code, e.g. `MyFunctionName()`."
        ),
    )


class CreateReviewRequest(BaseModel):
    """Schema for operations that require a username as input."""

    instructions: str = Field(
        ...,
        description="GitHub username of the user being requested, e.g. `my_username`.",
    )


class SearchIssuesAndPRs(BaseModel):
    """Schema for operations that require a search query as input."""

    instructions: str = Field(
        ...,
        description="Natural language search query, e.g. `My issue title or topic`.",
    )



class GitHubActionPatched(BaseTool):  # type: ignore[override]
    """Tool for interacting with the GitHub API."""

    api_wrapper: GitHubAPIWrapper = Field(default_factory=GitHubAPIWrapper)  # type: ignore[arg-type]
    mode: str
    name: str = ""
    description: str = ""
    args_schema: Optional[Type[BaseModel]] = None

    def _run(
        self,
        instructions: Optional[str] = "",
        run_manager: Optional[CallbackManagerForToolRun] = None,
        **kwargs: Any,
    ) -> str:
        """Use the GitHub API to run an operation."""
        if not instructions or instructions == "{}":
            # Catch other forms of empty input that GPT-4 likes to send.
            instructions = ""
        if self.args_schema is not None:
            field_names = list(self.args_schema.schema()["properties"].keys())
            if len(field_names) > 1:
                raise AssertionError(
                    f"Expected one argument in tool schema, got {field_names}."
                )
            if field_names:
                field = field_names[0]
            else:
                field = ""
            query = str(kwargs.get(field, ""))
        else:
            query = instructions
        if query == "":
            query = instructions
        return self.api_wrapper.run(self.mode, query)



class GitHubToolkitPatched(BaseToolkit):
    """GitHub Toolkit.

    *Security Note*: This toolkit contains tools that can read and modify
        the state of a service; e.g., by creating, deleting, or updating,
        reading underlying data.

        For example, this toolkit can be used to create issues, pull requests,
        and comments on GitHub.

        See [Security](https://python.langchain.com/docs/security) for more information.
    """

    tools: List[BaseTool] = []

    @classmethod
    def from_github_api_wrapper(
        cls, github_api_wrapper: GitHubAPIWrapper
    ) -> "GitHubToolkit":
        operations: List[Dict] = [
            {
                "mode": "get_issues",
                "name": "Get Issues",
                "description": GET_ISSUES_PROMPT,
                "args_schema": NoInput,
            },
            {
                "mode": "get_issue",
                "name": "Get Issue",
                "description": GET_ISSUE_PROMPT,
                "args_schema": GetIssue,
            },
            {
                "mode": "comment_on_issue",
                "name": "Comment on Issue",
                "description": COMMENT_ON_ISSUE_PROMPT,
                "args_schema": CommentOnIssue,
            },
            {
                "mode": "list_open_pull_requests",
                "name": "List open pull requests (PRs)",
                "description": LIST_PRS_PROMPT,
                "args_schema": NoInput,
            },
            {
                "mode": "get_pull_request",
                "name": "Get Pull Request",
                "description": GET_PR_PROMPT,
                "args_schema": GetPR,
            },
            {
                "mode": "list_pull_request_files",
                "name": "Overview of files included in PR",
                "description": LIST_PULL_REQUEST_FILES,
                "args_schema": GetPR,
            },
            {
                "mode": "create_pull_request",
                "name": "Create Pull Request",
                "description": CREATE_PULL_REQUEST_PROMPT,
                "args_schema": CreatePR,
            },
            {
                "mode": "list_pull_request_files",
                "name": "List Pull Requests' Files",
                "description": LIST_PULL_REQUEST_FILES,
                "args_schema": GetPR,
            },
            {
                "mode": "create_file",
                "name": "Create File",
                "description": CREATE_FILE_PROMPT,
                "args_schema": CreateFile,
            },
            {
                "mode": "read_file",
                "name": "Read File",
                "description": READ_FILE_PROMPT,
                "args_schema": ReadFile,
            },
            {
                "mode": "update_file",
                "name": "Update File",
                "description": UPDATE_FILE_PROMPT,
                "args_schema": UpdateFile,
            },
            {
                "mode": "delete_file",
                "name": "Delete File",
                "description": DELETE_FILE_PROMPT,
                "args_schema": DeleteFile,
            },
            {
                "mode": "list_files_in_main_branch",
                "name": "Overview of existing files in Main branch",
                "description": OVERVIEW_EXISTING_FILES_IN_MAIN,
                "args_schema": NoInput,
            },
            {
                "mode": "list_files_in_bot_branch",
                "name": "Overview of files in current working branch",
                "description": OVERVIEW_EXISTING_FILES_BOT_BRANCH,
                "args_schema": NoInput,
            },
            {
                "mode": "list_branches_in_repo",
                "name": "List branches in this repository",
                "description": LIST_BRANCHES_IN_REPO_PROMPT,
                "args_schema": NoInput,
            },
            {
                "mode": "set_active_branch",
                "name": "Set active branch",
                "description": SET_ACTIVE_BRANCH_PROMPT,
                "args_schema": BranchName,
            },
            {
                "mode": "create_branch",
                "name": "Create a new branch",
                "description": CREATE_BRANCH_PROMPT,
                "args_schema": BranchName,
            },
            {
                "mode": "get_files_from_directory",
                "name": "Get files from a directory",
                "description": GET_FILES_FROM_DIRECTORY_PROMPT,
                "args_schema": DirectoryPath,
            },
            {
                "mode": "search_issues_and_prs",
                "name": "Search issues and pull requests",
                "description": SEARCH_ISSUES_AND_PRS_PROMPT,
                "args_schema": SearchIssuesAndPRs,
            },
            {
                "mode": "search_code",
                "name": "Search code",
                "description": SEARCH_CODE_PROMPT,
                "args_schema": SearchCode,
            },
            {
                "mode": "create_review_request",
                "name": "Create review request",
                "description": CREATE_REVIEW_REQUEST_PROMPT,
                "args_schema": CreateReviewRequest,
            },
        ]
        tools = [
            GitHubActionPatched(
                name=action["name"],
                description=action["description"],
                mode=action["mode"],
                api_wrapper=github_api_wrapper,
                args_schema=action.get("args_schema", None),
            )
            for action in operations
        ]
        return cls(tools=tools)

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return self.tools
