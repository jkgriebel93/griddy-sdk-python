"""Tests for griddy.core.base_griddy_sdk module."""

import warnings
from typing import Any

import httpx
import pytest

from griddy.core._lazy_load import LazySubSDKMixin
from griddy.core.base_griddy_sdk import BaseGriddySDK
from griddy.core.basesdk import BaseSDK as CoreBaseSDK
from griddy.core.hooks.sdkhooks import SDKHooks
from griddy.core.sdkconfiguration import SDKConfiguration


class ConcreteTestSDK(LazySubSDKMixin, BaseGriddySDK, CoreBaseSDK):
    """Minimal concrete implementation for testing BaseGriddySDK."""

    _sub_sdk_map = {}

    def _get_debug_logger_env_var(self) -> str:
        return "TEST_DEBUG"

    def _create_security(self, auth: Any) -> Any:
        return None

    def _create_sdk_configuration(self, **kwargs: Any) -> Any:
        return SDKConfiguration(**kwargs)

    def _create_hooks(self) -> Any:
        return SDKHooks()

    def __init__(self, **kwargs: Any) -> None:
        self._init_sdk(auth=None, **kwargs)


@pytest.mark.unit
class TestClientCreationAndValidation:
    def test_creates_default_clients(self):
        sdk = ConcreteTestSDK()
        assert sdk.sdk_configuration.client is not None
        assert sdk.sdk_configuration.async_client is not None
        assert sdk.sdk_configuration.client_supplied is False
        assert sdk.sdk_configuration.async_client_supplied is False

    def test_accepts_supplied_sync_client(self):
        client = httpx.Client()
        sdk = ConcreteTestSDK(client=client)
        assert sdk.sdk_configuration.client is client
        assert sdk.sdk_configuration.client_supplied is True

    def test_accepts_supplied_async_client(self):
        async_client = httpx.AsyncClient()
        sdk = ConcreteTestSDK(async_client=async_client)
        assert sdk.sdk_configuration.async_client is async_client
        assert sdk.sdk_configuration.async_client_supplied is True

    def test_rejects_invalid_sync_client(self):
        with pytest.raises(TypeError, match="HttpClient"):
            ConcreteTestSDK(client=object())

    def test_rejects_invalid_async_client(self):
        with pytest.raises(TypeError, match="AsyncHttpClient"):
            ConcreteTestSDK(async_client=object())


@pytest.mark.unit
class TestSyncContextManager:
    def test_returns_self_on_enter(self):
        with ConcreteTestSDK() as sdk:
            assert isinstance(sdk, ConcreteTestSDK)

    def test_clients_cleared_on_exit(self):
        with ConcreteTestSDK() as sdk:
            assert sdk.sdk_configuration.client is not None
        assert sdk.sdk_configuration.client is None
        assert sdk.sdk_configuration.async_client is None

    def test_does_not_close_supplied_sync_client(self):
        client = httpx.Client()
        with ConcreteTestSDK(client=client) as sdk:
            pass
        # ref cleared but client not closed
        assert sdk.sdk_configuration.client is None
        assert not client.is_closed


@pytest.mark.unit
class TestAsyncContextManager:
    @pytest.mark.asyncio
    async def test_returns_self_on_aenter(self):
        async with ConcreteTestSDK() as sdk:
            assert isinstance(sdk, ConcreteTestSDK)

    @pytest.mark.asyncio
    async def test_clients_cleared_on_aexit(self):
        async with ConcreteTestSDK() as sdk:
            assert sdk.sdk_configuration.async_client is not None
        assert sdk.sdk_configuration.async_client is None
        assert sdk.sdk_configuration.client is None

    @pytest.mark.asyncio
    async def test_does_not_close_supplied_async_client(self):
        async_client = httpx.AsyncClient()
        async with ConcreteTestSDK(async_client=async_client) as sdk:
            pass
        assert sdk.sdk_configuration.async_client is None
        assert not async_client.is_closed
        await async_client.aclose()


@pytest.mark.unit
class TestCloseIdempotency:
    def test_close_idempotent(self):
        sdk = ConcreteTestSDK()
        sdk.close()
        sdk.close()  # Should not raise

    @pytest.mark.asyncio
    async def test_aclose_idempotent(self):
        sdk = ConcreteTestSDK()
        await sdk.aclose()
        await sdk.aclose()  # Should not raise


@pytest.mark.unit
class TestResourceWarning:
    def test_warns_when_unclosed_with_owned_clients(self):
        sdk = ConcreteTestSDK()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            sdk.__del__()
            our_warnings = [
                x
                for x in w
                if issubclass(x.category, ResourceWarning)
                and "Unclosed ConcreteTestSDK" in str(x.message)
            ]
            assert len(our_warnings) == 1

    def test_no_warning_after_close(self):
        sdk = ConcreteTestSDK()
        sdk.close()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            sdk.__del__()
            assert len(w) == 0

    @pytest.mark.asyncio
    async def test_no_warning_after_aclose(self):
        sdk = ConcreteTestSDK()
        await sdk.aclose()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            sdk.__del__()
            assert len(w) == 0

    def test_no_warning_for_supplied_clients(self):
        client = httpx.Client()
        async_client = httpx.AsyncClient()
        sdk = ConcreteTestSDK(client=client, async_client=async_client)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            sdk.__del__()
            assert len(w) == 0

    def test_no_warning_when_init_failed(self):
        """__del__ should not crash if __init__ never completed."""
        sdk = ConcreteTestSDK.__new__(ConcreteTestSDK)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            sdk.__del__()
            assert len(w) == 0


@pytest.mark.unit
class TestServerUrlTemplating:
    def test_server_url_with_params(self):
        sdk = ConcreteTestSDK(
            server_url="https://{region}.example.com",
            url_params={"region": "us-east"},
        )
        assert sdk.sdk_configuration.server_url == "https://us-east.example.com"

    def test_server_url_without_params(self):
        sdk = ConcreteTestSDK(server_url="https://custom.example.com")
        assert sdk.sdk_configuration.server_url == "https://custom.example.com"

    def test_no_server_url(self):
        sdk = ConcreteTestSDK()
        assert sdk.sdk_configuration.server_url is None


@pytest.mark.unit
class TestHooksInitialization:
    def test_hooks_registered(self):
        sdk = ConcreteTestSDK()
        hooks = sdk.sdk_configuration.hooks
        assert isinstance(hooks, SDKHooks)
