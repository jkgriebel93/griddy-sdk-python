"""Tests for griddy.core.base_client."""

from unittest.mock import MagicMock, patch

import pytest

from griddy_core.base_client import BaseClient
from griddy_core.exceptions import (
    APIError,
    AuthenticationError,
    NotFoundError,
    RateLimitError,
)


@pytest.mark.unit
class TestBaseClientInit:
    def test_default_construction(self):
        client = BaseClient(base_url="https://api.nfl.com")
        assert client.base_url == "https://api.nfl.com"
        assert client.timeout == 30
        assert client.rate_limit_delay == 1.0
        client.close()

    def test_trailing_slash_removed(self):
        client = BaseClient(base_url="https://api.nfl.com/")
        assert client.base_url == "https://api.nfl.com"
        client.close()

    def test_custom_headers(self):
        client = BaseClient(
            base_url="https://api.nfl.com",
            headers={"X-Custom": "value"},
        )
        assert "X-Custom" in client.session.headers
        client.close()


@pytest.mark.unit
class TestHandleResponse:
    def _make_client(self):
        return BaseClient(base_url="https://api.nfl.com", rate_limit_delay=0)

    def _make_response(self, status_code, json_data=None, headers=None):
        resp = MagicMock()
        resp.status_code = status_code
        resp.content = b'{"test": true}' if json_data is not None else b""
        resp.json.return_value = json_data if json_data is not None else {}
        resp.text = ""
        resp.url = "https://api.nfl.com/test"
        resp.headers = headers or {}
        return resp

    def test_200_ok(self):
        client = self._make_client()
        resp = self._make_response(200, {"games": []})
        result = client._handle_response(resp)
        assert result == {"games": []}
        client.close()

    def test_404_not_found(self):
        client = self._make_client()
        resp = self._make_response(404, {"message": "Not found"})
        with pytest.raises(NotFoundError) as exc_info:
            client._handle_response(resp)
        assert exc_info.value.status_code == 404
        client.close()

    def test_401_authentication(self):
        client = self._make_client()
        resp = self._make_response(401, {"message": "Unauthorized"})
        with pytest.raises(AuthenticationError) as exc_info:
            client._handle_response(resp)
        assert exc_info.value.status_code == 401
        client.close()

    def test_429_rate_limit(self):
        client = self._make_client()
        resp = self._make_response(
            429, {"message": "Too many requests"}, headers={"Retry-After": "60"}
        )
        with pytest.raises(RateLimitError) as exc_info:
            client._handle_response(resp)
        assert exc_info.value.retry_after == 60
        client.close()

    def test_429_rate_limit_no_retry_after(self):
        client = self._make_client()
        resp = self._make_response(429, {"message": "Too many requests"})
        with pytest.raises(RateLimitError) as exc_info:
            client._handle_response(resp)
        assert exc_info.value.retry_after is None
        client.close()

    def test_500_api_error(self):
        client = self._make_client()
        resp = self._make_response(500, {"message": "Internal Server Error"})
        with pytest.raises(APIError) as exc_info:
            client._handle_response(resp)
        assert exc_info.value.status_code == 500
        client.close()

    def test_empty_content(self):
        client = self._make_client()
        resp = self._make_response(200)
        resp.content = b""
        result = client._handle_response(resp)
        assert result == {}
        client.close()

    def test_invalid_json(self):
        client = self._make_client()
        resp = MagicMock()
        resp.status_code = 200
        resp.content = b"not json"
        resp.json.side_effect = ValueError("bad json")
        resp.text = "not json"
        result = client._handle_response(resp)
        assert result == {"message": "not json"}
        client.close()


@pytest.mark.unit
class TestEnforceRateLimit:
    @patch("griddy_core.base_client.time")
    def test_rate_limit_sleeps(self, mock_time):
        mock_time.time.side_effect = [0.0, 0.5, 1.5]
        mock_time.sleep = MagicMock()
        client = BaseClient(base_url="https://api.nfl.com", rate_limit_delay=1.0)
        client._last_request_time = 0.0

        # First time.time() returns 0.5 (within rate limit window)
        client._enforce_rate_limit()
        mock_time.sleep.assert_called_once()
        client.close()

    def test_no_rate_limit_when_zero(self):
        client = BaseClient(base_url="https://api.nfl.com", rate_limit_delay=0)
        # Should not sleep
        client._enforce_rate_limit()
        client.close()
