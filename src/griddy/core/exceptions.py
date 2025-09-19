"""Custom exceptions for Griddy SDK."""


class GriddyError(Exception):
    """Base exception for all Griddy SDK errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response_data: dict[str, any] | None = None,
    ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_data = response_data or {}


class APIError(GriddyError):
    """Raised when an API request fails."""

    pass


class RateLimitError(GriddyError):
    """Raised when rate limit is exceeded."""

    def __init__(self, message: str, retry_after: int | None = None, **kwargs):
        super().__init__(message, **kwargs)
        self.retry_after = retry_after


class NotFoundError(GriddyError):
    """Raised when a requested resource is not found."""

    pass


class AuthenticationError(GriddyError):
    """Raised when authentication fails."""

    pass


class ValidationError(GriddyError):
    """Raised when request validation fails."""

    pass
