"""Tests for griddy.pfr.backends module — pluggable scraping backend protocols."""

from unittest.mock import Mock, patch

import httpx
import pytest

from griddy.core.utils.logger import Logger
from griddy.pfr import GriddyPFR
from griddy.pfr.backends import AsyncScrapingBackend, ScrapingBackend
from griddy.pfr.basesdk import BaseSDK, EndpointConfig
from griddy.pfr.sdkconfiguration import SDKConfiguration
from griddy.pfr.utils.browserless import AsyncBrowserless, Browserless

# ---------------------------------------------------------------------------
# Helpers — minimal backend implementations for testing
# ---------------------------------------------------------------------------


class StubSyncBackend:
    """Minimal sync backend satisfying the ScrapingBackend protocol."""

    def __init__(self, html: str = "<html>stub</html>") -> None:
        self.html = html
        self.calls: list[tuple[str, str]] = []

    def get_page_content(self, url: str, wait_for_element: str) -> str:
        self.calls.append((url, wait_for_element))
        return self.html


class StubAsyncBackend:
    """Minimal async backend satisfying the AsyncScrapingBackend protocol."""

    def __init__(self, html: str = "<html>async-stub</html>") -> None:
        self.html = html
        self.calls: list[tuple[str, str]] = []

    async def get_page_content(self, url: str, wait_for_element: str) -> str:
        self.calls.append((url, wait_for_element))
        return self.html


# ---------------------------------------------------------------------------
# Protocol conformance
# ---------------------------------------------------------------------------


@pytest.mark.unit
class TestScrapingBackendProtocol:
    def test_stub_satisfies_sync_protocol(self):
        backend = StubSyncBackend()
        assert isinstance(backend, ScrapingBackend)

    def test_stub_satisfies_async_protocol(self):
        backend = StubAsyncBackend()
        assert isinstance(backend, AsyncScrapingBackend)

    def test_browserless_satisfies_sync_protocol(self):
        assert issubclass(Browserless, ScrapingBackend)

    def test_async_browserless_satisfies_async_protocol(self):
        assert issubclass(AsyncBrowserless, AsyncScrapingBackend)

    def test_lambda_does_not_satisfy_protocol(self):
        """A plain callable is not a valid backend (needs method, not __call__)."""
        fn = lambda url, wait_for_element: "<html/>"
        assert not isinstance(fn, ScrapingBackend)

    def test_mock_satisfies_sync_protocol(self):
        mock = Mock(spec=ScrapingBackend)
        assert isinstance(mock, ScrapingBackend)


# ---------------------------------------------------------------------------
# BaseSDK backend resolution
# ---------------------------------------------------------------------------


@pytest.fixture
def mock_logger():
    return Mock(spec=Logger)


def _make_sdk_config(
    mock_logger,
    scraping_backend=None,
    async_scraping_backend=None,
):
    return SDKConfiguration(
        client=httpx.Client(),
        client_supplied=False,
        async_client=None,
        async_client_supplied=True,
        debug_logger=mock_logger,
        scraping_backend=scraping_backend,
        async_scraping_backend=async_scraping_backend,
    )


@pytest.mark.unit
class TestBaseSDKBackendResolution:
    def test_uses_custom_sync_backend_from_config(self, mock_logger):
        backend = StubSyncBackend()
        config = _make_sdk_config(mock_logger, scraping_backend=backend)
        sdk = BaseSDK(sdk_config=config)
        assert sdk.browserless is backend

    def test_uses_custom_async_backend_from_config(self, mock_logger):
        backend = StubAsyncBackend()
        config = _make_sdk_config(mock_logger, async_scraping_backend=backend)
        sdk = BaseSDK(sdk_config=config)
        assert sdk.async_browserless is backend

    def test_falls_back_to_browserless_when_no_custom_backend(self, mock_logger):
        config = _make_sdk_config(mock_logger)
        sdk = BaseSDK(sdk_config=config)
        assert isinstance(sdk.browserless, Browserless)
        assert isinstance(sdk.async_browserless, AsyncBrowserless)

    def test_custom_backend_used_in_execute_endpoint(self, mock_logger):
        html = '<html><body><table id="t"><tr><td>x</td></tr></table></body></html>'
        backend = StubSyncBackend(html=html)
        config = _make_sdk_config(mock_logger, scraping_backend=backend)
        sdk = BaseSDK(sdk_config=config)

        mock_response_type = Mock()
        mock_response_type.model_validate = lambda d: d

        ep_config = EndpointConfig(
            path_template="/test.htm",
            operation_id="test_op",
            wait_for_element="table#t",
            parser=lambda html: {"ok": True},
            response_type=mock_response_type,
        )

        result = sdk._execute_endpoint(ep_config)
        assert result == {"ok": True}
        assert len(backend.calls) == 1
        assert backend.calls[0][1] == "table#t"

    @pytest.mark.asyncio
    async def test_custom_async_backend_used_in_execute_endpoint_async(
        self, mock_logger
    ):
        html = '<html><body><table id="t"><tr><td>x</td></tr></table></body></html>'
        async_backend = StubAsyncBackend(html=html)
        # Still need a sync backend to avoid Browserless env var requirement
        sync_backend = StubSyncBackend()
        config = _make_sdk_config(
            mock_logger,
            scraping_backend=sync_backend,
            async_scraping_backend=async_backend,
        )
        sdk = BaseSDK(sdk_config=config)

        mock_response_type = Mock()
        mock_response_type.model_validate = lambda d: d

        ep_config = EndpointConfig(
            path_template="/test.htm",
            operation_id="test_op",
            wait_for_element="table#t",
            parser=lambda html: {"ok": True},
            response_type=mock_response_type,
        )

        result = await sdk._execute_endpoint_async(ep_config)
        assert result == {"ok": True}
        assert len(async_backend.calls) == 1


# ---------------------------------------------------------------------------
# GriddyPFR integration
# ---------------------------------------------------------------------------


@pytest.mark.unit
class TestGriddyPFRWithCustomBackend:
    def test_accepts_scraping_backend(self):
        backend = StubSyncBackend()
        pfr = GriddyPFR(scraping_backend=backend)
        assert pfr.browserless is backend

    def test_accepts_async_scraping_backend(self):
        backend = StubAsyncBackend()
        pfr = GriddyPFR(async_scraping_backend=backend)
        assert pfr.async_browserless is backend

    def test_accepts_both_backends(self):
        sync_be = StubSyncBackend()
        async_be = StubAsyncBackend()
        pfr = GriddyPFR(scraping_backend=sync_be, async_scraping_backend=async_be)
        assert pfr.browserless is sync_be
        assert pfr.async_browserless is async_be

    def test_backend_propagates_to_sub_sdk(self):
        sync_be = StubSyncBackend()
        async_be = StubAsyncBackend()
        pfr = GriddyPFR(scraping_backend=sync_be, async_scraping_backend=async_be)
        # Access a sub-SDK — it should inherit the backend from SDKConfiguration
        schedule = pfr.schedule
        assert schedule.browserless is sync_be
        assert schedule.async_browserless is async_be

    def test_default_browserless_when_no_backend(self):
        pfr = GriddyPFR()
        assert isinstance(pfr.browserless, Browserless)
        assert isinstance(pfr.async_browserless, AsyncBrowserless)

    def test_sub_sdk_endpoint_uses_custom_backend(self):
        html = '<html><body><table id="games"></table></body></html>'
        backend = StubSyncBackend(html=html)
        pfr = GriddyPFR(scraping_backend=backend)

        # Mock the parser to avoid needing real HTML structure
        with patch.object(pfr.schedule, "_parse_and_validate", return_value=[]):
            pfr.schedule.get_season_schedule(season=2024)

        assert len(backend.calls) == 1
        assert "2024" in backend.calls[0][0]

    def test_browserless_config_ignored_when_backend_provided(self):
        from griddy.pfr.utils.browserless import BrowserlessConfig

        backend = StubSyncBackend()
        custom_config = BrowserlessConfig(proxy="custom", ttl=99)
        pfr = GriddyPFR(scraping_backend=backend, browserless_config=custom_config)
        # Custom backend takes priority — browserless_config is ignored
        assert pfr.browserless is backend
        assert not isinstance(pfr.browserless, Browserless)
