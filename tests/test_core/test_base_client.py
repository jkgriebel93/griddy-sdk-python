"""Tests for BaseClient functionality."""

import pytest
import requests_mock
from unittest.mock import patch, MagicMock

from griddy.core.base_client import BaseClient
from griddy.core.exceptions import (
    APIError,
    RateLimitError,
    NotFoundError,
    AuthenticationError,
)


class TestBaseClient:
    """Test cases for BaseClient class."""

    def test_initialization(self):
        """Test BaseClient initialization with default parameters."""
        client = BaseClient("https://api.example.com")

        assert client.base_url == "https://api.example.com"
        assert client.timeout == 30
        assert client.rate_limit_delay == 1.0
        assert "Griddy-SDK/0.1.0" in client.session.headers["User-Agent"]

    def test_initialization_with_custom_params(self):
        """Test BaseClient initialization with custom parameters."""
        headers = {"Custom-Header": "test-value"}
        client = BaseClient(
            "https://api.example.com/",
            timeout=60,
            rate_limit_delay=2.0,
            headers=headers,
        )

        assert client.base_url == "https://api.example.com"
        assert client.timeout == 60
        assert client.rate_limit_delay == 2.0
        assert client.session.headers["Custom-Header"] == "test-value"

    @requests_mock.Mocker()
    def test_successful_get_request(self, m):
        """Test successful GET request."""
        client = BaseClient("https://api.example.com")
        expected_data = {"result": "success", "data": [1, 2, 3]}

        m.get("https://api.example.com/test", json=expected_data)

        result = client.get("test")
        assert result == expected_data

    @requests_mock.Mocker()
    def test_get_request_with_params(self, m):
        """Test GET request with query parameters."""
        client = BaseClient("https://api.example.com")
        expected_data = {"filtered": "data"}

        m.get("https://api.example.com/search?q=test&limit=10", json=expected_data)

        result = client.get("search", params={"q": "test", "limit": 10})
        assert result == expected_data

    @requests_mock.Mocker()
    def test_404_error(self, m):
        """Test 404 error handling."""
        client = BaseClient("https://api.example.com")

        m.get(
            "https://api.example.com/notfound",
            status_code=404,
            json={"error": "Not found"},
        )

        with pytest.raises(NotFoundError) as exc_info:
            client.get("notfound")

        assert exc_info.value.status_code == 404

    @requests_mock.Mocker()
    def test_401_error(self, m):
        """Test 401 authentication error handling."""
        client = BaseClient("https://api.example.com")

        m.get(
            "https://api.example.com/secure",
            status_code=401,
            json={"error": "Unauthorized"},
        )

        with pytest.raises(AuthenticationError) as exc_info:
            client.get("secure")

        assert exc_info.value.status_code == 401

    @requests_mock.Mocker()
    def test_429_rate_limit_error(self, m):
        """Test 429 rate limit error handling."""
        client = BaseClient("https://api.example.com")

        m.get(
            "https://api.example.com/limited",
            status_code=429,
            json={"error": "Rate limit exceeded"},
            headers={"Retry-After": "60"},
        )

        with pytest.raises(RateLimitError) as exc_info:
            client.get("limited")

        assert exc_info.value.status_code == 429
        assert exc_info.value.retry_after == 60

    @requests_mock.Mocker()
    def test_500_server_error(self, m):
        """Test 500 server error handling."""
        client = BaseClient("https://api.example.com")

        m.get(
            "https://api.example.com/error",
            status_code=500,
            json={"error": "Server error"},
        )

        with pytest.raises(APIError) as exc_info:
            client.get("error")

        assert exc_info.value.status_code == 500

    @requests_mock.Mocker()
    def test_post_request(self, m):
        """Test successful POST request."""
        client = BaseClient("https://api.example.com")
        expected_data = {"created": "success"}

        m.post("https://api.example.com/create", json=expected_data)

        result = client.post("create", json_data={"name": "test"})
        assert result == expected_data

    @patch("time.sleep")
    def test_rate_limiting(self, mock_sleep):
        """Test rate limiting functionality."""
        client = BaseClient("https://api.example.com", rate_limit_delay=1.0)

        with requests_mock.Mocker() as m:
            m.get("https://api.example.com/test", json={"success": True})

            # Make two requests
            client.get("test")
            client.get("test")

            # Sleep should be called once between requests
            mock_sleep.assert_called()

    def test_close_session(self):
        """Test closing the HTTP session."""
        client = BaseClient("https://api.example.com")

        with patch.object(client.session, "close") as mock_close:
            client.close()
            mock_close.assert_called_once()

    @requests_mock.Mocker()
    def test_non_json_response(self, m):
        """Test handling of non-JSON response."""
        client = BaseClient("https://api.example.com")

        m.get("https://api.example.com/text", text="Plain text response")

        result = client.get("text")
        assert result == {"message": "Plain text response"}

    @requests_mock.Mocker()
    def test_empty_response(self, m):
        """Test handling of empty response."""
        client = BaseClient("https://api.example.com")

        m.get("https://api.example.com/empty", text="")

        result = client.get("empty")
        assert result == {}


if __name__ == "__main__":
    pytest.main([__file__])
