"""Tests for PFF client."""

from datetime import datetime

import pytest
import requests_mock

from griddy.pff.client import PFFClient
from griddy.pff.models import PFFPlayerGrades, PFFSeasonSummary, PFFTeamGrades


class TestPFFClient:
    """Test cases for PFFClient class."""

    def test_initialization_without_api_key(self):
        """Test PFFClient initialization without API key."""
        client = PFFClient()

        assert client.base_url == "https://api.pff.com/v1"
        assert "application/json" in client.session.headers["Accept"]
        assert "Authorization" not in client.session.headers

    def test_initialization_with_api_key(self):
        """Test PFFClient initialization with API key."""
        api_key = "test_api_key_123"
        client = PFFClient(api_key=api_key)

        assert client.base_url == "https://api.pff.com/v1"
        assert client.session.headers["Authorization"] == f"Bearer {api_key}"

    @requests_mock.Mocker()
    def test_get_player_grades_success(self, m):
        """Test successful player grades retrieval."""
        client = PFFClient()
        mock_response = {
            "grades": {
                "playerId": "player123",
                "pffId": "pff123",
                "season": 2024,
                "week": 1,
                "team": "KC",
                "position": "QB",
                "overallGrade": 92.5,
                "overallRank": 1,
                "snapsPlayed": 65,
                "snapPercentage": 98.5,
                "passing": {
                    "overallGrade": 94.2,
                    "accuracyGrade": 91.8,
                    "deepBallGrade": 88.5,
                    "pocketGrade": 95.1,
                    "bigTimeThrows": 3,
                    "turnoverWorthyPlays": 0,
                },
            }
        }

        m.get(
            "https://api.pff.com/v1/players/player123/grades?season=2024&week=1",
            json=mock_response,
        )

        grades = client.get_player_grades("player123", season=2024, week=1)

        assert grades is not None
        assert grades.player_id == "player123"
        assert grades.overall_grade == 92.5
        assert grades.overall_rank == 1
        assert grades.snaps_played == 65
        assert grades.passing is not None
        assert grades.passing.overall_grade == 94.2
        assert grades.passing.big_time_throws == 3

    @requests_mock.Mocker()
    def test_get_player_grades_season_totals(self, m):
        """Test player grades retrieval for season totals."""
        client = PFFClient()
        mock_response = {
            "grades": {
                "playerId": "player123",
                "season": 2024,
                "team": "KC",
                "position": "QB",
                "overallGrade": 89.7,
                "snapsPlayed": 1024,
                "rushing": {
                    "overallGrade": 75.3,
                    "visionGrade": 78.1,
                    "forcedMissedTackles": 12,
                    "yardsAfterContact": 2.8,
                },
            }
        }

        m.get(
            "https://api.pff.com/v1/players/player123/grades?season=2024",
            json=mock_response,
        )

        grades = client.get_player_grades("player123", season=2024)

        assert grades is not None
        assert grades.week is None  # Season totals
        assert grades.overall_grade == 89.7
        assert grades.rushing is not None
        assert grades.rushing.forced_missed_tackles == 12

    @requests_mock.Mocker()
    def test_get_team_grades_success(self, m):
        """Test successful team grades retrieval."""
        client = PFFClient()
        mock_response = {
            "grades": {
                "overallOffenseGrade": 85.2,
                "overallDefenseGrade": 78.9,
                "overallSpecialTeamsGrade": 72.4,
                "passingOffenseGrade": 88.1,
                "rushingOffenseGrade": 82.3,
                "passDefenseGrade": 81.5,
                "runDefenseGrade": 76.2,
                "pressureRate": 28.5,
                "redZoneEfficiency": 65.8,
            }
        }

        m.get(
            "https://api.pff.com/v1/teams/KC/grades?season=2024&week=1",
            json=mock_response,
        )

        grades = client.get_team_grades("KC", season=2024, week=1)

        assert grades is not None
        assert grades.team_id == "KC"
        assert grades.season == 2024
        assert grades.week == 1
        assert grades.overall_offense_grade == 85.2
        assert grades.overall_defense_grade == 78.9
        assert grades.pressure_rate == 28.5

    @requests_mock.Mocker()
    def test_get_position_rankings_success(self, m):
        """Test successful position rankings retrieval."""
        client = PFFClient()
        mock_response = {
            "rankings": [
                {
                    "playerId": "player1",
                    "season": 2024,
                    "position": "QB",
                    "overallGrade": 92.5,
                    "overallRank": 1,
                    "snapsPlayed": 650,
                },
                {
                    "playerId": "player2",
                    "season": 2024,
                    "position": "QB",
                    "overallGrade": 89.3,
                    "overallRank": 2,
                    "snapsPlayed": 598,
                },
            ]
        }

        m.get(
            "https://api.pff.com/v1/rankings?position=QB&season=2024&limit=50",
            json=mock_response,
        )

        rankings = client.get_position_rankings("QB", season=2024)

        assert len(rankings) == 2
        assert rankings[0].overall_grade == 92.5
        assert rankings[0].overall_rank == 1
        assert rankings[1].overall_grade == 89.3
        assert rankings[1].overall_rank == 2

    @requests_mock.Mocker()
    def test_get_season_summary_success(self, m):
        """Test successful season summary retrieval."""
        client = PFFClient()
        mock_response = {
            "summary": {
                "team": "KC",
                "position": "QB",
                "gamesPlayed": 17,
                "snapsPlayed": 1024,
                "overallGrade": 89.7,
                "positionRank": 2,
                "pffAllPro": "First Team",
                "teamOfTheWeekAwards": 4,
                "playerOfTheWeekAwards": 1,
                "highestGradedGame": 95.2,
                "lowestGradedGame": 78.1,
                "passingGrade": 91.3,
                "consistencyRating": 88.5,
            }
        }

        m.get(
            "https://api.pff.com/v1/players/player123/seasons/2024", json=mock_response
        )

        summary = client.get_season_summary("player123", 2024)

        assert summary is not None
        assert summary.player_id == "player123"
        assert summary.season == 2024
        assert summary.team == "KC"
        assert summary.games_played == 17
        assert summary.overall_grade == 89.7
        assert summary.pff_all_pro == "First Team"
        assert summary.team_of_the_week_awards == 4

    @requests_mock.Mocker()
    def test_get_player_grades_not_found(self, m):
        """Test player grades retrieval when player not found."""
        client = PFFClient()

        m.get(
            "https://api.pff.com/v1/players/invalid/grades?season=2024", status_code=404
        )

        grades = client.get_player_grades("invalid", season=2024)
        assert grades is None

    @requests_mock.Mocker()
    def test_get_all_pro_teams_success(self, m):
        """Test All-Pro teams retrieval."""
        client = PFFClient()
        mock_response = {
            "teams": {
                "first_team": [
                    {
                        "id": "player1",
                        "name": "Player One",
                        "position": "QB",
                        "team": "KC",
                    }
                ],
                "second_team": [
                    {
                        "id": "player2",
                        "name": "Player Two",
                        "position": "QB",
                        "team": "BUF",
                    }
                ],
            }
        }

        m.get("https://api.pff.com/v1/awards/all-pro/2024", json=mock_response)

        teams = client.get_all_pro_teams(2024)

        assert "first_team" in teams
        assert "second_team" in teams
        assert len(teams["first_team"]) == 1
        assert len(teams["second_team"]) == 1
        assert teams["first_team"][0].name == "Player One"

    @requests_mock.Mocker()
    def test_get_draft_board_success(self, m):
        """Test draft board retrieval."""
        client = PFFClient()
        mock_response = {
            "prospects": [
                {
                    "id": "prospect1",
                    "name": "Top Prospect",
                    "position": "QB",
                    "college": "Alabama",
                    "pffGrade": 92.5,
                    "draftRanking": 1,
                    "positionRanking": 1,
                    "roundProjection": 1,
                    "strengths": ["Arm strength", "Accuracy"],
                    "weaknesses": ["Mobility"],
                }
            ]
        }

        m.get("https://api.pff.com/v1/draft/2024/board?limit=100", json=mock_response)

        prospects = client.get_draft_board(2024)

        assert len(prospects) == 1
        assert prospects[0].name == "Top Prospect"
        assert prospects[0].pff_grade == 92.5
        assert prospects[0].draft_ranking == 1
        assert "Arm strength" in prospects[0].strengths

    def test_parse_player_grades_with_minimal_data(self):
        """Test player grades parsing with minimal data."""
        client = PFFClient()
        grades_data = {
            "playerId": "test_player",
            "season": 2024,
            "team": "KC",
            "position": "QB",
            "overallGrade": 85.0,
            "snapsPlayed": 500,
        }

        grades = client._parse_player_grades(grades_data)

        assert grades is not None
        assert grades.player_id == "test_player"
        assert grades.overall_grade == 85.0
        assert grades.snaps_played == 500
        assert grades.passing is None  # No passing data provided

    def test_parse_player_grades_with_invalid_data(self):
        """Test player grades parsing with invalid data."""
        client = PFFClient()

        # Missing required fields should return None
        grades = client._parse_player_grades({})
        assert grades is None

    @requests_mock.Mocker()
    def test_get_pressure_leaders_success(self, m):
        """Test pressure leaders retrieval."""
        client = PFFClient()
        mock_response = {
            "leaders": [
                {
                    "playerId": "rusher1",
                    "season": 2024,
                    "position": "EDGE",
                    "overallGrade": 91.2,
                    "snapsPlayed": 600,
                    "defense": {
                        "passRushGrade": 93.5,
                        "pressureRate": 18.5,
                        "passRushWinRate": 22.3,
                    },
                }
            ]
        }

        m.get(
            "https://api.pff.com/v1/leaders?category=pressure&position=EDGE&season=2024&limit=20",
            json=mock_response,
        )

        leaders = client.get_pressure_leaders(2024, "EDGE")

        assert len(leaders) == 1
        assert leaders[0].player_id == "rusher1"
        assert leaders[0].defense is not None
        assert leaders[0].defense.pass_rush_grade == 93.5


if __name__ == "__main__":
    pytest.main([__file__])
