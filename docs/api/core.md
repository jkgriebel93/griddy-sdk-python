# Core Module API Reference

The `griddy.core` module provides shared functionality used across all SDK modules.

## Module: griddy

::: griddy
    options:
      show_root_heading: true
      show_source: false
      members:
        - __version__
        - GriddyError
        - APIError
        - RateLimitError
        - NotFoundError
        - AuthenticationError
        - ValidationError

## Module: griddy.core

::: griddy.core
    options:
      show_root_heading: true
      show_source: false

## BaseClient

The `BaseClient` class provides HTTP functionality with built-in rate limiting and error handling.

::: griddy.core.base_client.BaseClient
    options:
      show_root_heading: true
      members:
        - __init__
        - get
        - post
        - close
        - _enforce_rate_limit
        - _handle_response

### Usage Example

```python
from griddy.core import BaseClient

# Create a client for a custom API
client = BaseClient(
    base_url="https://api.example.com",
    timeout=30,
    max_retries=3,
    rate_limit_delay=1.0,
    headers={"Authorization": "Bearer token"},
)

# Make requests
response = client.get("/endpoint", params={"key": "value"})

# Clean up
client.close()
```

## BaseModel

Base Pydantic model used by all SDK data models.

::: griddy.core.models.BaseModel
    options:
      show_root_heading: true
      show_source: false

## Utility Functions

### Cookie Utilities

The SDK includes utilities for extracting cookies from Netscape-format cookies.txt files:

```python
from griddy.core.utils import extract_cookies_as_header, extract_cookies_as_dict

# Extract cookies for a specific URL
cookies_dict = extract_cookies_as_dict("cookies.txt", "https://nfl.com")
cookie_header = extract_cookies_as_header("cookies.txt", "https://nfl.com")

# Use with requests
import requests
response = requests.get("https://nfl.com/api", cookies=cookies_dict)
```

### Rate Limit Decorator

The `retry_on_rate_limit` decorator automatically retries requests that hit rate limits:

```python
from griddy.core.utils import retry_on_rate_limit

@retry_on_rate_limit(max_retries=3)
def make_api_call():
    return client.get("/endpoint")
```
