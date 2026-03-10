import os
import time
from random import uniform
from typing import Any, Dict, Optional

from pydantic import BaseModel

from griddy.core.utils.logger import Logger, NoOpLogger

# Re-export generic security functions from core
from griddy.core.utils.security import (
    _apply_bearer,  # noqa: F401
    _parse_basic_auth_scheme,  # noqa: F401
    _parse_security_option,  # noqa: F401
    _parse_security_scheme,  # noqa: F401
    _parse_security_scheme_value,  # noqa: F401
    get_security,  # noqa: F401
)


def get_security_from_env(security: Any, security_class: Any) -> Optional[BaseModel]:
    """NFL-specific security env var resolution."""
    if security is not None:
        return security

    if not issubclass(security_class, BaseModel):
        raise TypeError("security_class must be a pydantic model class")

    security_dict: Any = {}

    if os.getenv("GRIDDY_NFL_NFL_AUTH"):
        security_dict["nfl_auth"] = os.getenv("GRIDDY_NFL_NFL_AUTH")

    return security_class(**security_dict) if security_dict else None


def do_browser_auth(
    email: str,
    password: str,
    headless: bool = False,
    logger: Optional[Logger] = None,
) -> Dict:
    """Authenticate via browser automation and return the token response dict."""
    if logger is None:
        logger = NoOpLogger()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise ImportError(
            "Playwright is required for browser-based authentication but is not "
            "installed. Install it with: pip install griddy[browser-auth]"
        ) from None

    logger.debug("Begin do_browser_auth.")
    with sync_playwright() as p:
        logger.debug("Launching browser.")
        browser = p.firefox.launch(headless=headless)

        page = browser.new_page()
        logger.debug("Opening login page")
        page.goto("https://id.nfl.com/account/sign-in")

        logger.debug("Acknowledge tracking")
        page.get_by_role("button", name="Acknowledge Tracking").click()

        logger.debug("Enter email")
        page.get_by_test_id("email-input").fill(email)
        time.sleep(uniform(2.5, 3.5))

        logger.debug("Click continue button")
        page.get_by_role("button", name="Continue").click()
        time.sleep(uniform(2.5, 3.5))

        logger.debug("Click login with password button")
        page.get_by_role("button", name="Sign in with password").click()
        time.sleep(uniform(2.5, 3.5))

        logger.debug("Entering password")
        page.get_by_test_id("password-input").fill(password)
        time.sleep(uniform(0.75, 1.25))

        with page.expect_response("**/token") as response_info:
            logger.debug("Click login button")
            page.get_by_role("button", name="Sign in").click()

        response_json = response_info.value.json()
        browser.close()

        return response_json
