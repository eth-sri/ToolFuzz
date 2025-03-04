#!/bin/bash

# Define variables
PROJECT_NAME=$1
BRANCH_PREFIX="feature"
NUM_BRANCHES=5

# Check if project directory exists
if [ ! -d "$PROJECT_NAME" ]; then
    echo "Error: Project directory '$PROJECT_NAME' does not exist. Run the first script to create the base project."
    exit 1
fi

# Navigate to project directory
cd $PROJECT_NAME

# Initialize Git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: Base Java Servlet project"
else
    echo "Git repository already initialized."
fi

# Create branches and add dummy commits
for i in $(seq 1 $NUM_BRANCHES); do
    BRANCH_NAME="${BRANCH_PREFIX}_branch_${i}"
    echo "Creating branch: $BRANCH_NAME"
    git checkout -b $BRANCH_NAME

    # Create a dummy file and commit it
    DUMMY_FILE="dummy_file_${i}.txt"
    echo "This is dummy content for branch $BRANCH_NAME" > $DUMMY_FILE
    git add $DUMMY_FILE
    git commit -m "Add $DUMMY_FILE for $BRANCH_NAME"
done

# Switch back to main branch
git checkout main

echo "Branches and dummy commits created successfully."
echo "Available branches:"
git branch
