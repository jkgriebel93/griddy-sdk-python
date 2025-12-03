# Configuration

This guide covers all configuration options available in the Griddy SDK.

## GriddyNFL Configuration

The `GriddyNFL` client accepts several configuration parameters:

```python
from griddy.nfl import GriddyNFL
from griddy.nfl.utils.retries import RetryConfig

nfl = GriddyNFL(
    # Authentication (required - choose one)
    nfl_auth={"accessToken": "your_token"},
    # OR
    login_email="email@example.com",
    login_password="password",
    headless_login=True,

    # HTTP Client options
    client=None,           # Custom sync httpx.Client
    async_client=None,     # Custom async httpx.AsyncClient
    timeout_ms=30000,      # Request timeout in milliseconds

    # Server configuration
    server_url=None,       # Override base URL
    server_idx=None,       # Server index (if multiple configured)
    url_params=None,       # URL template parameters

    # Retry configuration
    retry_config=RetryConfig(
        strategy="backoff",
        backoff=BackoffStrategy(
            initial_interval=500,
            max_interval=60000,
            exponent=1.5,
            max_elapsed_time=300000,
        ),
        retry_connection_errors=True,
    ),

    # Debugging
    debug_logger=None,     # Custom logger
)
```

## Authentication Options

### Pre-obtained Token

```python
auth_info = {
    "accessToken": "your_access_token"
}
nfl = GriddyNFL(nfl_auth=auth_info)
```

### Browser Authentication

```python
nfl = GriddyNFL(
    login_email="your_email@example.com",
    login_password="your_password",
    headless_login=True,  # False to see browser window
)
```

## Timeout Configuration

Set request timeout in milliseconds:

```python
# 60 second timeout
nfl = GriddyNFL(
    nfl_auth=auth_info,
    timeout_ms=60000,
)
```

## Retry Configuration

Configure automatic retry behavior for failed requests:

```python
from griddy.nfl.utils.retries import RetryConfig, BackoffStrategy

retry_config = RetryConfig(
    strategy="backoff",  # "none", "backoff", or "fixed"
    backoff=BackoffStrategy(
        initial_interval=500,      # Start with 500ms
        max_interval=60000,        # Max 60 seconds between retries
        exponent=1.5,              # Exponential factor
        max_elapsed_time=300000,   # Give up after 5 minutes
    ),
    retry_connection_errors=True,  # Retry on network errors
)

nfl = GriddyNFL(
    nfl_auth=auth_info,
    retry_config=retry_config,
)
```

### Retry Strategies

| Strategy | Description |
|----------|-------------|
| `"none"` | No automatic retries |
| `"backoff"` | Exponential backoff |
| `"fixed"` | Fixed delay between retries |

## Custom HTTP Clients

Provide your own HTTP clients for advanced configuration:

```python
import httpx

# Custom sync client with specific settings
custom_client = httpx.Client(
    timeout=60.0,
    follow_redirects=True,
    http2=True,
)

# Custom async client
custom_async_client = httpx.AsyncClient(
    timeout=60.0,
    follow_redirects=True,
    http2=True,
)

nfl = GriddyNFL(
    nfl_auth=auth_info,
    client=custom_client,
    async_client=custom_async_client,
)
```

## Debug Logging

Enable debug logging to troubleshoot issues:

```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("griddy")
logger.setLevel(logging.DEBUG)

# Or provide a custom logger
from griddy.nfl.utils.logger import Logger

class CustomLogger(Logger):
    def log(self, level: str, message: str, **kwargs):
        print(f"[{level}] {message} {kwargs}")

nfl = GriddyNFL(
    nfl_auth=auth_info,
    debug_logger=CustomLogger(),
)
```

## Environment Variables

Configure the SDK using environment variables:

```bash
# Set in your environment or .env file
export NFL_CLIENT_KEY="your_client_key"
export NFL_CLIENT_SECRET="your_client_secret"
export NFL_EMAIL="your_email@example.com"
export NFL_PASSWORD="your_password"
```

Access in code:

```python
import os

nfl = GriddyNFL(
    login_email=os.environ.get("NFL_EMAIL"),
    login_password=os.environ.get("NFL_PASSWORD"),
    headless_login=True,
)
```

## Base Client Configuration

The core `BaseClient` class (used by some internal modules) accepts:

```python
from griddy.core import BaseClient

client = BaseClient(
    base_url="https://api.example.com",
    timeout=30,              # Seconds
    max_retries=3,           # Number of retries
    rate_limit_delay=1.0,    # Delay between requests
    headers={                # Custom headers
        "User-Agent": "MyApp/1.0",
    },
    cookies_file="cookies.txt",  # Path to cookies file
)
```

## Per-Request Configuration

Override configuration for individual requests:

```python
# Some endpoints accept additional parameters
games = nfl.games.get_games(
    season=2024,
    week=1,
    # These may vary by endpoint
)
```

## Configuration Best Practices

### Production Settings

```python
# Recommended production configuration
nfl = GriddyNFL(
    nfl_auth=auth_info,
    timeout_ms=30000,
    retry_config=RetryConfig(
        strategy="backoff",
        backoff=BackoffStrategy(
            initial_interval=1000,
            max_interval=60000,
            exponent=2.0,
            max_elapsed_time=300000,
        ),
        retry_connection_errors=True,
    ),
)
```

### Development Settings

```python
# Development with more verbose output
import logging
logging.basicConfig(level=logging.DEBUG)

nfl = GriddyNFL(
    nfl_auth=auth_info,
    timeout_ms=60000,  # Longer timeout for debugging
    retry_config=RetryConfig(strategy="none"),  # Fail fast
)
```

### Testing Settings

```python
# Testing with mocked responses
import httpx
from unittest.mock import Mock

mock_client = Mock(spec=httpx.Client)
mock_async_client = Mock(spec=httpx.AsyncClient)

nfl = GriddyNFL(
    nfl_auth=auth_info,
    client=mock_client,
    async_client=mock_async_client,
)
```

## Settings File

The SDK uses a settings file at `src/griddy/settings.py`:

```python
# Default NFL settings
NFL = {
    "clientKey": os.environ.get("NFL_CLIENT_KEY", "default_key"),
    "clientSecret": os.environ.get("NFL_CLIENT_SECRET", "default_secret"),
}
```

## Next Steps

- [Error Handling](error-handling.md) - Handle configuration errors
- [API Reference](../api/index.md) - Complete API documentation
