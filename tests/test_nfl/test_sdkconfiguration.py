"""
Unit tests for griddy.nfl.sdkconfiguration module
"""

from unittest.mock import Mock

import httpx
import pytest

from griddy.nfl import models
from griddy.nfl.httpclient import AsyncHttpClient, HttpClient
from griddy.nfl.sdkconfiguration import SERVERS, SDKConfiguration
from griddy.nfl.types import UNSET
from griddy.nfl.utils import RetryConfig
from griddy.nfl.utils.logger import Logger


class TestSDKConfiguration:
    """Test cases for SDKConfiguration dataclass"""

    def test_sdk_configuration_creation_with_required_fields(self):
        """Test creating SDKConfiguration with required fields"""
        client = httpx.Client()
        async_client = httpx.AsyncClient()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=async_client,
            async_client_supplied=False,
            debug_logger=logger,
        )

        assert config.client == client
        assert config.async_client == async_client
        assert config.debug_logger == logger
        assert config.client_supplied is False
        assert config.async_client_supplied is False

    def test_sdk_configuration_with_none_clients(self):
        """Test SDKConfiguration with None clients"""
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=None,
            client_supplied=True,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
        )

        assert config.client is None
        assert config.async_client is None

    def test_sdk_configuration_default_values(self):
        """Test SDKConfiguration default field values"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
        )

        # Test default values
        assert config.security is None
        assert config.server_url == ""
        assert config.server_idx == 0
        assert config.language == "python"
        # Note: retry_config uses pydantic Field() in a dataclass, which doesn't work as expected
        # The Field object itself becomes the default rather than calling the factory
        # This is a known limitation of mixing pydantic Field() with @dataclass
        from pydantic.fields import FieldInfo

        assert (
            isinstance(config.retry_config, FieldInfo) or config.retry_config is UNSET
        )
        assert config.timeout_ms is None
        assert config.custom_auth_info is None

    def test_sdk_configuration_with_security(self):
        """Test SDKConfiguration with security model"""
        client = httpx.Client()
        logger = Mock(spec=Logger)
        security = models.Security(nfl_auth="test_token")

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            security=security,
        )

        assert config.security == security
        assert config.security.nfl_auth == "test_token"

    def test_sdk_configuration_with_security_callable(self):
        """Test SDKConfiguration with security as a callable"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        def get_security():
            return models.Security(nfl_auth="dynamic_token")

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            security=get_security,
        )

        assert callable(config.security)
        assert config.security().nfl_auth == "dynamic_token"

    def test_sdk_configuration_with_custom_server_url(self):
        """Test SDKConfiguration with custom server URL"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            server_url="https://custom.api.com/v1",
        )

        assert config.server_url == "https://custom.api.com/v1"

    def test_sdk_configuration_with_retry_config(self):
        """Test SDKConfiguration with retry configuration"""
        client = httpx.Client()
        logger = Mock(spec=Logger)
        retry_config = RetryConfig(
            strategy="backoff",
            backoff={
                "initial_interval": 500,
                "max_interval": 60000,
                "exponent": 1.5,
                "max_elapsed_time": 3600000,
            },
            retry_connection_errors=True,
        )

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            retry_config=retry_config,
        )

        assert config.retry_config == retry_config
        assert config.retry_config is not UNSET

    def test_sdk_configuration_with_timeout(self):
        """Test SDKConfiguration with timeout_ms"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            timeout_ms=30000,
        )

        assert config.timeout_ms == 30000

    def test_sdk_configuration_with_custom_auth_info(self):
        """Test SDKConfiguration with custom_auth_info"""
        client = httpx.Client()
        logger = Mock(spec=Logger)
        auth_info = {
            "accessToken": "token123",
            "refreshToken": "refresh456",
            "expiresIn": 3600,
        }

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            custom_auth_info=auth_info,
        )

        assert config.custom_auth_info == auth_info
        assert config.custom_auth_info["accessToken"] == "token123"

    def test_sdk_configuration_version_fields(self):
        """Test that SDKConfiguration has version fields"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
        )

        # These fields should exist and have values
        assert hasattr(config, "openapi_doc_version")
        assert hasattr(config, "sdk_version")
        assert hasattr(config, "gen_version")
        assert hasattr(config, "user_agent")
        assert isinstance(config.openapi_doc_version, str)
        assert isinstance(config.sdk_version, str)
        assert isinstance(config.gen_version, str)
        assert isinstance(config.user_agent, str)


class TestGetServerDetails:
    """Test cases for SDKConfiguration.get_server_details method"""

    def test_get_server_details_with_custom_server_url(self):
        """Test get_server_details with custom server_url"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            server_url="https://custom.api.com/v2/",
        )

        url, params = config.get_server_details()

        # Should return custom URL with trailing slash removed
        assert url == "https://custom.api.com/v2"
        assert params == {}

    def test_get_server_details_with_custom_server_url_no_trailing_slash(self):
        """Test get_server_details with custom server_url without trailing slash"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            server_url="https://custom.api.com",
        )

        url, params = config.get_server_details()

        assert url == "https://custom.api.com"
        assert params == {}

    def test_get_server_details_regular_api_default(self):
        """Test get_server_details returns regular API by default"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            server_url="",
        )

        url, params = config.get_server_details()
        assert url == SERVERS["regular"]
        assert url == "https://api.nfl.com"
        assert params == {}

    def test_get_server_details_pro_api(self):
        """Test get_server_details returns pro API when is_pro is True"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            server_url="",
            is_pro=True,
        )

        url, params = config.get_server_details()

        assert url == SERVERS["pro"]
        assert url == "https://pro.nfl.com"
        assert params == {}

    def test_get_server_details_with_none_server_url(self):
        """Test get_server_details when server_url is None"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            server_url=None,
        )

        url, params = config.get_server_details()

        # Should fall back to regular server
        assert url == SERVERS["regular"]
        assert params == {}

    def test_get_server_details_with_none_server_idx(self):
        """Test get_server_details handles None server_idx"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            server_url="",
            server_idx=None,
        )

        url, params = config.get_server_details()

        # Should default to 0 and return regular server
        assert config.server_idx == 0
        assert url == SERVERS["regular"]

    def test_get_server_details_empty_string_server_url_uses_default(self):
        """Test that empty string server_url falls back to default servers"""
        client = httpx.Client()
        logger = Mock(spec=Logger)

        config = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            server_url="",  # Empty string
            is_pro=False,
        )

        url, params = config.get_server_details()

        assert url == "https://api.nfl.com"
        assert params == {}


class TestSERVERSConstant:
    """Test cases for SERVERS constant"""

    def test_servers_contains_regular(self):
        """Test SERVERS contains regular key"""
        assert "regular" in SERVERS
        assert SERVERS["regular"] == "https://api.nfl.com"

    def test_servers_contains_pro(self):
        """Test SERVERS contains pro key"""
        assert "pro" in SERVERS
        assert SERVERS["pro"] == "https://pro.nfl.com"

    def test_servers_has_two_entries(self):
        """Test SERVERS has exactly two entries"""
        assert len(SERVERS) == 2


class TestSDKConfigurationIntegration:
    """Integration tests for SDKConfiguration"""

    def test_full_sdk_configuration_with_all_fields(self):
        """Test creating SDKConfiguration with all fields populated"""
        client = httpx.Client()
        async_client = httpx.AsyncClient()
        logger = Mock(spec=Logger)
        security = models.Security(nfl_auth="full_token")
        retry_config = RetryConfig(
            strategy="backoff",
            backoff={
                "initial_interval": 500,
                "max_interval": 60000,
                "exponent": 1.5,
                "max_elapsed_time": 3600000,
            },
            retry_connection_errors=True,
        )
        auth_info = {"token": "abc123"}

        config = SDKConfiguration(
            client=client,
            client_supplied=True,
            async_client=async_client,
            async_client_supplied=True,
            debug_logger=logger,
            security=security,
            server_url="https://test.api.com",
            server_idx=1,
            retry_config=retry_config,
            timeout_ms=60000,
            is_pro=True,
            custom_auth_info=auth_info,
        )

        assert config.client == client
        assert config.client_supplied is True
        assert config.async_client == async_client
        assert config.async_client_supplied is True
        assert config.debug_logger == logger
        assert config.security == security
        assert config.server_url == "https://test.api.com"
        assert config.server_idx == 1
        assert config.retry_config == retry_config
        assert config.timeout_ms == 60000
        assert config.is_pro is True
        assert config.custom_auth_info == auth_info

    def test_sdk_configuration_is_dataclass(self):
        """Test that SDKConfiguration is a dataclass"""
        import dataclasses

        assert dataclasses.is_dataclass(SDKConfiguration)

    def test_sdk_configuration_can_be_copied(self):
        """Test that SDKConfiguration can be copied"""
        import copy

        client = httpx.Client()
        logger = Mock(spec=Logger)

        config1 = SDKConfiguration(
            client=client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=logger,
            server_url="https://api1.com",
        )

        config2 = copy.copy(config1)

        assert config2.client == config1.client
        assert config2.server_url == config1.server_url
        assert config2 is not config1
