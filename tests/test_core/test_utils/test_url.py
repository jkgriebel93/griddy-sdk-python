"""Tests for griddy.core.utils.url."""

import pytest

from griddy.core.utils.url import build_url


@pytest.mark.unit
class TestBuildUrl:
    def test_basic(self):
        result = build_url("https://api.nfl.com", "games")
        assert result == "https://api.nfl.com/games"

    def test_with_params(self):
        result = build_url("https://api.nfl.com", "games", {"season": 2024})
        assert "season=2024" in result
        assert result.startswith("https://api.nfl.com/games?")

    def test_trailing_slash(self):
        result = build_url("https://api.nfl.com/", "/games")
        assert result == "https://api.nfl.com/games"

    def test_params_with_none_filtered(self):
        result = build_url(
            "https://api.nfl.com", "games", {"season": 2024, "week": None}
        )
        assert "season=2024" in result
        assert "week" not in result

    def test_empty_path(self):
        result = build_url("https://api.nfl.com", "")
        assert result == "https://api.nfl.com"

    def test_no_params(self):
        result = build_url("https://api.nfl.com", "games")
        assert "?" not in result
