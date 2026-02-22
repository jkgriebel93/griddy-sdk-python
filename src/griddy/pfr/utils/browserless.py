"""Browserless fetch utility for bypassing bot detection on PFR pages.

Uses the Browserless /chromium/unblock API with a residential proxy to fetch
HTML content from Pro Football Reference pages that are protected by bot
detection.

Requires:
    - BROWSERLESS_API_KEY environment variable
    - playwright and requests packages
"""

import os
from typing import Optional

import requests
from playwright.sync_api import sync_playwright

BROWSERLESS_HOST = "production-sfo.browserless.io"


class BrowserlessError(Exception):
    """Raised when a Browserless API call or browser interaction fails."""


def fetch_page_html(
    url: str,
    *,
    wait_for_selector: str = "table",
    timeout_ms: int = 15_000,
) -> str:
    """Fetch a page's HTML via Browserless unblock API + Playwright.

    Calls the Browserless /chromium/unblock endpoint with a residential proxy
    to bypass bot detection, then connects Playwright over CDP to extract the
    fully-rendered page HTML.

    Args:
        url: The full URL to fetch.
        wait_for_selector: CSS selector to wait for before extracting HTML.
        timeout_ms: Milliseconds to wait for the selector.

    Returns:
        The page's outer HTML as a string.

    Raises:
        BrowserlessError: If the API key is missing, the API call fails,
            or the page cannot be loaded.
    """
    token = os.environ.get("BROWSERLESS_API_KEY", "")
    if not token:
        raise BrowserlessError("BROWSERLESS_API_KEY environment variable is not set.")

    unblock_url = f"https://{BROWSERLESS_HOST}/chromium/unblock"
    query_params = {
        "token": token,
        "proxy": "residential",
        "timeout": 60_000,
    }
    payload = {
        "url": url,
        "browserWSEndpoint": True,
        "cookies": True,
        "content": False,
        "screenshot": False,
        "ttl": 30_000,
    }

    try:
        resp = requests.post(
            unblock_url,
            json=payload,
            params=query_params,
            headers={"Content-Type": "application/json"},
        )
        resp.raise_for_status()
    except requests.RequestException as exc:
        raise BrowserlessError(
            f"Browserless /chromium/unblock request failed: {exc}"
        ) from exc

    data = resp.json()
    ws_endpoint = data.get("browserWSEndpoint")
    if not ws_endpoint:
        raise BrowserlessError("Browserless response missing browserWSEndpoint.")
    cookies = data.get("cookies", [])

    with sync_playwright() as pw:
        try:
            browser = pw.chromium.connect_over_cdp(ws_endpoint)
        except Exception as exc:
            raise BrowserlessError(
                f"Failed to connect Playwright via CDP: {exc}"
            ) from exc

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
            page.goto(url, wait_until="domcontentloaded", timeout=60_000)

        page.wait_for_selector(wait_for_selector, timeout=timeout_ms)
        html = page.content()
        browser.close()

    return html
