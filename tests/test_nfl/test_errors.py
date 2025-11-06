"""
Unit tests for griddy.nfl.errors module
"""

import httpx
import pytest

from griddy.nfl.errors import (
    GriddyNFLDefaultError,
    GriddyNFLError,
    NoResponseError,
    ResponseValidationError,
)


class TestGriddyNFLError:
    """Test cases for GriddyNFLError base class"""

    def test_error_initialization(self):
        """Test GriddyNFLError initialization with response"""
        response = httpx.Response(
            status_code=404,
            text="Not Found",
            headers={"content-type": "application/json"},
            request=httpx.Request("GET", "https://api.example.com"),
        )

        error = GriddyNFLError("Resource not found", response)

        assert error.message == "Resource not found"
        assert error.status_code == 404
        assert error.body == "Not Found"
        assert isinstance(error.headers, httpx.Headers)
        assert error.raw_response == response

    def test_error_initialization_with_custom_body(self):
        """Test GriddyNFLError initialization with custom body"""
        response = httpx.Response(
            status_code=500,
            text="Server Error",
            headers={"content-type": "text/plain"},
            request=httpx.Request("POST", "https://api.example.com"),
        )

        custom_body = "Custom error body"
        error = GriddyNFLError("Server error occurred", response, body=custom_body)

        assert error.message == "Server error occurred"
        assert error.status_code == 500
        assert error.body == custom_body
        assert error.body != response.text

    def test_error_str_representation(self):
        """Test GriddyNFLError string representation"""
        response = httpx.Response(
            status_code=400,
            text="Bad Request",
            request=httpx.Request("PUT", "https://api.example.com"),
        )

        error = GriddyNFLError("Invalid request", response)

        assert str(error) == "Invalid request"

    def test_error_is_exception(self):
        """Test that GriddyNFLError is an Exception"""
        response = httpx.Response(
            status_code=403,
            text="Forbidden",
            request=httpx.Request("GET", "https://api.example.com"),
        )

        error = GriddyNFLError("Access denied", response)

        assert isinstance(error, Exception)

    def test_error_is_frozen_dataclass(self):
        """Test that GriddyNFLError is a frozen dataclass"""
        response = httpx.Response(
            status_code=401,
            text="Unauthorized",
            request=httpx.Request("GET", "https://api.example.com"),
        )

        error = GriddyNFLError("Auth error", response)

        # Should not be able to modify frozen dataclass
        with pytest.raises(AttributeError):
            error.message = "New message"


class TestGriddyNFLDefaultError:
    """Test cases for GriddyNFLDefaultError"""

    def test_default_error_with_json_content_type(self):
        """Test default error formatting with JSON content type"""
        response = httpx.Response(
            status_code=404,
            text='{"error": "not found"}',
            headers={"content-type": "application/json"},
            request=httpx.Request("GET", "https://api.example.com/resource"),
        )

        error = GriddyNFLDefaultError("API error occurred", response)

        assert "API error occurred:" in error.message
        assert "Status 404" in error.message
        assert '{"error": "not found"}' in error.message
        # Content-Type should not be included for application/json
        assert "Content-Type" not in error.message

    def test_default_error_with_non_json_content_type(self):
        """Test default error formatting with non-JSON content type"""
        response = httpx.Response(
            status_code=500,
            text="<html>Server Error</html>",
            headers={"content-type": "text/html"},
            request=httpx.Request("POST", "https://api.example.com"),
        )

        error = GriddyNFLDefaultError("Server error", response)

        assert "Server error:" in error.message
        assert "Status 500" in error.message
        assert "Content-Type text/html" in error.message
        assert "<html>Server Error</html>" in error.message

    def test_default_error_with_content_type_with_spaces(self):
        """Test default error formatting with content type containing spaces"""
        response = httpx.Response(
            status_code=415,
            text="Unsupported",
            headers={"content-type": "text/plain; charset=utf-8"},
            request=httpx.Request("PUT", "https://api.example.com"),
        )

        error = GriddyNFLDefaultError("Unsupported media type", response)

        assert "Status 415" in error.message
        assert 'Content-Type "text/plain; charset=utf-8"' in error.message

    def test_default_error_truncates_long_body(self):
        """Test that default error truncates very long response bodies"""
        long_body = "x" * 15000  # More than MAX_MESSAGE_LEN (10000)
        response = httpx.Response(
            status_code=400,
            text=long_body,
            headers={"content-type": "text/plain"},
            request=httpx.Request("GET", "https://api.example.com"),
        )

        error = GriddyNFLDefaultError("Long error", response)

        assert "...and 5000 more chars" in error.message
        assert long_body not in error.message  # Full body should not be included

    def test_default_error_with_empty_message(self):
        """Test default error with empty message string"""
        response = httpx.Response(
            status_code=503,
            text="Service Unavailable",
            headers={"content-type": "text/plain"},
            request=httpx.Request("GET", "https://api.example.com"),
        )

        error = GriddyNFLDefaultError("", response)

        # Should still contain status and body
        assert "Status 503" in error.message
        assert "Service Unavailable" in error.message

    def test_default_error_inherits_from_base_error(self):
        """Test that GriddyNFLDefaultError inherits from GriddyNFLError"""
        response = httpx.Response(
            status_code=400,
            text="Bad Request",
            request=httpx.Request("POST", "https://api.example.com"),
        )

        error = GriddyNFLDefaultError("Error", response)

        assert isinstance(error, GriddyNFLError)
        assert isinstance(error, Exception)


class TestNoResponseError:
    """Test cases for NoResponseError"""

    def test_no_response_error_default_message(self):
        """Test NoResponseError with default message"""
        error = NoResponseError()

        assert error.message == "No response received"
        assert str(error) == "No response received"

    def test_no_response_error_custom_message(self):
        """Test NoResponseError with custom message"""
        custom_message = "Connection timeout - no response"
        error = NoResponseError(custom_message)

        assert error.message == custom_message
        assert str(error) == custom_message

    def test_no_response_error_is_exception(self):
        """Test that NoResponseError is an Exception"""
        error = NoResponseError()

        assert isinstance(error, Exception)

    def test_no_response_error_is_frozen(self):
        """Test that NoResponseError is a frozen dataclass"""
        error = NoResponseError("Test message")

        # Should not be able to modify frozen dataclass
        with pytest.raises(AttributeError):
            error.message = "New message"

    def test_no_response_error_can_be_raised(self):
        """Test that NoResponseError can be raised and caught"""
        with pytest.raises(NoResponseError) as exc_info:
            raise NoResponseError("Test error")

        assert exc_info.value.message == "Test error"


class TestResponseValidationError:
    """Test cases for ResponseValidationError"""

    def test_response_validation_error_initialization(self):
        """Test ResponseValidationError initialization"""
        response = httpx.Response(
            status_code=200,
            text='{"invalid": "data"}',
            headers={"content-type": "application/json"},
            request=httpx.Request("GET", "https://api.example.com"),
        )

        cause = ValueError("Field 'required_field' is missing")
        error = ResponseValidationError(
            "Response validation failed", response, cause=cause
        )

        assert "Response validation failed:" in error.message
        assert "Field 'required_field' is missing" in error.message
        assert error.status_code == 200

    def test_response_validation_error_message_includes_cause(self):
        """Test ResponseValidationError message includes cause"""
        response = httpx.Response(
            status_code=200,
            text="{}",
            request=httpx.Request("GET", "https://api.example.com"),
        )

        cause = TypeError("Invalid type")
        error = ResponseValidationError("Validation error", response, cause=cause)

        # The message should include both the main message and the cause
        assert "Validation error:" in error.message
        assert "Invalid type" in error.message

    def test_response_validation_error_with_custom_body(self):
        """Test ResponseValidationError with custom body"""
        response = httpx.Response(
            status_code=200,
            text='{"data": "original"}',
            request=httpx.Request("POST", "https://api.example.com"),
        )

        cause = ValueError("Validation failed")
        custom_body = '{"data": "custom"}'
        error = ResponseValidationError(
            "Custom validation error", response, cause=cause, body=custom_body
        )

        assert error.body == custom_body
        assert error.body != response.text

    def test_response_validation_error_inherits_from_base_error(self):
        """Test that ResponseValidationError inherits from GriddyNFLError"""
        response = httpx.Response(
            status_code=200,
            text="data",
            request=httpx.Request("GET", "https://api.example.com"),
        )

        cause = Exception("Test cause")
        error = ResponseValidationError("Test", response, cause=cause)

        assert isinstance(error, GriddyNFLError)
        assert isinstance(error, Exception)


class TestErrorsModuleLazyLoading:
    """Test the lazy loading mechanism in errors module"""

    def test_can_import_all_errors_from_module(self):
        """Test that all error classes can be imported from the module"""
        from griddy.nfl import errors

        assert hasattr(errors, "GriddyNFLError")
        assert hasattr(errors, "GriddyNFLDefaultError")
        assert hasattr(errors, "NoResponseError")
        assert hasattr(errors, "ResponseValidationError")

    def test_dynamic_import_returns_error_classes(self):
        """Test that __getattr__ returns the correct error classes"""
        from griddy.nfl import errors

        # Access via __getattr__
        GriddyNFLDefaultError = errors.GriddyNFLDefaultError
        assert GriddyNFLDefaultError.__name__ == "GriddyNFLDefaultError"

    def test_invalid_attribute_raises_error(self):
        """Test that accessing invalid attribute raises AttributeError"""
        from griddy.nfl import errors

        with pytest.raises(AttributeError):
            _ = errors.NonExistentError
