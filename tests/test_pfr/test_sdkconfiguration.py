"""Tests for griddy.pfr.sdkconfiguration module."""

from unittest.mock import Mock

import httpx
import pytest

from griddy.core.sdkconfiguration import SDKConfiguration as CoreSDKConfiguration
from griddy.core.utils.logger import Logger
from griddy.pfr.sdkconfiguration import SERVERS, SDKConfiguration


@pytest.fixture
def mock_logger():
    return Mock(spec=Logger)


@pytest.mark.unit
class TestPFRServers:
    def test_default_server(self):
        assert "default" in SERVERS
        assert SERVERS["default"] == "https://www.pro-football-reference.com"


@pytest.mark.unit
class TestPFRSDKConfiguration:
    def test_inherits_from_core(self):
        assert issubclass(SDKConfiguration, CoreSDKConfiguration)

    def test_default_server_type(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
        )
        assert config.server_type == "default"

    def test_get_server_details_default(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
        )
        url, variables = config.get_server_details()
        assert url == "https://www.pro-football-reference.com"
        assert variables == {}

    def test_get_server_details_with_custom_url(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://custom.pfr.com/",
        )
        url, variables = config.get_server_details()
        assert url == "https://custom.pfr.com"
        assert variables == {}

    def test_get_server_details_strips_trailing_slash(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com/api/",
        )
        url, _ = config.get_server_details()
        assert not url.endswith("/")

    def test_get_server_details_with_none_server_idx(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_idx=None,
        )
        url, variables = config.get_server_details()
        assert url == "https://www.pro-football-reference.com"
        assert config.server_idx == 0  # Should be reset to 0

    def test_has_version_and_user_agent(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
        )
        assert config.sdk_version is not None
        assert isinstance(config.sdk_version, str)
        assert config.user_agent is not None
        assert isinstance(config.user_agent, str)
        assert len(config.user_agent) > 0
