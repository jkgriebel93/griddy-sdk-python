"""
Unit tests for griddy.nfl.basesdk module helper methods
"""

from unittest.mock import AsyncMock, Mock, patch

import httpx
import pytest

from griddy_nfl import errors, models
from griddy_nfl._hooks.types import HookContext
from griddy_nfl.basesdk import BaseSDK
from griddy_nfl.sdkconfiguration import SDKConfiguration
from griddy_nfl.types import UNSET
from griddy_nfl.utils import RetryConfig
from griddy_nfl.utils.logger import Logger


@pytest.fixture
def mock_logger():
    """Create a mock logger."""
    return Mock(spec=Logger)


@pytest.fixture
def mock_sdk_config(mock_logger):
    """Create a mock SDK configuration."""
    client = httpx.Client()
    async_client = httpx.AsyncClient()
    security = models.Security(nfl_auth="test_token")

    config = SDKConfiguration(
        client=client,
        client_supplied=False,
        async_client=async_client,
        async_client_supplied=False,
        debug_logger=mock_logger,
        security=security,
        server_url="",
        timeout_ms=30000,
    )
    return config


@pytest.fixture
def base_sdk(mock_sdk_config):
    """Create a BaseSDK instance with mock configuration."""
    return BaseSDK(sdk_config=mock_sdk_config)


@pytest.mark.unit
class TestResolveBaseUrl:
    """Test cases for BaseSDK._resolve_base_url method"""

    def test_returns_server_url_when_provided(self, base_sdk):
        """Test that server_url override is returned when provided."""
        result = base_sdk._resolve_base_url(server_url="https://custom.api.com")
        assert result == "https://custom.api.com"

    def test_returns_sdk_url_when_no_override(self, base_sdk):
        """Test that SDK URL is returned when no override provided."""
        result = base_sdk._resolve_base_url()
        # Should return the regular API URL since is_pro defaults to False
        assert result == "https://api.nfl.com"

    def test_returns_sdk_url_with_none_server_url(self, base_sdk):
        """Test that SDK URL is returned when server_url is None."""
        result = base_sdk._resolve_base_url(server_url=None)
        assert result == "https://api.nfl.com"

    def test_uses_url_variables_when_no_override(self, base_sdk):
        """Test that url_variables are passed through when no server_url."""
        # url_variables would be used for template URL substitution
        result = base_sdk._resolve_base_url(url_variables={"version": "v2"})
        # The base URL should still resolve, variables are for templating
        assert "api.nfl.com" in result or "pro.nfl.com" in result


@pytest.mark.unit
class TestResolveTimeout:
    """Test cases for BaseSDK._resolve_timeout method"""

    def test_returns_provided_timeout(self, base_sdk):
        """Test that provided timeout is returned."""
        result = base_sdk._resolve_timeout(timeout_ms=5000)
        assert result == 5000

    def test_returns_config_timeout_when_none_provided(self, base_sdk):
        """Test that config timeout is returned when none provided."""
        # mock_sdk_config has timeout_ms=30000
        result = base_sdk._resolve_timeout(timeout_ms=None)
        assert result == 30000

    def test_returns_config_timeout_by_default(self, base_sdk):
        """Test that config timeout is returned by default."""
        result = base_sdk._resolve_timeout()
        assert result == 30000

    def test_returns_none_when_no_timeout_configured(self, mock_logger):
        """Test that None is returned when no timeout configured anywhere."""
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            timeout_ms=None,
        )
        sdk = BaseSDK(sdk_config=config)

        result = sdk._resolve_timeout()
        assert result is None


@pytest.mark.unit
class TestResolveRetryConfig:
    """Test cases for BaseSDK._resolve_retry_config method"""

    def test_returns_none_when_unset_and_no_config(self, mock_logger):
        """Test that None is returned when retries is UNSET and no config."""
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            retry_config=UNSET,
        )
        sdk = BaseSDK(sdk_config=config)

        result = sdk._resolve_retry_config(UNSET)
        assert result is None

    def test_returns_retry_config_tuple_when_provided(self, base_sdk):
        """Test that (RetryConfig, status_codes) tuple is returned when provided."""
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

        result = base_sdk._resolve_retry_config(retry_config)

        assert result is not None
        assert result[0] == retry_config
        assert result[1] == ["429", "500", "502", "503", "504"]

    def test_uses_custom_retry_status_codes(self, base_sdk):
        """Test that custom retry status codes are used."""
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
        custom_codes = ["503", "504"]

        result = base_sdk._resolve_retry_config(
            retry_config, retry_status_codes=custom_codes
        )

        assert result is not None
        assert result[1] == custom_codes

    def test_falls_back_to_config_retry_when_unset(self, mock_logger):
        """Test that config retry_config is used when retries is UNSET."""
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
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            retry_config=retry_config,
        )
        sdk = BaseSDK(sdk_config=config)

        result = sdk._resolve_retry_config(UNSET)

        assert result is not None
        assert result[0] == retry_config


@pytest.mark.unit
class TestCreateHookContext:
    """Test cases for BaseSDK._create_hook_context method"""

    def test_creates_hook_context_with_operation_id(self, base_sdk):
        """Test that HookContext is created with correct operation_id."""
        result = base_sdk._create_hook_context(
            operation_id="testOperation", base_url="https://api.test.com"
        )

        assert isinstance(result, HookContext)
        assert result.operation_id == "testOperation"
        assert result.base_url == "https://api.test.com"

    def test_creates_hook_context_with_empty_base_url(self, base_sdk):
        """Test that empty string is used for None base_url."""
        result = base_sdk._create_hook_context(operation_id="testOp", base_url="")

        assert result.base_url == ""

    def test_creates_hook_context_with_config(self, base_sdk, mock_sdk_config):
        """Test that HookContext has correct config reference."""
        result = base_sdk._create_hook_context(
            operation_id="testOp", base_url="https://test.com"
        )

        assert result.config == mock_sdk_config

    def test_creates_hook_context_with_empty_oauth_scopes(self, base_sdk):
        """Test that HookContext has empty oauth2_scopes."""
        result = base_sdk._create_hook_context(
            operation_id="testOp", base_url="https://test.com"
        )

        assert result.oauth2_scopes == []


@pytest.mark.unit
class TestHandleJsonResponse:
    """Test cases for BaseSDK._handle_json_response method"""

    def test_returns_unmarshaled_response_on_200(self, base_sdk):
        """Test that response is unmarshaled on 200 status."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.text = '{"nfl_auth": "test"}'

        with patch(
            "griddy_nfl.basesdk.utils.match_response", return_value=True
        ) as mock_match:
            with patch("griddy_nfl.basesdk.unmarshal_json_response") as mock_unmarshal:
                mock_unmarshal.return_value = models.Security(nfl_auth="test")

                result = base_sdk._handle_json_response(
                    mock_response,
                    models.Security,
                    ["400", "401", "4XX", "500", "5XX"],
                )

                mock_unmarshal.assert_called_once_with(models.Security, mock_response)
                assert isinstance(result, models.Security)

    def test_raises_error_on_4xx(self, base_sdk):
        """Test that GriddyNFLDefaultError is raised on 4XX status."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.headers = {"content-type": "application/json"}
        mock_response.url = "https://api.test.com/endpoint"

        def match_side_effect(response, status, content_type):
            if status == "200":
                return False
            if status == ["400", "401", "4XX"]:
                return True
            return False

        with patch(
            "griddy_nfl.basesdk.utils.match_response", side_effect=match_side_effect
        ):
            with patch(
                "griddy_nfl.basesdk.utils.stream_to_text", return_value="Bad Request"
            ):
                with pytest.raises(errors.GriddyNFLDefaultError) as exc_info:
                    base_sdk._handle_json_response(
                        mock_response,
                        models.Security,
                        ["400", "401", "4XX", "500", "5XX"],
                    )

                assert "API error occurred" in str(exc_info.value)

    def test_raises_error_on_5xx(self, base_sdk):
        """Test that GriddyNFLDefaultError is raised on 5XX status."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 500
        mock_response.headers = {"content-type": "application/json"}
        mock_response.url = "https://api.test.com/endpoint"

        def match_side_effect(response, status, content_type):
            if status == "200":
                return False
            if isinstance(status, list) and "500" in status:
                # Check if it's the 5XX check
                if "4XX" not in status:
                    return True
            return False

        with patch(
            "griddy_nfl.basesdk.utils.match_response", side_effect=match_side_effect
        ):
            with patch(
                "griddy_nfl.basesdk.utils.stream_to_text",
                return_value="Internal Server Error",
            ):
                with pytest.raises(errors.GriddyNFLDefaultError) as exc_info:
                    base_sdk._handle_json_response(
                        mock_response,
                        models.Security,
                        ["400", "401", "4XX", "500", "5XX"],
                    )

                assert "API error occurred" in str(exc_info.value)

    def test_raises_unexpected_response_error(self, base_sdk):
        """Test that error is raised for unexpected response."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 302
        mock_response.headers = {"content-type": "text/html"}
        mock_response.url = "https://api.test.com/endpoint"
        mock_response.text = "Redirect"

        with patch("griddy_nfl.basesdk.utils.match_response", return_value=False):
            with pytest.raises(errors.GriddyNFLDefaultError) as exc_info:
                base_sdk._handle_json_response(
                    mock_response, models.Security, ["400", "401", "4XX", "500", "5XX"]
                )

            assert "Unexpected response received" in str(exc_info.value)


@pytest.mark.unit
class TestHandleJsonResponseAsync:
    """Test cases for BaseSDK._handle_json_response_async method"""

    @pytest.mark.asyncio
    async def test_returns_unmarshaled_response_on_200(self, base_sdk):
        """Test that response is unmarshaled on 200 status."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.text = '{"nfl_auth": "test"}'

        with patch(
            "griddy_nfl.basesdk.utils.match_response", return_value=True
        ) as mock_match:
            with patch("griddy_nfl.basesdk.unmarshal_json_response") as mock_unmarshal:
                mock_unmarshal.return_value = models.Security(nfl_auth="test")

                result = await base_sdk._handle_json_response_async(
                    mock_response,
                    models.Security,
                    ["400", "401", "4XX", "500", "5XX"],
                )

                mock_unmarshal.assert_called_once_with(models.Security, mock_response)
                assert isinstance(result, models.Security)

    @pytest.mark.asyncio
    async def test_raises_error_on_4xx(self, base_sdk):
        """Test that GriddyNFLDefaultError is raised on 4XX status."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.headers = {"content-type": "application/json"}
        mock_response.url = "https://api.test.com/endpoint"

        def match_side_effect(response, status, content_type):
            if status == "200":
                return False
            if status == ["400", "401", "4XX"]:
                return True
            return False

        with patch(
            "griddy_nfl.basesdk.utils.match_response", side_effect=match_side_effect
        ):
            with patch(
                "griddy_nfl.basesdk.utils.stream_to_text_async",
                new_callable=AsyncMock,
                return_value="Bad Request",
            ):
                with pytest.raises(errors.GriddyNFLDefaultError) as exc_info:
                    await base_sdk._handle_json_response_async(
                        mock_response,
                        models.Security,
                        ["400", "401", "4XX", "500", "5XX"],
                    )

                assert "API error occurred" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_raises_unexpected_response_error(self, base_sdk):
        """Test that error is raised for unexpected response."""
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 302
        mock_response.headers = {"content-type": "text/html"}
        mock_response.url = "https://api.test.com/endpoint"
        mock_response.text = "Redirect"

        with patch("griddy_nfl.basesdk.utils.match_response", return_value=False):
            with pytest.raises(errors.GriddyNFLDefaultError) as exc_info:
                await base_sdk._handle_json_response_async(
                    mock_response, models.Security, ["400", "401", "4XX", "500", "5XX"]
                )

            assert "Unexpected response received" in str(exc_info.value)
