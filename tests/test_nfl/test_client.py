"""Tests for NFL client."""

from datetime import datetime

import pytest
import requests_mock

from griddy.nfl.client import NFLClient
from griddy.nfl.models import NFLGame, NFLPlayer, NFLTeam


class TestNFLClient:
    """Test cases for NFLClient class."""

    def test_initialization(self):
        """Test NFLClient initialization."""
        client = NFLClient()

        assert client.base_url == "https://api.nfl.com"
        assert "application/json" in client.session.headers["Accept"]

    @requests_mock.Mocker()
    def test_get_games_success(self, m):
        """Test successful games retrieval."""
        client = NFLClient()
        mock_response = {
            "games": [
                {
                    "id": "game1",
                    "homeTeam": {"abbreviation": "KC"},
                    "awayTeam": {"abbreviation": "BUF"},
                    "homeScore": 24,
                    "awayScore": 20,
                    "status": "final",
                    "week": 1,
                    "season": 2024,
                    "seasonType": "regular",
                }
            ]
        }

        m.get(
            "https://api.nfl.com/games?season=2024&seasonType=regular&week=1",
            json=mock_response,
        )

        games = client.get_games(season=2024, week=1)

        assert len(games) == 1
        assert games[0].id == "game1"
        assert games[0].home_team == "KC"
        assert games[0].away_team == "BUF"
        assert games[0].home_score == 24
        assert games[0].away_score == 20

    @requests_mock.Mocker()
    def test_get_games_empty_response(self, m):
        """Test games retrieval with empty response."""
        client = NFLClient()

        m.get(
            "https://api.nfl.com/games?season=2024&seasonType=regular",
            json={"games": []},
        )

        games = client.get_games(season=2024)
        assert games == []

    @requests_mock.Mocker()
    def test_get_games_api_error(self, m):
        """Test games retrieval with API error."""
        client = NFLClient()

        m.get(
            "https://api.nfl.com/games?season=2024&seasonType=regular", status_code=500
        )

        games = client.get_games(season=2024)
        assert games == []

    @requests_mock.Mocker()
    def test_get_teams_success(self, m):
        """Test successful teams retrieval."""
        client = NFLClient()
        mock_response = {
            "teams": [
                {
                    "id": "KC",
                    "name": "Kansas City Chiefs",
                    "abbreviation": "KC",
                    "city": "Kansas City",
                    "conference": "AFC",
                    "division": "West",
                }
            ]
        }

        m.get("https://api.nfl.com/teams", json=mock_response)

        teams = client.get_teams()

        assert len(teams) == 1
        assert teams[0].id == "KC"
        assert teams[0].name == "Kansas City Chiefs"
        assert teams[0].abbreviation == "KC"

    @requests_mock.Mocker()
    def test_get_team_success(self, m):
        """Test successful single team retrieval."""
        client = NFLClient()
        mock_response = {
            "team": {
                "id": "KC",
                "name": "Kansas City Chiefs",
                "abbreviation": "KC",
                "city": "Kansas City",
            }
        }

        m.get("https://api.nfl.com/teams/KC", json=mock_response)

        team = client.get_team("KC")

        assert team is not None
        assert team.id == "KC"
        assert team.name == "Kansas City Chiefs"

    @requests_mock.Mocker()
    def test_get_team_not_found(self, m):
        """Test team retrieval when team not found."""
        client = NFLClient()

        m.get("https://api.nfl.com/teams/INVALID", status_code=404)

        team = client.get_team("INVALID")
        assert team is None

    @requests_mock.Mocker()
    def test_get_players_success(self, m):
        """Test successful players retrieval."""
        client = NFLClient()
        mock_response = {
            "players": [
                {
                    "id": "player1",
                    "name": "Patrick Mahomes",
                    "teamId": "KC",
                    "position": "QB",
                    "jerseyNumber": 15,
                }
            ]
        }

        m.get("https://api.nfl.com/players?status=active&team=KC", json=mock_response)

        players = client.get_players(team="KC")

        assert len(players) == 1
        assert players[0].id == "player1"
        assert players[0].name == "Patrick Mahomes"
        assert players[0].position == "QB"

    @requests_mock.Mocker()
    def test_get_player_stats_success(self, m):
        """Test successful player stats retrieval."""
        client = NFLClient()
        mock_response = {
            "stats": [
                {
                    "season": 2024,
                    "week": 1,
                    "passingYards": 300,
                    "passingTouchdowns": 3,
                    "interceptions": 0,
                }
            ]
        }

        m.get(
            "https://api.nfl.com/players/player1/stats?season=2024&seasonType=regular&week=1",
            json=mock_response,
        )

        stats = client.get_player_stats("player1", season=2024, week=1)

        assert len(stats) == 1
        assert stats[0].player_id == "player1"
        assert stats[0].season == 2024
        assert stats[0].week == 1
        assert stats[0].passing_yards == 300

    def test_parse_game_with_minimal_data(self):
        """Test game parsing with minimal data."""
        client = NFLClient()
        game_data = {
            "id": "test_game",
            "homeTeam": {"abbreviation": "KC"},
            "awayTeam": {"abbreviation": "BUF"},
            "status": "scheduled",
        }

        game = client._parse_game(game_data)

        assert game is not None
        assert game.id == "test_game"
        assert game.home_team == "KC"
        assert game.away_team == "BUF"
        assert game.status == "scheduled"

    def test_parse_game_with_invalid_data(self):
        """Test game parsing with invalid data."""
        client = NFLClient()

        # Missing required fields should return None
        game = client._parse_game({})
        assert game is None

    def test_parse_team_with_minimal_data(self):
        """Test team parsing with minimal data."""
        client = NFLClient()
        team_data = {"id": "KC", "name": "Kansas City Chiefs", "abbreviation": "KC"}

        team = client._parse_team(team_data)

        assert team is not None
        assert team.id == "KC"
        assert team.name == "Kansas City Chiefs"
        assert team.abbreviation == "KC"


if __name__ == "__main__":
    pytest.main([__file__])
