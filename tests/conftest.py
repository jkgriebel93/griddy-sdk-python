"""Pytest configuration and shared fixtures."""

import asyncio
import time
from typing import Any, Dict
from unittest.mock import Mock

import pytest

from griddy import settings
from griddy.nfl.sdk import GriddyNFL


class _MockResponse:
    """Minimal mock response object for requests.post patches."""

    def __init__(self, payload: Dict[str, Any], status_code: int = 200) -> None:
        self._payload = payload
        self.status_code = status_code
        self.headers: Dict[str, str] = {}
        self.content = b""
        self.text = ""

    def json(self) -> Dict[str, Any]:
        return self._payload

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RuntimeError(f"Mocked HTTP error: {self.status_code}")


@pytest.fixture
def mock_response():
    """Create a mock HTTP response for testing."""
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"success": True}
    response.headers = {}
    response.content = b'{"success": true}'
    response.text = '{"success": true}'
    response.url = "https://api.example.com/test"
    return response


@pytest.fixture
def sample_game_data():
    """Sample game data for testing."""
    return {
        "id": "game123",
        "homeTeam": {"abbreviation": "KC"},
        "awayTeam": {"abbreviation": "BUF"},
        "homeScore": 31,
        "awayScore": 24,
        "status": "final",
        "startTime": "2024-01-01T13:00:00Z",
        "week": 1,
        "season": 2024,
        "seasonType": "regular",
    }


@pytest.fixture
def sample_team_data():
    """Sample team data for testing."""
    return {
        "id": "KC",
        "name": "Kansas City Chiefs",
        "abbreviation": "KC",
        "city": "Kansas City",
        "conference": "AFC",
        "division": "West",
    }


@pytest.fixture
def sample_player_data():
    """Sample player data for testing."""
    return {
        "id": "player123",
        "name": "Patrick Mahomes",
        "teamId": "KC",
        "position": "QB",
        "jerseyNumber": 15,
        "height": "6-3",
        "weight": 230,
        "age": 28,
        "college": "Texas Tech",
    }


@pytest.fixture
def mocked_nfl_sdk(monkeypatch, tmp_path):
    """Provide a GriddyNFL instance with external HTTP calls patched out."""

    cookies_file = tmp_path / "cookies.txt"
    cookies_file.write_text("# Netscape HTTP Cookie File\n", encoding="utf-8")

    monkeypatch.setitem(settings.NFL, "api_key", "fake_api_key")
    monkeypatch.setitem(settings.NFL, "clientKey", "fake_client_key")
    monkeypatch.setitem(settings.NFL, "clientSecret", "fake_client_secret")

    def fake_extract(cookies_path: str, auth_url: str):
        assert cookies_path == str(cookies_file)
        return {f"glt_{settings.NFL['api_key']}": "fake_login_token"}

    monkeypatch.setattr("griddy.nfl.sdk.extract_cookies_as_dict", fake_extract)

    def fake_post(url, data=None, headers=None):
        if url == settings.NFL["account_url"]:
            return _MockResponse(
                {
                    "UID": "fake_uid",
                    "UIDSignature": "fake_signature",
                    "signatureTimestamp": "1234567890",
                }
            )
        if url.startswith(settings.NFL["token_url"]):
            return _MockResponse(
                {
                    "accessToken": "fake_access_token",
                    "refreshToken": "fake_refresh_token",
                    "expiresIn": int(time.time()) + 3600,
                }
            )

        raise AssertionError(f"Unexpected URL in fake_post: {url}")

    monkeypatch.setattr("griddy.nfl.sdk.requests.post", fake_post)

    sdk = GriddyNFL(str(cookies_file))

    yield sdk

    client = sdk.sdk_configuration.client
    if client is not None:
        client.close()

    async_client = sdk.sdk_configuration.async_client
    if async_client is not None:
        try:
            asyncio.run(async_client.aclose())
        except RuntimeError:
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = None
            if loop is not None:
                loop.create_task(async_client.aclose())


@pytest.fixture
def nfl_scores(mocked_nfl_sdk):
    """Access the Scores sub-SDK for NFL endpoint tests."""

    return mocked_nfl_sdk.scores


@pytest.fixture
def nfl_football(mocked_nfl_sdk):
    """Access the Football sub-SDK for NFL endpoint tests."""

    return mocked_nfl_sdk.football


@pytest.fixture
def nfl_win_probability(mocked_nfl_sdk):
    """Access the WinProbability sub-SDK for NFL endpoint tests."""

    return mocked_nfl_sdk.win_probability


@pytest.fixture
def nfl_season_schedule(mocked_nfl_sdk):
    """Access the SeasonSchedule sub-SDK for NFL endpoint tests."""

    return mocked_nfl_sdk.season_schedule
