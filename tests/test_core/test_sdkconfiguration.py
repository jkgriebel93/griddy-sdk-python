"""Tests for griddy.core.sdkconfiguration module."""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.sdkconfiguration import SDKConfiguration
from griddy.core.types import UNSET
from griddy.core.utils.logger import Logger


@pytest.fixture
def mock_logger():
    return Mock(spec=Logger)


@pytest.mark.unit
class TestSDKConfiguration:
    def test_default_values(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
        )
        assert config.security is None
        assert config.server_url == ""
        assert config.server_idx == 0
        assert config.language == "python"
        assert config.sdk_version == "0.0.0"
        assert config.user_agent == "griddy-sdk-python"
        assert config.retry_config == UNSET
        assert config.timeout_ms is None

    def test_get_server_details_with_url(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com/api/",
        )
        url, variables = config.get_server_details()
        assert url == "https://example.com/api"
        assert variables == {}

    def test_get_server_details_strips_trailing_slash(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com/",
        )
        url, _ = config.get_server_details()
        assert not url.endswith("/")

    def test_get_server_details_returns_empty_when_no_url(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="",
        )
        url, variables = config.get_server_details()
        assert url == ""
        assert variables == {}

    def test_get_server_details_returns_empty_when_url_is_none(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url=None,
        )
        url, variables = config.get_server_details()
        assert url == ""
        assert variables == {}

    def test_custom_timeout(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            timeout_ms=5000,
        )
        assert config.timeout_ms == 5000
