#!/bin/bash

PR_VERSION=$(grep -E '^version = ' pyproject.toml | head -1 | cut -d'"' -f2)

git fetch origin master
MASTER_VERSION=$(git show origin/master:pyproject.toml | grep -E '^version = ' | head -1 | cut -d'"' -f2)

echo -e "Master version: $MASTER_VERSION"
echo -e "PR version: $PR_VERSION"

if [ "$PR_VERSION" = "$MASTER_VERSION" ]; then
    echo -e "Error: You must increase the SDK version before merging to master!"
    exit -1
fi

echo -e "This pull request has modified the SDK version, the check passes."
