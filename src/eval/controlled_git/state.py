from pydantic import BaseModel, Field


class Issue(BaseModel):
    title: str = Field(description="The title of the issue")
    body: str = Field(description="The description of the issue")


class PullRequest(BaseModel):
    title: str = Field(description="The title of the PR")
    body: str = Field(description="The description of the PR")
    head: str = Field(description="The feature branch name")
    base: str = Field(description="The branch in which we merge")


issues = [
    Issue(
        title="Documentation request",
        body="The library seems cool, but there is 0 documentation on how to actually use it. Is there a roadmap and if so where in it have you planned to release documentation. Thanks!"
    ),
    Issue(
        title="Security breach found in dependencies.",
        body="I've foudn a security breach in the requirements.txt. The package MyTrendyAuthenticator is not compiant with latest JWT."
    ),
    Issue(
        title="Feature request: Add support for Python 3.10",
        body="The project currently does not support Python 3.10. It would be great to have compatibility with the latest Python version."
    ),
    Issue(
        title="Bug: Unexpected crash on empty input",
        body="The application crashes when it receives an empty string as input. A proper error handling mechanism should be implemented."
    ),
    Issue(
        title="Enhancement: Improve performance of data processing",
        body="The data processing module is significantly slower when dealing with large datasets. Optimization is needed to enhance performance."
    ),
    Issue(
        title="Test suite missing for core functionalities",
        body="There are no unit tests for the core functionalities of the project. Adding a test suite would help in maintaining code quality."
    ),
    Issue(
        title="Inconsistent naming conventions",
        body="The codebase uses inconsistent naming conventions for variables and functions. It would be beneficial to standardize them."
    ),
    Issue(
        title="Feature request: Add logging support",
        body="Currently, there is no logging mechanism in place. Adding logging would help in debugging and monitoring the application."
    ),
    Issue(
        title="Bug: Memory leak in data analysis module",
        body="There seems to be a memory leak in the data analysis module when processing large files. This needs to be investigated and fixed."
    ),
    Issue(
        title="Accessibility improvements needed",
        body="The user interface does not fully comply with accessibility standards. Improvements are needed to support all users better."
    ),
    Issue(
        title="Dependency update: Outdated library version",
        body="The project is using an outdated version of the Requests library. Updating to the latest version is recommended."
    ),
    Issue(
        title="Suggestion: Add a contribution guide",
        body="It would be helpful to have a CONTRIBUTING.md to guide new contributors on how to get started with the project."
    )
]
pull_requests = [
    PullRequest(title="Feature image optimization",
                body="""This pull request includes multiple changes across various files to enhance functionality, fix bugs, and improve documentation and styling. The most important changes are grouped by theme below.

Functionality Enhancements:
src/modules/new_module.py: Added a new module function new_module() that returns "New Module".
src/services/api_integration.py: Added a new function api_integration() that returns "API Integrated".
Bug Fixes:
src/services/service.py: Fixed a bug in the service_function().
tests/test_main.py: Fixed test errors in the TestMain class.
Documentation and Style Improvements:
docs/api.md: Added a new documentation section.
assets/styles/style.css: Updated the body background color to #f0f0f0.
These changes improve the overall functionality, fix existing issues, and enhance the documentation and user interface styling.""",
                head='main',
                base='feature-image-optimization'),
    PullRequest(title="Feature api integration",
                body="""This pull request includes several changes to improve the user interface and integrate an API. The most important changes are grouped into UI enhancements and API integration.

UI enhancements:

assets/styles/style.css: Added a background color to the body element to improve the visual appearance.
src/ui.html: Added an <h1> element with the text "Enhanced UI" for better user interface presentation.
API integration:

src/services/api_integration.py: Added a new function api_integration that returns the string "API Integrated" to facilitate API integration.""",
                head='main',
                base='feature-api-integration'),
    PullRequest(title="Fix service bug",
                body="""This pull request includes several changes across different files to add new functionality, fix bugs, and enhance the user interface. The most important changes are grouped by theme below:

New Functionality:
src/modules/new_module.py: Added a new module function new_module that returns "New Module".
src/services/api_integration.py: Added a new function api_integration that returns "API Integrated".
Bug Fixes:
src/services/service.py: Fixed a bug in the service_function.
UI Enhancements:
assets/styles/style.css: Changed the background color of the body to #f0f0f0.
src/ui.html: Added an <h1> tag with the text "Enhanced UI".""",
                head='main',
                base='fix-service-bug'),
    PullRequest(title="Feature database setup",
                body="""This pull request includes several changes across different parts of the codebase, including new features, bug fixes, and documentation updates. The most important changes are summarized below:
New Features:
src/modules/new_module.py: Added a new module function new_module that returns "New Module".
src/services/api_integration.py: Added a new function api_integration that returns "API Integrated".
src/services/database.py: Added a new configuration dictionary DATABASE_CONFIG with the host set to "localhost".
Bug Fixes:
src/services/service.py: Fixed a bug in the service_function.
Documentation Updates:
docs/api.md: Added a new section to the API documentation.
UI Enhancements:
src/ui.html: Added a new header <h1>Enhanced UI</h1>.
Style Updates:
assets/styles/style.css: Updated the body background color to #f0f0f0.
Testing:
tests/test_feature.py: Added a new test function test_feature that asserts True.""",
                head='main',
                base='feature-database-setup'),
    PullRequest(title="Changes in feature-enhanced-ui",
                body="""
                This pull request includes some small changes to enhance the user interface and improve the styling of the webpage.

UI Enhancements:

src/ui.html: Added a heading to enhance the user interface.
Styling Improvements:

assets/styles/style.css: Changed the background color of the body to a light grey.""",
                head="main",
                base="feature-enhanced-ui"),
    PullRequest(title="Feature new module",
                body="""New features:

src/modules/new_module.py: Added a new function new_module that returns "New Module".""",
                head='main',
                base='feature-new-module'),
    PullRequest(title="Fix test errors",
                body="""Bug Fixes:
src/services/service.py: Added a comment indicating a bug fix in the service_function.
tests/test_main.py: Added a comment to fix test errors in the TestMain class.""",
                head='main',
                base='fix-test-errors'),
    PullRequest(title="Feature test coverage",
                body="""Testing:
Added a new test function test_feature in tests/test_feature.py that asserts True.""",
                head='main',
                base='feature-test-coverage'),
    PullRequest(title="Feature new docs",
                body="""The most important changes are summarized below:

Documentation:
docs/api.md: Added a new section to the API documentation.""",
                head='main',
                base='feature-new-docs'),
    PullRequest(title="Feature add logging",
                body='Added logging capabilities to the project.',
                head='main',
                base='feature-add-logging'),
]
