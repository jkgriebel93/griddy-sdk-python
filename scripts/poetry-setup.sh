#!/bin/bash

set -e

job_type=$1

sudo apt install -y pipx
pipx install poetry
poetry install --all-groups
eval $(poetry env activate)

if [ "$job_type" = "formatting" ]; then
    isort --check-only --diff "."
    black --check --diff .
elif [ "$job_type" = "tests" ]; then
    pytest -m unit --cov=src/griddy --cov-report=term --cov-report=xml
fi