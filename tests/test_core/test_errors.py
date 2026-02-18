"""Tests for griddy.core.errors module."""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.errors.defaultsdkerror import DefaultSDKError
from griddy.core.errors.no_response_error import NoResponseError
from griddy.core.errors.responsevalidationerror import ResponseValidationError
from griddy.core.errors.sdkerror import SDKError


def _make_response(status_code=400, content_type="application/json", text="error body"):
    response = Mock(spec=httpx.Response)
    response.status_code = status_code
    response.headers = httpx.Headers({"content-type": content_type})
    response.text = text
    return response


@pytest.mark.unit
class TestSDKError:
    def test_basic_creation(self):
        response = _make_response()
        err = SDKError("test error", response)
        assert err.message == "test error"
        assert err.status_code == 400
        assert err.body == "error body"
        assert str(err) == "test error"

    def test_with_custom_body(self):
        response = _make_response()
        err = SDKError("test error", response, body="custom body")
        assert err.body == "custom body"

    def test_body_defaults_to_response_text(self):
        response = _make_response(text="response text")
        err = SDKError("msg", response)
        assert err.body == "response text"

    def test_headers_from_response(self):
        response = _make_response()
        err = SDKError("msg", response)
        assert err.headers == response.headers

    def test_raw_response_stored(self):
        response = _make_response()
        err = SDKError("msg", response)
        assert err.raw_response is response

    def test_is_exception(self):
        assert issubclass(SDKError, Exception)


@pytest.mark.unit
class TestDefaultSDKError:
    def test_inherits_from_sdk_error(self):
        assert issubclass(DefaultSDKError, SDKError)

    def test_message_includes_status(self):
        response = _make_response(status_code=500)
        err = DefaultSDKError("API error", response)
        assert "Status 500" in str(err)

    def test_message_includes_body(self):
        response = _make_response(text="Server Error")
        err = DefaultSDKError("error", response)
        assert "Server Error" in str(err)

    def test_non_json_content_type_included(self):
        response = _make_response(content_type="text/html")
        err = DefaultSDKError("error", response)
        assert "text/html" in str(err)

    def test_json_content_type_excluded(self):
        response = _make_response(content_type="application/json")
        err = DefaultSDKError("error", response)
        assert "Content-Type" not in str(err)

    def test_content_type_with_spaces_quoted(self):
        response = _make_response(content_type="text/html; charset=utf-8")
        err = DefaultSDKError("error", response)
        assert '"text/html; charset=utf-8"' in str(err)

    def test_long_body_truncated(self):
        response = _make_response(text="x" * 20000)
        err = DefaultSDKError("error", response)
        msg = str(err)
        assert "more chars" in msg
        assert len(msg) < 20000

    def test_empty_body_uses_empty_string(self):
        response = _make_response(text="")
        err = DefaultSDKError("error", response)
        assert '""' in str(err)

    def test_empty_message_prefix(self):
        response = _make_response()
        err = DefaultSDKError("", response)
        msg = str(err)
        assert msg.startswith("Status 400")


@pytest.mark.unit
class TestResponseValidationError:
    def test_inherits_from_sdk_error(self):
        assert issubclass(ResponseValidationError, SDKError)

    def test_message_includes_cause(self):
        response = _make_response()
        cause = ValueError("invalid data")
        err = ResponseValidationError("Validation failed", response, cause)
        assert "invalid data" in str(err)
        assert "Validation failed" in str(err)

    def test_cause_property(self):
        response = _make_response()
        cause = ValueError("bad")
        err = ResponseValidationError("msg", response, cause)
        # cause property returns __cause__ (which is None unless explicitly chained)
        assert err.cause is None


@pytest.mark.unit
class TestErrorModuleLazyLoading:
    def test_lazy_import_default_sdk_error(self):
        from griddy.core import errors

        assert errors.DefaultSDKError is DefaultSDKError

    def test_lazy_import_no_response_error(self):
        from griddy.core import errors

        assert errors.NoResponseError is NoResponseError

    def test_lazy_import_response_validation_error(self):
        from griddy.core import errors

        assert errors.ResponseValidationError is ResponseValidationError

    def test_sdk_error_directly_imported(self):
        from griddy.core import errors

        assert errors.SDKError is SDKError

    def test_unknown_attr_raises(self):
        from griddy.core import errors

        with pytest.raises(AttributeError):
            _ = errors.NonExistentError

    def test_dir_lists_lazy_attrs(self):
        from griddy.core import errors

        d = dir(errors)
        assert "DefaultSDKError" in d
        assert "NoResponseError" in d
        assert "ResponseValidationError" in d
