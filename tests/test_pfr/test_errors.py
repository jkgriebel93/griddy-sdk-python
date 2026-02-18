"""Tests for griddy.pfr.errors module."""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.errors.sdkerror import SDKError
from griddy.pfr.errors import GriddyPFRError
from griddy.pfr.errors.griddypfrdefaulterror import GriddyPFRDefaultError
from griddy.pfr.errors.no_response_error import NoResponseError
from griddy.pfr.errors.responsevalidationerror import ResponseValidationError


def _make_response(status_code=400, content_type="application/json", text="error body"):
    response = Mock(spec=httpx.Response)
    response.status_code = status_code
    response.headers = httpx.Headers({"content-type": content_type})
    response.text = text
    return response


@pytest.mark.unit
class TestGriddyPFRError:
    def test_inherits_from_sdk_error(self):
        assert issubclass(GriddyPFRError, SDKError)

    def test_inherits_from_exception(self):
        assert issubclass(GriddyPFRError, Exception)

    def test_basic_creation(self):
        response = _make_response()
        err = GriddyPFRError("test error", response)
        assert err.message == "test error"
        assert err.status_code == 400
        assert err.body == "error body"
        assert str(err) == "test error"

    def test_with_custom_body(self):
        response = _make_response()
        err = GriddyPFRError("test error", response, body="custom body")
        assert err.body == "custom body"


@pytest.mark.unit
class TestGriddyPFRDefaultError:
    def test_inherits_from_pfr_error(self):
        assert issubclass(GriddyPFRDefaultError, GriddyPFRError)

    def test_message_includes_status_code(self):
        response = _make_response(status_code=500)
        err = GriddyPFRDefaultError("API error occurred", response)
        assert "Status 500" in str(err)

    def test_message_includes_body(self):
        response = _make_response(text="Internal Server Error")
        err = GriddyPFRDefaultError("API error occurred", response)
        assert "Internal Server Error" in str(err)

    def test_message_includes_content_type_for_non_json(self):
        response = _make_response(content_type="text/html")
        err = GriddyPFRDefaultError("error", response)
        assert "text/html" in str(err)

    def test_message_excludes_content_type_for_json(self):
        response = _make_response(content_type="application/json")
        err = GriddyPFRDefaultError("error", response)
        assert "Content-Type" not in str(err)

    def test_long_body_truncated(self):
        response = _make_response(text="x" * 20000)
        err = GriddyPFRDefaultError("error", response)
        assert "more chars" in str(err)

    def test_content_type_with_spaces_quoted(self):
        response = _make_response(content_type="text/html; charset=utf-8")
        err = GriddyPFRDefaultError("error", response)
        assert '"text/html; charset=utf-8"' in str(err)

    def test_empty_message_prefix(self):
        response = _make_response()
        err = GriddyPFRDefaultError("", response)
        msg = str(err)
        assert msg.startswith("Status 400")

    def test_empty_body_uses_empty_string(self):
        response = _make_response(text="")
        err = GriddyPFRDefaultError("error", response)
        assert '""' in str(err)


@pytest.mark.unit
class TestNoResponseError:
    def test_default_message(self):
        err = NoResponseError()
        assert str(err) == "No response received"

    def test_custom_message(self):
        err = NoResponseError("Server timed out")
        assert str(err) == "Server timed out"

    def test_is_exception(self):
        assert issubclass(NoResponseError, Exception)


@pytest.mark.unit
class TestResponseValidationError:
    def test_inherits_from_pfr_error(self):
        assert issubclass(ResponseValidationError, GriddyPFRError)

    def test_includes_cause_in_message(self):
        response = _make_response()
        cause = ValueError("bad data")
        err = ResponseValidationError("Validation failed", response, cause)
        assert "bad data" in str(err)
        assert "Validation failed" in str(err)

    def test_cause_property_returns_none_by_default(self):
        response = _make_response()
        err = ResponseValidationError("msg", response, ValueError("x"))
        assert err.cause is None


@pytest.mark.unit
class TestErrorModuleLazyLoading:
    def test_lazy_import_default_error(self):
        from griddy.pfr import errors

        assert hasattr(errors, "GriddyPFRDefaultError")

    def test_lazy_import_no_response_error(self):
        from griddy.pfr import errors

        assert hasattr(errors, "NoResponseError")

    def test_lazy_import_response_validation_error(self):
        from griddy.pfr import errors

        assert hasattr(errors, "ResponseValidationError")

    def test_unknown_attr_raises(self):
        from griddy.pfr import errors

        with pytest.raises(AttributeError):
            _ = errors.NonExistentError

    def test_dir_lists_error_classes(self):
        from griddy.pfr import errors

        d = dir(errors)
        assert "GriddyPFRDefaultError" in d
        assert "NoResponseError" in d
        assert "ResponseValidationError" in d
