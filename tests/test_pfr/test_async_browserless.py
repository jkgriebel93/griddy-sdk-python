"""Tests for griddy.pfr.utils.browserless.AsyncBrowserless."""

from unittest.mock import AsyncMock, MagicMock, Mock, patch

import httpx
import pytest
from playwright.async_api import Error as AsyncPlaywrightError

from griddy.pfr.utils.browserless import AsyncBrowserless, BrowserlessError

_SETTINGS = "griddy.pfr.utils.browserless"


@pytest.fixture
def async_browserless():
    return AsyncBrowserless()


@pytest.fixture
def async_browserless_custom_timeout():
    return AsyncBrowserless(default_timeout_ms=30000)


@pytest.mark.unit
class TestAsyncBrowserlessInit:
    def test_default_timeout(self, async_browserless):
        assert async_browserless.timeout == 60000

    def test_custom_timeout(self, async_browserless_custom_timeout):
        assert async_browserless_custom_timeout.timeout == 30000

    def test_data_initially_none(self, async_browserless):
        assert async_browserless.data is None

    def test_stores_host_and_token(self, async_browserless):
        assert async_browserless.host == "fake-host.example.com"
        assert async_browserless.token == "fake-token"

    def test_raises_when_host_missing(self):
        with patch(f"{_SETTINGS}.BROWSERLESS_HOST", None):
            with pytest.raises(BrowserlessError, match="BROWSERLESS_HOST"):
                AsyncBrowserless()

    def test_raises_when_token_missing(self):
        with patch(f"{_SETTINGS}.BROWSERLESS_TOKEN", None):
            with pytest.raises(BrowserlessError, match="BROWSERLESS_TOKEN"):
                AsyncBrowserless()


@pytest.mark.unit
class TestAsyncFetchData:
    @pytest.mark.asyncio
    async def test_returns_json_on_success(self, async_browserless):
        mock_resp = Mock()
        mock_resp.json.return_value = {
            "browserWSEndpoint": "ws://localhost:3000",
            "cookies": [{"name": "a", "value": "b"}],
        }

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_resp
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch(
            "griddy.pfr.utils.browserless.httpx.AsyncClient",
            return_value=mock_client,
        ):
            result = await async_browserless.fetch_data("https://example.com/page")

        mock_client.post.assert_awaited_once()
        call_kwargs = mock_client.post.call_args
        assert call_kwargs[1]["json"]["url"] == "https://example.com/page"
        assert call_kwargs[1]["json"]["browserWSEndpoint"] is True
        assert call_kwargs[1]["params"]["proxy"] == "residential"
        assert result["browserWSEndpoint"] == "ws://localhost:3000"

    @pytest.mark.asyncio
    async def test_uses_instance_host_and_token(self, async_browserless):
        mock_resp = Mock()
        mock_resp.json.return_value = {}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_resp
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch(
            "griddy.pfr.utils.browserless.httpx.AsyncClient",
            return_value=mock_client,
        ):
            await async_browserless.fetch_data("https://example.com")

        call_kwargs = mock_client.post.call_args
        assert "fake-host.example.com" in call_kwargs[0][0]
        assert call_kwargs[1]["params"]["token"] == "fake-token"

    @pytest.mark.asyncio
    async def test_calls_raise_for_status(self, async_browserless):
        mock_resp = Mock()
        mock_resp.json.return_value = {}

        mock_client = AsyncMock()
        mock_client.post.return_value = mock_resp
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch(
            "griddy.pfr.utils.browserless.httpx.AsyncClient",
            return_value=mock_client,
        ):
            await async_browserless.fetch_data("https://example.com")

        mock_resp.raise_for_status.assert_called_once()

    @pytest.mark.asyncio
    async def test_raises_browserless_error_on_request_exception(
        self, async_browserless
    ):
        mock_client = AsyncMock()
        mock_client.post.side_effect = httpx.HTTPError("connection refused")
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)

        with patch(
            "griddy.pfr.utils.browserless.httpx.AsyncClient",
            return_value=mock_client,
        ):
            with pytest.raises(BrowserlessError, match="request failed"):
                await async_browserless.fetch_data("https://example.com")


@pytest.mark.unit
class TestAsyncHandlePageNavigation:
    def _make_page(self, url: str, content: str = "<html></html>"):
        page = MagicMock()
        page.url = url
        page.content = AsyncMock(return_value=content)
        page.goto = AsyncMock()
        page.locator.return_value.wait_for = AsyncMock()
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

    @pytest.mark.asyncio
    async def test_finds_existing_page_by_url(self, async_browserless):
        page = self._make_page("https://example.com/games", "<table>data</table>")
        browser = self._make_browser(pages=[page])

        result = await async_browserless._handle_page_navigation(
            browser, "https://example.com/games", cookies={}, element="#games"
        )

        assert result == "<table>data</table>"
        page.locator.assert_called_once_with("#games")
        page.locator("#games").wait_for.assert_awaited_once_with(
            timeout=async_browserless.timeout
        )
        browser.new_context.assert_not_called()

    @pytest.mark.asyncio
    async def test_creates_new_page_when_not_found(self, async_browserless):
        browser = self._make_browser(pages=[])
        new_page = self._make_page("https://example.com/games", "<html>new</html>")
        new_context = AsyncMock()
        new_context.new_page.return_value = new_page
        browser.new_context = AsyncMock(return_value=new_context)

        result = await async_browserless._handle_page_navigation(
            browser, "https://example.com/games", cookies={}, element="#tbl"
        )

        assert result == "<html>new</html>"
        browser.new_context.assert_awaited_once()
        new_context.new_page.assert_awaited_once()
        new_page.goto.assert_awaited_once_with(
            "https://example.com/games",
            wait_until="domcontentloaded",
            timeout=async_browserless.timeout,
        )

    @pytest.mark.asyncio
    async def test_adds_cookies_when_present(self, async_browserless):
        browser = self._make_browser(pages=[])
        new_page = self._make_page("https://example.com", "<html/>")
        new_context = AsyncMock()
        new_context.new_page.return_value = new_page
        browser.new_context = AsyncMock(return_value=new_context)
        cookies = [{"name": "sid", "value": "abc123"}]

        await async_browserless._handle_page_navigation(
            browser, "https://example.com", cookies=cookies, element="#el"
        )

        new_context.add_cookies.assert_awaited_once_with(cookies)

    @pytest.mark.asyncio
    async def test_skips_cookies_when_empty(self, async_browserless):
        browser = self._make_browser(pages=[])
        new_page = self._make_page("https://example.com", "<html/>")
        new_context = AsyncMock()
        new_context.new_page.return_value = new_page
        browser.new_context = AsyncMock(return_value=new_context)

        await async_browserless._handle_page_navigation(
            browser, "https://example.com", cookies={}, element="#el"
        )

        new_context.add_cookies.assert_not_awaited()


@pytest.mark.unit
class TestAsyncGetPageContent:
    @pytest.mark.asyncio
    async def test_orchestrates_fetch_navigate_and_close(self, async_browserless):
        mock_browser = AsyncMock()
        mock_pw = AsyncMock()
        mock_pw.chromium.connect_over_cdp.return_value = mock_browser

        with (
            patch.object(
                async_browserless,
                "fetch_data",
                new_callable=AsyncMock,
                return_value={
                    "browserWSEndpoint": "ws://host:3000/devtools",
                    "cookies": [{"name": "c", "value": "v"}],
                },
            ),
            patch("griddy.pfr.utils.browserless.async_playwright") as mock_ap,
            patch.object(
                async_browserless,
                "_handle_page_navigation",
                new_callable=AsyncMock,
                return_value="<html>content</html>",
            ) as mock_nav,
        ):
            mock_ap.return_value.__aenter__ = AsyncMock(return_value=mock_pw)
            mock_ap.return_value.__aexit__ = AsyncMock(return_value=False)

            result = await async_browserless.get_page_content(
                "https://pfr.com/page", wait_for_element="#tbl"
            )

        assert result == "<html>content</html>"
        mock_pw.chromium.connect_over_cdp.assert_awaited_once_with(
            "ws://host:3000/devtools"
        )
        mock_nav.assert_awaited_once_with(
            browser=mock_browser,
            url="https://pfr.com/page",
            cookies=[{"name": "c", "value": "v"}],
            element="#tbl",
        )
        mock_browser.close.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_defaults_cookies_to_empty_list(self, async_browserless):
        mock_browser = AsyncMock()
        mock_pw = AsyncMock()
        mock_pw.chromium.connect_over_cdp.return_value = mock_browser

        with (
            patch.object(
                async_browserless,
                "fetch_data",
                new_callable=AsyncMock,
                return_value={"browserWSEndpoint": "ws://host"},
            ),
            patch("griddy.pfr.utils.browserless.async_playwright") as mock_ap,
            patch.object(
                async_browserless,
                "_handle_page_navigation",
                new_callable=AsyncMock,
                return_value="<html/>",
            ) as mock_nav,
        ):
            mock_ap.return_value.__aenter__ = AsyncMock(return_value=mock_pw)
            mock_ap.return_value.__aexit__ = AsyncMock(return_value=False)

            await async_browserless.get_page_content(
                "https://pfr.com", wait_for_element="#el"
            )

        assert mock_nav.call_args[1]["cookies"] == []

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "exc",
        [
            AsyncPlaywrightError("CDP refused"),
            ConnectionError("connection reset"),
            httpx.HTTPError("transport error"),
        ],
        ids=["playwright_error", "connection_error", "httpx_error"],
    )
    async def test_raises_browserless_error_on_cdp_failure(
        self, async_browserless, exc
    ):
        mock_pw = AsyncMock()
        mock_pw.chromium.connect_over_cdp.side_effect = exc

        with (
            patch.object(
                async_browserless,
                "fetch_data",
                new_callable=AsyncMock,
                return_value={"browserWSEndpoint": "ws://host"},
            ),
            patch("griddy.pfr.utils.browserless.async_playwright") as mock_ap,
        ):
            mock_ap.return_value.__aenter__ = AsyncMock(return_value=mock_pw)
            mock_ap.return_value.__aexit__ = AsyncMock(return_value=False)

            with pytest.raises(BrowserlessError, match="Failed to connect Playwright"):
                await async_browserless.get_page_content(
                    "https://pfr.com", wait_for_element="#el"
                )

    @pytest.mark.asyncio
    async def test_does_not_catch_unrelated_exceptions(self, async_browserless):
        mock_pw = AsyncMock()
        mock_pw.chromium.connect_over_cdp.side_effect = RuntimeError("unexpected")

        with (
            patch.object(
                async_browserless,
                "fetch_data",
                new_callable=AsyncMock,
                return_value={"browserWSEndpoint": "ws://host"},
            ),
            patch("griddy.pfr.utils.browserless.async_playwright") as mock_ap,
        ):
            mock_ap.return_value.__aenter__ = AsyncMock(return_value=mock_pw)
            mock_ap.return_value.__aexit__ = AsyncMock(return_value=False)

            with pytest.raises(RuntimeError, match="unexpected"):
                await async_browserless.get_page_content(
                    "https://pfr.com", wait_for_element="#el"
                )
