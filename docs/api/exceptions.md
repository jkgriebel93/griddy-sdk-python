# Exceptions API Reference

The Griddy SDK provides a hierarchy of custom exceptions for precise error handling.

## Exception Hierarchy

```
Exception
└── GriddyError (Base SDK exception)
    ├── APIError (General API errors)
    ├── RateLimitError (Rate limiting)
    ├── NotFoundError (404 errors)
    ├── AuthenticationError (401 errors)
    └── ValidationError (Request validation)
```

## GriddyError

::: griddy.core.exceptions.GriddyError
    options:
      show_root_heading: true
      members:
        - __init__
        - message
        - status_code
        - response_data

### Usage

```python
from griddy import GriddyError

try:
    result = nfl.games.get_games(season=2024)
except GriddyError as e:
    print(f"Error: {e.message}")
    print(f"Status: {e.status_code}")
    print(f"Data: {e.response_data}")
```

## APIError

::: griddy.core.exceptions.APIError
    options:
      show_root_heading: true

### Usage

```python
from griddy import APIError

try:
    result = nfl.games.get_games(season=2024)
except APIError as e:
    if e.status_code >= 500:
        # Server error - retry later
        print("Server error, will retry")
    else:
        # Client error
        print(f"API error: {e.message}")
```

## RateLimitError

::: griddy.core.exceptions.RateLimitError
    options:
      show_root_heading: true
      members:
        - __init__
        - retry_after

### Usage

```python
import time
from griddy import RateLimitError

try:
    result = nfl.games.get_games(season=2024)
except RateLimitError as e:
    wait_time = e.retry_after or 60
    print(f"Rate limited. Waiting {wait_time}s...")
    time.sleep(wait_time)
    # Retry the request
```

## NotFoundError

::: griddy.core.exceptions.NotFoundError
    options:
      show_root_heading: true

### Usage

```python
from griddy import NotFoundError

try:
    player = nfl.players.get_player(player_id="invalid_id")
except NotFoundError as e:
    print(f"Player not found: {e.message}")
    player = None
```

## AuthenticationError

::: griddy.core.exceptions.AuthenticationError
    options:
      show_root_heading: true

### Usage

```python
from griddy import AuthenticationError

try:
    result = nfl.games.get_games(season=2024)
except AuthenticationError as e:
    print("Token expired. Please re-authenticate.")
    # Refresh token and retry
```

## ValidationError

::: griddy.core.exceptions.ValidationError
    options:
      show_root_heading: true

### Usage

```python
from griddy import ValidationError

try:
    # Invalid parameter
    result = nfl.games.get_games(season="invalid")
except ValidationError as e:
    print(f"Invalid input: {e.message}")
```

## Comprehensive Error Handling

Here's a pattern for handling all exception types:

```python
from griddy import (
    GriddyError,
    APIError,
    RateLimitError,
    NotFoundError,
    AuthenticationError,
    ValidationError,
)
import time

def safe_api_call(func, *args, max_retries=3, **kwargs):
    """Execute an API call with comprehensive error handling."""
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)

        except RateLimitError as e:
            wait = e.retry_after or (60 * (attempt + 1))
            print(f"Rate limited. Waiting {wait}s (attempt {attempt + 1})")
            time.sleep(wait)

        except NotFoundError as e:
            print(f"Resource not found: {e.message}")
            return None

        except AuthenticationError as e:
            print(f"Auth failed: {e.message}")
            raise  # Can't recover without new credentials

        except ValidationError as e:
            print(f"Invalid request: {e.message}")
            raise  # Programming error - fix the code

        except APIError as e:
            if e.status_code and e.status_code >= 500:
                wait = 5 * (attempt + 1)
                print(f"Server error. Retrying in {wait}s")
                time.sleep(wait)
            else:
                raise  # Client error - can't retry

        except GriddyError as e:
            print(f"Unexpected SDK error: {e.message}")
            raise

    raise GriddyError("Max retries exceeded")

# Usage
games = safe_api_call(nfl.games.get_games, season=2024, week=1)
```

## Exception Attributes Reference

| Exception | Attributes |
|-----------|------------|
| `GriddyError` | `message`, `status_code`, `response_data` |
| `APIError` | (inherits from GriddyError) |
| `RateLimitError` | `retry_after` + (inherits from GriddyError) |
| `NotFoundError` | (inherits from GriddyError) |
| `AuthenticationError` | (inherits from GriddyError) |
| `ValidationError` | (inherits from GriddyError) |

## HTTP Status Code Mapping

| Status Code | Exception |
|-------------|-----------|
| 400 | `APIError` or `ValidationError` |
| 401 | `AuthenticationError` |
| 403 | `APIError` |
| 404 | `NotFoundError` |
| 429 | `RateLimitError` |
| 500-599 | `APIError` |
