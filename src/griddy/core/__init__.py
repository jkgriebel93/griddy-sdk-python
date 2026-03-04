"""Core module for the Griddy SDK.

This module provides shared functionality used across all SDK modules:

- **Exceptions**: Custom exception classes for different error scenarios
- **Models**: Base Pydantic models for data validation

Example:
    >>> from griddy.core import GriddyError
    >>> try:
    ...     data = sdk.some_method()
    ... except GriddyError as e:
    ...     print(f"Error: {e.message}")
"""

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
    "BaseModel",
    "GriddyError",
    "APIError",
    "RateLimitError",
    "NotFoundError",
    "AuthenticationError",
    "ValidationError",
]
