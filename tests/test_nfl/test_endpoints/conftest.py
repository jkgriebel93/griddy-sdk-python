"""Pytest configuration for NFL SDK endpoint tests."""

import pytest
from unittest.mock import Mock, patch
import httpx
from typing import Dict, Any, Optional


@pytest.fixture
def mock_sdk_configuration():
    """Create a mock SDK configuration for testing."""
    config = Mock()
    config.client = Mock(spec=httpx.Client)
    config.async_client = Mock(spec=httpx.AsyncClient)
    config.timeout_ms = 30000
    config.retry_config = Mock()
    config.security = None
    config.user_agent = "griddy-sdk-test/1.0"
    config.debug_logger = Mock()
    config.debug_logger.debug = Mock()

    # Mock hooks
    hooks = Mock()
    hooks.before_request = Mock(side_effect=lambda ctx, req: req)
    hooks.after_success = Mock(side_effect=lambda ctx, res: res)
    hooks.after_error = Mock(return_value=(None, None))
    config.__dict__["_hooks"] = hooks

    return config


@pytest.fixture
def mock_http_response():
    """Create a mock HTTP response for successful requests."""
    response = Mock(spec=httpx.Response)
    response.status_code = 200
    response.headers = {"content-type": "application/json"}
    response.text = '{"success": true}'
    response.content = b'{"success": true}'
    response.json = Mock(return_value={"success": True})
    response.url = "https://api.example.com/test"
    response.is_error = False
    response.is_success = True
    return response


@pytest.fixture
def mock_error_response():
    """Create a mock HTTP response for error requests."""
    response = Mock(spec=httpx.Response)
    response.status_code = 400
    response.headers = {"content-type": "application/json"}
    response.text = '{"error": "Bad Request"}'
    response.content = b'{"error": "Bad Request"}'
    response.json = Mock(return_value={"error": "Bad Request"})
    response.url = "https://api.example.com/test"
    response.is_error = True
    response.is_success = False
    return response


@pytest.fixture
def mock_httpx_client(mock_http_response):
    """Create a mock httpx client that returns successful responses."""
    client = Mock(spec=httpx.Client)
    client.build_request = Mock(return_value=Mock(spec=httpx.Request))
    client.send = Mock(return_value=mock_http_response)
    return client


def create_mock_response(
    data: Dict[str, Any],
    status_code: int = 200,
    headers: Optional[Dict[str, str]] = None
) -> Mock:
    """
    Helper function to create a mock HTTP response with custom data.

    Args:
        data: Response data dictionary
        status_code: HTTP status code
        headers: Optional response headers

    Returns:
        Mock httpx.Response object
    """
    response = Mock(spec=httpx.Response)
    response.status_code = status_code
    response.headers = headers or {"content-type": "application/json"}
    response.json = Mock(return_value=data)
    response.text = str(data)
    response.content = str(data).encode()
    response.is_error = status_code >= 400
    response.is_success = 200 <= status_code < 300
    return response


@pytest.fixture
def sample_player_stats():
    """Sample player statistics data for testing."""
    return {
        "playerId": "player123",
        "season": 2024,
        "week": 1,
        "seasonType": "regular",
        "passingYards": 350,
        "passingTouchdowns": 3,
        "interceptions": 0,
        "completions": 28,
        "attempts": 38,
        "rushingYards": 25,
        "rushingTouchdowns": 0,
    }


@pytest.fixture
def sample_team_stats():
    """Sample team statistics data for testing."""
    return {
        "teamId": "KC",
        "season": 2024,
        "week": 1,
        "totalYards": 425,
        "passingYards": 325,
        "rushingYards": 100,
        "pointsScored": 31,
        "turnovers": 1,
        "firstDowns": 24,
    }


@pytest.fixture
def sample_game_schedule():
    """Sample game schedule data for testing."""
    return {
        "gameId": "game123",
        "season": 2024,
        "week": 1,
        "seasonType": "regular",
        "homeTeam": "KC",
        "awayTeam": "BUF",
        "gameTime": "2024-09-05T20:20:00Z",
        "venue": "GEHA Field at Arrowhead Stadium",
        "status": "scheduled",
    }


@pytest.fixture
def sample_defensive_stats():
    """Sample defensive statistics data for testing."""
    return {
        "playerId": "def123",
        "season": 2024,
        "week": 1,
        "tackles": 12,
        "soloTackles": 8,
        "assistedTackles": 4,
        "sacks": 2.0,
        "interceptions": 1,
        "passDeflections": 3,
        "forcedFumbles": 1,
    }


@pytest.fixture
def sample_betting_odds():
    """Sample betting odds data for testing."""
    return {
        "gameId": "game123",
        "homeTeam": "KC",
        "awayTeam": "BUF",
        "spread": -3.5,
        "overUnder": 47.5,
        "homeMoneyline": -175,
        "awayMoneyline": 155,
    }


class MockSDKHelper:
    """Helper class for mocking SDK behavior in tests."""

    @staticmethod
    def mock_successful_request(sdk_instance, response_data: Dict[str, Any]):
        """
        Mock a successful SDK request.

        Args:
            sdk_instance: The SDK instance to mock
            response_data: Data to return in the response
        """
        mock_response = create_mock_response(response_data)
        sdk_instance.sdk_configuration.client.send = Mock(return_value=mock_response)
        return mock_response

    @staticmethod
    def mock_error_request(sdk_instance, status_code: int = 400, error_message: str = "Bad Request"):
        """
        Mock a failed SDK request.

        Args:
            sdk_instance: The SDK instance to mock
            status_code: HTTP error status code
            error_message: Error message to return
        """
        error_data = {"error": error_message}
        mock_response = create_mock_response(error_data, status_code=status_code)
        sdk_instance.sdk_configuration.client.send = Mock(return_value=mock_response)
        return mock_response


@pytest.fixture
def mock_sdk_helper():
    """Provide MockSDKHelper instance for tests."""
    return MockSDKHelper()


# Markers for different test categories
def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "endpoint: mark test as an endpoint test"
    )
    config.addinivalue_line(
        "markers", "player_stats: mark test as player statistics endpoint test"
    )
    config.addinivalue_line(
        "markers", "team_stats: mark test as team statistics endpoint test"
    )
    config.addinivalue_line(
        "markers", "defensive_stats: mark test as defensive statistics endpoint test"
    )
    config.addinivalue_line(
        "markers", "schedules: mark test as schedule endpoint test"
    )
    config.addinivalue_line(
        "markers", "game_data: mark test as game data endpoint test"
    )
    config.addinivalue_line(
        "markers", "content: mark test as content endpoint test"
    )
    config.addinivalue_line(
        "markers", "async_: mark test as asynchronous test"
    )
