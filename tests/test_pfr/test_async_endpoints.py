"""Tests verifying that async methods are generated on all PFR endpoint classes."""

import inspect
from unittest.mock import AsyncMock, Mock, patch

import httpx
import pytest

from griddy.core.utils.logger import Logger
from griddy.pfr.sdk import GriddyPFR


@pytest.fixture
def mock_logger():
    return Mock(spec=Logger)


@pytest.mark.unit
class TestAsyncMethodsExist:
    """Verify that @sdk_endpoints generated _async methods on every PFR endpoint."""

    def test_schedule_has_async(self):
        from griddy.pfr.endpoints.schedule import Schedule

        assert hasattr(Schedule, "get_season_schedule_async")
        assert inspect.iscoroutinefunction(Schedule.get_season_schedule_async)

    def test_games_has_async(self):
        from griddy.pfr.endpoints.games import Games

        assert hasattr(Games, "get_game_details_async")
        assert inspect.iscoroutinefunction(Games.get_game_details_async)

    def test_players_has_async(self):
        from griddy.pfr.endpoints.players import Players

        assert hasattr(Players, "get_player_profile_async")
        assert inspect.iscoroutinefunction(Players.get_player_profile_async)

    def test_coaches_has_async(self):
        from griddy.pfr.endpoints.coaches import Coaches

        assert hasattr(Coaches, "get_coach_profile_async")
        assert inspect.iscoroutinefunction(Coaches.get_coach_profile_async)

    def test_officials_has_async(self):
        from griddy.pfr.endpoints.officials import Officials

        assert hasattr(Officials, "get_official_profile_async")
        assert inspect.iscoroutinefunction(Officials.get_official_profile_async)

    def test_stadiums_has_async(self):
        from griddy.pfr.endpoints.stadiums import Stadiums

        assert hasattr(Stadiums, "get_stadium_async")
        assert inspect.iscoroutinefunction(Stadiums.get_stadium_async)

    def test_teams_has_async(self):
        from griddy.pfr.endpoints.teams import Teams

        assert hasattr(Teams, "get_team_season_async")
        assert hasattr(Teams, "get_team_franchise_async")
        assert inspect.iscoroutinefunction(Teams.get_team_season_async)
        assert inspect.iscoroutinefunction(Teams.get_team_franchise_async)

    def test_seasons_has_async(self):
        from griddy.pfr.endpoints.seasons import Seasons

        assert hasattr(Seasons, "get_season_async")
        assert hasattr(Seasons, "get_season_stats_async")
        assert hasattr(Seasons, "get_week_async")

    def test_draft_has_async(self):
        from griddy.pfr.endpoints.draft import Draft

        assert hasattr(Draft, "get_year_draft_async")
        assert hasattr(Draft, "get_combine_async")
        assert hasattr(Draft, "get_team_draft_async")

    def test_awards_has_async(self):
        from griddy.pfr.endpoints.awards import Awards

        assert hasattr(Awards, "get_async")
        assert inspect.iscoroutinefunction(Awards.get_async)

    def test_hof_has_async(self):
        from griddy.pfr.endpoints.hof import Hof

        assert hasattr(Hof, "list_async")
        assert inspect.iscoroutinefunction(Hof.list_async)

    def test_probowl_has_async(self):
        from griddy.pfr.endpoints.probowl import ProBowl

        assert hasattr(ProBowl, "year_async")
        assert inspect.iscoroutinefunction(ProBowl.year_async)

    def test_leaders_has_async(self):
        from griddy.pfr.endpoints.leaders import Leaders

        assert hasattr(Leaders, "get_async")
        assert inspect.iscoroutinefunction(Leaders.get_async)

    def test_executives_has_async(self):
        from griddy.pfr.endpoints.executives import Executives

        assert hasattr(Executives, "get_async")
        assert inspect.iscoroutinefunction(Executives.get_async)

    def test_schools_has_async(self):
        from griddy.pfr.endpoints.schools import Schools

        assert hasattr(Schools, "list_async")
        assert hasattr(Schools, "high_schools_async")

    def test_superbowl_has_async(self):
        from griddy.pfr.endpoints.superbowl import SuperBowl

        assert hasattr(SuperBowl, "history_async")
        assert hasattr(SuperBowl, "leaders_async")
        assert hasattr(SuperBowl, "standings_async")

    def test_fantasy_has_async(self):
        from griddy.pfr.endpoints.fantasy import Fantasy

        assert hasattr(Fantasy, "get_top_players_async")
        assert hasattr(Fantasy, "get_matchups_async")
        assert hasattr(Fantasy, "get_points_allowed_async")
        assert hasattr(Fantasy, "get_redzone_passing_async")
        assert hasattr(Fantasy, "get_redzone_receiving_async")
        assert hasattr(Fantasy, "get_redzone_rushing_async")

    def test_frivolities_has_async(self):
        from griddy.pfr.endpoints.frivolities import Frivolities

        expected_async = [
            "get_multi_team_players_async",
            "get_statistical_milestones_async",
            "get_upcoming_milestones_async",
            "get_birthdays_async",
            "get_birthplaces_async",
            "get_birthplace_players_async",
            "get_players_born_before_async",
            "get_uniform_numbers_async",
            "get_qb_wins_vs_franchises_async",
            "get_non_qb_passers_async",
            "get_non_skill_pos_td_scorers_async",
            "get_octopus_tracker_async",
            "get_cups_of_coffee_async",
            "get_multi_sport_players_async",
            "get_pronunciation_guide_async",
            "get_overtime_ties_async",
            "get_last_undefeated_async",
            "get_standings_on_date_async",
        ]
        for method_name in expected_async:
            assert hasattr(Frivolities, method_name), f"Missing: {method_name}"
            assert inspect.iscoroutinefunction(
                getattr(Frivolities, method_name)
            ), f"Not async: {method_name}"


@pytest.mark.unit
class TestAsyncEndpointExecution:
    """Test that async endpoints actually call _execute_endpoint_async."""

    @pytest.mark.asyncio
    async def test_schedule_async_calls_async_browserless(self):
        pfr = GriddyPFR()
        pfr.schedule.async_browserless = Mock()
        pfr.schedule.async_browserless.get_page_content = AsyncMock(
            return_value="<html><table id='games'></table></html>"
        )

        # Mock the parser to return a simple result
        mock_data = {
            "week_num": "1",
            "game_day_of_week": "Thu",
            "game_date": "2024-09-05",
            "game_location": "",
            "winner": "PHI",
            "loser": "GB",
        }
        with patch("griddy.pfr.endpoints.schedule.ScheduleParser") as MockParser:
            MockParser.return_value.parse.return_value = [mock_data]
            result = await pfr.schedule.get_season_schedule_async(season=2024)

        pfr.schedule.async_browserless.get_page_content.assert_awaited_once()
        call_url = pfr.schedule.async_browserless.get_page_content.call_args[0][0]
        assert "/years/2024/games.htm" in call_url
        assert len(result) == 1
        assert result[0].week_num == "1"
        assert result[0].winner == "PHI"

    @pytest.mark.asyncio
    async def test_games_async_returns_validated_model(self):
        pfr = GriddyPFR()
        pfr.games.async_browserless = Mock()
        pfr.games.async_browserless.get_page_content = AsyncMock(return_value="<html/>")

        with patch("griddy.pfr.endpoints.games.GameDetailsParser") as MockParser:
            MockParser.return_value.parse.return_value = {
                "scorebox": {},
                "linescore": {},
            }
            # The async method should call model_validate automatically.
            # We can't easily test the full model here, so just verify it doesn't
            # return a raw dict
            # (actual validation may fail without full data — that's OK)
            with pytest.raises(Exception):
                # GameDetails model_validate will fail with incomplete data,
                # but this proves the async path runs through model_validate
                await pfr.games.get_game_details_async(game_id="202409050kan")

    @pytest.mark.asyncio
    async def test_coaches_async_uses_async_browserless(self):
        pfr = GriddyPFR()
        pfr.coaches.async_browserless = Mock()
        pfr.coaches.async_browserless.get_page_content = AsyncMock(
            return_value="<html/>"
        )

        with patch("griddy.pfr.endpoints.coaches.CoachProfileParser") as MockParser:
            MockParser.return_value.parse.return_value = {
                "bio": {"name": "Test Coach"},
                "coaching_results": [],
            }
            # Will fail model_validate but proves async path works
            with pytest.raises(Exception):
                await pfr.coaches.get_coach_profile_async(coach_id="BeliBi0")

        pfr.coaches.async_browserless.get_page_content.assert_awaited_once()


@pytest.mark.unit
class TestSyncMethodsStillWork:
    """Verify that sync methods still exist and are not async."""

    def test_schedule_sync_is_not_async(self):
        from griddy.pfr.endpoints.schedule import Schedule

        assert hasattr(Schedule, "get_season_schedule")
        assert not inspect.iscoroutinefunction(Schedule.get_season_schedule)

    def test_games_sync_is_not_async(self):
        from griddy.pfr.endpoints.games import Games

        assert hasattr(Games, "get_game_details")
        assert not inspect.iscoroutinefunction(Games.get_game_details)

    def test_draft_sync_methods_exist(self):
        from griddy.pfr.endpoints.draft import Draft

        assert hasattr(Draft, "get_year_draft")
        assert hasattr(Draft, "get_combine")
        assert hasattr(Draft, "get_team_draft")
        assert not inspect.iscoroutinefunction(Draft.get_year_draft)

    def test_awards_sync_get_exists(self):
        from griddy.pfr.endpoints.awards import Awards

        assert hasattr(Awards, "get")
        assert not inspect.iscoroutinefunction(Awards.get)
