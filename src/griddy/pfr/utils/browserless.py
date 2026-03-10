"""Browserless fetch utility for bypassing bot detection on PFR pages.

Uses the Browserless /chromium/unblock API with a residential proxy to fetch
HTML content from Pro Football Reference pages that are protected by bot
detection.

Requires:
    - BROWSERLESS_TOKEN environment variable
    - BROWSERLESS_HOST environment variable
    - httpx package
    - playwright package (optional: pip install griddy[browser-auth])
"""

from dataclasses import dataclass
from typing import Any

import httpx

from griddy.settings import BROWSERLESS_HOST, BROWSERLESS_TOKEN

_PLAYWRIGHT_INSTALL_MSG = (
    "Playwright is required for Browserless page fetching but is not installed. "
    "Install it with: pip install griddy[browser-auth]"
)


def _import_sync_playwright() -> tuple:
    """Import sync Playwright components, raising a clear error if missing."""
    try:
        from playwright.sync_api import Error as PlaywrightError
        from playwright.sync_api import sync_playwright

        return sync_playwright, PlaywrightError
    except ImportError:
        raise ImportError(_PLAYWRIGHT_INSTALL_MSG) from None


def _import_async_playwright() -> tuple:
    """Import async Playwright components, raising a clear error if missing."""
    try:
        from playwright.async_api import Error as AsyncPlaywrightError
        from playwright.async_api import async_playwright

        return async_playwright, AsyncPlaywrightError
    except ImportError:
        raise ImportError(_PLAYWRIGHT_INSTALL_MSG) from None


@dataclass
class BrowserlessConfig:
    """Configuration for Browserless API requests.

    Extracts previously hardcoded values so they can be overridden per instance.
    """

    proxy: str = "residential"
    request_timeout: int = 60_000
    ttl: int = 30_000
    default_timeout_ms: int = 60_000


class BrowserlessError(Exception):
    """Raised when a Browserless API call or browser interaction fails."""


class Browserless:
    """Synchronous client for fetching web pages via the Browserless unblock API.

    Combines the Browserless ``/chromium/unblock`` endpoint (which uses a
    residential proxy to bypass bot detection) with Playwright CDP connections
    to extract fully-rendered page HTML.
    """

    def __init__(self, config: BrowserlessConfig | None = None) -> None:
        """Initialise the Browserless client.

        Args:
            config: Optional configuration overrides. Uses
                :class:`BrowserlessConfig` defaults when *None*.

        Raises:
            BrowserlessError: If ``BROWSERLESS_HOST`` or ``BROWSERLESS_TOKEN``
                environment variables are not set.
        """
        if not BROWSERLESS_HOST:
            raise BrowserlessError("BROWSERLESS_HOST environment variable is not set.")
        if not BROWSERLESS_TOKEN:
            raise BrowserlessError("BROWSERLESS_TOKEN environment variable is not set.")
        self.config = config or BrowserlessConfig()
        self.host = BROWSERLESS_HOST
        self.token = BROWSERLESS_TOKEN
        self.data: dict | None = None
        self.timeout = self.config.default_timeout_ms

    def fetch_data(self, url: str) -> dict[str, Any]:
        """Call the Browserless ``/chromium/unblock`` endpoint.

        Args:
            url: The target URL to unblock.

        Returns:
            The JSON response from the unblock API, containing keys such as
            ``browserWSEndpoint`` and ``cookies``.

        Raises:
            BrowserlessError: If the HTTP request fails.
        """
        unblock_url = f"https://{self.host}/chromium/unblock"
        query_params = {
            "token": self.token,
            "proxy": self.config.proxy,
            "timeout": self.config.request_timeout,
        }
        payload = {
            "url": url,
            "browserWSEndpoint": True,
            "cookies": True,
            "content": False,
            "screenshot": False,
            "ttl": self.config.ttl,
        }

        try:
            resp = httpx.post(
                unblock_url,
                json=payload,
                params=query_params,
                headers={"Content-Type": "application/json"},
                timeout=self.config.request_timeout / 1000,
            )
            resp.raise_for_status()
        except httpx.HTTPError as exc:
            raise BrowserlessError(
                f"Browserless /chromium/unblock request failed: {exc}"
            ) from exc

        return resp.json()

    def _handle_page_navigation(
        self, browser: Any, url: str, cookies: dict, element: str
    ) -> str:
        """Locate or create a page in *browser* and wait for *element*.

        If the unblock API already opened a page matching *url*, that page is
        reused. Otherwise a new browser context is created, cookies are
        injected, and the page is navigated to *url*.

        Args:
            browser: A Playwright ``Browser`` instance connected via CDP.
            url: The target URL.
            cookies: Cookies returned by the unblock API to inject into the
                new context (if one is created).
            element: CSS selector to wait for before extracting content.

        Returns:
            The page's outer HTML as a string.
        """
        # The unblock API already navigated to the URL in the first page.
        page = None
        for ctx in browser.contexts:
            for p in ctx.pages:
                if url in p.url:
                    page = p
                    break
            if page:
                break

        if page is None:
            context = browser.new_context()
            page = context.new_page()
            if cookies:
                context.add_cookies(cookies)
            page.goto(url, wait_until="domcontentloaded", timeout=self.timeout)

        page.locator(element).wait_for(timeout=self.timeout)

        return page.content()

    def get_page_content(self, url: str, wait_for_element: str) -> str:
        """Fetch a page's HTML via Browserless unblock API + Playwright.

        Calls the Browserless /chromium/unblock endpoint with a residential proxy
        to bypass bot detection, then connects Playwright over CDP to extract the
        fully-rendered page HTML.

        Args:
            url: The full URL to fetch.
            wait_for_element: HTML Element id to wait for before extracting HTML.
            timeout_ms: Milliseconds to wait for the selector.

        Returns:
            The page's outer HTML as a string.

        Raises:
            BrowserlessError: If the API key is missing, the API call fails,
                or the page cannot be loaded.
        """
        browserless_data = self.fetch_data(url=url)

        ws_endpoint = browserless_data.get("browserWSEndpoint")
        cookies = browserless_data.get("cookies", [])

        sync_playwright, PlaywrightError = _import_sync_playwright()

        with sync_playwright() as pw:
            try:
                browser = pw.chromium.connect_over_cdp(ws_endpoint)
            except (PlaywrightError, ConnectionError, httpx.HTTPError) as exc:
                raise BrowserlessError(
                    f"Failed to connect Playwright via CDP: {exc}"
                ) from exc

            html = self._handle_page_navigation(
                browser=browser, url=url, cookies=cookies, element=wait_for_element
            )
            browser.close()

        return html


class AsyncBrowserless:
    """Async variant of :class:`Browserless`.

    Uses ``httpx.AsyncClient`` for the unblock API call and
    ``playwright.async_api`` for CDP browser interaction.
    """

    def __init__(self, config: BrowserlessConfig | None = None) -> None:
        """Initialise the async Browserless client.

        Args:
            config: Optional configuration overrides. Uses
                :class:`BrowserlessConfig` defaults when *None*.

        Raises:
            BrowserlessError: If ``BROWSERLESS_HOST`` or ``BROWSERLESS_TOKEN``
                environment variables are not set.
        """
        if not BROWSERLESS_HOST:
            raise BrowserlessError("BROWSERLESS_HOST environment variable is not set.")
        if not BROWSERLESS_TOKEN:
            raise BrowserlessError("BROWSERLESS_TOKEN environment variable is not set.")
        self.config = config or BrowserlessConfig()
        self.host = BROWSERLESS_HOST
        self.token = BROWSERLESS_TOKEN
        self.data: dict | None = None
        self.timeout = self.config.default_timeout_ms

    async def fetch_data(self, url: str) -> dict[str, Any]:
        """Call the Browserless ``/chromium/unblock`` endpoint asynchronously.

        Args:
            url: The target URL to unblock.

        Returns:
            The JSON response from the unblock API, containing keys such as
            ``browserWSEndpoint`` and ``cookies``.

        Raises:
            BrowserlessError: If the HTTP request fails.
        """
        unblock_url = f"https://{self.host}/chromium/unblock"
        query_params = {
            "token": self.token,
            "proxy": self.config.proxy,
            "timeout": self.config.request_timeout,
        }
        payload = {
            "url": url,
            "browserWSEndpoint": True,
            "cookies": True,
            "content": False,
            "screenshot": False,
            "ttl": self.config.ttl,
        }

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    unblock_url,
                    json=payload,
                    params=query_params,
                    headers={"Content-Type": "application/json"},
                    timeout=self.config.request_timeout / 1000,
                )
                resp.raise_for_status()
        except httpx.HTTPError as exc:
            raise BrowserlessError(
                f"Browserless /chromium/unblock request failed: {exc}"
            ) from exc

        return resp.json()

    async def _handle_page_navigation(
        self, browser: Any, url: str, cookies: dict, element: str
    ) -> str:
        """Locate or create a page in *browser* and wait for *element*.

        Async counterpart of :meth:`Browserless._handle_page_navigation`.

        Args:
            browser: An async Playwright ``Browser`` instance connected via CDP.
            url: The target URL.
            cookies: Cookies returned by the unblock API to inject into the
                new context (if one is created).
            element: CSS selector to wait for before extracting content.

        Returns:
            The page's outer HTML as a string.
        """
        page = None
        for ctx in browser.contexts:
            for p in ctx.pages:
                if url in p.url:
                    page = p
                    break
            if page:
                break

        if page is None:
            context = await browser.new_context()
            page = await context.new_page()
            if cookies:
                await context.add_cookies(cookies)
            await page.goto(url, wait_until="domcontentloaded", timeout=self.timeout)

        await page.locator(element).wait_for(timeout=self.timeout)

        return await page.content()

    async def get_page_content(self, url: str, wait_for_element: str) -> str:
        """Async version of :meth:`Browserless.get_page_content`.

        Args:
            url: The full URL to fetch.
            wait_for_element: CSS selector to wait for before extracting HTML.

        Returns:
            The page's outer HTML as a string.

        Raises:
            BrowserlessError: On API or browser connection failure.
        """
        browserless_data = await self.fetch_data(url=url)

        ws_endpoint = browserless_data.get("browserWSEndpoint")
        cookies = browserless_data.get("cookies", [])

        async_playwright, AsyncPlaywrightError = _import_async_playwright()

        async with async_playwright() as pw:
            try:
                browser = await pw.chromium.connect_over_cdp(ws_endpoint)
            except (
                AsyncPlaywrightError,
                ConnectionError,
                httpx.HTTPError,
            ) as exc:
                raise BrowserlessError(
                    f"Failed to connect Playwright via CDP: {exc}"
                ) from exc

            html = await self._handle_page_navigation(
                browser=browser, url=url, cookies=cookies, element=wait_for_element
            )
            await browser.close()

        return html
