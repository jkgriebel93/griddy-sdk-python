# Error Handling

The Griddy SDK provides comprehensive error handling with specific exception types for different error scenarios.

## Exception Hierarchy

```
GriddyError (Base)
├── APIError           # General API errors
├── RateLimitError     # Rate limit exceeded
├── NotFoundError      # Resource not found (404)
├── AuthenticationError # Authentication failed (401)
└── ValidationError    # Request validation failed
```

## Importing Exceptions

```python
from griddy import (
    GriddyError,
    APIError,
    RateLimitError,
    NotFoundError,
    AuthenticationError,
    ValidationError,
)

# Or import from core module
from griddy.core.exceptions import GriddyError, APIError
```

## Exception Details

All exceptions include useful information:

```python
try:
    games = nfl.games.get_games(season=2024)
except GriddyError as e:
    print(f"Message: {e.message}")
    print(f"Status Code: {e.status_code}")
    print(f"Response Data: {e.response_data}")
```

### GriddyError

Base exception for all SDK errors.

**Attributes:**

- `message` - Human-readable error message
- `status_code` - HTTP status code (if applicable)
- `response_data` - Raw response data from the API

```python
try:
    result = nfl.games.get_games(season=2024)
except GriddyError as e:
    logger.error(f"SDK error: {e.message}")
```

### APIError

Raised for general API errors (5xx errors, unexpected responses).

```python
try:
    result = nfl.games.get_games(season=2024)
except APIError as e:
    if e.status_code >= 500:
        # Server error - retry later
        logger.warning(f"Server error: {e.message}")
    else:
        # Client error
        logger.error(f"API error: {e.message}")
```

### RateLimitError

Raised when API rate limits are exceeded (429 status).

**Additional Attributes:**

- `retry_after` - Seconds to wait before retrying (if provided by API)

```python
import time

try:
    result = nfl.games.get_games(season=2024)
except RateLimitError as e:
    wait_time = e.retry_after or 60  # Default to 60 seconds
    print(f"Rate limited. Waiting {wait_time} seconds...")
    time.sleep(wait_time)
    # Retry the request
    result = nfl.games.get_games(season=2024)
```

### NotFoundError

Raised when a requested resource doesn't exist (404 status).

```python
try:
    player = nfl.players.get_player(player_id="invalid_id")
except NotFoundError as e:
    print(f"Player not found: {e.message}")
    # Handle missing resource gracefully
    player = None
```

### AuthenticationError

Raised when authentication fails (401 status).

```python
try:
    result = nfl.games.get_games(season=2024)
except AuthenticationError as e:
    print("Authentication failed. Please refresh your token.")
    # Refresh token and retry
    new_token = refresh_auth_token()
    nfl = GriddyNFL(nfl_auth={"accessToken": new_token})
```

### ValidationError

Raised when request parameters are invalid.

```python
try:
    # Invalid season value
    result = nfl.games.get_games(season="invalid")
except ValidationError as e:
    print(f"Invalid parameters: {e.message}")
```

## Best Practices

### Comprehensive Error Handling

Handle specific exceptions before general ones:

```python
from griddy import (
    GriddyError,
    RateLimitError,
    NotFoundError,
    AuthenticationError,
)

def get_games_safely(nfl, season, week):
    """Fetch games with comprehensive error handling."""
    try:
        return nfl.games.get_games(season=season, week=week)

    except RateLimitError as e:
        # Handle rate limiting with exponential backoff
        wait_time = e.retry_after or 60
        logger.warning(f"Rate limited, waiting {wait_time}s")
        time.sleep(wait_time)
        return get_games_safely(nfl, season, week)  # Retry

    except NotFoundError:
        # Resource doesn't exist
        logger.info(f"No games found for {season} week {week}")
        return None

    except AuthenticationError:
        # Auth failed - can't recover without new credentials
        logger.error("Authentication failed")
        raise

    except GriddyError as e:
        # Catch-all for other SDK errors
        logger.error(f"API error: {e.message} (status: {e.status_code})")
        return None
```

### Retry Logic with Backoff

Implement exponential backoff for transient errors:

```python
import time
from typing import TypeVar, Callable

T = TypeVar('T')

def retry_with_backoff(
    func: Callable[[], T],
    max_retries: int = 3,
    base_delay: float = 1.0,
) -> T:
    """Execute function with exponential backoff on failure."""
    last_exception = None

    for attempt in range(max_retries):
        try:
            return func()
        except RateLimitError as e:
            delay = e.retry_after or (base_delay * (2 ** attempt))
            logger.warning(f"Rate limited, attempt {attempt + 1}, waiting {delay}s")
            time.sleep(delay)
            last_exception = e
        except APIError as e:
            if e.status_code and e.status_code >= 500:
                delay = base_delay * (2 ** attempt)
                logger.warning(f"Server error, attempt {attempt + 1}, waiting {delay}s")
                time.sleep(delay)
                last_exception = e
            else:
                raise  # Don't retry client errors

    raise last_exception or GriddyError("Max retries exceeded")

# Usage
games = retry_with_backoff(lambda: nfl.games.get_games(season=2024))
```

### Logging Errors

Always log errors with context:

```python
import logging

logger = logging.getLogger(__name__)

try:
    games = nfl.games.get_games(season=2024, week=1)
except GriddyError as e:
    logger.error(
        "Failed to fetch games",
        extra={
            "season": 2024,
            "week": 1,
            "error_message": e.message,
            "status_code": e.status_code,
            "response_data": e.response_data,
        },
        exc_info=True,
    )
```

### Graceful Degradation

Design your application to handle errors gracefully:

```python
def get_player_stats_with_fallback(nfl, player_id, season):
    """Get player stats with fallback to cached data."""
    try:
        stats = nfl.players.get_player(player_id=player_id)
        # Cache the successful response
        cache.set(f"player:{player_id}", stats)
        return stats

    except NotFoundError:
        logger.info(f"Player {player_id} not found")
        return None

    except (RateLimitError, APIError):
        # Try to use cached data
        cached = cache.get(f"player:{player_id}")
        if cached:
            logger.info(f"Using cached data for player {player_id}")
            return cached
        raise  # No fallback available
```

## Error Codes Reference

| Status Code | Exception | Description |
|-------------|-----------|-------------|
| 400 | APIError | Bad request - invalid parameters |
| 401 | AuthenticationError | Unauthorized - invalid/expired token |
| 403 | APIError | Forbidden - insufficient permissions |
| 404 | NotFoundError | Resource not found |
| 429 | RateLimitError | Too many requests |
| 500+ | APIError | Server errors |

## Next Steps

- [Configuration](configuration.md) - Configure retry behavior
- [API Reference](../api/exceptions.md) - Exception API docs
