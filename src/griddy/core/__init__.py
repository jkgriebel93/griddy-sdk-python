"""Core module for the Griddy SDK.

This module provides shared functionality used across all SDK modules:

- **BaseClient**: HTTP client with rate limiting, retries, and error handling
- **Exceptions**: Custom exception classes for different error scenarios
- **Models**: Base Pydantic models for data validation

Example:
    >>> from griddy.core import BaseClient, GriddyError
    >>> client = BaseClient(base_url="https://api.example.com")
    >>> try:
    ...     data = client.get("/endpoint")
    ... except GriddyError as e:
    ...     print(f"Error: {e.message}")
"""

from .base_client import BaseClient
from .exceptions import (
    APIError,
    AuthenticationError,
    GriddyError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)
from .models import BaseModel

__all__ = [
    "BaseClient",
    "BaseModel",
    "GriddyError",
    "APIError",
    "RateLimitError",
    "NotFoundError",
    "AuthenticationError",
    "ValidationError",
]
