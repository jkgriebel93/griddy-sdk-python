"""Tests for griddy.pfr.errors module."""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.errors.sdkerror import SDKError
from griddy.core.exceptions import APIError, GriddyError
from griddy.pfr.errors import GriddyPFRError, ParsingError
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
    @pytest.mark.parametrize(
        "parent_class",
        [
            pytest.param(SDKError, id="SDKError"),
            pytest.param(Exception, id="Exception"),
        ],
    )
    def test_inherits_from(self, parent_class):
        assert issubclass(GriddyPFRError, parent_class)

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

    @pytest.mark.parametrize(
        "content_type,should_include_ct",
        [
            pytest.param("text/html", True, id="html_includes_ct"),
            pytest.param("application/json", False, id="json_excludes_ct"),
            pytest.param("text/html; charset=utf-8", True, id="charset_ct_quoted"),
        ],
    )
    def test_content_type_handling(self, content_type, should_include_ct):
        response = _make_response(content_type=content_type)
        err = GriddyPFRDefaultError("error", response)
        msg = str(err)
        if should_include_ct:
            assert content_type in msg
        else:
            assert "Content-Type" not in msg

    @pytest.mark.parametrize(
        "status_code,text,check_field,check_value",
        [
            pytest.param(
                500,
                "Internal Server Error",
                "status",
                "Status 500",
                id="includes_status_code",
            ),
            pytest.param(
                400,
                "Internal Server Error",
                "body",
                "Internal Server Error",
                id="includes_body",
            ),
        ],
    )
    def test_message_contents(self, status_code, text, check_field, check_value):
        response = _make_response(status_code=status_code, text=text)
        err = GriddyPFRDefaultError("API error occurred", response)
        assert check_value in str(err)

    def test_long_body_truncated(self):
        response = _make_response(text="x" * 20000)
        err = GriddyPFRDefaultError("error", response)
        assert "more chars" in str(err)

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
    @pytest.mark.parametrize(
        "message,expected",
        [
            pytest.param(None, "No response received", id="default_message"),
            pytest.param("Server timed out", "Server timed out", id="custom_message"),
        ],
    )
    def test_message(self, message, expected):
        err = NoResponseError() if message is None else NoResponseError(message)
        assert str(err) == expected

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

    def test_cause_property_has_return_type_annotation(self):
        import typing

        hints = typing.get_type_hints(ResponseValidationError.cause.fget)
        assert hints["return"] == BaseException | None


@pytest.mark.unit
class TestErrorModuleLazyLoading:
    @pytest.mark.parametrize(
        "attr_name",
        [
            pytest.param("GriddyPFRDefaultError", id="GriddyPFRDefaultError"),
            pytest.param("NoResponseError", id="NoResponseError"),
            pytest.param("ResponseValidationError", id="ResponseValidationError"),
        ],
    )
    def test_lazy_import(self, attr_name):
        from griddy.pfr import errors

        assert hasattr(errors, attr_name)

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

    def test_dir_returns_list_of_strings(self):
        from griddy.pfr import errors

        result = dir(errors)
        assert isinstance(result, list)
        assert all(isinstance(name, str) for name in result)


@pytest.mark.unit
class TestParsingError:
    def test_inherits_from_griddy_error(self):
        assert issubclass(ParsingError, GriddyError)

    def test_basic_creation(self):
        err = ParsingError("Could not find table")
        assert err.message == "Could not find table"
        assert err.url is None
        assert err.selector is None
        assert err.html_sample is None

    def test_with_full_context(self):
        err = ParsingError(
            "Could not find table",
            url="https://www.pro-football-reference.com/years/2024/games.htm",
            selector="games",
            html_sample="<html><body>...</body></html>",
        )
        assert err.url == "https://www.pro-football-reference.com/years/2024/games.htm"
        assert err.selector == "games"
        assert err.html_sample == "<html><body>...</body></html>"

    @pytest.mark.parametrize(
        "kwargs,expected_str",
        [
            pytest.param(
                {"message": "Could not find table"},
                "Could not find table",
                id="message_only",
            ),
            pytest.param(
                {
                    "message": "Could not find table",
                    "url": "https://example.com/page",
                    "selector": "games",
                },
                "Could not find table | url=https://example.com/page | selector=games",
                id="url_and_selector",
            ),
            pytest.param(
                {"message": "Could not find table", "selector": "games"},
                "Could not find table | selector=games",
                id="selector_only",
            ),
        ],
    )
    def test_str_representation(self, kwargs, expected_str):
        err = ParsingError(**kwargs)
        assert str(err) == expected_str

    def test_caught_by_griddy_error(self):
        with pytest.raises(GriddyError):
            raise ParsingError("parsing failed", selector="games")

    def test_url_can_be_set_after_creation(self):
        err = ParsingError("Could not find table", selector="games")
        err.url = "https://example.com/page"
        assert err.url == "https://example.com/page"
        assert "url=https://example.com/page" in str(err)


@pytest.mark.unit
class TestUnifiedHierarchy:
    """Tests that PFR errors are catchable via public GriddyError/APIError."""

    @pytest.mark.parametrize(
        "child,parent",
        [
            pytest.param(GriddyPFRError, APIError, id="PFRError_is_APIError"),
            pytest.param(GriddyPFRError, GriddyError, id="PFRError_is_GriddyError"),
            pytest.param(
                GriddyPFRDefaultError,
                GriddyError,
                id="PFRDefaultError_is_GriddyError",
            ),
        ],
    )
    def test_inheritance(self, child, parent):
        assert issubclass(child, parent)

    @pytest.mark.parametrize(
        "error_class",
        [
            pytest.param(GriddyPFRError, id="GriddyPFRError"),
            pytest.param(GriddyPFRDefaultError, id="GriddyPFRDefaultError"),
        ],
    )
    def test_caught_by_griddy_error(self, error_class):
        response = _make_response()
        with pytest.raises(GriddyError):
            raise error_class("pfr error", response)
