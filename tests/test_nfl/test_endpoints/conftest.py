"""
Pytest configuration and fixtures for NFL SDK endpoint tests.

This module provides shared fixtures and utilities for testing NFL SDK endpoints.
Related to GitHub issue #25.
"""

import pytest
from unittest.mock import Mock, MagicMock, patch
import httpx
from typing import Dict, Any, List, Optional
from datetime import datetime


# ================================================================================
# SDK Configuration Fixtures
# ================================================================================

@pytest.fixture
def mock_sdk_configuration():
    """Create a mock SDK configuration for testing."""
    config = Mock()
    config.client = Mock(spec=httpx.Client)
    config.async_client = Mock(spec=httpx.AsyncClient)
    config.timeout_ms = 30000
    config.retry_config = Mock()
    config.security = None
    config.user_agent = "griddy-nfl-sdk/test"
    config.debug_logger = Mock()
    config.debug_logger.debug = Mock()

    # Set up the base URL and server details
    config.get_server_details = Mock(return_value=("https://api.nfl.com", {}))

    # Mock hooks
    hooks = Mock()
    hooks.before_request = Mock(side_effect=lambda ctx, req: req)
    hooks.after_success = Mock(side_effect=lambda ctx, res: res)
    hooks.after_error = Mock(return_value=(None, None))
    config.__dict__["_hooks"] = hooks

    return config


@pytest.fixture
def mock_base_sdk(mock_sdk_configuration):
    """Create a mock base SDK instance."""
    from griddy.nfl.basesdk import BaseSDK
    sdk = BaseSDK(mock_sdk_configuration)
    return sdk


# ================================================================================
# HTTP Response Fixtures
# ================================================================================

@pytest.fixture
def mock_http_response():
    """Create a mock successful HTTP response."""
    response = Mock(spec=httpx.Response)
    response.status_code = 200
    response.headers = {"content-type": "application/json"}
    response.text = '{"success": true}'
    response.content = b'{"success": true}'
    response.json = Mock(return_value={"success": True})
    response.url = "https://api.nfl.com/test"
    response.is_error = False
    response.is_success = True
    response.iter_bytes = Mock(return_value=iter([b'{"success": true}']))
    response.iter_lines = Mock(return_value=iter(['{"success": true}']))
    return response


@pytest.fixture
def mock_error_response():
    """Create a mock error HTTP response."""
    response = Mock(spec=httpx.Response)
    response.status_code = 400
    response.headers = {"content-type": "application/json"}
    response.text = '{"error": "Bad Request", "message": "Invalid parameters"}'
    response.content = b'{"error": "Bad Request", "message": "Invalid parameters"}'
    response.json = Mock(return_value={"error": "Bad Request", "message": "Invalid parameters"})
    response.url = "https://api.nfl.com/test"
    response.is_error = True
    response.is_success = False
    return response


@pytest.fixture
def mock_not_found_response():
    """Create a mock 404 Not Found response."""
    response = Mock(spec=httpx.Response)
    response.status_code = 404
    response.headers = {"content-type": "application/json"}
    response.text = '{"error": "Not Found"}'
    response.content = b'{"error": "Not Found"}'
    response.json = Mock(return_value={"error": "Not Found"})
    response.url = "https://api.nfl.com/test"
    response.is_error = True
    response.is_success = False
    return response


@pytest.fixture
def mock_rate_limit_response():
    """Create a mock rate limit (429) response."""
    response = Mock(spec=httpx.Response)
    response.status_code = 429
    response.headers = {
        "content-type": "application/json",
        "Retry-After": "60"
    }
    response.text = '{"error": "Rate limit exceeded"}'
    response.content = b'{"error": "Rate limit exceeded"}'
    response.json = Mock(return_value={"error": "Rate limit exceeded"})
    response.url = "https://api.nfl.com/test"
    response.is_error = True
    response.is_success = False
    return response


# ================================================================================
# Sample Data Fixtures - Player Statistics
# ================================================================================

@pytest.fixture
def sample_player_stats():
    """Sample player statistics data."""
    return {
        "player_id": "player_123",
        "name": "Patrick Mahomes",
        "team": "KC",
        "position": "QB",
        "season": 2024,
        "week": 1,
        "passing": {
            "attempts": 38,
            "completions": 28,
            "yards": 350,
            "touchdowns": 3,
            "interceptions": 0,
            "rating": 118.4
        },
        "rushing": {
            "attempts": 5,
            "yards": 25,
            "touchdowns": 0,
            "average": 5.0
        }
    }


@pytest.fixture
def sample_player_receiving_stats():
    """Sample player receiving statistics data."""
    return {
        "player_id": "player_456",
        "name": "Travis Kelce",
        "team": "KC",
        "position": "TE",
        "season": 2024,
        "week": 1,
        "receiving": {
            "targets": 12,
            "receptions": 9,
            "yards": 125,
            "touchdowns": 1,
            "average": 13.9,
            "long": 28
        }
    }


@pytest.fixture
def sample_player_rushing_stats():
    """Sample player rushing statistics data."""
    return {
        "player_id": "player_789",
        "name": "Isiah Pacheco",
        "team": "KC",
        "position": "RB",
        "season": 2024,
        "week": 1,
        "rushing": {
            "attempts": 18,
            "yards": 82,
            "touchdowns": 1,
            "average": 4.6,
            "long": 15,
            "fumbles": 0
        }
    }


# ================================================================================
# Sample Data Fixtures - Team Statistics
# ================================================================================

@pytest.fixture
def sample_team_stats():
    """Sample team statistics data."""
    return {
        "team_id": "KC",
        "name": "Kansas City Chiefs",
        "season": 2024,
        "week": 1,
        "offense": {
            "total_yards": 425,
            "passing_yards": 325,
            "rushing_yards": 100,
            "points": 31,
            "turnovers": 1,
            "first_downs": 24,
            "third_down_efficiency": "8/14",
            "time_of_possession": "32:15"
        },
        "defense": {
            "yards_allowed": 350,
            "passing_yards_allowed": 250,
            "rushing_yards_allowed": 100,
            "points_allowed": 24,
            "turnovers_forced": 2,
            "sacks": 3,
            "interceptions": 1,
            "fumbles_recovered": 1
        }
    }


@pytest.fixture
def sample_team_defense_stats():
    """Sample team defense statistics data."""
    return {
        "team_id": "KC",
        "season": 2024,
        "week": 1,
        "yards_allowed": 350,
        "passing_yards_allowed": 250,
        "rushing_yards_allowed": 100,
        "points_allowed": 24,
        "sacks": 3,
        "interceptions": 1,
        "fumbles_recovered": 1,
        "tackles_for_loss": 8,
        "qb_hits": 10,
        "passes_defended": 12
    }


# ================================================================================
# Sample Data Fixtures - Defensive Player Statistics
# ================================================================================

@pytest.fixture
def sample_defensive_player_stats():
    """Sample defensive player statistics data."""
    return {
        "player_id": "def_123",
        "name": "Chris Jones",
        "team": "KC",
        "position": "DT",
        "season": 2024,
        "week": 1,
        "tackles": {
            "total": 5,
            "solo": 3,
            "assists": 2,
            "for_loss": 2
        },
        "sacks": 1.5,
        "qb_hits": 3,
        "passes_defended": 1,
        "forced_fumbles": 0,
        "fumbles_recovered": 0,
        "interceptions": 0
    }


@pytest.fixture
def sample_defensive_pass_rush_stats():
    """Sample defensive pass rush statistics data."""
    return {
        "player_id": "def_456",
        "name": "George Karlaftis",
        "team": "KC",
        "position": "DE",
        "season": 2024,
        "week": 1,
        "pass_rush": {
            "pass_rush_snaps": 35,
            "pressures": 8,
            "sacks": 1,
            "qb_hits": 2,
            "hurries": 5,
            "pressure_rate": 22.9,
            "win_rate": 18.5
        }
    }


# ================================================================================
# Sample Data Fixtures - Game and Schedule Data
# ================================================================================

@pytest.fixture
def sample_game_schedule():
    """Sample game schedule data."""
    return {
        "game_id": "game_123",
        "season": 2024,
        "week": 1,
        "season_type": "regular",
        "home_team": "KC",
        "away_team": "BAL",
        "game_time": "2024-09-05T20:20:00Z",
        "venue": "GEHA Field at Arrowhead Stadium",
        "status": "scheduled",
        "tv_broadcast": "NBC",
        "weather": {
            "temperature": 72,
            "condition": "Clear",
            "wind_speed": 8,
            "wind_direction": "NW"
        }
    }


@pytest.fixture
def sample_game_score():
    """Sample game score data."""
    return {
        "game_id": "game_123",
        "home_team": "KC",
        "away_team": "BAL",
        "home_score": 27,
        "away_score": 20,
        "status": "final",
        "quarter": 4,
        "time_remaining": "0:00",
        "scoring_plays": [
            {
                "quarter": 1,
                "time": "10:25",
                "team": "KC",
                "type": "touchdown",
                "description": "Patrick Mahomes 15 yard TD pass to Travis Kelce",
                "score": "7-0"
            }
        ]
    }


@pytest.fixture
def sample_play_data():
    """Sample play-by-play data."""
    return {
        "play_id": "play_123",
        "game_id": "game_123",
        "quarter": 1,
        "time": "14:30",
        "down": 1,
        "distance": 10,
        "yard_line": 25,
        "possession": "KC",
        "play_type": "pass",
        "description": "Patrick Mahomes pass complete to Travis Kelce for 12 yards",
        "yards_gained": 12,
        "result": "first_down"
    }


@pytest.fixture
def sample_win_probability():
    """Sample win probability data."""
    return {
        "game_id": "game_123",
        "play_id": "play_123",
        "home_team": "KC",
        "away_team": "BAL",
        "home_win_probability": 0.65,
        "away_win_probability": 0.35,
        "home_win_probability_change": 0.05
    }


# ================================================================================
# Sample Data Fixtures - Content and Media
# ================================================================================

@pytest.fixture
def sample_content_insights():
    """Sample content insights data."""
    return {
        "content_id": "content_123",
        "title": "Week 1 Preview: Chiefs vs Ravens",
        "type": "preview",
        "author": "NFL Media",
        "published_date": "2024-09-04T12:00:00Z",
        "tags": ["preview", "chiefs", "ravens", "week1"],
        "content": "The defending champions begin their title defense...",
        "insights": [
            {
                "type": "matchup",
                "description": "Patrick Mahomes vs Ravens Defense",
                "analysis": "Key matchup to watch..."
            }
        ]
    }


@pytest.fixture
def sample_video_data():
    """Sample video/filmroom data."""
    return {
        "video_id": "video_123",
        "title": "Chiefs Offensive Highlights Week 1",
        "duration": 185,
        "url": "https://nfl.com/videos/123",
        "thumbnail": "https://nfl.com/thumbnails/123.jpg",
        "tags": ["highlights", "chiefs", "offense"],
        "plays": [
            {
                "play_id": "play_123",
                "timestamp": 45,
                "description": "Mahomes TD pass to Kelce"
            }
        ]
    }


# ================================================================================
# Sample Data Fixtures - Fantasy and Betting
# ================================================================================

@pytest.fixture
def sample_fantasy_stats():
    """Sample fantasy statistics data."""
    return {
        "player_id": "player_123",
        "name": "Patrick Mahomes",
        "team": "KC",
        "position": "QB",
        "week": 1,
        "fantasy_points": {
            "standard": 24.5,
            "ppr": 24.5,
            "half_ppr": 24.5
        },
        "projections": {
            "standard": 22.0,
            "ppr": 22.0,
            "half_ppr": 22.0
        }
    }


@pytest.fixture
def sample_betting_odds():
    """Sample betting odds data."""
    return {
        "game_id": "game_123",
        "home_team": "KC",
        "away_team": "BAL",
        "odds": {
            "spread": {
                "line": -3.5,
                "home_odds": -110,
                "away_odds": -110
            },
            "total": {
                "line": 47.5,
                "over_odds": -110,
                "under_odds": -110
            },
            "moneyline": {
                "home_odds": -175,
                "away_odds": 155
            }
        }
    }


# ================================================================================
# Helper Functions
# ================================================================================

def create_mock_response(
    data: Dict[str, Any] = None,
    status_code: int = 200,
    headers: Optional[Dict[str, str]] = None
) -> Mock:
    """
    Helper function to create a mock HTTP response with custom data.

    Args:
        data: Response data dictionary
        status_code: HTTP status code
        headers: Response headers

    Returns:
        Mock httpx.Response object
    """
    response = Mock(spec=httpx.Response)
    response.status_code = status_code
    response.headers = headers or {"content-type": "application/json"}

    if data is not None:
        import json
        json_str = json.dumps(data)
        response.text = json_str
        response.content = json_str.encode()
        response.json = Mock(return_value=data)
    else:
        response.text = ""
        response.content = b""
        response.json = Mock(return_value={})

    response.is_error = status_code >= 400
    response.is_success = 200 <= status_code < 300
    response.url = "https://api.nfl.com/test"

    return response


@pytest.fixture
def mock_response_factory():
    """Factory fixture for creating mock responses."""
    return create_mock_response


# ================================================================================
# Mock SDK Endpoint Classes
# ================================================================================

@pytest.fixture
def mock_do_request(mock_http_response):
    """Mock do_request method."""
    return Mock(return_value=mock_http_response)


@pytest.fixture
def mock_do_request_async(mock_http_response):
    """Mock do_request_async method."""
    async def async_mock(*args, **kwargs):
        return mock_http_response
    return Mock(side_effect=async_mock)


# ================================================================================
# Assertion Helpers
# ================================================================================

class AssertionHelpers:
    """Helper class for common test assertions."""

    @staticmethod
    def assert_called_with_params(mock_func: Mock, expected_params: Dict[str, Any]):
        """Assert that a mock function was called with expected parameters."""
        mock_func.assert_called()
        call_kwargs = mock_func.call_args.kwargs
        for key, value in expected_params.items():
            assert key in call_kwargs, f"Expected parameter '{key}' not in call"
            assert call_kwargs[key] == value, f"Parameter '{key}' mismatch: expected {value}, got {call_kwargs[key]}"

    @staticmethod
    def assert_response_structure(response: Any, expected_fields: List[str]):
        """Assert that a response has the expected structure."""
        for field in expected_fields:
            assert hasattr(response, field), f"Response missing expected field: {field}"

    @staticmethod
    def assert_valid_http_request(request: Mock, method: str, path: str):
        """Assert that an HTTP request has valid parameters."""
        assert request.method == method
        assert path in str(request.url)


@pytest.fixture
def assertion_helpers():
    """Provide assertion helpers for tests."""
    return AssertionHelpers()


# ================================================================================
# Test Markers
# ================================================================================
# Markers are already defined in pyproject.toml[tool.pytest.ini_options.markers]