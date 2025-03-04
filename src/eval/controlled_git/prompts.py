pull_requests = [
    """
    Feature image optimization #12
    This pull request includes multiple changes across various files to enhance functionality, fix bugs, and improve documentation and styling. The most important changes are grouped by theme below.
    
    Functionality Enhancements:
    src/modules/new_module.py: Added a new module function new_module() that returns "New Module".
    src/services/api_integration.py: Added a new function api_integration() that returns "API Integrated".
    Bug Fixes:
    src/services/service.py: Fixed a bug in the service_function().
    tests/test_main.py: Fixed test errors in the TestMain class.
    Documentation and Style Improvements:
    docs/api.md: Added a new documentation section.
    assets/styles/style.css: Updated the body background color to #f0f0f0.
    These changes improve the overall functionality, fix existing issues, and enhance the documentation and user interface styling.
    """,
    """
    Feature api integration #11
    
    This pull request includes several changes to improve the user interface and integrate an API. The most important changes are grouped into UI enhancements and API integration.
    
    UI enhancements:
    
    assets/styles/style.css: Added a background color to the body element to improve the visual appearance.
    src/ui.html: Added an <h1> element with the text "Enhanced UI" for better user interface presentation.
    API integration:
    
    src/services/api_integration.py: Added a new function api_integration that returns the string "API Integrated" to facilitate API integration.""",
    """
    This pull request includes several changes to improve the user interface and integrate an API. The most important changes are grouped into UI enhancements and API integration.
    UI enhancements:
    assets/styles/style.css: Added a background color to the body element to improve the visual appearance.
    src/ui.html: Added an <h1> element with the text "Enhanced UI" for better user interface presentation.
    API integration:
    src/services/api_integration.py: Added a new function api_integration that returns the string "API Integrated" to facilitate API integration.    
    """,
    """Fix service bug #10
    
    This pull request includes several changes across different files to add new functionality, fix bugs, and enhance the user interface. The most important changes are grouped by theme below:
    New Functionality:
    src/modules/new_module.py: Added a new module function new_module that returns "New Module".
    src/services/api_integration.py: Added a new function api_integration that returns "API Integrated".
    Bug Fixes:
    src/services/service.py: Fixed a bug in the service_function.
    UI Enhancements:
    assets/styles/style.css: Changed the background color of the body to #f0f0f0.
    src/ui.html: Added an <h1> tag with the text "Enhanced UI".""",
    """
    Feature database setup #9
    
    This pull request includes several changes across different parts of the codebase, including new features, bug fixes, and documentation updates. The most important changes are summarized below:
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
    """
    Feature database setup #9
    
    This pull request includes several changes across different parts of the codebase, including new features, bug fixes, and documentation updates. The most important changes are summarized below:
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
    """
    Changes in feature-enhanced-ui #8
    
    This pull request includes some small changes to enhance the user interface and improve the styling of the webpage.
    UI Enhancements:
    src/ui.html: Added a heading to enhance the user interface.
    Styling Improvements:
    assets/styles/style.css: Changed the background color of the body to a light grey.
    """,
    """Feature new module #7
    
    New features:
    src/modules/new_module.py: Added a new function new_module that returns "New Module".
    """,
    """
    Fix test errors #6

    Bug Fixes:
    src/services/service.py: Added a comment indicating a bug fix in the service_function.
    tests/test_main.py: Added a comment to fix test errors in the TestMain class.
    """,
    """
    Feature test coverage #5
    
    Testing:
    Added a new test function test_feature in tests/test_feature.py that asserts True.""",
    """
    Feature new docs #4

    The most important changes are summarized below:
    Documentation:
    docs/api.md: Added a new section to the API documentation.""",
    """
    Feature add logging #3 (closed unmerged)

    Added logging capabilities to the project.""",
]

branches = [
    "feature-add-logging",
    "feature-api-integration",
    "feature-database-setup",
    "feature-enhanced-ui",
    "feature-image-optimization",
    "feature-new-docs",
    "feature-new-module",
    "feature-test-coverage",
    "fix-service-bug",
    "fix-test-errors",
    "main"
]

issues = [
    """Documentation request #2
The library seems cool, but there is 0 documentation on how to actually use it. Is there a roadmap and if so where in it have you planned to release documentation.
Thanks!""",
    """Security breach found in dependencies. #1
I've foudn a security breach in the requirements.txt. The package MyTrendyAuthenticator is not compiant with latest JWT."""
]

repo_structure = """
.
├── assets
│   ├── images
│   │   └── sample_image.md
│   └── styles
│       └── style.css
├── docs
│   └── api.md
├── README.md
├── src
│   ├── main.py
│   ├── modules
│   │   └── module.py
│   ├── services
│   │   └── service.py
│   └── utils
│       └── helpers.py
└── tests
    └── test_main.py

"""
