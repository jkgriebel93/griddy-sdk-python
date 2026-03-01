"""Tests for PFR Frivolities endpoints.

Covers:
- Multi-Team Players
  (``/friv/players-who-played-for-multiple-teams-franchises.fcgi``)
"""

from unittest.mock import patch

import pytest

from griddy.pfr.models import (
    MultiTeamPlayers,
    MultiTeamPlayerStats,
    StatsTable,
    TopPlayerSummary,
)
from griddy.pfr.parsers.multi_team_players import MultiTeamPlayersParser
from griddy.pfr.sdk import GriddyPFR
from griddy.settings import FIXTURE_DIR

FIXTURE_DIR = FIXTURE_DIR / "pfr" / "frivolities"

_parser = MultiTeamPlayersParser()

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def multi_team_html() -> str:
    return (FIXTURE_DIR / "multi_team_players_crd_atl.html").read_text()


@pytest.fixture(scope="module")
def multi_team_parsed(multi_team_html: str) -> dict:
    return _parser.parse(multi_team_html)


@pytest.fixture(scope="module")
def multi_team_model(multi_team_parsed: dict) -> MultiTeamPlayers:
    return MultiTeamPlayers.model_validate(multi_team_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestMultiTeamPlayersSmoke:
    def test_parse_returns_dict(self, multi_team_parsed):
        assert isinstance(multi_team_parsed, dict)

    def test_has_required_keys(self, multi_team_parsed):
        assert "title" in multi_team_parsed
        assert "teams" in multi_team_parsed
        assert "top_players" in multi_team_parsed
        assert "stats_tables" in multi_team_parsed

    def test_model_validates(self, multi_team_model):
        assert isinstance(multi_team_model, MultiTeamPlayers)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestMultiTeamMetadata:
    def test_title(self, multi_team_model):
        assert (
            multi_team_model.title
            == "Players who played for Arizona Cardinals and Atlanta Falcons"
        )

    def test_total_players(self, multi_team_model):
        assert multi_team_model.total_players == 75

    def test_teams(self, multi_team_model):
        assert multi_team_model.teams == ["Arizona Cardinals", "Atlanta Falcons"]


# =========================================================================
# Top players
# =========================================================================


@pytest.mark.unit
class TestTopPlayers:
    def test_count(self, multi_team_model):
        assert len(multi_team_model.top_players) == 5

    def test_types(self, multi_team_model):
        for tp in multi_team_model.top_players:
            assert isinstance(tp, TopPlayerSummary)

    def test_first_player(self, multi_team_model):
        first = multi_team_model.top_players[0]
        assert first.name == "Calais Campbell"
        assert first.player_href == "/players/C/CampCa99.htm"
        assert first.player_id == "CampCa99"
        assert "10 seasons for the Arizona Cardinals" in first.description
        assert "88 Approximate Value" in first.description

    def test_last_player(self, multi_team_model):
        last = multi_team_model.top_players[4]
        assert last.name == "Ken Reaves"
        assert last.player_id == "ReavKe00"


# =========================================================================
# Stats tables — structure
# =========================================================================


@pytest.mark.unit
class TestStatsTableStructure:
    def test_table_count(self, multi_team_model):
        assert len(multi_team_model.stats_tables) == 4

    def test_table_types(self, multi_team_model):
        for st in multi_team_model.stats_tables:
            assert isinstance(st, StatsTable)

    def test_categories(self, multi_team_model):
        categories = [t.category for t in multi_team_model.stats_tables]
        assert categories == ["Passing", "Rushing", "Receiving", "All Players"]

    def test_each_table_has_teams(self, multi_team_model):
        for st in multi_team_model.stats_tables:
            assert st.teams == ["Arizona Cardinals", "Atlanta Falcons"]


# =========================================================================
# Passing table
# =========================================================================


@pytest.mark.unit
class TestPassingTable:
    def test_player_count(self, multi_team_model):
        passing = multi_team_model.stats_tables[0]
        assert len(passing.players) == 3

    def test_first_player_identity(self, multi_team_model):
        player = multi_team_model.stats_tables[0].players[0]
        assert isinstance(player, MultiTeamPlayerStats)
        assert player.player == "Chris Chandler"
        assert player.player_href == "/players/C/ChanCh00.htm"
        assert player.player_id == "ChanCh00"

    def test_first_player_crd_stats(self, multi_team_model):
        stats = multi_team_model.stats_tables[0].players[0].stats
        assert stats["crd_games"] == 22
        assert stats["crd_av"] == 13
        assert stats["crd_pass_td"] == 19
        assert stats["crd_pass_int"] == 19
        assert stats["crd_pass_yds"] == 3592

    def test_first_player_atl_stats(self, multi_team_model):
        stats = multi_team_model.stats_tables[0].players[0].stats
        assert stats["atl_games"] == 68
        assert stats["atl_av"] == 50
        assert stats["atl_pass_td"] == 87
        assert stats["atl_pass_yds"] == 13268


# =========================================================================
# Rushing table
# =========================================================================


@pytest.mark.unit
class TestRushingTable:
    def test_player_count(self, multi_team_model):
        rushing = multi_team_model.stats_tables[1]
        assert len(rushing.players) == 9

    def test_first_player(self, multi_team_model):
        player = multi_team_model.stats_tables[1].players[0]
        assert player.player == "Tony Baker"
        assert player.player_id == "BakeTo20"


# =========================================================================
# Receiving table
# =========================================================================


@pytest.mark.unit
class TestReceivingTable:
    def test_player_count(self, multi_team_model):
        receiving = multi_team_model.stats_tables[2]
        assert len(receiving.players) == 7


# =========================================================================
# All Players table
# =========================================================================


@pytest.mark.unit
class TestAllPlayersTable:
    def test_player_count(self, multi_team_model):
        all_players = multi_team_model.stats_tables[3]
        assert len(all_players.players) == 75

    def test_first_player(self, multi_team_model):
        player = multi_team_model.stats_tables[3].players[0]
        assert player.player == "John Abraham"
        assert player.player_id == "AbraJo00"
        assert player.stats["crd_av"] == 9
        assert player.stats["atl_av"] == 62

    def test_last_player(self, multi_team_model):
        player = multi_team_model.stats_tables[3].players[-1]
        assert player.player == "John Zook"
        assert player.player_id == "ZookJo00"


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestParserErrors:
    def test_raises_on_missing_tables(self):
        with pytest.raises(ValueError, match="Could not find"):
            _parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestEndpointConfig:
    def test_config_basic(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_multi_team_players_config(t1="crd", t2="atl")
        assert config.query_params["t1"] == "crd"
        assert config.query_params["t2"] == "atl"
        assert config.query_params["level"] == "franch"
        assert "t3" not in config.query_params
        assert "t4" not in config.query_params
        assert "exclusively" not in config.query_params

    def test_config_with_all_params(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_multi_team_players_config(
            t1="crd", t2="atl", t3="pit", t4="nwe", exclusively=True
        )
        assert config.query_params["t3"] == "pit"
        assert config.query_params["t4"] == "nwe"
        assert config.query_params["exclusively"] == "1"

    def test_config_operation_id(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_multi_team_players_config(t1="crd", t2="atl")
        assert config.operation_id == "getMultiTeamPlayers"

    def test_endpoint_via_mock(self, multi_team_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=multi_team_html,
        ):
            result = pfr.frivolities.get_multi_team_players(t1="crd", t2="atl")
        assert isinstance(result, MultiTeamPlayers)
        assert result.total_players == 75
        assert len(result.stats_tables) == 4
