"""Utility functions for Griddy SDK."""

import time
from functools import wraps
from datetime import datetime, timezone
from typing import TypeVar, Callable

T = TypeVar('T')


def retry_on_rate_limit(max_retries: int = 3, backoff_factor: float = 1.0) -> Callable:
    """
    Decorator to retry function calls on rate limit errors.

    Args:
        max_retries: Maximum number of retry attempts
        backoff_factor: Factor for exponential backoff
    """
    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            from .exceptions import RateLimitError

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except RateLimitError as e:
                    if attempt == max_retries:
                        raise

                    # Calculate backoff time
                    backoff_time = backoff_factor * (2 ** attempt)
                    if e.retry_after:
                        backoff_time = max(backoff_time, e.retry_after)

                    time.sleep(backoff_time)

            return func(*args, **kwargs)  # This should never be reached
        return wrapper
    return decorator


def parse_date(date_str: str | None) -> datetime | None:
    """
    Parse date string into datetime object.

    Args:
        date_str: Date string in various formats

    Returns:
        Parsed datetime object or None
    """
    if not date_str:
        return None

    # Common date formats to try
    formats = [
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%m/%d/%Y %H:%M:%S",
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(date_str, fmt)
            # Add timezone info if not present
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue

    # If no format matches, return None
    return None


def clean_text(text: str | None) -> str | None:
    """
    Clean and normalize text data.

    Args:
        text: Text to clean

    Returns:
        Cleaned text or None
    """
    if not text:
        return None

    # Strip whitespace and normalize
    cleaned = text.strip()
    if not cleaned:
        return None

    return cleaned


def safe_int(value: any) -> int | None:
    """
    Safely convert value to integer.

    Args:
        value: Value to convert

    Returns:
        Integer value or None
    """
    if value is None:
        return None

    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def safe_float(value: any) -> float | None:
    """
    Safely convert value to float.

    Args:
        value: Value to convert

    Returns:
        Float value or None
    """
    if value is None:
        return None

    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def build_url(base_url: str, path: str, params: dict[str, any] | None = None) -> str:
    """
    Build URL from base URL, path, and parameters.

    Args:
        base_url: Base URL
        path: URL path
        params: Query parameters

    Returns:
        Complete URL
    """
    # Ensure base_url doesn't end with slash and path starts without slash
    base_url = base_url.rstrip('/')
    path = path.lstrip('/')

    url = f"{base_url}/{path}" if path else base_url

    if params:
        # Filter out None values
        filtered_params = {k: v for k, v in params.items() if v is not None}
        if filtered_params:
            from urllib.parse import urlencode
            url += f"?{urlencode(filtered_params)}"

    return url