"""Tests for griddy.core.basesdk module."""

from unittest.mock import AsyncMock, Mock, patch

import httpx
import pytest

from griddy.core.basesdk import BaseSDK, EndpointConfig
from griddy.core.errors.defaultsdkerror import DefaultSDKError
from griddy.core.errors.no_response_error import NoResponseError
from griddy.core.hooks.types import HookContext
from griddy.core.sdkconfiguration import SDKConfiguration
from griddy.core.types import UNSET
from griddy.core.utils import RetryConfig
from griddy.core.utils.logger import Logger


@pytest.fixture
def mock_logger():
    return Mock(spec=Logger)


@pytest.fixture
def mock_sdk_config(mock_logger):
    return SDKConfiguration(
        client=httpx.Client(),
        client_supplied=False,
        async_client=httpx.AsyncClient(),
        async_client_supplied=False,
        debug_logger=mock_logger,
        server_url="https://example.com",
        timeout_ms=30000,
    )


@pytest.fixture
def base_sdk(mock_sdk_config):
    return BaseSDK(sdk_config=mock_sdk_config)


@pytest.mark.unit
class TestBaseSDKInit:
    def test_stores_sdk_configuration(self, base_sdk, mock_sdk_config):
        assert base_sdk.sdk_configuration is mock_sdk_config

    def test_stores_parent_ref(self, mock_sdk_config):
        parent = object()
        sdk = BaseSDK(sdk_config=mock_sdk_config, parent_ref=parent)
        assert sdk.parent_ref is parent

    def test_parent_ref_defaults_to_none(self, base_sdk):
        assert base_sdk.parent_ref is None


@pytest.mark.unit
class TestDefaultErrorClasses:
    def test_default_error_cls_is_default_sdk_error(self, base_sdk):
        assert base_sdk._default_error_cls is DefaultSDKError

    def test_no_response_error_cls_is_no_response_error(self, base_sdk):
        assert base_sdk._no_response_error_cls is NoResponseError

    def test_security_model_cls_defaults_to_none(self, base_sdk):
        assert base_sdk._security_model_cls is None

    def test_security_env_mapping_defaults_to_none(self, base_sdk):
        assert base_sdk._security_env_mapping is None


@pytest.mark.unit
class TestResolveBaseUrl:
    def test_returns_server_url_when_provided(self, base_sdk):
        result = base_sdk._resolve_base_url(server_url="https://custom.api.com")
        assert result == "https://custom.api.com"

    def test_returns_sdk_url_when_no_override(self, base_sdk):
        result = base_sdk._resolve_base_url()
        assert result == "https://example.com"

    def test_returns_sdk_url_with_none_server_url(self, base_sdk):
        result = base_sdk._resolve_base_url(server_url=None)
        assert result == "https://example.com"


@pytest.mark.unit
class TestResolveTimeout:
    def test_returns_provided_timeout(self, base_sdk):
        assert base_sdk._resolve_timeout(timeout_ms=5000) == 5000

    def test_returns_config_timeout_when_none(self, base_sdk):
        assert base_sdk._resolve_timeout(timeout_ms=None) == 30000

    def test_returns_config_timeout_by_default(self, base_sdk):
        assert base_sdk._resolve_timeout() == 30000

    def test_returns_none_when_no_timeout(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            timeout_ms=None,
        )
        sdk = BaseSDK(sdk_config=config)
        assert sdk._resolve_timeout() is None


@pytest.mark.unit
class TestResolveRetryConfig:
    def test_returns_none_when_unset_and_no_config(self, mock_logger):
        config = SDKConfiguration(
            client=httpx.Client(),
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            retry_config=UNSET,
        )
        sdk = BaseSDK(sdk_config=config)
        assert sdk._resolve_retry_config(UNSET) is None

    def test_returns_tuple_when_retry_config_provided(self, base_sdk):
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
        result = base_sdk._resolve_retry_config(
            retry_config, retry_status_codes=["503"]
        )
        assert result[1] == ["503"]


@pytest.mark.unit
class TestCreateHookContext:
    def test_creates_hook_context(self, base_sdk):
        ctx = base_sdk._create_hook_context(
            operation_id="testOp", base_url="https://example.com"
        )
        assert isinstance(ctx, HookContext)
        assert ctx.operation_id == "testOp"
        assert ctx.base_url == "https://example.com"

    def test_hook_context_has_empty_oauth_scopes(self, base_sdk):
        ctx = base_sdk._create_hook_context(
            operation_id="testOp", base_url="https://example.com"
        )
        assert ctx.oauth2_scopes == []

    def test_hook_context_has_config_reference(self, base_sdk, mock_sdk_config):
        ctx = base_sdk._create_hook_context(
            operation_id="testOp", base_url="https://example.com"
        )
        assert ctx.config is mock_sdk_config


@pytest.mark.unit
class TestHandleJsonResponse:
    def test_returns_unmarshaled_on_200(self, base_sdk):
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.text = '{"key": "value"}'

        with patch("griddy.core.basesdk.utils.match_response", return_value=True):
            with patch("griddy.core.basesdk.unmarshal_json_response") as mock_unmarshal:
                mock_unmarshal.return_value = {"key": "value"}
                result = base_sdk._handle_json_response(
                    mock_response, dict, ["400", "4XX", "500", "5XX"]
                )
                assert result == {"key": "value"}

    def test_raises_default_error_on_4xx(self, base_sdk):
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.headers = {"content-type": "application/json"}
        mock_response.url = "https://example.com/test"

        def match_side_effect(response, status, content_type):
            if status == "200":
                return False
            if isinstance(status, list) and "4XX" in status:
                return True
            return False

        with patch(
            "griddy.core.basesdk.utils.match_response", side_effect=match_side_effect
        ):
            with patch(
                "griddy.core.basesdk.utils.stream_to_text", return_value="Bad Request"
            ):
                with pytest.raises(DefaultSDKError) as exc_info:
                    base_sdk._handle_json_response(
                        mock_response, dict, ["400", "4XX", "500", "5XX"]
                    )
                assert "API error occurred" in str(exc_info.value)

    def test_raises_default_error_on_5xx(self, base_sdk):
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 500
        mock_response.headers = {"content-type": "application/json"}
        mock_response.url = "https://example.com/test"

        def match_side_effect(response, status, content_type):
            if status == "200":
                return False
            if isinstance(status, list) and "5XX" in status and "4XX" not in status:
                return True
            return False

        with patch(
            "griddy.core.basesdk.utils.match_response", side_effect=match_side_effect
        ):
            with patch(
                "griddy.core.basesdk.utils.stream_to_text",
                return_value="Internal Server Error",
            ):
                with pytest.raises(DefaultSDKError) as exc_info:
                    base_sdk._handle_json_response(
                        mock_response, dict, ["400", "4XX", "500", "5XX"]
                    )
                assert "API error occurred" in str(exc_info.value)

    def test_raises_default_error_on_unexpected(self, base_sdk):
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 302
        mock_response.headers = {"content-type": "text/html"}
        mock_response.url = "https://example.com/test"
        mock_response.text = "Redirect"

        with patch("griddy.core.basesdk.utils.match_response", return_value=False):
            with pytest.raises(DefaultSDKError) as exc_info:
                base_sdk._handle_json_response(
                    mock_response, dict, ["400", "4XX", "500", "5XX"]
                )
            assert "Unexpected response received" in str(exc_info.value)


@pytest.mark.unit
class TestHandleJsonResponseAsync:
    @pytest.mark.asyncio
    async def test_returns_unmarshaled_on_200(self, base_sdk):
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 200
        mock_response.headers = {"content-type": "application/json"}
        mock_response.text = '{"key": "value"}'

        with patch("griddy.core.basesdk.utils.match_response", return_value=True):
            with patch("griddy.core.basesdk.unmarshal_json_response") as mock_unmarshal:
                mock_unmarshal.return_value = {"key": "value"}
                result = await base_sdk._handle_json_response_async(
                    mock_response, dict, ["400", "4XX", "500", "5XX"]
                )
                assert result == {"key": "value"}

    @pytest.mark.asyncio
    async def test_raises_default_error_on_4xx(self, base_sdk):
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 400
        mock_response.headers = {"content-type": "application/json"}
        mock_response.url = "https://example.com/test"

        def match_side_effect(response, status, content_type):
            if status == "200":
                return False
            if isinstance(status, list) and "4XX" in status:
                return True
            return False

        with patch(
            "griddy.core.basesdk.utils.match_response", side_effect=match_side_effect
        ):
            with patch(
                "griddy.core.basesdk.utils.stream_to_text_async",
                new_callable=AsyncMock,
                return_value="Bad Request",
            ):
                with pytest.raises(DefaultSDKError) as exc_info:
                    await base_sdk._handle_json_response_async(
                        mock_response, dict, ["400", "4XX", "500", "5XX"]
                    )
                assert "API error occurred" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_raises_default_error_on_5xx(self, base_sdk):
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 500
        mock_response.headers = {"content-type": "application/json"}
        mock_response.url = "https://example.com/test"

        def match_side_effect(response, status, content_type):
            if status == "200":
                return False
            if isinstance(status, list) and "5XX" in status and "4XX" not in status:
                return True
            return False

        with patch(
            "griddy.core.basesdk.utils.match_response", side_effect=match_side_effect
        ):
            with patch(
                "griddy.core.basesdk.utils.stream_to_text_async",
                new_callable=AsyncMock,
                return_value="Internal Server Error",
            ):
                with pytest.raises(DefaultSDKError) as exc_info:
                    await base_sdk._handle_json_response_async(
                        mock_response, dict, ["400", "4XX", "500", "5XX"]
                    )
                assert "API error occurred" in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_raises_default_error_on_unexpected(self, base_sdk):
        mock_response = Mock(spec=httpx.Response)
        mock_response.status_code = 302
        mock_response.headers = {"content-type": "text/html"}
        mock_response.url = "https://example.com/test"
        mock_response.text = "Redirect"

        with patch("griddy.core.basesdk.utils.match_response", return_value=False):
            with pytest.raises(DefaultSDKError) as exc_info:
                await base_sdk._handle_json_response_async(
                    mock_response, dict, ["400", "4XX", "500", "5XX"]
                )
            assert "Unexpected response received" in str(exc_info.value)


@pytest.mark.unit
class TestGetSecurityFromEnv:
    def test_returns_security_unchanged_when_not_none(self, base_sdk):
        security = object()
        result = base_sdk._get_security_from_env(security)
        assert result is security

    def test_returns_security_when_no_model_class(self, mock_sdk_config):
        sdk = BaseSDK(sdk_config=mock_sdk_config)
        # Core BaseSDK has _security_model_cls = None
        assert sdk._get_security_from_env(None) is None


@pytest.mark.unit
class TestEndpointConfig:
    def test_default_values(self):
        config = EndpointConfig(
            method="GET",
            path="/test",
            operation_id="testOp",
            request=None,
            response_type=dict,
            error_status_codes=["400"],
        )
        assert config.request_body_required is False
        assert config.request_has_path_params is False
        assert config.request_has_query_params is True
        assert config.return_raw_json is False
        assert config.accept_header_value == "application/json"
        assert config.user_agent_header == "user-agent"
        assert config.server_url is None
        assert config.timeout_ms is None

    def test_custom_values(self):
        config = EndpointConfig(
            method="POST",
            path="/test/{id}",
            operation_id="createTest",
            request={"id": "123"},
            response_type=dict,
            error_status_codes=["400", "500"],
            request_body_required=True,
            request_has_path_params=True,
            timeout_ms=5000,
        )
        assert config.method == "POST"
        assert config.request_body_required is True
        assert config.request_has_path_params is True
        assert config.timeout_ms == 5000
