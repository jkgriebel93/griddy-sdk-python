#!/bin/bash

git fetch origin master

# Check if any .py files were modified compared to master
PY_FILES_CHANGED=$(git diff --name-only origin/master...HEAD -- '*.py' | wc -l)

if [ "$PY_FILES_CHANGED" -eq 0 ]; then
    echo -e "No Python files were modified. Skipping version bump check."
    exit 0
fi

echo -e "Python files modified: $PY_FILES_CHANGED"

PR_VERSION=$(grep -E '^version = ' pyproject.toml | head -1 | cut -d'"' -f2)
MASTER_VERSION=$(git show origin/master:pyproject.toml | grep -E '^version = ' | head -1 | cut -d'"' -f2)

echo -e "Master version: $MASTER_VERSION"
echo -e "PR version: $PR_VERSION"

if [ "$PR_VERSION" = "$MASTER_VERSION" ]; then
    echo -e "Error: You must increase the SDK version before merging to master!"
    exit 1
fi

echo -e "This pull request has modified the SDK version, the check passes."
