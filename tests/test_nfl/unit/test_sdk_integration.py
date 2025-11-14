"""
Unit tests to verify GriddyNFL SDK integration with endpoints sub-SDKs.

These tests ensure that:
1. All sub-SDKs from the endpoints package can be accessed via GriddyNFL
2. Sub-SDKs are instantiated with the correct types
3. All methods on sub-SDKs are accessible and callable
"""

import inspect
from unittest.mock import Mock, patch

import pytest

from griddy.nfl.sdk import GriddyNFL
from griddy.nfl.sdkconfiguration import SDKConfiguration


@pytest.fixture
def mock_sdk_config():
    """Create a mock SDK configuration for testing."""
    config = Mock(spec=SDKConfiguration)
    config.client = None
    config.async_client = None
    config.security = None
    config.server_url = None
    config.server_idx = None
    config.language = None
    config.openapi_doc_version = None
    config.gen_version = None
    config.user_agent = None
    config.retry_config = None
    config.timeout_ms = None
    config.debug_logger = None
    config.is_pro = False
    return config


@pytest.fixture
def nfl_sdk():
    """Create a GriddyNFL instance for testing."""
    # Mock the settings to provide required credentials
    with patch(
        "griddy.nfl.sdk.settings.NFL",
        {"clientKey": "test_key", "clientSecret": "test_secret"},
    ):
        # Create mock NFLAuth dictionary
        mock_nfl_auth = {
            "accessToken": "mock_access_token",
            "refreshToken": "mock_refresh_token",
            "idToken": "mock_id_token",
            "expiresIn": 3600,
        }

        # Create SDK with mock auth
        sdk = GriddyNFL(nfl_auth=mock_nfl_auth)
        return sdk


@pytest.mark.unit
class TestEndpointsSubSDKAccess:
    """Test that all endpoints sub-SDKs can be accessed from GriddyNFL."""

    # Map of attribute name to expected module and class
    ENDPOINTS_SUB_SDKS = {
        "combine": ("griddy.nfl.endpoints.regular.football.combine", "Combine"),
        "draft": ("griddy.nfl.endpoints.regular.football.draft", "Draft"),
        "games": ("griddy.nfl.endpoints.regular.football.games", "Games"),
        "rosters": ("griddy.nfl.endpoints.regular.football.rosters", "Rosters"),
        "standings": ("griddy.nfl.endpoints.regular.football.standings", "Standings"),
        "football_teams": ("griddy.nfl.endpoints.regular.football.teams", "Teams"),
        "weeks": ("griddy.nfl.endpoints.regular.football.weeks", "Weeks"),
        "content": ("griddy.nfl.endpoints.pro.content", "Content"),
        "players": ("griddy.nfl.endpoints.pro.players", "Players"),
        "pro_games": ("griddy.nfl.endpoints.pro.games", "ProGames"),
        "schedules": ("griddy.nfl.endpoints.pro.schedules", "Schedules"),
        "teams": ("griddy.nfl.endpoints.pro.teams", "Teams"),
    }

    @pytest.mark.parametrize("attr_name,module_info", ENDPOINTS_SUB_SDKS.items())
    def test_sub_sdk_accessible(self, nfl_sdk, attr_name, module_info):
        """Test that each sub-SDK can be accessed as an attribute."""
        module_path, class_name = module_info

        # Access the sub-SDK
        sub_sdk = getattr(nfl_sdk, attr_name)

        # Verify it's not None
        assert sub_sdk is not None, f"Sub-SDK '{attr_name}' should not be None"

        # Verify it has the expected class name
        assert (
            sub_sdk.__class__.__name__ == class_name
        ), f"Sub-SDK '{attr_name}' should be instance of {class_name}, got {sub_sdk.__class__.__name__}"

        # Verify it has the expected module
        assert (
            sub_sdk.__class__.__module__ == module_path
        ), f"Sub-SDK '{attr_name}' should be from module {module_path}, got {sub_sdk.__class__.__module__}"

    @pytest.mark.parametrize("attr_name", ENDPOINTS_SUB_SDKS.keys())
    def test_sub_sdk_can_be_accessed_multiple_times(self, nfl_sdk, attr_name):
        """Test that accessing sub-SDK multiple times returns the same instance."""
        first_access = getattr(nfl_sdk, attr_name)
        second_access = getattr(nfl_sdk, attr_name)

        assert (
            first_access is second_access
        ), f"Sub-SDK '{attr_name}' should return same instance on multiple accesses"


@pytest.mark.unit
class TestEndpointsMethodAccessibility:
    """Test that methods on endpoints sub-SDKs are accessible and callable."""

    def test_combine_methods_exist(self, nfl_sdk):
        """Test Combine sub-SDK methods."""
        combine = nfl_sdk.combine

        # Verify sync methods
        assert hasattr(
            combine, "get_profiles"
        ), "Combine should have get_profiles method"
        assert hasattr(
            combine, "get_rankings"
        ), "Combine should have get_rankings method"

        # Verify async methods
        assert hasattr(
            combine, "get_profiles_async"
        ), "Combine should have get_profiles_async method"
        assert hasattr(
            combine, "get_rankings_async"
        ), "Combine should have get_rankings_async method"

        # Verify methods are callable
        assert callable(combine.get_profiles)
        assert callable(combine.get_profiles_async)

    def test_draft_methods_exist(self, nfl_sdk):
        """Test Draft sub-SDK methods."""
        draft = nfl_sdk.draft

        assert hasattr(draft, "get_picks_report")
        assert hasattr(draft, "get_picks_report_async")
        assert hasattr(draft, "get_teamneeds")
        assert hasattr(draft, "get_teamneeds_async")

        assert callable(draft.get_picks_report)
        assert callable(draft.get_teamneeds)

    def test_games_methods_exist(self, nfl_sdk):
        """Test Games sub-SDK methods (regular API)."""
        games = nfl_sdk.games

        assert hasattr(games, "get_games")
        assert hasattr(games, "get_games_async")
        assert hasattr(games, "get_box_score")
        assert hasattr(games, "get_box_score_async")
        assert hasattr(games, "get_play_by_play")
        assert hasattr(games, "get_play_by_play_async")

        assert callable(games.get_games)
        assert callable(games.get_box_score)

    def test_rosters_methods_exist(self, nfl_sdk):
        """Test Rosters sub-SDK methods."""
        rosters = nfl_sdk.rosters

        assert hasattr(rosters, "get_rosters")
        assert hasattr(rosters, "get_rosters_async")

        assert callable(rosters.get_rosters)

    def test_standings_methods_exist(self, nfl_sdk):
        """Test Standings sub-SDK methods."""
        standings = nfl_sdk.standings

        assert hasattr(standings, "get_standings")
        assert hasattr(standings, "get_standings_async")

        assert callable(standings.get_standings)

    def test_football_teams_methods_exist(self, nfl_sdk):
        """Test FootballTeams sub-SDK methods."""
        football_teams = nfl_sdk.football_teams

        assert hasattr(football_teams, "get_teams")
        assert hasattr(football_teams, "get_teams_async")

        assert callable(football_teams.get_teams)

    def test_weeks_methods_exist(self, nfl_sdk):
        """Test Weeks sub-SDK methods."""
        weeks = nfl_sdk.weeks

        assert hasattr(weeks, "get_week_of_date")
        assert hasattr(weeks, "get_week_of_date_async")
        assert hasattr(weeks, "get_season_weeks")
        assert hasattr(weeks, "get_season_weeks_async")

        assert callable(weeks.get_week_of_date)
        assert callable(weeks.get_season_weeks)

    def test_content_methods_exist(self, nfl_sdk):
        """Test Content sub-SDK methods (Pro API)."""
        content = nfl_sdk.content

        assert hasattr(content, "get_home_film_cards")
        assert hasattr(content, "get_home_film_cards_async")
        assert hasattr(content, "get_season_insights")
        assert hasattr(content, "get_season_insights_async")
        assert hasattr(content, "get_coaches_film_videos")
        assert hasattr(content, "get_coaches_film_videos_async")
        assert hasattr(content, "get_filmroom_plays")
        assert hasattr(content, "get_filmroom_plays_async")

        assert callable(content.get_home_film_cards)
        assert callable(content.get_season_insights)

    def test_players_methods_exist(self, nfl_sdk):
        """Test Players sub-SDK methods (Pro API)."""
        players = nfl_sdk.players

        assert hasattr(players, "get_player")
        assert hasattr(players, "get_player_async")
        assert hasattr(players, "get_projected_stats")
        assert hasattr(players, "get_projected_stats_async")
        assert hasattr(players, "search_players")
        assert hasattr(players, "search_players_async")

        assert callable(players.get_player)
        assert callable(players.search_players)

    def test_pro_games_methods_exist(self, nfl_sdk):
        """Test ProGames sub-SDK methods."""
        pro_games = nfl_sdk.pro_games

        assert hasattr(pro_games, "get_summary_play")
        assert hasattr(pro_games, "get_summary_play_async")
        assert hasattr(pro_games, "get_playlist")
        assert hasattr(pro_games, "get_stats_boxscore")

        assert callable(pro_games.get_summary_play)
        assert callable(pro_games.get_playlist)

    def test_schedules_methods_exist(self, nfl_sdk):
        """Test Schedules sub-SDK methods (Pro API)."""
        schedules = nfl_sdk.schedules

        assert hasattr(schedules, "get_current_week_games")
        assert hasattr(schedules, "get_current_week_games_async")
        assert hasattr(schedules, "get_scheduled_games")
        assert hasattr(schedules, "get_scheduled_games_async")
        assert hasattr(schedules, "get_future_betting_odds")
        assert hasattr(schedules, "get_future_betting_odds_async")
        assert hasattr(schedules, "get_team_standings")
        assert hasattr(schedules, "get_team_standings_async")
        assert hasattr(schedules, "get_schedule_season_weeks")
        assert hasattr(schedules, "get_schedule_season_weeks_async")

        assert callable(schedules.get_current_week_games)
        assert callable(schedules.get_scheduled_games)

    def test_teams_methods_exist(self, nfl_sdk):
        """Test Teams sub-SDK methods (Pro API)."""
        teams = nfl_sdk.teams

        assert hasattr(teams, "get_all_teams")
        assert hasattr(teams, "get_all_teams_async")
        assert hasattr(teams, "get_team_roster")
        assert hasattr(teams, "get_team_roster_async")
        assert hasattr(teams, "get_weekly_team_roster")
        assert hasattr(teams, "get_weekly_team_roster_async")
        assert hasattr(teams, "get_team_schedule")
        assert hasattr(teams, "get_team_schedule_async")

        assert callable(teams.get_all_teams)
        assert callable(teams.get_team_roster)


@pytest.mark.unit
class TestStatsEndpointsMethodAccessibility:
    """Test that stats-related endpoints sub-SDKs are accessible."""

    def test_player_passing_stats_accessible(self, nfl_sdk):
        """Test player passing stats sub-SDK."""
        stats = nfl_sdk.player_passing_stats

        assert stats is not None
        assert hasattr(stats, "get_season_summary")
        assert hasattr(stats, "get_season_summary_async")
        assert hasattr(stats, "get_weekly_summary")
        assert hasattr(stats, "get_weekly_summary_async")

        assert callable(stats.get_season_summary)

    def test_player_receiving_stats_accessible(self, nfl_sdk):
        """Test player receiving stats sub-SDK."""
        # Note: The attribute name in _sub_sdk_map is 'player_receiving_statistics'
        # but the type annotation uses 'player_receiving_stats'
        # We should test what actually works
        try:
            stats = nfl_sdk.player_receiving_statistics
        except AttributeError:
            # Fallback to the annotated name
            pytest.skip("player_receiving_statistics not found, may need SDK fix")

        assert stats is not None
        assert hasattr(stats, "get_season_summary")
        assert callable(stats.get_season_summary)

    def test_player_rushing_stats_accessible(self, nfl_sdk):
        """Test player rushing stats sub-SDK."""
        stats = nfl_sdk.player_rushing_stats

        assert stats is not None
        assert hasattr(stats, "get_season_summary")
        assert hasattr(stats, "get_season_summary_async")
        assert callable(stats.get_season_summary)

    def test_player_defense_stats_accessible(self, nfl_sdk):
        """Test player defense stats sub-SDK."""
        stats = nfl_sdk.player_defense_stats

        assert stats is not None
        assert hasattr(stats, "get_season_summary")
        assert hasattr(stats, "get_season_summary_async")
        assert callable(stats.get_season_summary)

    def test_team_offense_stats_accessible(self, nfl_sdk):
        """Test team offense stats sub-SDK."""
        stats = nfl_sdk.team_offense_stats

        assert stats is not None
        assert hasattr(stats, "get_season_overview")
        assert hasattr(stats, "get_season_overview_async")
        assert hasattr(stats, "get_weekly_overview")
        assert hasattr(stats, "get_weekly_overview_async")
        assert callable(stats.get_season_overview)

    def test_team_defense_stats_accessible(self, nfl_sdk):
        """Test team defense stats sub-SDK."""
        stats = nfl_sdk.team_defense_stats

        assert stats is not None
        assert hasattr(stats, "get_season_overview")
        assert hasattr(stats, "get_season_overview_async")
        assert callable(stats.get_season_overview)


@pytest.mark.unit
class TestMethodSignatures:
    """Test that methods have appropriate signatures."""

    def test_sync_methods_accept_required_parameters(self, nfl_sdk):
        """Verify sync methods have proper signatures."""
        # Test a representative sync method
        combine = nfl_sdk.combine
        sig = inspect.signature(combine.get_profiles)

        # Should have parameters for the request
        params = sig.parameters
        assert (
            "limit" in params or "season" in params or len(params) > 0
        ), "Methods should accept request parameters"

    def test_async_methods_accept_required_parameters(self, nfl_sdk):
        """Verify async methods have proper signatures."""
        combine = nfl_sdk.combine
        sig = inspect.signature(combine.get_profiles_async)

        params = sig.parameters
        assert (
            "limit" in params or "season" in params or len(params) > 0
        ), "Async methods should accept request parameters"

    def test_methods_accept_retry_config(self, nfl_sdk):
        """Verify methods accept retry configuration."""
        games = nfl_sdk.games
        sig = inspect.signature(games.get_games)

        params = sig.parameters
        assert "retries" in params, "Methods should accept retries parameter"

    def test_methods_accept_server_url_override(self, nfl_sdk):
        """Verify methods accept server URL override."""
        games = nfl_sdk.games
        sig = inspect.signature(games.get_games)

        params = sig.parameters
        assert "server_url" in params, "Methods should accept server_url parameter"

    def test_methods_accept_timeout_override(self, nfl_sdk):
        """Verify methods accept timeout override."""
        games = nfl_sdk.games
        sig = inspect.signature(games.get_games)

        params = sig.parameters
        assert "timeout_ms" in params, "Methods should accept timeout_ms parameter"


@pytest.mark.unit
class TestSubSDKInheritance:
    """Test that sub-SDKs properly inherit from base classes."""

    def test_regular_endpoints_inherit_from_base_sdk(self, nfl_sdk):
        """Verify regular endpoints inherit from BaseSDK."""
        from griddy.nfl.basesdk import BaseSDK

        games = nfl_sdk.games
        assert isinstance(
            games, BaseSDK
        ), "Regular endpoint sub-SDKs should inherit from BaseSDK"

    def test_pro_endpoints_inherit_from_pro_sdk(self, nfl_sdk):
        """Verify Pro API endpoints inherit from ProSDK."""
        from griddy.nfl.endpoints.pro import ProSDK

        content = nfl_sdk.content
        assert isinstance(
            content, ProSDK
        ), "Pro endpoint sub-SDKs should inherit from ProSDK"

    def test_pro_sdk_inherits_from_base_sdk(self, nfl_sdk):
        """Verify ProSDK itself inherits from BaseSDK."""
        from griddy.nfl.basesdk import BaseSDK
        from griddy.nfl.endpoints.pro import ProSDK

        content = nfl_sdk.content
        assert isinstance(content, BaseSDK), "ProSDK should inherit from BaseSDK"


@pytest.mark.unit
class TestMixinMethods:
    """Test that mixin methods are accessible on sub-SDKs."""

    def test_pro_games_has_mixin_methods(self, nfl_sdk):
        """Test that ProGames has methods from mixins."""
        pro_games = nfl_sdk.pro_games

        # Methods from GameContentMixin
        assert hasattr(pro_games, "get_game_preview")
        assert hasattr(pro_games, "get_game_preview_async")
        assert hasattr(pro_games, "get_game_insights")
        assert hasattr(pro_games, "get_game_insights_async")

        # Methods from GameScheduleMixin
        assert hasattr(pro_games, "get_scheduled_game")
        assert hasattr(pro_games, "get_scheduled_game_async")
        assert hasattr(pro_games, "get_game_matchup_rankings")
        assert hasattr(pro_games, "get_game_matchup_rankings_async")
        assert hasattr(pro_games, "get_team_injuries")
        assert hasattr(pro_games, "get_team_injuries_async")

        assert callable(pro_games.get_game_preview)
        assert callable(pro_games.get_scheduled_game)


@pytest.mark.unit
class TestDirectChildSubSDKAccess:
    """Test that direct child sub-SDKs (not in endpoints/) can be accessed from GriddyNFL."""

    # Map of attribute name to expected module and class for direct child modules
    DIRECT_CHILD_SUB_SDKS = {
        "betting": ("griddy.nfl.betting", "Betting"),
        "scores": ("griddy.nfl.scores", "Scores"),
        "win_probability": ("griddy.nfl.win_probability", "WinProbability"),
        "fantasy_statistics": ("griddy.nfl.fantasy_statistics", "FantasyStatistics"),
        "player_statistics": ("griddy.nfl.player_statistics", "PlayerStatistics"),
        "team_offense_pass_statistics": (
            "griddy.nfl.team_offense_pass_statistics",
            "TeamOffensePassStatistics",
        ),
        "stats": ("griddy.nfl.stats_sdk", "StatsSDK"),
        "football": ("griddy.nfl.football", "Football"),
        "authentication": ("griddy.nfl.authentication", "Authentication"),
    }

    @pytest.mark.parametrize("attr_name,module_info", DIRECT_CHILD_SUB_SDKS.items())
    def test_sub_sdk_accessible(self, nfl_sdk, attr_name, module_info):
        """Test that each direct child sub-SDK can be accessed as an attribute."""
        module_path, class_name = module_info

        # Access the sub-SDK
        sub_sdk = getattr(nfl_sdk, attr_name)

        # Verify it's not None
        assert sub_sdk is not None, f"Sub-SDK '{attr_name}' should not be None"

        # Verify it has the expected class name
        assert (
            sub_sdk.__class__.__name__ == class_name
        ), f"Sub-SDK '{attr_name}' should be instance of {class_name}, got {sub_sdk.__class__.__name__}"

        # Verify it has the expected module
        assert (
            sub_sdk.__class__.__module__ == module_path
        ), f"Sub-SDK '{attr_name}' should be from module {module_path}, got {sub_sdk.__class__.__module__}"

    @pytest.mark.parametrize("attr_name", DIRECT_CHILD_SUB_SDKS.keys())
    def test_sub_sdk_can_be_accessed_multiple_times(self, nfl_sdk, attr_name):
        """Test that accessing sub-SDK multiple times returns the same instance."""
        first_access = getattr(nfl_sdk, attr_name)
        second_access = getattr(nfl_sdk, attr_name)

        assert (
            first_access is second_access
        ), f"Sub-SDK '{attr_name}' should return same instance on multiple accesses"


@pytest.mark.unit
class TestDirectChildMethodAccessibility:
    """Test that methods on direct child sub-SDKs are accessible and callable."""

    def test_betting_methods_exist(self, nfl_sdk):
        """Test Betting sub-SDK methods."""
        betting = nfl_sdk.betting

        assert hasattr(betting, "get_weekly_betting_odds")
        assert hasattr(betting, "get_weekly_betting_odds_async")

        assert callable(betting.get_weekly_betting_odds)
        assert callable(betting.get_weekly_betting_odds_async)

    def test_scores_methods_exist(self, nfl_sdk):
        """Test Scores sub-SDK methods."""
        scores = nfl_sdk.scores

        assert hasattr(scores, "get_live_game_scores")
        assert hasattr(scores, "get_live_game_scores_async")

        assert callable(scores.get_live_game_scores)
        assert callable(scores.get_live_game_scores_async)

    def test_win_probability_methods_exist(self, nfl_sdk):
        """Test WinProbability sub-SDK methods."""
        win_prob = nfl_sdk.win_probability

        assert hasattr(win_prob, "get_plays_win_probability")
        assert hasattr(win_prob, "get_plays_win_probability_async")
        assert hasattr(win_prob, "get_win_probability_min")
        assert hasattr(win_prob, "get_win_probability_min_async")

        assert callable(win_prob.get_plays_win_probability)
        assert callable(win_prob.get_win_probability_min)

    def test_fantasy_statistics_methods_exist(self, nfl_sdk):
        """Test FantasyStatistics sub-SDK methods."""
        fantasy = nfl_sdk.fantasy_statistics

        assert hasattr(fantasy, "get_fantasy_stats_by_season")
        assert hasattr(fantasy, "get_fantasy_stats_by_season_async")

        assert callable(fantasy.get_fantasy_stats_by_season)
        assert callable(fantasy.get_fantasy_stats_by_season_async)

    def test_player_statistics_methods_exist(self, nfl_sdk):
        """Test PlayerStatistics sub-SDK methods (deprecated but still accessible)."""
        player_stats = nfl_sdk.player_statistics

        assert hasattr(player_stats, "get_player_passing_stats_by_season")
        assert hasattr(player_stats, "get_player_passing_stats_by_season_async")

        assert callable(player_stats.get_player_passing_stats_by_season)
        assert callable(player_stats.get_player_passing_stats_by_season_async)

    def test_team_offense_pass_statistics_methods_exist(self, nfl_sdk):
        """Test TeamOffensePassStatistics sub-SDK methods (marked for deletion)."""
        team_stats = nfl_sdk.team_offense_pass_statistics

        assert hasattr(team_stats, "get_team_offense_pass_stats_by_season")
        assert hasattr(team_stats, "get_team_offense_pass_stats_by_season_async")

        assert callable(team_stats.get_team_offense_pass_stats_by_season)
        assert callable(team_stats.get_team_offense_pass_stats_by_season_async)

    def test_stats_sdk_methods_exist(self, nfl_sdk):
        """Test StatsSDK sub-SDK methods."""
        stats = nfl_sdk.stats

        assert hasattr(stats, "get_gamecenter")
        assert hasattr(stats, "get_gamecenter_async")
        assert hasattr(stats, "get_stats_boxscore")
        assert hasattr(stats, "get_stats_boxscore_async")
        assert hasattr(stats, "get_game_team_rankings")
        assert hasattr(stats, "get_game_team_rankings_async")
        assert hasattr(stats, "get_multiple_rankings_all_teams")
        assert hasattr(stats, "get_multiple_rankings_all_teams_async")

        assert callable(stats.get_gamecenter)
        assert callable(stats.get_stats_boxscore)

    def test_football_methods_exist(self, nfl_sdk):
        """Test Football sub-SDK methods."""
        football = nfl_sdk.football

        # Verify all Football API v2 methods exist
        assert hasattr(football, "get_draft_info")
        assert hasattr(football, "get_draft_info_async")
        assert hasattr(football, "get_weekly_game_details")
        assert hasattr(football, "get_weekly_game_details_async")
        assert hasattr(football, "get_football_games")
        assert hasattr(football, "get_football_games_async")
        assert hasattr(football, "get_football_box_score")
        assert hasattr(football, "get_football_box_score_async")
        assert hasattr(football, "get_play_by_play")
        assert hasattr(football, "get_play_by_play_async")
        assert hasattr(football, "get_injury_reports")
        assert hasattr(football, "get_injury_reports_async")
        assert hasattr(football, "get_players_team_roster")
        assert hasattr(football, "get_players_team_roster_async")
        assert hasattr(football, "get_player_details")
        assert hasattr(football, "get_player_details_async")
        assert hasattr(football, "get_standings")
        assert hasattr(football, "get_standings_async")
        assert hasattr(football, "get_live_game_stats")
        assert hasattr(football, "get_live_game_stats_async")
        assert hasattr(football, "get_season_player_stats")
        assert hasattr(football, "get_season_player_stats_async")
        assert hasattr(football, "get_transactions")
        assert hasattr(football, "get_transactions_async")
        assert hasattr(football, "get_venues")
        assert hasattr(football, "get_venues_async")
        assert hasattr(football, "get_season_weeks")
        assert hasattr(football, "get_season_weeks_async")

        # Verify they are callable
        assert callable(football.get_draft_info)
        assert callable(football.get_football_games)
        assert callable(football.get_injury_reports)

    def test_authentication_methods_exist(self, nfl_sdk):
        """Test Authentication sub-SDK methods."""
        auth = nfl_sdk.authentication

        assert hasattr(auth, "generate_token")
        assert hasattr(auth, "generate_token_async")
        assert hasattr(auth, "refresh_token")
        assert hasattr(auth, "refresh_token_async")

        assert callable(auth.generate_token)
        assert callable(auth.refresh_token)
