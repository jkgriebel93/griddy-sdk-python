"""Tests for NFL client."""

import pytest
import requests_mock
from datetime import datetime

from griddy import settings
from griddy.nfl.client import NFLClient
from griddy.nfl.models_original import NFLGame, NFLTeam, NFLPlayer


class TestNFLClient:
    """Test cases for NFLClient class."""

    def test_initialization(self):
        """Test NFLClient initialization."""
        client = NFLClient()

        assert client.base_url == settings.NFL.get("base_api_url")
        assert "application/json" in client.session.headers["Accept"]


if __name__ == "__main__":
    pytest.main([__file__])
