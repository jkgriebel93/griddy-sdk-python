"""
Unit tests for griddy.nfl.errors module
"""

import httpx
import pytest

from griddy.core.exceptions import APIError, GriddyError
from griddy.nfl.errors import (
    GriddyNFLDefaultError,
    GriddyNFLError,
    NoResponseError,
    ResponseValidationError,
)


def _make_response(status_code=400, method="GET", text="Bad Request", headers=None):
    return httpx.Response(
        status_code=status_code,
        text=text,
        headers=headers or {},
        request=httpx.Request(method, "https://api.example.com"),
    )


@pytest.mark.unit
class TestGriddyNFLError:
    """Test cases for GriddyNFLError base class"""

    @pytest.mark.parametrize(
        "status_code,text,method,message",
        [
            pytest.param(404, "Not Found", "GET", "Resource not found", id="404_GET"),
            pytest.param(
                500, "Server Error", "POST", "Server error occurred", id="500_POST"
            ),
            pytest.param(400, "Bad Request", "PUT", "Invalid request", id="400_PUT"),
            pytest.param(403, "Forbidden", "GET", "Access denied", id="403_GET"),
            pytest.param(401, "Unauthorized", "GET", "Auth error", id="401_GET"),
        ],
    )
    def test_error_initialization(self, status_code, text, method, message):
        response = _make_response(status_code=status_code, text=text, method=method)
        error = GriddyNFLError(message, response)

        assert error.message == message
        assert error.status_code == status_code
        assert error.body == text
        assert isinstance(error.headers, httpx.Headers)
        assert error.raw_response == response
        assert isinstance(error, Exception)

    def test_error_initialization_with_custom_body(self):
        response = _make_response(status_code=500, text="Server Error")
        custom_body = "Custom error body"
        error = GriddyNFLError("Server error occurred", response, body=custom_body)

        assert error.body == custom_body
        assert error.body != response.text

    def test_error_str_representation(self):
        response = _make_response(status_code=400, text="Bad Request")
        error = GriddyNFLError("Invalid request", response)
        assert str(error) == "Invalid request"

    def test_error_is_frozen_dataclass(self):
        response = _make_response(status_code=401, text="Unauthorized")
        error = GriddyNFLError("Auth error", response)
        with pytest.raises(AttributeError):
            error.message = "New message"


@pytest.mark.unit
class TestGriddyNFLDefaultError:
    """Test cases for GriddyNFLDefaultError"""

    @pytest.mark.parametrize(
        "status_code,content_type,text,should_include_ct",
        [
            pytest.param(
                404,
                "application/json",
                '{"error": "not found"}',
                False,
                id="json_excludes_content_type",
            ),
            pytest.param(
                500,
                "text/html",
                "<html>Server Error</html>",
                True,
                id="html_includes_content_type",
            ),
            pytest.param(
                415,
                "text/plain; charset=utf-8",
                "Unsupported",
                True,
                id="charset_content_type_quoted",
            ),
        ],
    )
    def test_content_type_handling(
        self, status_code, content_type, text, should_include_ct
    ):
        response = _make_response(
            status_code=status_code,
            text=text,
            headers={"content-type": content_type},
        )
        error = GriddyNFLDefaultError("API error", response)

        assert f"Status {status_code}" in error.message
        assert text in error.message
        if should_include_ct:
            assert content_type in error.message
        else:
            assert "Content-Type" not in error.message

    def test_default_error_truncates_long_body(self):
        long_body = "x" * 15000
        response = _make_response(
            text=long_body,
            headers={"content-type": "text/plain"},
        )
        error = GriddyNFLDefaultError("Long error", response)

        assert "...and 5000 more chars" in error.message
        assert long_body not in error.message

    def test_default_error_with_empty_message(self):
        response = _make_response(
            status_code=503,
            text="Service Unavailable",
            headers={"content-type": "text/plain"},
        )
        error = GriddyNFLDefaultError("", response)
        assert "Status 503" in error.message
        assert "Service Unavailable" in error.message

    def test_default_error_inherits_from_base_error(self):
        response = _make_response()
        error = GriddyNFLDefaultError("Error", response)
        assert isinstance(error, GriddyNFLError)
        assert isinstance(error, Exception)


@pytest.mark.unit
class TestNoResponseError:
    """Test cases for NoResponseError"""

    @pytest.mark.parametrize(
        "message,expected",
        [
            pytest.param(None, "No response received", id="default_message"),
            pytest.param(
                "Connection timeout - no response",
                "Connection timeout - no response",
                id="custom_message",
            ),
        ],
    )
    def test_message(self, message, expected):
        error = NoResponseError() if message is None else NoResponseError(message)
        assert error.message == expected
        assert str(error) == expected

    def test_no_response_error_is_exception(self):
        assert isinstance(NoResponseError(), Exception)

    def test_no_response_error_is_frozen(self):
        error = NoResponseError("Test message")
        with pytest.raises(AttributeError):
            error.message = "New message"

    def test_no_response_error_can_be_raised(self):
        with pytest.raises(NoResponseError) as exc_info:
            raise NoResponseError("Test error")
        assert exc_info.value.message == "Test error"


@pytest.mark.unit
class TestResponseValidationError:
    """Test cases for ResponseValidationError"""

    @pytest.mark.parametrize(
        "cause_class,cause_msg",
        [
            pytest.param(
                ValueError, "Field 'required_field' is missing", id="value_error"
            ),
            pytest.param(TypeError, "Invalid type", id="type_error"),
        ],
    )
    def test_message_includes_cause(self, cause_class, cause_msg):
        response = _make_response(status_code=200, text="{}")
        cause = cause_class(cause_msg)
        error = ResponseValidationError("Validation error", response, cause=cause)

        assert "Validation error:" in error.message
        assert cause_msg in error.message

    def test_response_validation_error_with_custom_body(self):
        response = _make_response(status_code=200, text='{"data": "original"}')
        custom_body = '{"data": "custom"}'
        error = ResponseValidationError(
            "Custom validation error",
            response,
            cause=ValueError("Validation failed"),
            body=custom_body,
        )
        assert error.body == custom_body
        assert error.body != response.text

    def test_cause_property_returns_base_exception_or_none(self):
        response = _make_response(status_code=200, text="{}")
        cause = ValueError("bad value")
        error = ResponseValidationError("Test", response, cause=cause)
        result = error.cause
        assert result is None or isinstance(result, BaseException)

    def test_response_validation_error_inherits_from_base_error(self):
        response = _make_response(status_code=200, text="data")
        error = ResponseValidationError("Test", response, cause=Exception("Test cause"))
        assert isinstance(error, GriddyNFLError)
        assert isinstance(error, Exception)


@pytest.mark.unit
class TestErrorsModuleLazyLoading:
    """Test the lazy loading mechanism in errors module"""

    @pytest.mark.parametrize(
        "attr_name",
        [
            pytest.param("GriddyNFLError", id="GriddyNFLError"),
            pytest.param("GriddyNFLDefaultError", id="GriddyNFLDefaultError"),
            pytest.param("NoResponseError", id="NoResponseError"),
            pytest.param("ResponseValidationError", id="ResponseValidationError"),
        ],
    )
    def test_can_import_error_from_module(self, attr_name):
        from griddy.nfl import errors

        assert hasattr(errors, attr_name)

    def test_dynamic_import_returns_error_classes(self):
        from griddy.nfl import errors

        GriddyNFLDefaultError = errors.GriddyNFLDefaultError
        assert GriddyNFLDefaultError.__name__ == "GriddyNFLDefaultError"

    def test_dir_returns_list_of_strings(self):
        from griddy.nfl import errors

        result = dir(errors)
        assert isinstance(result, list)
        assert all(isinstance(name, str) for name in result)

    def test_invalid_attribute_raises_error(self):
        from griddy.nfl import errors

        with pytest.raises(AttributeError):
            _ = errors.NonExistentError


@pytest.mark.unit
class TestUnifiedHierarchy:
    """Tests that NFL errors are catchable via public GriddyError/APIError."""

    @pytest.mark.parametrize(
        "child,parent",
        [
            pytest.param(GriddyNFLError, APIError, id="NFLError_is_APIError"),
            pytest.param(GriddyNFLError, GriddyError, id="NFLError_is_GriddyError"),
            pytest.param(
                GriddyNFLDefaultError,
                GriddyError,
                id="NFLDefaultError_is_GriddyError",
            ),
        ],
    )
    def test_inheritance(self, child, parent):
        assert issubclass(child, parent)

    @pytest.mark.parametrize(
        "error_class",
        [
            pytest.param(GriddyNFLError, id="GriddyNFLError"),
            pytest.param(GriddyNFLDefaultError, id="GriddyNFLDefaultError"),
        ],
    )
    def test_caught_by_griddy_error(self, error_class):
        response = _make_response(status_code=500, text="error")
        with pytest.raises(GriddyError):
            raise error_class("nfl error", response)
