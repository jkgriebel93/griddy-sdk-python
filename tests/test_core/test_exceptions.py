"""Tests for griddy.core.exceptions."""

import pytest

from griddy.core.exceptions import (
    APIError,
    AuthenticationError,
    GriddyError,
    NotFoundError,
    RateLimitError,
    ValidationError,
)


@pytest.mark.unit
class TestGriddyError:
    def test_construction(self):
        err = GriddyError("test error", status_code=500, response_data={"key": "val"})
        assert err.message == "test error"
        assert err.status_code == 500
        assert err.response_data == {"key": "val"}
        assert str(err) == "test error"

    def test_defaults(self):
        err = GriddyError("test")
        assert err.status_code is None
        assert err.response_data == {}

    def test_is_exception(self):
        assert issubclass(GriddyError, Exception)


@pytest.mark.unit
class TestExceptionSubclasses:
    @pytest.mark.parametrize(
        "exc_class",
        [
            pytest.param(APIError, id="APIError"),
            pytest.param(RateLimitError, id="RateLimitError"),
            pytest.param(NotFoundError, id="NotFoundError"),
            pytest.param(AuthenticationError, id="AuthenticationError"),
            pytest.param(ValidationError, id="ValidationError"),
        ],
    )
    def test_inherits_from_griddy_error(self, exc_class):
        assert issubclass(exc_class, GriddyError)

    @pytest.mark.parametrize(
        "exc_class,kwargs,expected_status",
        [
            pytest.param(
                APIError,
                {"message": "api failed", "status_code": 503},
                503,
                id="APIError",
            ),
            pytest.param(
                NotFoundError,
                {"message": "not found", "status_code": 404},
                404,
                id="NotFoundError",
            ),
            pytest.param(
                ValidationError,
                {"message": "bad input", "status_code": 400},
                400,
                id="ValidationError",
            ),
        ],
    )
    def test_construction_with_status_code(self, exc_class, kwargs, expected_status):
        err = exc_class(**kwargs)
        assert err.message == kwargs["message"]
        assert err.status_code == expected_status


@pytest.mark.unit
class TestRateLimitError:
    @pytest.mark.parametrize(
        "retry_after,expected",
        [
            pytest.param(60, 60, id="with_retry_after"),
            pytest.param(None, None, id="without_retry_after"),
        ],
    )
    def test_retry_after(self, retry_after, expected):
        kwargs = {"message": "rate limited"}
        if retry_after is not None:
            kwargs["retry_after"] = retry_after
        err = RateLimitError(**kwargs)
        assert err.retry_after == expected
        assert err.message == "rate limited"
