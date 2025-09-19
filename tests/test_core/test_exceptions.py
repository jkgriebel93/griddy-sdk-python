"""Tests for custom exceptions."""

import pytest

from griddy.core.exceptions import (
    GriddyError,
    APIError,
    RateLimitError,
    NotFoundError,
    AuthenticationError,
    ValidationError,
)


class TestExceptions:
    """Test cases for custom exceptions."""

    def test_griddy_error_basic(self):
        """Test basic GriddyError functionality."""
        error = GriddyError("Test error message")

        assert str(error) == "Test error message"
        assert error.message == "Test error message"
        assert error.status_code is None
        assert error.response_data == {}

    def test_griddy_error_with_details(self):
        """Test GriddyError with status code and response data."""
        response_data = {"error": "detailed error", "code": "E001"}
        error = GriddyError("Test error", status_code=400, response_data=response_data)

        assert error.message == "Test error"
        assert error.status_code == 400
        assert error.response_data == response_data

    def test_api_error_inheritance(self):
        """Test that APIError inherits from GriddyError."""
        error = APIError("API error", status_code=500)

        assert isinstance(error, GriddyError)
        assert error.message == "API error"
        assert error.status_code == 500

    def test_rate_limit_error_with_retry_after(self):
        """Test RateLimitError with retry_after parameter."""
        error = RateLimitError("Rate limit exceeded", status_code=429, retry_after=60)

        assert isinstance(error, GriddyError)
        assert error.message == "Rate limit exceeded"
        assert error.status_code == 429
        assert error.retry_after == 60

    def test_rate_limit_error_without_retry_after(self):
        """Test RateLimitError without retry_after parameter."""
        error = RateLimitError("Rate limit exceeded")

        assert error.retry_after is None

    def test_not_found_error(self):
        """Test NotFoundError functionality."""
        error = NotFoundError("Resource not found", status_code=404)

        assert isinstance(error, GriddyError)
        assert error.message == "Resource not found"
        assert error.status_code == 404

    def test_authentication_error(self):
        """Test AuthenticationError functionality."""
        error = AuthenticationError("Invalid credentials", status_code=401)

        assert isinstance(error, GriddyError)
        assert error.message == "Invalid credentials"
        assert error.status_code == 401

    def test_validation_error(self):
        """Test ValidationError functionality."""
        error = ValidationError("Invalid input data", status_code=422)

        assert isinstance(error, GriddyError)
        assert error.message == "Invalid input data"
        assert error.status_code == 422

    def test_exception_hierarchy(self):
        """Test that all custom exceptions inherit from GriddyError."""
        exceptions = [
            APIError("test"),
            RateLimitError("test"),
            NotFoundError("test"),
            AuthenticationError("test"),
            ValidationError("test"),
        ]

        for exception in exceptions:
            assert isinstance(exception, GriddyError)
            assert isinstance(exception, Exception)

    def test_exception_string_representation(self):
        """Test string representation of exceptions."""
        error = APIError("Something went wrong")
        assert str(error) == "Something went wrong"

    def test_exception_with_none_response_data(self):
        """Test exception with None response_data defaults to empty dict."""
        error = GriddyError("Test", response_data=None)
        assert error.response_data == {}


if __name__ == "__main__":
    pytest.main([__file__])
