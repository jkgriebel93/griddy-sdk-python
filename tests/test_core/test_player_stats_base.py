"""Unit tests for the PlayerStatsBase._make_stats_config helper."""

from dataclasses import dataclass
from typing import Mapping, Optional

import pytest

from griddy.core._constants import STATS_ERROR_CODES
from griddy.core.basesdk import EndpointConfig
from griddy.nfl.endpoints.pro.stats.base import PlayerStatsBase

# ---------------------------------------------------------------------------
# Minimal stubs
# ---------------------------------------------------------------------------


@dataclass
class FakeRequest:
    season: int
    season_type: str
    limit: int = 35


class FakeResponse:
    pass


class FakePlayerStats(PlayerStatsBase):
    """Concrete subclass for testing (avoids SDKConfiguration requirement)."""

    def __init__(self):
        # Bypass ProSDK.__init__ — we only need _make_stats_config
        pass


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


@pytest.mark.unit
class TestMakeStatsConfig:
    def setup_method(self):
        self.obj = FakePlayerStats()

    def test_returns_endpoint_config(self):
        config = self.obj._make_stats_config(
            "/api/stats/test/season",
            "getTestBySeason",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
        )
        assert isinstance(config, EndpointConfig)

    def test_method_is_get(self):
        config = self.obj._make_stats_config(
            "/api/stats/test/season",
            "getTestBySeason",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
        )
        assert config.method == "GET"

    def test_path_and_operation_id(self):
        config = self.obj._make_stats_config(
            "/api/stats/passing/week",
            "getPassingByWeek",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
        )
        assert config.path == "/api/stats/passing/week"
        assert config.operation_id == "getPassingByWeek"

    def test_request_constructed_from_kwargs(self):
        config = self.obj._make_stats_config(
            "/path",
            "op",
            FakeRequest,
            FakeResponse,
            season=2023,
            season_type="POST",
            limit=50,
        )
        assert isinstance(config.request, FakeRequest)
        assert config.request.season == 2023
        assert config.request.season_type == "POST"
        assert config.request.limit == 50

    def test_response_type_set(self):
        config = self.obj._make_stats_config(
            "/path",
            "op",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
        )
        assert config.response_type is FakeResponse

    def test_error_status_codes(self):
        config = self.obj._make_stats_config(
            "/path",
            "op",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
        )
        assert config.error_status_codes == STATS_ERROR_CODES

    def test_return_raw_json_is_false(self):
        config = self.obj._make_stats_config(
            "/path",
            "op",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
        )
        assert config.return_raw_json is False

    def test_server_url_forwarded(self):
        config = self.obj._make_stats_config(
            "/path",
            "op",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
            server_url="https://custom.example.com",
        )
        assert config.server_url == "https://custom.example.com"

    def test_timeout_ms_forwarded(self):
        config = self.obj._make_stats_config(
            "/path",
            "op",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
            timeout_ms=5000,
        )
        assert config.timeout_ms == 5000

    def test_http_headers_forwarded(self):
        headers = {"X-Custom": "value"}
        config = self.obj._make_stats_config(
            "/path",
            "op",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
            http_headers=headers,
        )
        assert config.http_headers == headers

    def test_config_keys_not_in_request(self):
        """server_url, timeout_ms, http_headers, retries should NOT leak into request."""
        config = self.obj._make_stats_config(
            "/path",
            "op",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
            server_url="https://example.com",
            timeout_ms=1000,
            http_headers={"X": "Y"},
        )
        req = config.request
        assert not hasattr(req, "server_url")
        assert not hasattr(req, "timeout_ms")
        assert not hasattr(req, "http_headers")

    def test_defaults_when_config_keys_omitted(self):
        config = self.obj._make_stats_config(
            "/path",
            "op",
            FakeRequest,
            FakeResponse,
            season=2024,
            season_type="REG",
        )
        assert config.server_url is None
        assert config.timeout_ms is None
        assert config.http_headers is None
