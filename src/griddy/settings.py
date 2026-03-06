"""Centralised configuration for the Griddy SDK.

Loads settings from environment variables using pydantic-settings and exposes
module-level convenience aliases for backwards compatibility.
"""

from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class NFLSettings(BaseSettings):
    """NFL.com API connection settings.

    All fields can be populated via environment variables prefixed with
    ``NFL_`` (e.g. ``NFL_API_KEY``, ``NFL_LOGIN_EMAIL``).

    Attributes:
        api_key: NFL API key extracted from NFL.com network requests.
        sdk_build: SDK build number sent with API requests.
        client_key: OAuth client key for NFL.com authentication.
        client_secret: OAuth client secret for NFL.com authentication.
        auth_url: Base URL for the NFL identity / auth service.
        account_url: Endpoint for retrieving NFL account information.
        token_url: Endpoint for obtaining an OAuth access token.
        base_api_url: Base URL for the public NFL Football v2 API.
        pro_api_base_url: Base URL for the NFL Pro (advanced stats) API.
        login_email: Email address for an NFL.com account with Pro access.
        login_password: Password for the NFL.com account.
    """

    model_config = {"env_prefix": "NFL_"}

    api_key: Optional[str] = None
    sdk_build: str = "15170"
    client_key: Optional[str] = None
    client_secret: Optional[str] = None
    auth_url: str = "https://auth-id.nfl.com/"
    account_url: str = "https://auth-id.nfl.com/accounts.getAccountInfo"
    token_url: str = "https://api.nfl.com/identity/v3/token"
    base_api_url: str = "https://api.nfl.com/football/v2/"
    pro_api_base_url: str = "https://pro.nfl.com/api/"
    login_email: Optional[str] = None
    login_password: Optional[str] = None


class BrowserlessSettings(BaseSettings):
    """Browserless API connection settings.

    Used by the PFR SDK to route requests through a Browserless instance
    that bypasses bot detection on Pro Football Reference pages.

    All fields can be populated via environment variables prefixed with
    ``BROWSERLESS_`` (e.g. ``BROWSERLESS_HOST``, ``BROWSERLESS_TOKEN``).

    Attributes:
        host: Hostname (or URL) of the Browserless instance.
        token: Authentication token for the Browserless API.
    """

    model_config = {"env_prefix": "BROWSERLESS_"}

    host: Optional[str] = None
    token: Optional[str] = None


class GriddySettings(BaseSettings):
    """Top-level settings container for the Griddy SDK.

    Aggregates :class:`NFLSettings` and :class:`BrowserlessSettings` into a
    single configuration object.  A module-level singleton is created at
    import time and exposed as :data:`settings`.

    Attributes:
        nfl: NFL.com API settings.
        browserless: Browserless API settings.
    """

    nfl: NFLSettings = Field(default_factory=NFLSettings)
    browserless: BrowserlessSettings = Field(default_factory=BrowserlessSettings)

    @property
    def fixture_dir(self) -> Path:
        """Return the path to the test fixtures directory.

        Resolves to ``<repo_root>/tests/fixtures`` relative to this file's
        location in the source tree.
        """
        return Path(__file__).resolve().parents[2] / "tests" / "fixtures"


settings = GriddySettings()

# Convenience aliases for backwards compatibility
NFL = settings.nfl
BROWSERLESS_HOST = settings.browserless.host
BROWSERLESS_TOKEN = settings.browserless.token
FIXTURE_DIR = settings.fixture_dir
