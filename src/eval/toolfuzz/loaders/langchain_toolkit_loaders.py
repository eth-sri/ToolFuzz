import os

from src.eval.toolfuzz.loaders.langchain_loader import ReactNewAgentLoader, ReactOldAgentLoader


class NasaToolkitLoader(ReactOldAgentLoader):
    def can_load(self, name: str) -> bool:
        return 'nasa' in name.lower() or name in [t.name for t in self.get_tool()]

    def get_tool(self):
        from langchain_community.agent_toolkits.nasa.toolkit import NasaToolkit
        from langchain_community.utilities.nasa import NasaAPIWrapper
        nasa = NasaAPIWrapper()
        toolkit = NasaToolkit.from_nasa_api_wrapper(nasa)
        return toolkit.get_tools()


class FileManagementToolkitLoader(ReactNewAgentLoader):
    def get_tool(self):
        from langchain_community.agent_toolkits import FileManagementToolkit

        toolkit = FileManagementToolkit(root_dir='/home/imilev/Workspace/agent-tool-testing/src/buggy_tools/resources')
        return toolkit.get_tools()

    def can_load(self, name: str) -> bool:
        return name.lower() == 'filemanagementtoolkit' or name in [t.name for t in self.get_tool()]


class RequestsAllToolkitLoader(ReactNewAgentLoader):
    def get_tool(self):
        from langchain_community.agent_toolkits.openapi.toolkit import RequestsToolkit
        from langchain_community.utilities import TextRequestsWrapper
        toolkit = RequestsToolkit(
            requests_wrapper=TextRequestsWrapper(headers={}),
            allow_dangerous_requests=True,
        )
        return toolkit.get_tools()

    def can_load(self, name: str) -> bool:
        return name.lower() == 'requests' or name.lower() == 'requests_all' or name in [t.name for t in self.get_tool()]


class PlayWrightBrowserToolkitLoader(ReactNewAgentLoader):
    def get_tool(self):
        from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
        from langchain_community.tools.playwright.utils import create_async_playwright_browser

        async_browser = create_async_playwright_browser()
        toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
        return toolkit.get_tools()

    def can_load(self, name: str) -> bool:
        return name.lower() == 'PlayWrightBrowser'.lower() or name in [t.name for t in self.get_tool()]


class GmailToolkitLoader(ReactNewAgentLoader):
    def __init__(self) -> None:
        super().__init__()
        # Patch for WSL on windows:
        import platform
        if 'WSL' in platform.uname().release:
            import webbrowser
            browser_path = "C:\\Users\\Ivan\\AppData\\Local\\Vivaldi\\Application\\vivaldi.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))

    def get_tool(self):
        from langchain_google_community.gmail.utils import (
            build_resource_service,
            get_gmail_credentials,
        )

        from langchain_google_community import GmailToolkit
        credentials = get_gmail_credentials(
            token_file="token.json",
            scopes=["https://mail.google.com/"],
            client_secrets_file="/home/imilev/Workspace/agent-tool-testing/src/test/loaders/client.json",
        )
        api_resource = build_resource_service(credentials=credentials)
        toolkit = GmailToolkit(api_resource=api_resource)
        # Filter out the send_gmail_message as it can be tricky.
        return [tool for tool in toolkit.get_tools() if tool.name != 'send_gmail_message']

    def can_load(self, name: str) -> bool:
        return name.lower() == 'gmail' or name in [t.name for t in self.get_tool()]


class GithubToolkitLoader(ReactNewAgentLoader):
    def __init__(self) -> None:
        super().__init__()
        os.environ["GITHUB_APP_ID"] = "934398"
        os.environ[
            "GITHUB_APP_PRIVATE_KEY"] = "/home/ivan/ETH/MasterThesis/code/Thesis/src/test/loaders/masterthesistesting.2024-11-14.private-key.pem"
        os.environ["GITHUB_REPOSITORY"] = "ivanmilevtues/ThesisTestForGitApp"
        os.environ["GITHUB_BRANCH"] = "test-branch"
        os.environ["GITHUB_BASE_BRANCH"] = "main"

    def get_tool(self):
        from langchain_community.agent_toolkits.github.toolkit import GitHubToolkit
        from langchain_community.utilities.github import GitHubAPIWrapper

        ghub = GitHubAPIWrapper()
        toolkit = GitHubToolkit.from_github_api_wrapper(ghub)
        toolkit_tools = toolkit.get_tools()
        for tool in toolkit_tools:
            tool.name = tool.name.replace(' ', '_')
            tool.name = tool.name.replace('(', '_')
            tool.name = tool.name.replace(')', '_')
            tool.name = tool.name.replace("'", '')

        return toolkit_tools

    def can_load(self, name: str) -> bool:
        return name.lower() == 'github' or name.lower() == 'githubtoolkit' or name.lower() == 'git' \
            or name in [t.name for t in self.get_tool()]
