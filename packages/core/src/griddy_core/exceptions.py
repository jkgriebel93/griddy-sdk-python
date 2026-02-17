"""Custom exceptions for the Griddy SDK.

This module defines a hierarchy of exceptions used throughout the Griddy SDK
to provide specific error information for different failure scenarios.

Exception Hierarchy:
    GriddyError (Base)
    ├── APIError           - General API request failures
    ├── RateLimitError     - Rate limit exceeded (429)
    ├── NotFoundError      - Resource not found (404)
    ├── AuthenticationError - Authentication failed (401)
    └── ValidationError    - Request validation failures

Example:
    >>> from griddy import GriddyError, RateLimitError
    >>> try:
    ...     result = nfl.games.get_games(season=2024)
    ... except RateLimitError as e:
    ...     print(f"Rate limited. Retry after: {e.retry_after}")
    ... except GriddyError as e:
    ...     print(f"Error: {e.message} (status: {e.status_code})")
"""

from typing import Any


class GriddyError(Exception):
    """Base exception for all Griddy SDK errors.

    All SDK-specific exceptions inherit from this class, allowing you to
    catch all SDK errors with a single except clause.

    Attributes:
        message: Human-readable error description.
        status_code: HTTP status code from the API response, if applicable.
        response_data: Raw response data from the API, if available.

    Example:
        >>> try:
        ...     result = nfl.games.get_games(season=2024)
        ... except GriddyError as e:
        ...     print(f"Error: {e.message}")
        ...     print(f"Status: {e.status_code}")
        ...     print(f"Data: {e.response_data}")
    """

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response_data: dict[str, Any] | None = None,
    ) -> None:
        """Initialize a GriddyError.

        Args:
            message: Human-readable error description.
            status_code: HTTP status code from the API response.
            response_data: Raw response data from the API.
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data or {}


class APIError(GriddyError):
    """Raised when an API request fails.

    This exception is raised for general API errors, including server errors
    (5xx status codes) and client errors that don't fit more specific categories.

    Example:
        >>> try:
        ...     result = nfl.games.get_games(season=2024)
        ... except APIError as e:
        ...     if e.status_code and e.status_code >= 500:
        ...         print("Server error - retry later")
        ...     else:
        ...         print(f"API error: {e.message}")
    """

    pass


class RateLimitError(GriddyError):
    """Raised when the API rate limit is exceeded.

    This exception is raised when the API returns a 429 status code,
    indicating too many requests have been made in a given time period.

    Attributes:
        retry_after: Number of seconds to wait before retrying, if provided
            by the API in the Retry-After header.

    Example:
        >>> import time
        >>> try:
        ...     result = nfl.games.get_games(season=2024)
        ... except RateLimitError as e:
        ...     wait_time = e.retry_after or 60
        ...     print(f"Rate limited. Waiting {wait_time} seconds...")
        ...     time.sleep(wait_time)
    """

    def __init__(
        self,
        message: str,
        retry_after: int | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize a RateLimitError.

        Args:
            message: Human-readable error description.
            retry_after: Seconds to wait before retrying, from Retry-After header.
            **kwargs: Additional arguments passed to GriddyError.
        """
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class NotFoundError(GriddyError):
    """Raised when a requested resource is not found.

    This exception is raised when the API returns a 404 status code,
    indicating the requested resource does not exist.

    Example:
        >>> try:
        ...     player = nfl.players.get_player(player_id="invalid_id")
        ... except NotFoundError as e:
        ...     print(f"Player not found: {e.message}")
        ...     player = None
    """

    pass


class AuthenticationError(GriddyError):
    """Raised when authentication fails.

    This exception is raised when the API returns a 401 status code,
    indicating the request lacks valid authentication credentials.

    Example:
        >>> try:
        ...     result = nfl.games.get_games(season=2024)
        ... except AuthenticationError:
        ...     print("Token expired. Please re-authenticate.")
    """

    pass


class ValidationError(GriddyError):
    """Raised when request validation fails.

    This exception is raised when the request parameters fail validation,
    either client-side or when the API returns a 400 status code.

    Example:
        >>> try:
        ...     result = nfl.games.get_games(season="invalid")
        ... except ValidationError as e:
        ...     print(f"Invalid parameters: {e.message}")
    """

    pass
