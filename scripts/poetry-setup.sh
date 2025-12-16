sudo apt install -y pipx
pipx install poetry
poetry install --all-groups
eval $(poetry env activate)