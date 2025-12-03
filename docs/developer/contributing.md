# Contributing Guide

Thank you for your interest in contributing to the Griddy SDK! This guide will help you get started.

## Development Setup

### Prerequisites

- Python 3.13 or higher
- Git
- pip

### Clone and Install

```bash
# Clone the repository
git clone https://github.com/jkgriebel93/griddy-sdk-python.git
cd griddy-sdk-python

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev,docs]"

# Install pre-commit hooks
pre-commit install
```

### Install Playwright (for browser auth tests)

```bash
playwright install chromium
```

## Development Workflow

### 1. Create a Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

Edit the code following our coding standards (see below).

### 3. Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/griddy --cov-report=html

# Run specific tests
pytest tests/test_nfl/ -v

# Run only unit tests
pytest -m "not integration"
```

### 4. Check Code Quality

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Run linter
flake8 src/ tests/

# Type checking
mypy src/
```

### 5. Commit Changes

```bash
git add .
git commit -m "Add feature: description of changes"
```

### 6. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Coding Standards

### Code Style

We follow PEP 8 with these tools:

- **black** - Code formatting (line length: 88)
- **isort** - Import sorting (black profile)
- **flake8** - Linting

### Type Hints

All code must include type hints:

```python
def get_games(
    self,
    season: int,
    week: int | None = None,
    season_type: str = "REG",
) -> GamesResponse:
    """Get games for a season."""
    ...
```

### Docstrings

Use Google-style docstrings:

```python
def get_games(self, season: int, week: int | None = None) -> GamesResponse:
    """Get games for a specific season and optional week.

    Retrieves game data from the NFL API for the specified season.
    If week is provided, only games for that week are returned.

    Args:
        season: The NFL season year (e.g., 2024).
        week: Optional week number (1-18 for regular season).

    Returns:
        GamesResponse containing the list of games.

    Raises:
        NotFoundError: If no games are found.
        RateLimitError: If API rate limit is exceeded.

    Example:
        >>> nfl = GriddyNFL(nfl_auth=auth)
        >>> games = nfl.games.get_games(season=2024, week=1)
        >>> print(len(games.games))
        16
    """
    ...
```

### Testing

- Write tests for all new functionality
- Use pytest fixtures for shared setup
- Mock external API calls in unit tests
- Mark integration tests with `@pytest.mark.integration`

```python
import pytest
from unittest.mock import Mock, patch

class TestGames:
    """Tests for Games endpoint."""

    def test_get_games_returns_response(self, nfl_client):
        """Test that get_games returns a valid response."""
        games = nfl_client.games.get_games(season=2024, week=1)
        assert games is not None
        assert len(games.games) > 0

    @pytest.mark.integration
    def test_get_games_integration(self, real_nfl_client):
        """Integration test with real API."""
        games = real_nfl_client.games.get_games(season=2024, week=1)
        assert games is not None
```

## Project Structure

```
griddy-sdk-python/
├── src/griddy/           # Main package
│   ├── __init__.py       # Package exports
│   ├── core/             # Core module
│   │   ├── base_client.py
│   │   ├── exceptions.py
│   │   └── models.py
│   └── nfl/              # NFL module
│       ├── sdk.py        # GriddyNFL class
│       ├── endpoints/    # API endpoints
│       └── models/       # Data models
├── tests/                # Test suite
│   ├── conftest.py       # Shared fixtures
│   ├── test_core/
│   └── test_nfl/
├── docs/                 # Documentation
├── examples/             # Usage examples
└── pyproject.toml        # Project config
```

## Adding New Features

### Adding a New Endpoint

See [Adding Methods to NFL SDK](adding-methods.md) for detailed instructions.

### Adding a New Model

1. Create model in `src/griddy/nfl/models/`
2. Add type hints and docstrings
3. Export from `__init__.py`
4. Add tests

### Adding Documentation

1. Update relevant docs in `docs/`
2. Add docstrings to new code
3. Build and verify docs locally:

```bash
mkdocs serve
```

## Pull Request Guidelines

### Before Submitting

- [ ] All tests pass (`pytest`)
- [ ] Code is formatted (`black`, `isort`)
- [ ] Linting passes (`flake8`)
- [ ] Type hints are complete (`mypy`)
- [ ] Documentation is updated
- [ ] Commit messages are clear

### PR Description

Include:

- Summary of changes
- Motivation/context
- Testing performed
- Screenshots (if UI changes)

### Review Process

1. Automated checks must pass
2. At least one maintainer review required
3. Address feedback promptly
4. Squash commits if requested

## Getting Help

- **Questions**: Open a GitHub Discussion
- **Bugs**: Open a GitHub Issue
- **Security**: Email security@example.com

## Code of Conduct

Be respectful, inclusive, and constructive. We're all here to build something great together.
