"""Tests for griddy.settings Pydantic BaseSettings configuration."""

from pathlib import Path
from unittest.mock import patch

import pytest

from griddy.settings import (
    BROWSERLESS_HOST,
    BROWSERLESS_TOKEN,
    FIXTURE_DIR,
    NFL,
    BrowserlessSettings,
    GriddySettings,
    NFLSettings,
    settings,
)


@pytest.mark.unit
class TestNFLSettings:
    def test_defaults(self):
        nfl = NFLSettings(
            _env_file=None,
            api_key=None,
            client_key=None,
            client_secret=None,
        )
        assert nfl.sdk_build == "15170"
        assert nfl.auth_url == "https://auth-id.nfl.com/"
        assert nfl.token_url == "https://api.nfl.com/identity/v3/token"
        assert nfl.base_api_url == "https://api.nfl.com/football/v2/"
        assert nfl.pro_api_base_url == "https://pro.nfl.com/api/"
        assert nfl.api_key is None
        assert nfl.client_key is None
        assert nfl.client_secret is None
        assert nfl.login_email is None
        assert nfl.login_password is None

    def test_env_prefix(self):
        env = {
            "NFL_API_KEY": "test_api_key",
            "NFL_SDK_BUILD": "99999",
            "NFL_CLIENT_KEY": "ck",
            "NFL_CLIENT_SECRET": "cs",
            "NFL_LOGIN_EMAIL": "test@example.com",
            "NFL_LOGIN_PASSWORD": "secret",
        }
        with patch.dict("os.environ", env, clear=False):
            nfl = NFLSettings(_env_file=None)
        assert nfl.api_key == "test_api_key"
        assert nfl.sdk_build == "99999"
        assert nfl.client_key == "ck"
        assert nfl.client_secret == "cs"
        assert nfl.login_email == "test@example.com"
        assert nfl.login_password == "secret"

    def test_explicit_values_override_env(self):
        with patch.dict("os.environ", {"NFL_API_KEY": "from_env"}, clear=False):
            nfl = NFLSettings(_env_file=None, api_key="explicit")
        assert nfl.api_key == "explicit"


@pytest.mark.unit
class TestBrowserlessSettings:
    def test_defaults(self):
        bl = BrowserlessSettings(_env_file=None, host=None, token=None)
        assert bl.host is None
        assert bl.token is None

    def test_env_prefix(self):
        env = {
            "BROWSERLESS_HOST": "http://localhost:3000",
            "BROWSERLESS_TOKEN": "bl_token",
        }
        with patch.dict("os.environ", env, clear=False):
            bl = BrowserlessSettings(_env_file=None)
        assert bl.host == "http://localhost:3000"
        assert bl.token == "bl_token"


@pytest.mark.unit
class TestGriddySettings:
    def test_nested_settings(self):
        gs = GriddySettings(
            _env_file=None,
            nfl=NFLSettings(_env_file=None, client_key="k", client_secret="s"),
            browserless=BrowserlessSettings(_env_file=None, host="h", token="t"),
        )
        assert gs.nfl.client_key == "k"
        assert gs.browserless.host == "h"

    def test_fixture_dir_is_path(self):
        gs = GriddySettings(_env_file=None)
        assert isinstance(gs.fixture_dir, Path)
        assert gs.fixture_dir.name == "fixtures"
        assert gs.fixture_dir.parent.name == "tests"


@pytest.mark.unit
class TestModuleLevelAliases:
    def test_nfl_alias(self):
        assert NFL is settings.nfl

    def test_browserless_aliases(self):
        assert BROWSERLESS_HOST is settings.browserless.host
        assert BROWSERLESS_TOKEN is settings.browserless.token

    def test_fixture_dir_alias(self):
        assert FIXTURE_DIR == settings.fixture_dir
