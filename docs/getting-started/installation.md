# Installation

This guide covers installing the Griddy SDK for different use cases.

## Requirements

- **Python 3.13** or higher
- **pip** package manager

## Standard Installation

Install the latest stable version from PyPI:

```bash
pip install griddy
```

## Development Installation

For contributing to the SDK or running from source:

```bash
# Clone the repository
git clone https://github.com/jkgriebel93/griddy-sdk-python.git
cd griddy-sdk-python

# Install with development dependencies
pip install -e ".[dev]"
```

## Documentation Dependencies

If you want to build the documentation locally:

```bash
pip install -e ".[docs]"
```

## Verify Installation

After installation, verify it works:

```python
import griddy
print(griddy.__version__)
```

You should see the version number printed (e.g., `0.7.0`).

## Dependencies

The SDK installs the following dependencies automatically:

| Package | Purpose |
|---------|---------|
| `requests` | HTTP client for core module |
| `httpx` | Modern async HTTP client for NFL module |
| `pydantic` | Data validation and parsing |
| `python-dateutil` | Date/time utilities |
| `pyyaml` | YAML configuration parsing |

## Optional Dependencies

### Browser Authentication

Install with `pip install griddy[browser-auth]`:

- `playwright` - Browser automation for NFL authentication and PFR page fetching

Most users do not need this extra. It is only required if you use browser-based NFL authentication (`login_email`/`login_password`) or the `GriddyPFR` client.

### Development Tools

Install with `pip install griddy[dev]`:

- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting
- `pytest-asyncio` - Async test support
- `black` - Code formatting
- `isort` - Import sorting
- `flake8` - Linting
- `mypy` - Type checking

### Documentation Tools

Install with `pip install griddy[docs]`:

- `mkdocs` - Documentation generator
- `mkdocs-material` - Material theme
- `mkdocstrings` - Auto-generate API docs from docstrings

## Troubleshooting

### Python Version Error

If you see an error about Python version:

```
ERROR: Package 'griddy' requires a different Python: X.X.X not in '>=3.13'
```

Upgrade your Python installation to 3.13 or higher.

### Playwright Installation

Playwright is an optional dependency used for browser-based NFL authentication and PFR page fetching. If you see an `ImportError` mentioning `browser-auth`:

```bash
# Install the browser-auth extra
pip install griddy[browser-auth]

# Then install Playwright browsers
playwright install chromium
```

### Import Errors

If you get import errors after installation:

1. Ensure you're using the correct Python environment
2. Try reinstalling: `pip install --force-reinstall griddy`
3. Check for conflicting packages: `pip check`

## Next Steps

- [Quick Start Guide](quickstart.md) - Get started with basic usage
- [Authentication](authentication.md) - Set up NFL authentication
