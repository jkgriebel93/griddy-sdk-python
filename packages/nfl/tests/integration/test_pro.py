import pytest

from griddy_nfl import GriddyNFL
from griddy_nfl.settings import NFL


@pytest.mark.integration
class TestProAPI:
    """
    Only test a few basic routes for now to verify that the NFL hasn't changed anything fundemental
    """

    @pytest.fixture(scope="class")
    def nfl(self):
        return GriddyNFL(
            login_email=NFL["login_email"],
            login_password=NFL["login_password"],
            headless_login=True,
        )

    def test_content(self, nfl):
        insights_result = nfl.content.get_season_insights(season=2025)
        assert len(insights_result) > 0

    def test_games(self, nfl):
        game_detail = nfl.games.get_scheduled_game(game_id="2025102610")
        assert game_detail is not None
        assert game_detail.home_display_name == "Pittsburgh Steelers"
        assert game_detail.visitor_display_name == "Green Bay Packers"

    def test_players(self, nfl):
        player_detail = nfl.players.get_player(nfl_id=28963)
        assert player_detail is not None
        assert player_detail["display_name"] == "Ben Roethlisberger"
        assert player_detail["uniform_number"] == "7"

    def test_schedules(self, nfl):
        schedule_result = nfl.schedules.get_scheduled_games(
            season=2025, season_type="REG", week=1
        )
        assert schedule_result is not None
        assert len(schedule_result.games) == 16

    def test_teams(self, nfl):
        teams_result = nfl.teams.get_all_teams()
        assert len(teams_result) > 0
        steelers = [tm for tm in teams_result if tm.abbr == "PIT"]
        assert len(steelers) == 1
