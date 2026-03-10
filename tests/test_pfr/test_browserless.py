"""Tests for griddy.pfr.utils.browserless module."""

import sys
from unittest.mock import MagicMock, Mock, patch

import httpx
import pytest

from griddy.pfr.utils.browserless import (
    Browserless,
    BrowserlessConfig,
    BrowserlessError,
)

# Playwright is an optional dependency; import its error type only when available.
try:
    from playwright.sync_api import Error as PlaywrightError
except ImportError:  # pragma: no cover
    PlaywrightError = None  # type: ignore[assignment,misc]

_SETTINGS = "griddy.pfr.utils.browserless"


@pytest.fixture
def browserless():
    return Browserless()


@pytest.fixture
def browserless_custom_config():
    return Browserless(config=BrowserlessConfig(default_timeout_ms=30000))


@pytest.mark.unit
class TestBrowserlessConfig:
    def test_defaults(self):
        config = BrowserlessConfig()
        assert config.proxy == "residential"
        assert config.request_timeout == 60_000
        assert config.ttl == 30_000
        assert config.default_timeout_ms == 60_000

    def test_custom_values(self):
        config = BrowserlessConfig(
            proxy="datacenter",
            request_timeout=90_000,
            ttl=15_000,
            default_timeout_ms=45_000,
        )
        assert config.proxy == "datacenter"
        assert config.request_timeout == 90_000
        assert config.ttl == 15_000
        assert config.default_timeout_ms == 45_000


@pytest.mark.unit
class TestBrowserlessInit:
    def test_default_timeout(self, browserless):
        assert browserless.timeout == 60000

    def test_custom_timeout(self, browserless_custom_config):
        assert browserless_custom_config.timeout == 30000

    def test_data_initially_none(self, browserless):
        assert browserless.data is None

    def test_stores_host_and_token(self, browserless):
        assert browserless.host == "fake-host.example.com"
        assert browserless.token == "fake-token"

    def test_stores_config(self, browserless):
        assert isinstance(browserless.config, BrowserlessConfig)

    def test_uses_default_config_when_none(self, browserless):
        assert browserless.config.proxy == "residential"
        assert browserless.config.request_timeout == 60_000
        assert browserless.config.ttl == 30_000

    def test_raises_when_host_missing(self):
        with patch(f"{_SETTINGS}.BROWSERLESS_HOST", None):
            with pytest.raises(BrowserlessError, match="BROWSERLESS_HOST"):
                Browserless()

    def test_raises_when_token_missing(self):
        with patch(f"{_SETTINGS}.BROWSERLESS_TOKEN", None):
            with pytest.raises(BrowserlessError, match="BROWSERLESS_TOKEN"):
                Browserless()


@pytest.mark.unit
class TestFetchData:
    def test_returns_json_on_success(self, browserless):
        mock_resp = Mock()
        mock_resp.json.return_value = {
            "browserWSEndpoint": "ws://localhost:3000",
            "cookies": [{"name": "a", "value": "b"}],
        }

        with patch(
            "griddy.pfr.utils.browserless.httpx.post", return_value=mock_resp
        ) as mock_post:
            result = browserless.fetch_data("https://example.com/page")

        mock_post.assert_called_once()
        call_kwargs = mock_post.call_args
        assert call_kwargs[1]["json"]["url"] == "https://example.com/page"
        assert call_kwargs[1]["json"]["browserWSEndpoint"] is True
        assert call_kwargs[1]["params"]["proxy"] == "residential"
        assert result["browserWSEndpoint"] == "ws://localhost:3000"

    def test_uses_instance_host_and_token(self, browserless):
        mock_resp = Mock()
        mock_resp.json.return_value = {}

        with patch(
            "griddy.pfr.utils.browserless.httpx.post", return_value=mock_resp
        ) as mock_post:
            browserless.fetch_data("https://example.com")

        call_kwargs = mock_post.call_args
        assert "fake-host.example.com" in call_kwargs[0][0]
        assert call_kwargs[1]["params"]["token"] == "fake-token"

    def test_uses_config_values_in_request(self):
        config = BrowserlessConfig(
            proxy="datacenter", request_timeout=90_000, ttl=15_000
        )
        b = Browserless(config=config)
        mock_resp = Mock()
        mock_resp.json.return_value = {}

        with patch(
            "griddy.pfr.utils.browserless.httpx.post", return_value=mock_resp
        ) as mock_post:
            b.fetch_data("https://example.com")

        call_kwargs = mock_post.call_args
        assert call_kwargs[1]["params"]["proxy"] == "datacenter"
        assert call_kwargs[1]["params"]["timeout"] == 90_000
        assert call_kwargs[1]["json"]["ttl"] == 15_000

    def test_calls_raise_for_status(self, browserless):
        mock_resp = Mock()
        mock_resp.json.return_value = {}

        with patch("griddy.pfr.utils.browserless.httpx.post", return_value=mock_resp):
            browserless.fetch_data("https://example.com")

        mock_resp.raise_for_status.assert_called_once()

    def test_raises_browserless_error_on_request_exception(self, browserless):
        with patch(
            "griddy.pfr.utils.browserless.httpx.post",
            side_effect=httpx.HTTPError("connection refused"),
        ):
            with pytest.raises(BrowserlessError, match="request failed"):
                browserless.fetch_data("https://example.com")

    def test_raises_browserless_error_on_http_error(self, browserless):
        mock_resp = Mock()
        mock_resp.raise_for_status.side_effect = httpx.HTTPStatusError(
            "503 Server Error",
            request=httpx.Request("POST", "https://example.com"),
            response=httpx.Response(503),
        )

        with patch("griddy.pfr.utils.browserless.httpx.post", return_value=mock_resp):
            with pytest.raises(BrowserlessError, match="request failed"):
                browserless.fetch_data("https://example.com")


@pytest.mark.unit
class TestHandlePageNavigation:
    def _make_page(self, url: str, content: str = "<html></html>"):
        page = MagicMock()
        page.url = url
        page.content.return_value = content
        return page

    def _make_browser(self, pages=None):
        browser = MagicMock()
        if pages is not None:
            ctx = MagicMock()
            ctx.pages = pages
            browser.contexts = [ctx]
        else:
            browser.contexts = []
        return browser

    def test_finds_existing_page_by_url(self, browserless):
        page = self._make_page("https://example.com/games", "<table>data</table>")
        browser = self._make_browser(pages=[page])

        result = browserless._handle_page_navigation(
            browser, "https://example.com/games", cookies={}, element="#games"
        )

        assert result == "<table>data</table>"
        page.locator.assert_called_once_with("#games")
        page.locator("#games").wait_for.assert_called_once_with(
            timeout=browserless.timeout
        )
        # Should not create a new context since the page was found.
        browser.new_context.assert_not_called()

    def test_creates_new_page_when_not_found(self, browserless):
        browser = self._make_browser(pages=[])
        new_page = self._make_page("https://example.com/games", "<html>new</html>")
        new_context = MagicMock()
        new_context.new_page.return_value = new_page
        browser.new_context.return_value = new_context

        result = browserless._handle_page_navigation(
            browser, "https://example.com/games", cookies={}, element="#tbl"
        )

        assert result == "<html>new</html>"
        browser.new_context.assert_called_once()
        new_context.new_page.assert_called_once()
        new_page.goto.assert_called_once_with(
            "https://example.com/games",
            wait_until="domcontentloaded",
            timeout=browserless.timeout,
        )

    def test_creates_new_page_when_no_contexts(self, browserless):
        browser = self._make_browser()  # empty contexts
        new_page = self._make_page("https://example.com", "<html/>")
        new_context = MagicMock()
        new_context.new_page.return_value = new_page
        browser.new_context.return_value = new_context

        browserless._handle_page_navigation(
            browser, "https://example.com", cookies={}, element="#el"
        )

        browser.new_context.assert_called_once()

    def test_adds_cookies_when_present(self, browserless):
        browser = self._make_browser(pages=[])
        new_page = self._make_page("https://example.com", "<html/>")
        new_context = MagicMock()
        new_context.new_page.return_value = new_page
        browser.new_context.return_value = new_context
        cookies = [{"name": "sid", "value": "abc123"}]

        browserless._handle_page_navigation(
            browser, "https://example.com", cookies=cookies, element="#el"
        )

        new_context.add_cookies.assert_called_once_with(cookies)

    def test_skips_cookies_when_empty(self, browserless):
        browser = self._make_browser(pages=[])
        new_page = self._make_page("https://example.com", "<html/>")
        new_context = MagicMock()
        new_context.new_page.return_value = new_page
        browser.new_context.return_value = new_context

        browserless._handle_page_navigation(
            browser, "https://example.com", cookies={}, element="#el"
        )

        new_context.add_cookies.assert_not_called()

    def test_uses_custom_timeout(self, browserless_custom_config):
        page = self._make_page("https://example.com/page", "<html/>")
        browser = self._make_browser(pages=[page])

        browserless_custom_config._handle_page_navigation(
            browser, "https://example.com/page", cookies={}, element="#tbl"
        )

        page.locator("#tbl").wait_for.assert_called_once_with(timeout=30000)

    def test_finds_page_across_multiple_contexts(self, browserless):
        wrong_page = self._make_page("https://other.com/page")
        right_page = self._make_page("https://example.com/games", "<table/>")

        ctx1 = MagicMock()
        ctx1.pages = [wrong_page]
        ctx2 = MagicMock()
        ctx2.pages = [right_page]

        browser = MagicMock()
        browser.contexts = [ctx1, ctx2]

        result = browserless._handle_page_navigation(
            browser, "https://example.com/games", cookies={}, element="#games"
        )

        assert result == "<table/>"
        browser.new_context.assert_not_called()


@pytest.mark.unit
class TestGetPageContent:
    def test_orchestrates_fetch_navigate_and_close(self, browserless):
        mock_browser = MagicMock()
        mock_pw = MagicMock()
        mock_pw.chromium.connect_over_cdp.return_value = mock_browser
        mock_sp = MagicMock()
        mock_sp.return_value.__enter__ = Mock(return_value=mock_pw)
        mock_sp.return_value.__exit__ = Mock(return_value=False)
        mock_error = type("PlaywrightError", (Exception,), {})

        with (
            patch.object(
                browserless,
                "fetch_data",
                return_value={
                    "browserWSEndpoint": "ws://host:3000/devtools",
                    "cookies": [{"name": "c", "value": "v"}],
                },
            ),
            patch(
                f"{_SETTINGS}._import_sync_playwright",
                return_value=(mock_sp, mock_error),
            ),
            patch.object(
                browserless,
                "_handle_page_navigation",
                return_value="<html>content</html>",
            ) as mock_nav,
        ):
            result = browserless.get_page_content(
                "https://pfr.com/page", wait_for_element="#tbl"
            )

        assert result == "<html>content</html>"
        mock_pw.chromium.connect_over_cdp.assert_called_once_with(
            "ws://host:3000/devtools"
        )
        mock_nav.assert_called_once_with(
            browser=mock_browser,
            url="https://pfr.com/page",
            cookies=[{"name": "c", "value": "v"}],
            element="#tbl",
        )
        mock_browser.close.assert_called_once()

    def test_defaults_cookies_to_empty_list(self, browserless):
        mock_browser = MagicMock()
        mock_pw = MagicMock()
        mock_pw.chromium.connect_over_cdp.return_value = mock_browser
        mock_sp = MagicMock()
        mock_sp.return_value.__enter__ = Mock(return_value=mock_pw)
        mock_sp.return_value.__exit__ = Mock(return_value=False)
        mock_error = type("PlaywrightError", (Exception,), {})

        with (
            patch.object(
                browserless,
                "fetch_data",
                return_value={"browserWSEndpoint": "ws://host"},
            ),
            patch(
                f"{_SETTINGS}._import_sync_playwright",
                return_value=(mock_sp, mock_error),
            ),
            patch.object(
                browserless,
                "_handle_page_navigation",
                return_value="<html/>",
            ) as mock_nav,
        ):
            browserless.get_page_content("https://pfr.com", wait_for_element="#el")

        assert mock_nav.call_args[1]["cookies"] == []

    @pytest.mark.parametrize(
        "exc",
        [
            pytest.param(
                PlaywrightError("CDP refused") if PlaywrightError else None,
                id="playwright_error",
                marks=pytest.mark.skipif(
                    PlaywrightError is None, reason="playwright not installed"
                ),
            ),
            pytest.param(ConnectionError("connection reset"), id="connection_error"),
            pytest.param(httpx.HTTPError("transport error"), id="httpx_error"),
        ],
    )
    def test_raises_browserless_error_on_cdp_failure(self, browserless, exc):
        mock_pw = MagicMock()
        mock_pw.chromium.connect_over_cdp.side_effect = exc
        mock_sp = MagicMock()
        mock_sp.return_value.__enter__ = Mock(return_value=mock_pw)
        mock_sp.return_value.__exit__ = Mock(return_value=False)
        pw_error = type(exc) if PlaywrightError is None else PlaywrightError

        with (
            patch.object(
                browserless,
                "fetch_data",
                return_value={"browserWSEndpoint": "ws://host"},
            ),
            patch(
                f"{_SETTINGS}._import_sync_playwright",
                return_value=(mock_sp, pw_error),
            ),
        ):
            with pytest.raises(BrowserlessError, match="Failed to connect Playwright"):
                browserless.get_page_content("https://pfr.com", wait_for_element="#el")

    def test_does_not_catch_unrelated_exceptions(self, browserless):
        mock_pw = MagicMock()
        mock_pw.chromium.connect_over_cdp.side_effect = RuntimeError("unexpected")
        mock_sp = MagicMock()
        mock_sp.return_value.__enter__ = Mock(return_value=mock_pw)
        mock_sp.return_value.__exit__ = Mock(return_value=False)
        mock_error = type("PlaywrightError", (Exception,), {})

        with (
            patch.object(
                browserless,
                "fetch_data",
                return_value={"browserWSEndpoint": "ws://host"},
            ),
            patch(
                f"{_SETTINGS}._import_sync_playwright",
                return_value=(mock_sp, mock_error),
            ),
        ):
            with pytest.raises(RuntimeError, match="unexpected"):
                browserless.get_page_content("https://pfr.com", wait_for_element="#el")

    def test_raises_import_error_when_playwright_missing(self, browserless):
        with (
            patch.object(
                browserless,
                "fetch_data",
                return_value={"browserWSEndpoint": "ws://host"},
            ),
            patch(
                f"{_SETTINGS}._import_sync_playwright",
                side_effect=ImportError("pip install griddy[browser-auth]"),
            ),
        ):
            with pytest.raises(ImportError, match="browser-auth"):
                browserless.get_page_content("https://pfr.com", wait_for_element="#el")


@pytest.mark.unit
class TestImportHelpers:
    def test_import_sync_playwright_raises_when_missing(self):
        from griddy.pfr.utils.browserless import _import_sync_playwright

        with patch.dict(sys.modules, {"playwright": None, "playwright.sync_api": None}):
            with pytest.raises(ImportError, match="browser-auth"):
                _import_sync_playwright()

    def test_import_async_playwright_raises_when_missing(self):
        from griddy.pfr.utils.browserless import _import_async_playwright

        with patch.dict(
            sys.modules, {"playwright": None, "playwright.async_api": None}
        ):
            with pytest.raises(ImportError, match="browser-auth"):
                _import_async_playwright()
