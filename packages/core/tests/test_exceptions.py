"""Tests for griddy.core.exceptions."""

import pytest

from griddy_core.exceptions import (
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
class TestAPIError:
    def test_inherits_from_griddy_error(self):
        assert issubclass(APIError, GriddyError)

    def test_construction(self):
        err = APIError("api failed", status_code=503)
        assert err.message == "api failed"
        assert err.status_code == 503


@pytest.mark.unit
class TestRateLimitError:
    def test_inherits_from_griddy_error(self):
        assert issubclass(RateLimitError, GriddyError)

    def test_retry_after(self):
        err = RateLimitError("rate limited", retry_after=60)
        assert err.retry_after == 60
        assert err.message == "rate limited"

    def test_retry_after_none(self):
        err = RateLimitError("rate limited")
        assert err.retry_after is None


@pytest.mark.unit
class TestNotFoundError:
    def test_inherits(self):
        assert issubclass(NotFoundError, GriddyError)

    def test_construction(self):
        err = NotFoundError("not found", status_code=404)
        assert err.status_code == 404


@pytest.mark.unit
class TestAuthenticationError:
    def test_inherits(self):
        assert issubclass(AuthenticationError, GriddyError)


@pytest.mark.unit
class TestValidationError:
    def test_inherits(self):
        assert issubclass(ValidationError, GriddyError)

    def test_construction(self):
        err = ValidationError("bad input", status_code=400)
        assert err.status_code == 400
