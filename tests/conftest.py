"""Pytest configuration and shared fixtures."""

import pytest
from unittest.mock import Mock


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
