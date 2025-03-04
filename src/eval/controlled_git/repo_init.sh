#!/bin/bash

# Set the root directory for the repository
root_dir=$1

# Ensure the root directory is specified
if [ -z "$root_dir" ]; then
    echo "Please set the root_dir variable to a valid path."
    exit 1
fi

# Create the root directory if it doesn't exist
mkdir -p "$root_dir"
cd "$root_dir" || exit

# Create a large initial file structure
mkdir -p \
    src/utils \
    src/modules \
    src/services \
    tests \
    docs \
    assets/images \
    assets/styles \
    configs \
    scripts

# Populate the initial file structure
echo "# Main README" > README.md
echo "print('Hello from main')" > src/main.py
echo "def util_function():\n    return 'Utility Function'" > src/utils/helpers.py
echo "def module_function():\n    return 'Module Function'" > src/modules/module.py
echo "def service_function():\n    return 'Service Function'" > src/services/service.py
echo "import unittest\n\nclass TestMain(unittest.TestCase):\n    pass" > tests/test_main.py
echo "API Documentation" > docs/api.md
echo "![Sample Image](image.png)" > assets/images/sample_image.md
echo "body { font-family: Arial; }" > assets/styles/style.css
echo "# Configuration file" > configs/app_config.yaml
echo "#!/bin/bash\necho 'Hello from script'" > scripts/setup.sh

# Initialize the Git repository
git init
git checkout -b main
git add .
git commit -m "Initial commit: Add full file structure and base files"

# Function to create branches, make changes, and commit them
create_branch_with_commits() {
    branch_name=$1
    shift
    file_edits=("$@")

    # Create and switch to the new branch
    git checkout -b "$branch_name"

    # Make edits as specified in file_edits
    for edit in "${file_edits[@]}"; do
        eval "$edit"
    done

    # Commit the changes
    git add .
    git commit -m "Changes in $branch_name"
}

# Create multiple branches with specific changes
create_branch_with_commits "feature-enhanced-ui" \
    "echo 'body { background-color: #f0f0f0; }' >> assets/styles/style.css" \
    "echo '<h1>Enhanced UI</h1>' > src/ui.html"

create_branch_with_commits "feature-api-integration" \
    "echo 'def api_integration():\n    return \"API Integrated\"' > src/services/api_integration.py"

create_branch_with_commits "feature-new-module" \
    "echo 'def new_module():\n    return \"New Module\"' > src/modules/new_module.py"

create_branch_with_commits "fix-service-bug" \
    "echo '# Fixed bug in service' >> src/services/service.py"

create_branch_with_commits "feature-test-coverage" \
    "echo 'def test_feature():\n    assert True' > tests/test_feature.py"

create_branch_with_commits "feature-new-docs" \
    "echo '## New Documentation Section' >> docs/api.md"

create_branch_with_commits "feature-database-setup" \
    "echo 'DATABASE_CONFIG = {\"host\": \"localhost\"}' > src/services/database.py"

create_branch_with_commits "fix-test-errors" \
    "echo '# Fix test errors\n' >> tests/test_main.py"

create_branch_with_commits "feature-image-optimization" \
    "echo '# Optimized image asset' >> assets/images/sample_image.md"

create_branch_with_commits "feature-add-logging" \
    "echo 'def log_action(action):\n    print(f\"Action: {action}\")' > src/utils/logger.py"

# Additional complex branches for extended testing
create_branch_with_commits "feature-security-updates" \
    "echo 'def validate_input(data):\n    if not isinstance(data, str): raise ValueError' > src/utils/security.py"

create_branch_with_commits "feature-cli-tool" \
    "echo '# CLI entry point\ndef cli_main():\n    print(\"CLI Tool\")' > src/cli_tool.py" \
    "chmod +x src/cli_tool.py"

create_branch_with_commits "refactor-codebase" \
    "sed -i 's/Utility Function/Updated Utility Function/' src/utils/helpers.py" \
    "sed -i 's/Module Function/Updated Module Function/' src/modules/module.py"

create_branch_with_commits "feature-deployment-script" \
    "echo '#!/bin/bash\necho \"Deploying application...\"' > scripts/deploy.sh" \
    "chmod +x scripts/deploy.sh"

create_branch_with_commits "feature-config-updates" \
    "echo 'app_name: DemoApp\nversion: 1.0.0' >> configs/app_config.yaml"

create_branch_with_commits "feature-new-assets" \
    "echo '![New Image](new_image.png)' > assets/images/new_image.md"

create_branch_with_commits "feature-new-tests" \
    "echo 'def test_new_feature():\n    assert True' > tests/test_new_feature.py"