"""Tests for griddy.nfl.utils.retries."""

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from griddy.nfl.utils.retries import (
    BackoffStrategy,
    PermanentError,
    Retries,
    RetryConfig,
    TemporaryError,
    retry,
    retry_async,
    retry_with_backoff,
    retry_with_backoff_async,
)


def _make_retries(
    strategy="backoff",
    status_codes=None,
    retry_connection_errors=True,
):
    if status_codes is None:
        status_codes = ["5XX", "429"]
    backoff = BackoffStrategy(
        initial_interval=100,
        max_interval=1000,
        exponent=1.5,
        max_elapsed_time=5000,
    )
    config = RetryConfig(
        strategy=strategy,
        backoff=backoff,
        retry_connection_errors=retry_connection_errors,
    )
    return Retries(config=config, status_codes=status_codes)


def _make_response(status_code=200):
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    return resp


@pytest.mark.unit
class TestBackoffStrategy:
    def test_construction(self):
        bs = BackoffStrategy(
            initial_interval=500,
            max_interval=60000,
            exponent=1.5,
            max_elapsed_time=3600000,
        )
        assert bs.initial_interval == 500
        assert bs.max_interval == 60000
        assert bs.exponent == 1.5
        assert bs.max_elapsed_time == 3600000


@pytest.mark.unit
class TestRetryConfig:
    def test_construction(self):
        bs = BackoffStrategy(100, 1000, 1.5, 5000)
        rc = RetryConfig(strategy="backoff", backoff=bs, retry_connection_errors=True)
        assert rc.strategy == "backoff"
        assert rc.retry_connection_errors is True


@pytest.mark.unit
class TestTemporaryError:
    def test_stores_response(self):
        resp = _make_response(503)
        err = TemporaryError(resp)
        assert err.response is resp


@pytest.mark.unit
class TestPermanentError:
    def test_stores_inner(self):
        inner = ValueError("bad")
        err = PermanentError(inner)
        assert err.inner is inner


@pytest.mark.unit
class TestRetry:
    @patch("griddy.nfl.utils.retries.retry_with_backoff")
    def test_success_on_first_try(self, mock_backoff):
        resp = _make_response(200)
        mock_backoff.return_value = resp
        retries = _make_retries()
        result = retry(lambda: resp, retries)
        assert result is resp

    def test_non_backoff_strategy_calls_directly(self):
        resp = _make_response(200)
        retries = _make_retries(strategy="none")
        result = retry(lambda: resp, retries)
        assert result is resp

    @patch("griddy.nfl.utils.retries.retry_with_backoff")
    def test_5xx_triggers_retry(self, mock_backoff):
        resp = _make_response(503)
        mock_backoff.return_value = resp
        retries = _make_retries(status_codes=["5XX"])
        # The retry function wraps the call and checks status codes
        result = retry(lambda: resp, retries)
        mock_backoff.assert_called_once()

    def test_connect_error_with_retry_enabled(self):
        retries = _make_retries(retry_connection_errors=True)

        def failing_func():
            raise httpx.ConnectError("Connection refused")

        # With retry_connection_errors=True, ConnectError re-raises (for backoff to catch)
        with patch(
            "griddy.nfl.utils.retries.retry_with_backoff",
            side_effect=httpx.ConnectError("Connection refused"),
        ):
            with pytest.raises(httpx.ConnectError):
                retry(failing_func, retries)

    def test_connect_error_without_retry(self):
        retries = _make_retries(retry_connection_errors=False)

        call_count = 0

        def failing_func():
            nonlocal call_count
            call_count += 1
            raise httpx.ConnectError("Connection refused")

        # With retry_connection_errors=False, wraps in PermanentError
        # retry_with_backoff will unwrap it
        with patch("griddy.nfl.utils.retries.retry_with_backoff") as mock_backoff:
            mock_backoff.side_effect = httpx.ConnectError("Connection refused")
            with pytest.raises(httpx.ConnectError):
                retry(failing_func, retries)


@pytest.mark.unit
class TestRetryWithBackoff:
    @patch("griddy.nfl.utils.retries.time")
    def test_success_first_try(self, mock_time):
        mock_time.time.return_value = 1000.0
        resp = _make_response(200)
        result = retry_with_backoff(lambda: resp)
        assert result is resp

    @patch("griddy.nfl.utils.retries.time")
    def test_permanent_error_unwraps(self, mock_time):
        mock_time.time.return_value = 1000.0
        inner = ValueError("bad value")

        def failing():
            raise PermanentError(inner)

        with pytest.raises(ValueError, match="bad value"):
            retry_with_backoff(failing)

    @patch("griddy.nfl.utils.retries.time")
    def test_temporary_error_timeout_returns_response(self, mock_time):
        resp = _make_response(503)
        # First call: time returns start time
        # retry_with_backoff checks (now - start > max_elapsed_time)
        mock_time.time.side_effect = [1.0, 100.0]  # start=1000, now=100000
        mock_time.sleep = MagicMock()

        def failing():
            raise TemporaryError(resp)

        result = retry_with_backoff(
            failing, max_elapsed_time=1  # 1ms - immediately expires
        )
        assert result is resp

    @patch("griddy.nfl.utils.retries.time")
    def test_general_exception_timeout_reraises(self, mock_time):
        mock_time.time.side_effect = [1.0, 100.0]
        mock_time.sleep = MagicMock()

        def failing():
            raise RuntimeError("something broke")

        with pytest.raises(RuntimeError, match="something broke"):
            retry_with_backoff(failing, max_elapsed_time=1)


@pytest.mark.unit
@pytest.mark.asyncio
class TestRetryAsync:
    async def test_non_backoff_calls_directly(self):
        resp = _make_response(200)

        async def func():
            return resp

        retries = _make_retries(strategy="none")
        result = await retry_async(func, retries)
        assert result is resp


@pytest.mark.unit
@pytest.mark.asyncio
class TestRetryWithBackoffAsync:
    @patch("griddy.nfl.utils.retries.time")
    async def test_success_first_try(self, mock_time):
        mock_time.time.return_value = 1000.0
        resp = _make_response(200)

        async def func():
            return resp

        result = await retry_with_backoff_async(func)
        assert result is resp

    @patch("griddy.nfl.utils.retries.time")
    async def test_permanent_error_unwraps(self, mock_time):
        mock_time.time.return_value = 1000.0
        inner = ValueError("bad")

        async def failing():
            raise PermanentError(inner)

        with pytest.raises(ValueError, match="bad"):
            await retry_with_backoff_async(failing)
