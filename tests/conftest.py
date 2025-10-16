"""Pytest configuration and shared fixtures."""

from unittest.mock import Mock, patch

import pytest

from griddy import settings


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


@pytest.fixture(autouse=True)
def mock_nfl_cookies():
    """Mock cookie extraction for all NFLClient tests."""
    # Get API key from settings, or use a mock value if not set
    api_key = settings.NFL.get("api_key") or "mock_api_key"

    mock_cookies = {
        f"glt_{api_key}": "mock_login_token_12345",
        "session_id": "mock_session_abc",
    }

    # Patch where the function is imported and used, not where it's defined
    with patch("griddy.nfl.client.extract_cookies_as_dict", return_value=mock_cookies):
        yield mock_cookies


@pytest.fixture(autouse=True)
def mock_nfl_auth_requests(requests_mock):
    """Mock authentication-related HTTP requests for NFLClient."""
    import time

    mock_account_response = {
        "signatureTimestamp": "1234567890",
        "UID": "mock_uid_12345",
        "UIDSignature": "mock_signature_abc",
    }

    mock_token_response = {
        "accessToken": "mock_access_token",
        "refreshToken": "mock_refresh_token",
        "expiresIn": int(time.time()) + 3600,  # 1 hour from now
    }

    # Mock the account info endpoint
    requests_mock.post(settings.NFL["account_url"], json=mock_account_response)

    # Mock the token endpoint (both initial and refresh)
    requests_mock.post(settings.NFL["token_url"], json=mock_token_response)

    requests_mock.post(f"{settings.NFL['token_url']}/refresh", json=mock_token_response)

    yield requests_mock
