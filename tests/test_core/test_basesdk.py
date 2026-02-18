"""Tests for griddy.core.basesdk module."""

from unittest.mock import AsyncMock, Mock, patch

import httpx
import pytest

from griddy.core.basesdk import BaseSDK, EndpointConfig
from griddy.core.errors.defaultsdkerror import DefaultSDKError
from griddy.core.errors.no_response_error import NoResponseError
from griddy.core.hooks.sdkhooks import SDKHooks
from griddy.core.hooks.types import HookContext
from griddy.core.sdkconfiguration import SDKConfiguration
from griddy.core.types import UNSET
from griddy.core.utils import RetryConfig
from griddy.core.utils.logger import Logger
from griddy.core.utils.requestbodies import SerializedRequestBody


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


def _make_sdk_with_hooks(mock_logger, client=None, async_client=None):
    """Create a BaseSDK with hooks installed (as real SDKs do)."""
    config = SDKConfiguration(
        client=client or Mock(spec=httpx.Client),
        client_supplied=False,
        async_client=async_client or Mock(spec=httpx.AsyncClient),
        async_client_supplied=False,
        debug_logger=mock_logger,
        server_url="https://example.com",
        timeout_ms=30000,
    )
    hooks = SDKHooks()
    config.__dict__["_hooks"] = hooks
    return BaseSDK(sdk_config=config), config, hooks


def _make_httpx_response(status_code=200, json_data=None, text=""):
    """Create a minimal mock httpx.Response."""
    resp = Mock(spec=httpx.Response)
    resp.status_code = status_code
    resp.headers = httpx.Headers({"content-type": "application/json"})
    resp.url = "https://example.com/test"
    resp.text = text or (str(json_data) if json_data else "")
    if json_data is not None:
        resp.json.return_value = json_data
    return resp


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


# ---------------------------------------------------------------------------
# _build_request / _build_request_async / _build_request_with_client
# ---------------------------------------------------------------------------
@pytest.mark.unit
class TestBuildRequest:
    """Tests for _build_request, _build_request_async, _build_request_with_client."""

    def _patch_utils(self, **overrides):
        """Return a dict of patches for the utility functions called by _build_request_with_client."""
        defaults = {
            "griddy.core.basesdk.utils.generate_url": "https://example.com/test",
            "griddy.core.basesdk.utils.get_query_params": {},
            "griddy.core.basesdk.utils.get_headers": {},
        }
        defaults.update(overrides)
        patches = {}
        for target, return_value in defaults.items():
            patches[target] = patch(target, return_value=return_value)
        return patches

    def test_basic_get_request(self, mock_logger):
        mock_client = Mock(spec=httpx.Client)
        mock_request = Mock(spec=httpx.Request)
        mock_client.build_request.return_value = mock_request

        config = SDKConfiguration(
            client=mock_client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com",
            user_agent="test-agent",
        )
        sdk = BaseSDK(sdk_config=config)

        with (
            patch(
                "griddy.core.basesdk.utils.generate_url",
                return_value="https://example.com/api/test",
            ),
            patch("griddy.core.basesdk.utils.get_query_params", return_value={}),
            patch("griddy.core.basesdk.utils.get_headers", return_value={}),
        ):
            result = sdk._build_request(
                method="GET",
                path="/api/test",
                base_url="https://example.com",
                url_variables=None,
                request=None,
                request_body_required=False,
                request_has_path_params=False,
                request_has_query_params=True,
                user_agent_header="user-agent",
                accept_header_value="application/json",
            )

        assert result is mock_request
        call_kwargs = mock_client.build_request.call_args
        assert call_kwargs[0][0] == "GET"
        assert call_kwargs[1]["headers"]["Accept"] == "application/json"
        assert call_kwargs[1]["headers"]["user-agent"] == "test-agent"

    def test_build_request_async_uses_async_client(self, mock_logger):
        mock_async_client = Mock(spec=httpx.AsyncClient)
        mock_request = Mock(spec=httpx.Request)
        mock_async_client.build_request.return_value = mock_request

        config = SDKConfiguration(
            client=None,
            client_supplied=True,
            async_client=mock_async_client,
            async_client_supplied=False,
            debug_logger=mock_logger,
            server_url="https://example.com",
        )
        sdk = BaseSDK(sdk_config=config)

        with (
            patch(
                "griddy.core.basesdk.utils.generate_url",
                return_value="https://example.com/test",
            ),
            patch("griddy.core.basesdk.utils.get_query_params", return_value={}),
            patch("griddy.core.basesdk.utils.get_headers", return_value={}),
        ):
            result = sdk._build_request_async(
                method="GET",
                path="/test",
                base_url="https://example.com",
                url_variables=None,
                request=None,
                request_body_required=False,
                request_has_path_params=False,
                request_has_query_params=True,
                user_agent_header="user-agent",
                accept_header_value="application/json",
            )

        assert result is mock_request
        mock_async_client.build_request.assert_called_once()

    def test_url_override_parses_query_params(self, mock_logger):
        mock_client = Mock(spec=httpx.Client)
        mock_client.build_request.return_value = Mock(spec=httpx.Request)

        config = SDKConfiguration(
            client=mock_client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com",
        )
        sdk = BaseSDK(sdk_config=config)

        with patch("griddy.core.basesdk.utils.get_headers", return_value={}):
            sdk._build_request(
                method="GET",
                path="/test",
                base_url="https://example.com",
                url_variables=None,
                request=None,
                request_body_required=False,
                request_has_path_params=False,
                request_has_query_params=False,
                user_agent_header="user-agent",
                accept_header_value="application/json",
                url_override="https://override.com/path?foo=bar&baz=qux",
            )

        call_kwargs = mock_client.build_request.call_args[1]
        assert "foo" in call_kwargs["params"]
        assert "baz" in call_kwargs["params"]

    def test_callable_security_is_called(self, mock_logger):
        mock_client = Mock(spec=httpx.Client)
        mock_client.build_request.return_value = Mock(spec=httpx.Request)

        config = SDKConfiguration(
            client=mock_client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com",
        )
        sdk = BaseSDK(sdk_config=config)

        security_value = Mock()
        callable_security = Mock(return_value=security_value)

        with (
            patch(
                "griddy.core.basesdk.utils.generate_url",
                return_value="https://example.com/test",
            ),
            patch("griddy.core.basesdk.utils.get_query_params", return_value={}),
            patch("griddy.core.basesdk.utils.get_headers", return_value={}),
            patch(
                "griddy.core.basesdk.utils.get_security",
                return_value=({"Authorization": "Bearer tok"}, {}),
            ),
        ):
            sdk._build_request(
                method="GET",
                path="/test",
                base_url="https://example.com",
                url_variables=None,
                request=None,
                request_body_required=False,
                request_has_path_params=False,
                request_has_query_params=True,
                user_agent_header="user-agent",
                accept_header_value="application/json",
                security=callable_security,
            )

        callable_security.assert_called_once()
        call_headers = mock_client.build_request.call_args[1]["headers"]
        assert call_headers["Authorization"] == "Bearer tok"

    def test_required_body_missing_raises(self, mock_logger):
        mock_client = Mock(spec=httpx.Client)

        config = SDKConfiguration(
            client=mock_client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com",
        )
        sdk = BaseSDK(sdk_config=config)

        with (
            patch(
                "griddy.core.basesdk.utils.generate_url",
                return_value="https://example.com/test",
            ),
            patch("griddy.core.basesdk.utils.get_query_params", return_value={}),
            patch("griddy.core.basesdk.utils.get_headers", return_value={}),
        ):
            with pytest.raises(ValueError, match="request body is required"):
                sdk._build_request(
                    method="POST",
                    path="/test",
                    base_url="https://example.com",
                    url_variables=None,
                    request=None,
                    request_body_required=True,
                    request_has_path_params=False,
                    request_has_query_params=True,
                    user_agent_header="user-agent",
                    accept_header_value="application/json",
                    get_serialized_body=lambda: None,
                )

    def test_serialized_body_sets_content_type(self, mock_logger):
        mock_client = Mock(spec=httpx.Client)
        mock_client.build_request.return_value = Mock(spec=httpx.Request)

        config = SDKConfiguration(
            client=mock_client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com",
        )
        sdk = BaseSDK(sdk_config=config)

        body = SerializedRequestBody(
            media_type="application/json", content=b'{"key": "value"}'
        )

        with (
            patch(
                "griddy.core.basesdk.utils.generate_url",
                return_value="https://example.com/test",
            ),
            patch("griddy.core.basesdk.utils.get_query_params", return_value={}),
            patch("griddy.core.basesdk.utils.get_headers", return_value={}),
        ):
            sdk._build_request(
                method="POST",
                path="/test",
                base_url="https://example.com",
                url_variables=None,
                request=None,
                request_body_required=True,
                request_has_path_params=False,
                request_has_query_params=True,
                user_agent_header="user-agent",
                accept_header_value="application/json",
                get_serialized_body=lambda: body,
            )

        call_headers = mock_client.build_request.call_args[1]["headers"]
        assert call_headers["content-type"] == "application/json"

    def test_multipart_body_does_not_set_content_type(self, mock_logger):
        mock_client = Mock(spec=httpx.Client)
        mock_client.build_request.return_value = Mock(spec=httpx.Request)

        config = SDKConfiguration(
            client=mock_client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com",
        )
        sdk = BaseSDK(sdk_config=config)

        body = SerializedRequestBody(media_type="multipart/form-data", data={"f": "v"})

        with (
            patch(
                "griddy.core.basesdk.utils.generate_url",
                return_value="https://example.com/test",
            ),
            patch("griddy.core.basesdk.utils.get_query_params", return_value={}),
            patch("griddy.core.basesdk.utils.get_headers", return_value={}),
        ):
            sdk._build_request(
                method="POST",
                path="/test",
                base_url="https://example.com",
                url_variables=None,
                request=None,
                request_body_required=False,
                request_has_path_params=False,
                request_has_query_params=True,
                user_agent_header="user-agent",
                accept_header_value="application/json",
                get_serialized_body=lambda: body,
            )

        call_headers = mock_client.build_request.call_args[1]["headers"]
        assert "content-type" not in call_headers

    def test_http_headers_override(self, mock_logger):
        mock_client = Mock(spec=httpx.Client)
        mock_client.build_request.return_value = Mock(spec=httpx.Request)

        config = SDKConfiguration(
            client=mock_client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com",
        )
        sdk = BaseSDK(sdk_config=config)

        with (
            patch(
                "griddy.core.basesdk.utils.generate_url",
                return_value="https://example.com/test",
            ),
            patch("griddy.core.basesdk.utils.get_query_params", return_value={}),
            patch("griddy.core.basesdk.utils.get_headers", return_value={}),
        ):
            sdk._build_request(
                method="GET",
                path="/test",
                base_url="https://example.com",
                url_variables=None,
                request=None,
                request_body_required=False,
                request_has_path_params=False,
                request_has_query_params=True,
                user_agent_header="user-agent",
                accept_header_value="application/json",
                http_headers={"X-Custom": "custom-value", "Accept": "text/plain"},
            )

        call_headers = mock_client.build_request.call_args[1]["headers"]
        assert call_headers["X-Custom"] == "custom-value"
        # http_headers override should take precedence
        assert call_headers["Accept"] == "text/plain"

    def test_timeout_ms_converted_to_seconds(self, mock_logger):
        mock_client = Mock(spec=httpx.Client)
        mock_client.build_request.return_value = Mock(spec=httpx.Request)

        config = SDKConfiguration(
            client=mock_client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com",
        )
        sdk = BaseSDK(sdk_config=config)

        with (
            patch(
                "griddy.core.basesdk.utils.generate_url",
                return_value="https://example.com/test",
            ),
            patch("griddy.core.basesdk.utils.get_query_params", return_value={}),
            patch("griddy.core.basesdk.utils.get_headers", return_value={}),
        ):
            sdk._build_request(
                method="GET",
                path="/test",
                base_url="https://example.com",
                url_variables=None,
                request=None,
                request_body_required=False,
                request_has_path_params=False,
                request_has_query_params=True,
                user_agent_header="user-agent",
                accept_header_value="application/json",
                timeout_ms=5000,
            )

        assert mock_client.build_request.call_args[1]["timeout"] == 5.0

    def test_no_timeout_passes_none(self, mock_logger):
        mock_client = Mock(spec=httpx.Client)
        mock_client.build_request.return_value = Mock(spec=httpx.Request)

        config = SDKConfiguration(
            client=mock_client,
            client_supplied=False,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
            server_url="https://example.com",
        )
        sdk = BaseSDK(sdk_config=config)

        with (
            patch(
                "griddy.core.basesdk.utils.generate_url",
                return_value="https://example.com/test",
            ),
            patch("griddy.core.basesdk.utils.get_query_params", return_value={}),
            patch("griddy.core.basesdk.utils.get_headers", return_value={}),
        ):
            sdk._build_request(
                method="GET",
                path="/test",
                base_url="https://example.com",
                url_variables=None,
                request=None,
                request_body_required=False,
                request_has_path_params=False,
                request_has_query_params=True,
                user_agent_header="user-agent",
                accept_header_value="application/json",
            )

        assert mock_client.build_request.call_args[1]["timeout"] is None


# ---------------------------------------------------------------------------
# do_request (sync)
# ---------------------------------------------------------------------------
@pytest.mark.unit
class TestDoRequest:
    """Tests for BaseSDK.do_request (sync HTTP execution with hooks)."""

    def test_successful_request(self, mock_logger):
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}
        mock_response = _make_httpx_response(200)
        config.client.send.return_value = mock_response

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            result = sdk.do_request(
                hook_ctx=hook_ctx,
                request=mock_request,
                error_status_codes=["4XX", "5XX"],
            )

        assert result is mock_response
        config.client.send.assert_called_once()

    def test_client_none_raises_value_error(self, mock_logger):
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        config.client = None
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with pytest.raises(ValueError, match="client is required"):
                sdk.do_request(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX", "5XX"],
                )

    def test_exception_during_send_propagates_via_after_error(self, mock_logger):
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        send_error = ConnectionError("Connection refused")
        config.client.send.side_effect = send_error
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with pytest.raises(ConnectionError, match="Connection refused"):
                sdk.do_request(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX", "5XX"],
                )

    def test_no_response_raises_no_response_error(self, mock_logger):
        """When after_error swallows the exception AND returns no response."""
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        config.client.send.side_effect = ConnectionError("fail")

        # Mock hooks so after_error returns (None, None) — swallowing the error
        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        mock_hooks.after_error.return_value = (None, None)
        config.__dict__["_hooks"] = mock_hooks

        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with pytest.raises(NoResponseError):
                sdk.do_request(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX", "5XX"],
                )

    def test_error_status_code_after_error_returns_err(self, mock_logger):
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}
        mock_response = _make_httpx_response(400, text="Bad Request")
        config.client.send.return_value = mock_response

        # Mock hooks so after_error returns an error
        replacement_error = RuntimeError("hook error")
        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        mock_hooks.after_error.return_value = (None, replacement_error)
        config.__dict__["_hooks"] = mock_hooks

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.match_status_codes", return_value=True
            ):
                with pytest.raises(RuntimeError, match="hook error"):
                    sdk.do_request(
                        hook_ctx=hook_ctx,
                        request=mock_request,
                        error_status_codes=["4XX"],
                    )

    def test_error_status_code_after_error_returns_result(self, mock_logger):
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}
        error_response = _make_httpx_response(400, text="Bad Request")
        fixed_response = _make_httpx_response(200, json_data={"ok": True})
        config.client.send.return_value = error_response

        # Mock hooks: after_error replaces with a good response
        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        mock_hooks.after_error.return_value = (fixed_response, None)
        mock_hooks.after_success.side_effect = lambda ctx, resp: resp
        config.__dict__["_hooks"] = mock_hooks

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        call_count = [0]
        original_match = None

        def match_side_effect(codes, status):
            call_count[0] += 1
            # First call (inside do()): error_response is 400, match error codes
            if call_count[0] == 1:
                return True
            # Second call (after do()): fixed_response is 200, no match
            return False

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.match_status_codes",
                side_effect=match_side_effect,
            ):
                result = sdk.do_request(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX"],
                )

        assert result is fixed_response

    def test_error_status_code_after_error_returns_neither(self, mock_logger):
        """When after_error returns (None, None) for error status → raise default error."""
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}
        error_response = _make_httpx_response(500, text="Server Error")
        config.client.send.return_value = error_response

        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        mock_hooks.after_error.return_value = (None, None)
        config.__dict__["_hooks"] = mock_hooks

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.match_status_codes", return_value=True
            ):
                with pytest.raises(DefaultSDKError, match="Unexpected error occurred"):
                    sdk.do_request(
                        hook_ctx=hook_ctx,
                        request=mock_request,
                        error_status_codes=["5XX"],
                    )

    def test_after_success_called_on_non_error(self, mock_logger):
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}
        mock_response = _make_httpx_response(200)
        config.client.send.return_value = mock_response

        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        modified_response = _make_httpx_response(200, json_data={"modified": True})
        mock_hooks.after_success.return_value = modified_response
        config.__dict__["_hooks"] = mock_hooks

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.match_status_codes", return_value=False
            ):
                result = sdk.do_request(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX", "5XX"],
                )

        assert result is modified_response
        mock_hooks.after_success.assert_called_once()

    def test_with_retry_config(self, mock_logger):
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}
        mock_response = _make_httpx_response(200)

        retry_cfg = RetryConfig(
            strategy="backoff",
            backoff={
                "initial_interval": 100,
                "max_interval": 1000,
                "exponent": 1.5,
                "max_elapsed_time": 5000,
            },
            retry_connection_errors=False,
        )

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.retry", return_value=mock_response
            ) as mock_retry:
                with patch(
                    "griddy.core.basesdk.utils.match_status_codes", return_value=False
                ):
                    result = sdk.do_request(
                        hook_ctx=hook_ctx,
                        request=mock_request,
                        error_status_codes=["5XX"],
                        retry_config=(retry_cfg, ["500", "502", "503"]),
                    )

        assert result is mock_response
        mock_retry.assert_called_once()

    def test_stream_response_logging(self, mock_logger):
        """Verify stream=True logs '<streaming response>' instead of body."""
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}
        mock_response = _make_httpx_response(200)
        config.client.send.return_value = mock_response

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.match_status_codes", return_value=False
            ):
                sdk.do_request(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX"],
                    stream=True,
                )

        # Verify "<streaming response>" appears in the debug log call
        response_log_call = mock_logger.debug.call_args_list[1]
        assert "<streaming response>" in str(response_log_call)


# ---------------------------------------------------------------------------
# do_request_async
# ---------------------------------------------------------------------------
@pytest.mark.unit
class TestDoRequestAsync:
    """Tests for BaseSDK.do_request_async (async HTTP execution with hooks)."""

    @pytest.mark.asyncio
    async def test_successful_request(self, mock_logger):
        mock_async_client = Mock(spec=httpx.AsyncClient)
        mock_response = _make_httpx_response(200)
        mock_async_client.send = AsyncMock(return_value=mock_response)

        sdk, config, hooks = _make_sdk_with_hooks(
            mock_logger, async_client=mock_async_client
        )
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            result = await sdk.do_request_async(
                hook_ctx=hook_ctx,
                request=mock_request,
                error_status_codes=["4XX", "5XX"],
            )

        assert result is mock_response

    @pytest.mark.asyncio
    async def test_client_none_raises_value_error(self, mock_logger):
        sdk, config, hooks = _make_sdk_with_hooks(mock_logger)
        config.async_client = None
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with pytest.raises(ValueError, match="client is required"):
                await sdk.do_request_async(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX"],
                )

    @pytest.mark.asyncio
    async def test_exception_during_send_propagates(self, mock_logger):
        mock_async_client = Mock(spec=httpx.AsyncClient)
        mock_async_client.send = AsyncMock(
            side_effect=ConnectionError("Connection refused")
        )

        sdk, config, hooks = _make_sdk_with_hooks(
            mock_logger, async_client=mock_async_client
        )
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with pytest.raises(ConnectionError, match="Connection refused"):
                await sdk.do_request_async(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX"],
                )

    @pytest.mark.asyncio
    async def test_no_response_raises_no_response_error(self, mock_logger):
        mock_async_client = Mock(spec=httpx.AsyncClient)
        mock_async_client.send = AsyncMock(side_effect=ConnectionError("fail"))

        sdk, config, hooks = _make_sdk_with_hooks(
            mock_logger, async_client=mock_async_client
        )

        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        mock_hooks.after_error.return_value = (None, None)
        config.__dict__["_hooks"] = mock_hooks

        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with pytest.raises(NoResponseError):
                await sdk.do_request_async(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX"],
                )

    @pytest.mark.asyncio
    async def test_error_status_after_error_returns_err(self, mock_logger):
        mock_async_client = Mock(spec=httpx.AsyncClient)
        error_response = _make_httpx_response(400, text="Bad Request")
        mock_async_client.send = AsyncMock(return_value=error_response)

        sdk, config, hooks = _make_sdk_with_hooks(
            mock_logger, async_client=mock_async_client
        )

        replacement_error = RuntimeError("hook error")
        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        mock_hooks.after_error.return_value = (None, replacement_error)
        config.__dict__["_hooks"] = mock_hooks

        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.match_status_codes", return_value=True
            ):
                with pytest.raises(RuntimeError, match="hook error"):
                    await sdk.do_request_async(
                        hook_ctx=hook_ctx,
                        request=mock_request,
                        error_status_codes=["4XX"],
                    )

    @pytest.mark.asyncio
    async def test_error_status_after_error_returns_result(self, mock_logger):
        mock_async_client = Mock(spec=httpx.AsyncClient)
        error_response = _make_httpx_response(400, text="Bad Request")
        mock_async_client.send = AsyncMock(return_value=error_response)

        sdk, config, hooks = _make_sdk_with_hooks(
            mock_logger, async_client=mock_async_client
        )

        fixed_response = _make_httpx_response(200, json_data={"ok": True})
        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        mock_hooks.after_error.return_value = (fixed_response, None)
        mock_hooks.after_success.side_effect = lambda ctx, resp: resp
        config.__dict__["_hooks"] = mock_hooks

        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        call_count = [0]

        def match_side_effect(codes, status):
            call_count[0] += 1
            return call_count[0] == 1  # True first, False second

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.match_status_codes",
                side_effect=match_side_effect,
            ):
                result = await sdk.do_request_async(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX"],
                )

        assert result is fixed_response

    @pytest.mark.asyncio
    async def test_error_status_after_error_returns_neither(self, mock_logger):
        mock_async_client = Mock(spec=httpx.AsyncClient)
        error_response = _make_httpx_response(500, text="Server Error")
        mock_async_client.send = AsyncMock(return_value=error_response)

        sdk, config, hooks = _make_sdk_with_hooks(
            mock_logger, async_client=mock_async_client
        )

        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        mock_hooks.after_error.return_value = (None, None)
        config.__dict__["_hooks"] = mock_hooks

        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.match_status_codes", return_value=True
            ):
                with pytest.raises(DefaultSDKError, match="Unexpected error occurred"):
                    await sdk.do_request_async(
                        hook_ctx=hook_ctx,
                        request=mock_request,
                        error_status_codes=["5XX"],
                    )

    @pytest.mark.asyncio
    async def test_after_success_called_on_non_error(self, mock_logger):
        mock_async_client = Mock(spec=httpx.AsyncClient)
        mock_response = _make_httpx_response(200)
        mock_async_client.send = AsyncMock(return_value=mock_response)

        sdk, config, hooks = _make_sdk_with_hooks(
            mock_logger, async_client=mock_async_client
        )

        modified_response = _make_httpx_response(200, json_data={"modified": True})
        mock_hooks = Mock()
        mock_hooks.before_request.side_effect = lambda ctx, req: req
        mock_hooks.after_success.return_value = modified_response
        config.__dict__["_hooks"] = mock_hooks

        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.match_status_codes", return_value=False
            ):
                result = await sdk.do_request_async(
                    hook_ctx=hook_ctx,
                    request=mock_request,
                    error_status_codes=["4XX"],
                )

        assert result is modified_response
        mock_hooks.after_success.assert_called_once()

    @pytest.mark.asyncio
    async def test_with_retry_config(self, mock_logger):
        mock_async_client = Mock(spec=httpx.AsyncClient)
        mock_response = _make_httpx_response(200)

        sdk, config, hooks = _make_sdk_with_hooks(
            mock_logger, async_client=mock_async_client
        )
        mock_request = Mock(spec=httpx.Request)
        mock_request.method = "GET"
        mock_request.url = "https://example.com/test"
        mock_request.headers = {}

        retry_cfg = RetryConfig(
            strategy="backoff",
            backoff={
                "initial_interval": 100,
                "max_interval": 1000,
                "exponent": 1.5,
                "max_elapsed_time": 5000,
            },
            retry_connection_errors=False,
        )

        hook_ctx = sdk._create_hook_context("testOp", "https://example.com")

        with patch("griddy.core.basesdk.get_body_content", return_value=""):
            with patch(
                "griddy.core.basesdk.utils.retry_async",
                new_callable=AsyncMock,
                return_value=mock_response,
            ) as mock_retry:
                with patch(
                    "griddy.core.basesdk.utils.match_status_codes", return_value=False
                ):
                    result = await sdk.do_request_async(
                        hook_ctx=hook_ctx,
                        request=mock_request,
                        error_status_codes=["5XX"],
                        retry_config=(retry_cfg, ["500", "502"]),
                    )

        assert result is mock_response
        mock_retry.assert_called_once()


# ---------------------------------------------------------------------------
# _execute_endpoint / _execute_endpoint_async
# ---------------------------------------------------------------------------
@pytest.mark.unit
class TestExecuteEndpoint:
    """Tests for _execute_endpoint (sync) full flow."""

    def test_successful_execution(self, mock_logger):
        sdk, config, _ = _make_sdk_with_hooks(mock_logger)
        mock_response = _make_httpx_response(200, json_data={"result": "ok"})

        endpoint_config = EndpointConfig(
            method="GET",
            path="/test",
            operation_id="testOp",
            request=None,
            response_type=dict,
            error_status_codes=["4XX", "5XX"],
        )

        with (
            patch.object(
                sdk,
                "_build_request",
                return_value=Mock(spec=httpx.Request),
            ),
            patch.object(sdk, "do_request", return_value=mock_response),
            patch.object(
                sdk, "_handle_json_response", return_value={"result": "ok"}
            ) as mock_handle,
        ):
            result = sdk._execute_endpoint(endpoint_config)

        assert result == {"result": "ok"}
        mock_handle.assert_called_once_with(mock_response, dict, ["4XX", "5XX"])

    def test_return_raw_json(self, mock_logger):
        sdk, config, _ = _make_sdk_with_hooks(mock_logger)
        mock_response = _make_httpx_response(200, json_data={"raw": True})

        endpoint_config = EndpointConfig(
            method="GET",
            path="/test",
            operation_id="testOp",
            request=None,
            response_type=dict,
            error_status_codes=["4XX", "5XX"],
            return_raw_json=True,
        )

        with (
            patch.object(
                sdk,
                "_build_request",
                return_value=Mock(spec=httpx.Request),
            ),
            patch.object(sdk, "do_request", return_value=mock_response),
            patch("griddy.core.basesdk.utils.match_response", return_value=True),
        ):
            result = sdk._execute_endpoint(endpoint_config)

        assert result == {"raw": True}
        mock_response.json.assert_called_once()

    def test_return_raw_json_falls_through_on_non_200(self, mock_logger):
        sdk, config, _ = _make_sdk_with_hooks(mock_logger)
        mock_response = _make_httpx_response(201)

        endpoint_config = EndpointConfig(
            method="POST",
            path="/test",
            operation_id="createOp",
            request=None,
            response_type=dict,
            error_status_codes=["4XX"],
            return_raw_json=True,
        )

        with (
            patch.object(
                sdk,
                "_build_request",
                return_value=Mock(spec=httpx.Request),
            ),
            patch.object(sdk, "do_request", return_value=mock_response),
            patch("griddy.core.basesdk.utils.match_response", return_value=False),
            patch.object(
                sdk, "_handle_json_response", return_value={"handled": True}
            ) as mock_handle,
        ):
            result = sdk._execute_endpoint(endpoint_config)

        assert result == {"handled": True}
        mock_handle.assert_called_once()


@pytest.mark.unit
class TestExecuteEndpointAsync:
    """Tests for _execute_endpoint_async (async) full flow."""

    @pytest.mark.asyncio
    async def test_successful_execution(self, mock_logger):
        sdk, config, _ = _make_sdk_with_hooks(mock_logger)
        mock_response = _make_httpx_response(200, json_data={"result": "ok"})

        endpoint_config = EndpointConfig(
            method="GET",
            path="/test",
            operation_id="testOp",
            request=None,
            response_type=dict,
            error_status_codes=["4XX", "5XX"],
        )

        with (
            patch.object(
                sdk,
                "_build_request_async",
                return_value=Mock(spec=httpx.Request),
            ),
            patch.object(
                sdk,
                "do_request_async",
                new_callable=AsyncMock,
                return_value=mock_response,
            ),
            patch.object(
                sdk,
                "_handle_json_response_async",
                new_callable=AsyncMock,
                return_value={"result": "ok"},
            ) as mock_handle,
        ):
            result = await sdk._execute_endpoint_async(endpoint_config)

        assert result == {"result": "ok"}
        mock_handle.assert_called_once_with(mock_response, dict, ["4XX", "5XX"])

    @pytest.mark.asyncio
    async def test_return_raw_json(self, mock_logger):
        sdk, config, _ = _make_sdk_with_hooks(mock_logger)
        mock_response = _make_httpx_response(200, json_data={"raw": True})

        endpoint_config = EndpointConfig(
            method="GET",
            path="/test",
            operation_id="testOp",
            request=None,
            response_type=dict,
            error_status_codes=["4XX", "5XX"],
            return_raw_json=True,
        )

        with (
            patch.object(
                sdk,
                "_build_request_async",
                return_value=Mock(spec=httpx.Request),
            ),
            patch.object(
                sdk,
                "do_request_async",
                new_callable=AsyncMock,
                return_value=mock_response,
            ),
            patch("griddy.core.basesdk.utils.match_response", return_value=True),
        ):
            result = await sdk._execute_endpoint_async(endpoint_config)

        assert result == {"raw": True}
        mock_response.json.assert_called_once()

    @pytest.mark.asyncio
    async def test_return_raw_json_falls_through_on_non_200(self, mock_logger):
        sdk, config, _ = _make_sdk_with_hooks(mock_logger)
        mock_response = _make_httpx_response(201)

        endpoint_config = EndpointConfig(
            method="POST",
            path="/test",
            operation_id="createOp",
            request=None,
            response_type=dict,
            error_status_codes=["4XX"],
            return_raw_json=True,
        )

        with (
            patch.object(
                sdk,
                "_build_request_async",
                return_value=Mock(spec=httpx.Request),
            ),
            patch.object(
                sdk,
                "do_request_async",
                new_callable=AsyncMock,
                return_value=mock_response,
            ),
            patch("griddy.core.basesdk.utils.match_response", return_value=False),
            patch.object(
                sdk,
                "_handle_json_response_async",
                new_callable=AsyncMock,
                return_value={"handled": True},
            ) as mock_handle,
        ):
            result = await sdk._execute_endpoint_async(endpoint_config)

        assert result == {"handled": True}
        mock_handle.assert_called_once()


# ---------------------------------------------------------------------------
# _get_security_from_env with actual security model
# ---------------------------------------------------------------------------
@pytest.mark.unit
class TestGetSecurityFromEnvWithModel:
    def test_delegates_to_get_security_from_env_when_model_set(self, mock_logger):
        """When _security_model_cls is set, delegates to core utility."""

        class FakeSecurity:
            pass

        class SDKWithSecurity(BaseSDK):
            @property
            def _security_model_cls(self):
                return FakeSecurity

            @property
            def _security_env_mapping(self):
                return {"api_key": "MY_API_KEY"}

        config = SDKConfiguration(
            client=None,
            client_supplied=True,
            async_client=None,
            async_client_supplied=True,
            debug_logger=mock_logger,
        )
        sdk = SDKWithSecurity(sdk_config=config)

        sentinel = object()
        with patch(
            "griddy.core.utils.security.get_security_from_env", return_value=sentinel
        ) as mock_fn:
            result = sdk._get_security_from_env(None)

        assert result is sentinel
        mock_fn.assert_called_once_with(None, FakeSecurity, {"api_key": "MY_API_KEY"})
