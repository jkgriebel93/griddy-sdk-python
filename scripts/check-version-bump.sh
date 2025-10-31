#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get the version from the PR branch
PR_VERSION=$(grep -E '^version = ' pyproject.toml | head -1 | cut -d'"' -f2)

# Get the version from master
git fetch origin master
MASTER_VERSION=$(git show origin/master:pyproject.toml | grep -E '^version = ' | head -1 | cut -d'"' -f2)

echo -e "${YELLOW}Master version:${NC} $MASTER_VERSION"
echo -e "${YELLOW}PR version:${NC} $PR_VERSION"

if [ "$PR_VERSION" = "$MASTER_VERSION" ]; then
  echo -e "${RED} Error: Version in pyproject.toml has not been updated!${NC}"
  echo -e "${RED}Current version: $MASTER_VERSION${NC}"
  echo -e "${RED}Please bump the version before merging to master.${NC}"
  exit 1
fi

echo -e "${GREEN} Version has been updated from $MASTER_VERSION to $PR_VERSION${NC}"