# API Reference

This section provides detailed API documentation for the Griddy SDK, auto-generated from source code docstrings.

## Module Overview

The Griddy SDK is organized into the following modules:

### Core Module

The [`griddy.core`](core.md) module provides shared functionality:

- **BaseClient** - HTTP client with rate limiting and error handling
- **Exceptions** - Custom exception classes for error handling
- **Models** - Base Pydantic models and utilities

### NFL Module

The [`griddy.nfl`](nfl.md) module provides NFL-specific functionality:

- **GriddyNFL** - Main client class for accessing NFL data
- **Endpoints** - Sub-SDKs for different API endpoints
- **Models** - NFL-specific data models

### Exceptions

The [`griddy.core.exceptions`](exceptions.md) module contains all exception classes:

- **GriddyError** - Base exception class
- **APIError** - General API errors
- **RateLimitError** - Rate limit exceeded
- **NotFoundError** - Resource not found
- **AuthenticationError** - Authentication failures
- **ValidationError** - Request validation errors

## Quick Links

| Module | Description | Link |
|--------|-------------|------|
| `griddy` | Package root | [Documentation](core.md#griddy) |
| `griddy.core` | Core utilities | [Documentation](core.md) |
| `griddy.nfl` | NFL SDK | [Documentation](nfl.md) |
| Exceptions | Error classes | [Documentation](exceptions.md) |

## Using the API Reference

### Navigating Documentation

Each module page includes:

- **Module overview** - High-level description
- **Classes** - Detailed class documentation
- **Methods** - Method signatures and descriptions
- **Attributes** - Class and instance attributes
- **Examples** - Usage examples

### Type Annotations

The SDK uses Python type hints throughout. In the documentation:

- `Optional[X]` means the value can be `X` or `None`
- `List[X]` means a list containing items of type `X`
- `Dict[K, V]` means a dictionary with keys of type `K` and values of type `V`
- `Union[X, Y]` means the value can be either `X` or `Y`

### Pydantic Models

Data models are built with Pydantic and include:

- Automatic validation
- JSON serialization/deserialization
- Type coercion
- Default values

## Code Examples

### Basic Usage

```python
from griddy.nfl import GriddyNFL

# Initialize client
nfl = GriddyNFL(nfl_auth={"accessToken": "your_token"})

# Access endpoints
games = nfl.games.get_games(season=2024, week=1)
```

### Error Handling

```python
from griddy import GriddyError, RateLimitError

try:
    games = nfl.games.get_games(season=2024)
except RateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after}")
except GriddyError as e:
    print(f"Error: {e.message}")
```

### Async Usage

```python
import asyncio
from griddy.nfl import GriddyNFL

async def main():
    async with GriddyNFL(nfl_auth=auth) as nfl:
        games = await nfl.games.get_games_async(season=2024)
        return games

games = asyncio.run(main())
```

## Version Information

```python
import griddy

# Check SDK version
print(griddy.__version__)
```
