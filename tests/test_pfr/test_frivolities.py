"""Tests for PFR Frivolities endpoints.

Covers:
- Multi-Team Players
  (``/friv/players-who-played-for-multiple-teams-franchises.fcgi``)
- Statistical Milestones
  (``/friv/milestones.cgi``)
- Upcoming Milestones
  (``/friv/upcoming-milestones.htm``)
- Birthdays
  (``/friv/birthdays.cgi``)
- Birthplaces
  (``/friv/birthplaces.htm`` and ``/friv/birthplaces.cgi``)
- Players Born Before a Date
  (``/friv/age.cgi``)
- Uniform Numbers
  (``/players/uniform.cgi``)
- QB Wins vs. Franchises
  (``/friv/qb-wins.htm``)
- Non-Quarterback Passers
  (``/friv/nonqb.htm``)
- Non-Skill Position TD Scorers
  (``/friv/odd_td.htm``)
- Octopus Tracker
  (``/friv/octopus-tracker.htm``)
"""

from unittest.mock import patch

import pytest

from griddy.pfr.models import (
    BirthdayPlayer,
    Birthdays,
    BirthplaceFiltered,
    BirthplaceLanding,
    BirthplaceLocation,
    BirthplacePlayer,
    CareerLeader,
    MilestoneEntry,
    MultiTeamPlayers,
    MultiTeamPlayerStats,
    NonQBPasserEntry,
    NonQBPassers,
    NonSkillPosTdEntry,
    NonSkillPosTdScorers,
    OctopusEntry,
    OctopusTracker,
    PlayerBornBefore,
    PlayersBornBefore,
    QBWinEntry,
    QBWins,
    StatisticalMilestones,
    StatsTable,
    TopPlayerSummary,
    UniformNumberPlayer,
    UniformNumbers,
    UpcomingLeaderboardEntry,
    UpcomingMilestoneEntry,
    UpcomingMilestones,
)
from griddy.pfr.parsers.birthdays import BirthdaysParser
from griddy.pfr.parsers.birthplaces import BirthplacesParser
from griddy.pfr.parsers.multi_team_players import MultiTeamPlayersParser
from griddy.pfr.parsers.non_qb_passers import NonQBPassersParser
from griddy.pfr.parsers.non_skill_pos_td import NonSkillPosTdParser
from griddy.pfr.parsers.octopus_tracker import OctopusTrackerParser
from griddy.pfr.parsers.players_born_before import PlayersBornBeforeParser
from griddy.pfr.parsers.qb_wins import QBWinsParser
from griddy.pfr.parsers.statistical_milestones import StatisticalMilestonesParser
from griddy.pfr.parsers.uniform_numbers import UniformNumbersParser
from griddy.pfr.parsers.upcoming_milestones import UpcomingMilestonesParser
from griddy.pfr.sdk import GriddyPFR
from griddy.settings import FIXTURE_DIR

FIXTURE_DIR = FIXTURE_DIR / "pfr" / "frivolities"

_parser = MultiTeamPlayersParser()
_milestones_parser = StatisticalMilestonesParser()
_upcoming_parser = UpcomingMilestonesParser()
_birthdays_parser = BirthdaysParser()
_birthplaces_parser = BirthplacesParser()
_born_before_parser = PlayersBornBeforeParser()
_uniform_numbers_parser = UniformNumbersParser()
_qb_wins_parser = QBWinsParser()
_non_qb_passers_parser = NonQBPassersParser()
_non_skill_pos_td_parser = NonSkillPosTdParser()
_octopus_tracker_parser = OctopusTrackerParser()

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


# #########################################################################
#
#  Statistical Milestones
#
# #########################################################################

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def milestones_html() -> str:
    return (FIXTURE_DIR / "statistical_milestones_pass_td.html").read_text()


@pytest.fixture(scope="module")
def milestones_parsed(milestones_html: str) -> dict:
    return _milestones_parser.parse(milestones_html)


@pytest.fixture(scope="module")
def milestones_model(milestones_parsed: dict) -> StatisticalMilestones:
    return StatisticalMilestones.model_validate(milestones_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestMilestonesSmoke:
    def test_parse_returns_dict(self, milestones_parsed):
        assert isinstance(milestones_parsed, dict)

    def test_has_required_keys(self, milestones_parsed):
        assert "title" in milestones_parsed
        assert "stat" in milestones_parsed
        assert "milestones" in milestones_parsed
        assert "career_leaders" in milestones_parsed

    def test_model_validates(self, milestones_model):
        assert isinstance(milestones_model, StatisticalMilestones)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestMilestonesMetadata:
    def test_title(self, milestones_model):
        assert milestones_model.title == "NFL Milestone Watch: Passing TD"

    def test_stat(self, milestones_model):
        assert milestones_model.stat == "pass_td"


# =========================================================================
# Milestones table
# =========================================================================


@pytest.mark.unit
class TestMilestonesTable:
    def test_milestone_count(self, milestones_model):
        assert len(milestones_model.milestones) == 15

    def test_milestone_types(self, milestones_model):
        for m in milestones_model.milestones:
            assert isinstance(m, MilestoneEntry)

    def test_first_milestone(self, milestones_model):
        first = milestones_model.milestones[0]
        assert first.player == "Aaron Rodgers"
        assert first.player_id == "RodgAa00"
        assert first.player_href == "/players/R/RodgAa00.htm"
        assert first.value == 527
        assert first.needed == "23 to milestone"
        assert first.milestone == "550 Passing TD"

    def test_second_milestone_threshold(self, milestones_model):
        second = milestones_model.milestones[1]
        assert second.player == "Philip Rivers"
        assert second.milestone == "450 Passing TD"
        assert second.value == 425

    def test_players_under_same_milestone(self, milestones_model):
        # Baker Mayfield and Lamar Jackson are both under "200 Passing TD"
        mayfield = milestones_model.milestones[4]
        jackson = milestones_model.milestones[5]
        assert mayfield.player == "Baker Mayfield"
        assert mayfield.milestone == "200 Passing TD"
        assert jackson.player == "Lamar Jackson"
        assert jackson.milestone == "200 Passing TD"

    def test_last_milestone(self, milestones_model):
        last = milestones_model.milestones[-1]
        assert last.player == "Teddy Bridgewater"
        assert last.value == 75
        assert last.needed == "25 to milestone"


# =========================================================================
# Career leaders table
# =========================================================================


@pytest.mark.unit
class TestCareerLeaders:
    def test_leader_count(self, milestones_model):
        assert len(milestones_model.career_leaders) == 25

    def test_leader_types(self, milestones_model):
        for leader in milestones_model.career_leaders:
            assert isinstance(leader, CareerLeader)

    def test_first_leader(self, milestones_model):
        first = milestones_model.career_leaders[0]
        assert first.rank == 1
        assert first.player == "Tom Brady"
        assert first.player_id == "BradTo00"
        assert first.player_href == "/players/B/BradTo00.htm"
        assert first.value == 649
        assert first.is_active is False
        assert first.needed is None

    def test_active_player(self, milestones_model):
        # Aaron Rodgers is rank 4 and active
        rodgers = milestones_model.career_leaders[3]
        assert rodgers.rank == 4
        assert rodgers.player == "Aaron Rodgers"
        assert rodgers.player_id == "RodgAa00"
        assert rodgers.value == 527
        assert rodgers.is_active is True
        assert rodgers.needed == "(needs 13 to move into 3rd place)"

    def test_hof_player(self, milestones_model):
        # Drew Brees is a HOF player (has * after name)
        brees = milestones_model.career_leaders[1]
        assert brees.rank == 2
        assert brees.player == "Drew Brees"
        assert brees.is_active is False

    def test_last_leader(self, milestones_model):
        last = milestones_model.career_leaders[-1]
        assert last.rank == 25
        assert last.player == "Jared Goff"
        assert last.is_active is True


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestMilestonesParserErrors:
    def test_raises_on_missing_milestones_table(self):
        with pytest.raises(ValueError, match="Could not find milestones table"):
            _milestones_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestMilestonesEndpointConfig:
    def test_config_basic(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_statistical_milestones_config(stat="pass_td")
        assert config.query_params["stat"] == "pass_td"
        assert config.operation_id == "getStatisticalMilestones"

    def test_config_different_stat(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_statistical_milestones_config(stat="rush_yds")
        assert config.query_params["stat"] == "rush_yds"

    def test_endpoint_via_mock(self, milestones_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=milestones_html,
        ):
            result = pfr.frivolities.get_statistical_milestones(stat="pass_td")
        assert isinstance(result, StatisticalMilestones)
        assert result.stat == "pass_td"
        assert len(result.milestones) == 15
        assert len(result.career_leaders) == 25


# #########################################################################
#
#  Upcoming Milestones
#
# #########################################################################

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def upcoming_html() -> str:
    return (FIXTURE_DIR / "upcoming_milestones.html").read_text()


@pytest.fixture(scope="module")
def upcoming_parsed(upcoming_html: str) -> dict:
    return _upcoming_parser.parse(upcoming_html)


@pytest.fixture(scope="module")
def upcoming_model(upcoming_parsed: dict) -> UpcomingMilestones:
    return UpcomingMilestones.model_validate(upcoming_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestUpcomingSmoke:
    def test_parse_returns_dict(self, upcoming_parsed):
        assert isinstance(upcoming_parsed, dict)

    def test_has_required_keys(self, upcoming_parsed):
        assert "title" in upcoming_parsed
        assert "description" in upcoming_parsed
        assert "milestones" in upcoming_parsed
        assert "leaderboards" in upcoming_parsed

    def test_model_validates(self, upcoming_model):
        assert isinstance(upcoming_model, UpcomingMilestones)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestUpcomingMetadata:
    def test_title(self, upcoming_model):
        assert (
            upcoming_model.title == "NFL Upcoming Milestones and Leaderboard Movement"
        )

    def test_description(self, upcoming_model):
        assert upcoming_model.description.startswith(
            "Potential leaderboard movements and milestones"
        )


# =========================================================================
# Milestones table
# =========================================================================


@pytest.mark.unit
class TestUpcomingMilestonesTable:
    def test_milestone_count(self, upcoming_model):
        assert len(upcoming_model.milestones) == 17

    def test_milestone_types(self, upcoming_model):
        for m in upcoming_model.milestones:
            assert isinstance(m, UpcomingMilestoneEntry)

    def test_first_milestone(self, upcoming_model):
        first = upcoming_model.milestones[0]
        assert first.category == "Yds From Scrimmage"
        assert first.player == "Christian McCaffrey"
        assert first.player_href == "/players/M/McCaCh01.htm"
        assert first.player_id == "McCaCh01"
        assert first.value == 12979
        assert first.needed == "21 to 13000"

    def test_milestone_with_small_value(self, upcoming_model):
        # Josh Allen — Rushing TD, value=79
        allen = upcoming_model.milestones[1]
        assert allen.player == "Josh Allen"
        assert allen.category == "Rushing TD"
        assert allen.value == 79
        assert allen.needed == "1 to 80"

    def test_last_milestone(self, upcoming_model):
        last = upcoming_model.milestones[-1]
        assert last.category == "Touchdowns"
        assert last.player == "Nick Chubb"
        assert last.player_id == "ChubNi00"
        assert last.value == 59
        assert last.needed == "1 to 60"

    def test_categories_present(self, upcoming_model):
        categories = {m.category for m in upcoming_model.milestones}
        assert "Yds From Scrimmage" in categories
        assert "Rushing TD" in categories
        assert "Receiving Yds" in categories
        assert "Passing TD" in categories
        assert "Touchdowns" in categories


# =========================================================================
# Leaderboards table
# =========================================================================


@pytest.mark.unit
class TestUpcomingLeaderboardsTable:
    def test_leaderboard_count(self, upcoming_model):
        assert len(upcoming_model.leaderboards) == 43

    def test_leaderboard_types(self, upcoming_model):
        for lb in upcoming_model.leaderboards:
            assert isinstance(lb, UpcomingLeaderboardEntry)

    def test_first_leaderboard(self, upcoming_model):
        first = upcoming_model.leaderboards[0]
        assert first.category == "Yds From Scrimmage"
        assert first.player == "Derrick Henry"
        assert first.player_href == "/players/H/HenrDe00.htm"
        assert first.player_id == "HenrDe00"
        assert first.value == 14819
        assert first.needed == "72 to 27th place"
        assert first.leader_href == "/leaders/yds_from_scrimmage_career.htm"

    def test_leaderboard_with_link(self, upcoming_model):
        # Matthew Stafford — Passing TD, moving to 6th place
        stafford = upcoming_model.leaderboards[25]
        assert stafford.player == "Matthew Stafford"
        assert stafford.category == "Passing TD"
        assert stafford.value == 423
        assert stafford.needed == "2 to 6th place"
        assert stafford.leader_href == "/leaders/pass_td_career.htm"

    def test_last_leaderboard(self, upcoming_model):
        last = upcoming_model.leaderboards[-1]
        assert last.category == "All-Purpose Yds"
        assert last.player == "Derrick Henry"
        assert last.player_id == "HenrDe00"
        assert last.value == 14813
        assert last.needed == "78 to 42nd place"
        assert last.leader_href == "/leaders/all_purpose_yds_career.htm"

    def test_categories_present(self, upcoming_model):
        categories = {lb.category for lb in upcoming_model.leaderboards}
        assert "Points Scored" in categories
        assert "Rushing TD" in categories
        assert "Receiving Yds" in categories
        assert "Games" in categories
        assert "Field Goals Made" in categories


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestUpcomingParserErrors:
    def test_raises_on_missing_milestones_table(self):
        with pytest.raises(
            ValueError, match="Could not find upcoming milestones table"
        ):
            _upcoming_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestUpcomingEndpointConfig:
    def test_config_basic(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_upcoming_milestones_config()
        assert config.operation_id == "getUpcomingMilestones"
        assert config.query_params == {}

    def test_endpoint_via_mock(self, upcoming_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=upcoming_html,
        ):
            result = pfr.frivolities.get_upcoming_milestones()
        assert isinstance(result, UpcomingMilestones)
        assert len(result.milestones) == 17
        assert len(result.leaderboards) == 43


# #########################################################################
#
#  Birthdays
#
# #########################################################################

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def birthdays_html() -> str:
    return (FIXTURE_DIR / "birthdays.html").read_text()


@pytest.fixture(scope="module")
def birthdays_parsed(birthdays_html: str) -> dict:
    return _birthdays_parser.parse(birthdays_html)


@pytest.fixture(scope="module")
def birthdays_model(birthdays_parsed: dict) -> Birthdays:
    return Birthdays.model_validate(birthdays_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestBirthdaysSmoke:
    def test_parse_returns_dict(self, birthdays_parsed):
        assert isinstance(birthdays_parsed, dict)

    def test_has_required_keys(self, birthdays_parsed):
        assert "title" in birthdays_parsed
        assert "month" in birthdays_parsed
        assert "day" in birthdays_parsed
        assert "players" in birthdays_parsed

    def test_model_validates(self, birthdays_model):
        assert isinstance(birthdays_model, Birthdays)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestBirthdaysMetadata:
    def test_title(self, birthdays_model):
        assert birthdays_model.title == "List of all NFL Players Born on March 2"

    def test_month(self, birthdays_model):
        assert birthdays_model.month == 3

    def test_day(self, birthdays_model):
        assert birthdays_model.day == 2


# =========================================================================
# Players table
# =========================================================================


@pytest.mark.unit
class TestBirthdaysPlayers:
    def test_player_count(self, birthdays_model):
        assert len(birthdays_model.players) == 90

    def test_player_types(self, birthdays_model):
        for p in birthdays_model.players:
            assert isinstance(p, BirthdayPlayer)

    def test_first_player(self, birthdays_model):
        first = birthdays_model.players[0]
        assert first.rank == 1
        assert first.player == "Jim Allison"
        assert first.player_href == "/players/A/AlliJi00.htm"
        assert first.player_id == "AlliJi00"
        assert first.pos == "RB"
        assert first.birth_year == 1943
        assert first.year_min == 1965
        assert first.year_max == 1968
        assert first.g == 43
        assert first.rush_att == 93
        assert first.rush_yds == 378
        assert first.rec == 22

    def test_notable_player_stats(self, birthdays_model):
        # Ben Roethlisberger — rank 68, QB with extensive career stats
        big_ben = birthdays_model.players[67]
        assert big_ben.rank == 68
        assert big_ben.player == "Ben Roethlisberger"
        assert big_ben.player_id == "RoetBe00"
        assert big_ben.pos == "QB"
        assert big_ben.birth_year == 1982
        assert big_ben.pro_bowls == 6
        assert big_ben.years_as_primary_starter == 17
        assert big_ben.career_av == 131
        assert big_ben.g == 249
        assert big_ben.pass_cmp == 5440
        assert big_ben.pass_yds == 64088
        assert big_ben.pass_td == 418
        assert big_ben.pass_int == 211
        assert big_ben.rush_att == 515

    def test_player_with_empty_stats(self, birthdays_model):
        # Last player (OG) — many stat fields should be None
        last = birthdays_model.players[-1]
        assert last.rank == 90
        assert last.player == "Cody Wichmann"
        assert last.player_id == "WichCo00"
        assert last.pos == "OG"
        assert last.pass_cmp is None
        assert last.rush_att is None
        assert last.rec is None

    def test_last_player(self, birthdays_model):
        last = birthdays_model.players[-1]
        assert last.rank == 90
        assert last.player == "Cody Wichmann"
        assert last.player_href == "/players/W/WichCo00.htm"
        assert last.birth_year == 1992
        assert last.g == 24


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestBirthdaysParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ValueError, match="Could not find birthdays table"):
            _birthdays_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Month/day extraction
# =========================================================================


@pytest.mark.unit
class TestBirthdaysMonthDayExtraction:
    def test_january(self):
        parser = BirthdaysParser()
        assert parser._extract_month_day(
            "List of all NFL Players Born on January 15"
        ) == (1, 15)

    def test_december(self):
        parser = BirthdaysParser()
        assert parser._extract_month_day(
            "List of all NFL Players Born on December 25"
        ) == (12, 25)

    def test_no_match(self):
        parser = BirthdaysParser()
        assert parser._extract_month_day("Some random title") == (0, 0)


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestBirthdaysEndpointConfig:
    def test_config_basic(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_birthdays_config(month=3, day=2)
        assert config.query_params["month"] == "3"
        assert config.query_params["day"] == "2"
        assert config.operation_id == "getBirthdays"

    def test_config_different_date(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_birthdays_config(month=12, day=25)
        assert config.query_params["month"] == "12"
        assert config.query_params["day"] == "25"

    def test_endpoint_via_mock(self, birthdays_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=birthdays_html,
        ):
            result = pfr.frivolities.get_birthdays(month=3, day=2)
        assert isinstance(result, Birthdays)
        assert result.month == 3
        assert result.day == 2
        assert len(result.players) == 90


# #########################################################################
#
#  Birthplaces — Landing Page
#
# #########################################################################

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def birthplaces_landing_html() -> str:
    return (FIXTURE_DIR / "birthplaces_landing.html").read_text()


@pytest.fixture(scope="module")
def birthplaces_landing_parsed(birthplaces_landing_html: str) -> dict:
    return _birthplaces_parser.parse_landing(birthplaces_landing_html)


@pytest.fixture(scope="module")
def birthplaces_landing_model(birthplaces_landing_parsed: dict) -> BirthplaceLanding:
    return BirthplaceLanding.model_validate(birthplaces_landing_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestBirthplacesLandingSmoke:
    def test_parse_returns_dict(self, birthplaces_landing_parsed):
        assert isinstance(birthplaces_landing_parsed, dict)

    def test_has_required_keys(self, birthplaces_landing_parsed):
        assert "title" in birthplaces_landing_parsed
        assert "locations" in birthplaces_landing_parsed

    def test_model_validates(self, birthplaces_landing_model):
        assert isinstance(birthplaces_landing_model, BirthplaceLanding)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestBirthplacesLandingMetadata:
    def test_title(self, birthplaces_landing_model):
        assert birthplaces_landing_model.title == "Birthplaces"


# =========================================================================
# Locations table
# =========================================================================


@pytest.mark.unit
class TestBirthplacesLandingLocations:
    def test_location_count(self, birthplaces_landing_model):
        assert len(birthplaces_landing_model.locations) == 181

    def test_location_types(self, birthplaces_landing_model):
        for loc in birthplaces_landing_model.locations:
            assert isinstance(loc, BirthplaceLocation)

    def test_first_location_unknown(self, birthplaces_landing_model):
        first = birthplaces_landing_model.locations[0]
        assert first.rank == 1
        assert first.birth_country == "Unknown"
        assert first.birth_country_href == "/friv/birthplaces.cgi?country=&state="
        assert first.birth_state is None
        assert first.players == 374
        assert first.players_active == 308
        assert first.hofers == 0
        assert first.g == 5524
        assert first.td == 206
        # Unknown has no notable players
        assert first.player_most_td is None
        assert first.player_most_g is None

    def test_usa_country_row(self, birthplaces_landing_model):
        usa = birthplaces_landing_model.locations[1]
        assert usa.rank == 2
        assert usa.birth_country == "USA"
        assert usa.birth_country_href == "/friv/birthplaces.cgi?country=USA&state="
        assert usa.birth_state is None
        assert usa.players == 272
        assert usa.players_active == 2
        assert usa.hofers == 0
        assert usa.most_td == 10
        assert usa.player_most_td_id == "NortMa20"
        assert usa.player_most_td_href == "/players/N/NortMa20.htm"
        assert usa.most_g == 44
        assert usa.player_most_g_id == "WillJa20"
        assert usa.player_most_g_href == "/players/W/WillJa20.htm"

    def test_state_row(self, birthplaces_landing_model):
        # Row 3 is USA/AK (Alaska)
        alaska = birthplaces_landing_model.locations[2]
        assert alaska.rank == 3
        assert alaska.birth_country == "USA"
        assert alaska.birth_country_href is None  # state rows have no country link
        assert alaska.birth_state == "AK"
        assert alaska.players == 16
        assert alaska.player_most_td_id == "SmitSt02"
        assert alaska.most_td == 12
        assert alaska.player_most_g_id == "SchlMa00"
        assert alaska.most_g == 156

    def test_last_location(self, birthplaces_landing_model):
        last = birthplaces_landing_model.locations[-1]
        assert last.rank == 181
        assert last.players == 1


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestBirthplacesLandingParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ValueError, match="Could not find birthplaces table"):
            _birthplaces_parser.parse_landing(
                "<html><body>No tables here</body></html>"
            )


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestBirthplacesLandingEndpointConfig:
    def test_config_basic(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_birthplaces_config()
        assert config.operation_id == "getBirthplaces"
        assert config.query_params == {}

    def test_endpoint_via_mock(self, birthplaces_landing_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=birthplaces_landing_html,
        ):
            result = pfr.frivolities.get_birthplaces()
        assert isinstance(result, BirthplaceLanding)
        assert result.title == "Birthplaces"
        assert len(result.locations) == 181


# #########################################################################
#
#  Birthplaces — Filtered Page
#
# #########################################################################

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def birthplaces_filtered_html() -> str:
    return (FIXTURE_DIR / "birthplaces_filtered_pa.html").read_text()


@pytest.fixture(scope="module")
def birthplaces_filtered_parsed(birthplaces_filtered_html: str) -> dict:
    return _birthplaces_parser.parse_filtered(birthplaces_filtered_html)


@pytest.fixture(scope="module")
def birthplaces_filtered_model(
    birthplaces_filtered_parsed: dict,
) -> BirthplaceFiltered:
    return BirthplaceFiltered.model_validate(birthplaces_filtered_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestBirthplacesFilteredSmoke:
    def test_parse_returns_dict(self, birthplaces_filtered_parsed):
        assert isinstance(birthplaces_filtered_parsed, dict)

    def test_has_required_keys(self, birthplaces_filtered_parsed):
        assert "title" in birthplaces_filtered_parsed
        assert "country" in birthplaces_filtered_parsed
        assert "state" in birthplaces_filtered_parsed
        assert "players" in birthplaces_filtered_parsed

    def test_model_validates(self, birthplaces_filtered_model):
        assert isinstance(birthplaces_filtered_model, BirthplaceFiltered)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestBirthplacesFilteredMetadata:
    def test_title(self, birthplaces_filtered_model):
        assert (
            birthplaces_filtered_model.title
            == "List of all NFL Players Born in Pennsylvania,  USA"
        )

    def test_country(self, birthplaces_filtered_model):
        assert birthplaces_filtered_model.country == "USA"

    def test_state(self, birthplaces_filtered_model):
        assert birthplaces_filtered_model.state == "Pennsylvania"


# =========================================================================
# Players table
# =========================================================================


@pytest.mark.unit
class TestBirthplacesFilteredPlayers:
    def test_player_count(self, birthplaces_filtered_model):
        assert len(birthplaces_filtered_model.players) == 200

    def test_player_types(self, birthplaces_filtered_model):
        for p in birthplaces_filtered_model.players:
            assert isinstance(p, BirthplacePlayer)

    def test_first_player(self, birthplaces_filtered_model):
        first = birthplaces_filtered_model.players[0]
        assert first.rank == 1
        assert first.player == "Cameron Heyward"
        assert first.player_href == "/players/H/HeywCa01.htm"
        assert first.player_id == "HeywCa01"
        assert first.pos == "DT"
        assert first.birth_city == "Pittsburgh"
        assert first.year_min == 2011
        assert first.year_max == 2025
        assert first.all_pros_first_team == 4
        assert first.pro_bowls == 7
        assert first.years_as_primary_starter == 12
        assert first.career_av == 115
        assert first.g == 228

    def test_second_player_kicker(self, birthplaces_filtered_model):
        kicker = birthplaces_filtered_model.players[1]
        assert kicker.rank == 2
        assert kicker.player == "Brandon McManus"
        assert kicker.player_id == "McMaBr01"
        assert kicker.pos == "K"
        assert kicker.birth_city == "Philadelphia"

    def test_player_with_empty_stats(self, birthplaces_filtered_model):
        # DT — many offensive stat fields should be None
        first = birthplaces_filtered_model.players[0]
        assert first.pass_cmp is None
        assert first.pass_att is None
        assert first.rush_att is None

    def test_last_player(self, birthplaces_filtered_model):
        last = birthplaces_filtered_model.players[-1]
        assert last.rank == 200
        assert last.player == "Chris Neild"
        assert last.player_id == "NeilCh00"
        assert last.pos == "NT"
        assert last.birth_city == "Stroudsburg"


# =========================================================================
# Country/state extraction
# =========================================================================


@pytest.mark.unit
class TestBirthplacesCountryStateExtraction:
    def test_usa_state(self):
        assert BirthplacesParser._extract_country_state(
            "List of all NFL Players Born in Pennsylvania,  USA"
        ) == ("USA", "Pennsylvania")

    def test_country_only(self):
        assert BirthplacesParser._extract_country_state(
            "List of all NFL Players Born in Canada"
        ) == ("Canada", "")

    def test_no_match(self):
        assert BirthplacesParser._extract_country_state("Some random title") == (
            "",
            "",
        )


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestBirthplacesFilteredParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ValueError, match="Could not find birthplaces table"):
            _birthplaces_parser.parse_filtered(
                "<html><body>No tables here</body></html>"
            )


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestBirthplacesFilteredEndpointConfig:
    def test_config_basic(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_birthplace_players_config(
            country="USA", state="PA"
        )
        assert config.query_params["country"] == "USA"
        assert config.query_params["state"] == "PA"
        assert config.operation_id == "getBirthplacePlayers"

    def test_config_country_only(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_birthplace_players_config(country="Canada")
        assert config.query_params["country"] == "Canada"
        assert config.query_params["state"] == ""

    def test_endpoint_via_mock(self, birthplaces_filtered_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=birthplaces_filtered_html,
        ):
            result = pfr.frivolities.get_birthplace_players(country="USA", state="PA")
        assert isinstance(result, BirthplaceFiltered)
        assert result.country == "USA"
        assert result.state == "Pennsylvania"
        assert len(result.players) == 200


# #########################################################################
#
#  Players Born Before a Date
#
# #########################################################################

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def born_before_html() -> str:
    return (FIXTURE_DIR / "players_born_before.html").read_text()


@pytest.fixture(scope="module")
def born_before_parsed(born_before_html: str) -> dict:
    return _born_before_parser.parse(born_before_html)


@pytest.fixture(scope="module")
def born_before_model(born_before_parsed: dict) -> PlayersBornBefore:
    return PlayersBornBefore.model_validate(born_before_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestPlayersBornBeforeSmoke:
    def test_parse_returns_dict(self, born_before_parsed):
        assert isinstance(born_before_parsed, dict)

    def test_has_required_keys(self, born_before_parsed):
        assert "title" in born_before_parsed
        assert "month" in born_before_parsed
        assert "day" in born_before_parsed
        assert "year" in born_before_parsed
        assert "players" in born_before_parsed

    def test_model_validates(self, born_before_model):
        assert isinstance(born_before_model, PlayersBornBefore)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestPlayersBornBeforeMetadata:
    def test_title(self, born_before_model):
        assert (
            born_before_model.title == "Active Players Born on or before August 5, 1993"
        )

    def test_month(self, born_before_model):
        assert born_before_model.month == 8

    def test_day(self, born_before_model):
        assert born_before_model.day == 5

    def test_year(self, born_before_model):
        assert born_before_model.year == 1993


# =========================================================================
# Players table
# =========================================================================


@pytest.mark.unit
class TestPlayersBornBeforePlayers:
    def test_player_count(self, born_before_model):
        assert len(born_before_model.players) == 150

    def test_player_types(self, born_before_model):
        for p in born_before_model.players:
            assert isinstance(p, PlayerBornBefore)

    def test_first_player(self, born_before_model):
        first = born_before_model.players[0]
        assert first.rank == 1
        assert first.player == "Philip Rivers"
        assert first.player_href == "/players/R/RivePh00.htm"
        assert first.player_id == "RivePh00"
        assert first.birth_date == "Dec 8, 1981"
        assert first.age == 45
        assert first.pos == "QB"
        assert first.year_min == 2004
        assert first.year_max == 2025
        assert first.all_pros_first_team == 0
        assert first.pro_bowls == 8
        assert first.years_as_primary_starter == 1
        assert first.career_av == 150
        assert first.g == 247
        assert first.pass_cmp == 5335
        assert first.pass_att == 8226
        assert first.pass_yds == 63984
        assert first.pass_td == 425
        assert first.pass_long == 84
        assert first.pass_int == 212
        assert first.pass_sacked == 469
        assert first.pass_sacked_yds == 2869
        assert first.rush_att == 385
        assert first.rush_yds == 600
        assert first.rush_td == 3
        assert first.rush_long == 18
        assert first.rec == 0
        assert first.rec_yds == -9
        assert first.rec_td == 0
        assert first.rec_long == 0

    def test_second_player(self, born_before_model):
        second = born_before_model.players[1]
        assert second.rank == 2
        assert second.player == "Aaron Rodgers"
        assert second.player_id == "RodgAa00"
        assert second.pos == "QB"
        assert second.birth_date == "Dec 2, 1983"
        assert second.age == 43

    def test_te_player_empty_passing_stats(self, born_before_model):
        # Marcedes Lewis (TE) — many passing stat fields should be None
        te = born_before_model.players[2]
        assert te.player == "Marcedes Lewis"
        assert te.pos == "TE"
        assert te.pass_cmp is None
        assert te.pass_att is None
        assert te.pass_yds is None
        assert te.rec == 437
        assert te.rec_yds == 5115
        assert te.rec_td == 40

    def test_last_player(self, born_before_model):
        last = born_before_model.players[-1]
        assert last.rank == 150


# =========================================================================
# Date extraction helper
# =========================================================================


@pytest.mark.unit
class TestPlayersBornBeforeDateExtraction:
    def test_full_date(self):
        assert PlayersBornBeforeParser._extract_month_day_year(
            "Active Players Born on or before August 5, 1993"
        ) == (8, 5, 1993)

    def test_different_date(self):
        assert PlayersBornBeforeParser._extract_month_day_year(
            "Active Players Born on or before January 15, 2000"
        ) == (1, 15, 2000)

    def test_no_match(self):
        assert PlayersBornBeforeParser._extract_month_day_year("Some random title") == (
            0,
            0,
            0,
        )


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestPlayersBornBeforeParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ValueError, match="Could not find players table"):
            _born_before_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestPlayersBornBeforeEndpointConfig:
    def test_config_basic(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_players_born_before_config(
            month=8, day=5, year=1993
        )
        assert config.operation_id == "getPlayersBornBefore"
        assert config.query_params["month"] == "8"
        assert config.query_params["day"] == "5"
        assert config.query_params["year"] == "1993"

    def test_endpoint_via_mock(self, born_before_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=born_before_html,
        ):
            result = pfr.frivolities.get_players_born_before(month=8, day=5, year=1993)
        assert isinstance(result, PlayersBornBefore)
        assert result.month == 8
        assert result.day == 5
        assert result.year == 1993
        assert len(result.players) == 150


# #########################################################################
# Uniform Numbers
# #########################################################################


@pytest.fixture(scope="module")
def uniform_numbers_html() -> str:
    return (FIXTURE_DIR / "uniform_numbers.html").read_text()


@pytest.fixture(scope="module")
def uniform_numbers_parsed(uniform_numbers_html: str) -> dict:
    return _uniform_numbers_parser.parse(uniform_numbers_html)


@pytest.fixture(scope="module")
def uniform_numbers_model(uniform_numbers_parsed: dict) -> UniformNumbers:
    return UniformNumbers.model_validate(uniform_numbers_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestUniformNumbersSmoke:
    def test_parse_returns_dict(self, uniform_numbers_parsed):
        assert isinstance(uniform_numbers_parsed, dict)

    def test_has_required_keys(self, uniform_numbers_parsed):
        assert "title" in uniform_numbers_parsed
        assert "number" in uniform_numbers_parsed
        assert "team" in uniform_numbers_parsed
        assert "players" in uniform_numbers_parsed

    def test_model_validates(self, uniform_numbers_model):
        assert isinstance(uniform_numbers_model, UniformNumbers)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestUniformNumbersMetadata:
    def test_title(self, uniform_numbers_model):
        assert (
            uniform_numbers_model.title
            == "All Players To Wear Number 6 For Pittsburgh Steelers"
        )

    def test_number(self, uniform_numbers_model):
        assert uniform_numbers_model.number == 6

    def test_team(self, uniform_numbers_model):
        assert uniform_numbers_model.team == "Pittsburgh Steelers"


# =========================================================================
# Players table
# =========================================================================


@pytest.mark.unit
class TestUniformNumbersPlayers:
    def test_player_count(self, uniform_numbers_model):
        assert len(uniform_numbers_model.players) == 8

    def test_player_types(self, uniform_numbers_model):
        for p in uniform_numbers_model.players:
            assert isinstance(p, UniformNumberPlayer)

    def test_first_player(self, uniform_numbers_model):
        first = uniform_numbers_model.players[0]
        assert first.player == "Bubby Brister"
        assert first.player_href == "/players/B/BrisBu00.htm"
        assert first.player_id == "BrisBu00"
        assert first.year_min == 1986
        assert first.year_max == 1992
        assert first.av == 34

    def test_player_with_empty_av(self, uniform_numbers_model):
        # Thomas Cosgrove has no AV value
        cosgrove = uniform_numbers_model.players[1]
        assert cosgrove.player == "Thomas Cosgrove"
        assert cosgrove.player_id == "CosgTh20"
        assert cosgrove.year_min == 1935
        assert cosgrove.year_max == 1935
        assert cosgrove.av is None

    def test_player_with_zero_av(self, uniform_numbers_model):
        # Devlin Hodges has AV of 0
        hodges = uniform_numbers_model.players[4]
        assert hodges.player == "Devlin Hodges"
        assert hodges.av == 0

    def test_last_player(self, uniform_numbers_model):
        last = uniform_numbers_model.players[-1]
        assert last.player == "Shaun Suisham"
        assert last.player_id == "suishsha01"
        assert last.year_min == 2010
        assert last.year_max == 2014
        assert last.av == 15


# =========================================================================
# Title extraction helpers
# =========================================================================


@pytest.mark.unit
class TestUniformNumbersExtraction:
    def test_extract_number(self):
        assert (
            UniformNumbersParser._extract_number(
                "All Players To Wear Number 6 For Pittsburgh Steelers"
            )
            == 6
        )

    def test_extract_number_no_team(self):
        assert (
            UniformNumbersParser._extract_number("All Players To Wear Number 12") == 12
        )

    def test_extract_number_no_match(self):
        assert UniformNumbersParser._extract_number("Some random title") == 0

    def test_extract_team(self):
        assert (
            UniformNumbersParser._extract_team(
                "All Players To Wear Number 6 For Pittsburgh Steelers"
            )
            == "Pittsburgh Steelers"
        )

    def test_extract_team_no_team(self):
        assert (
            UniformNumbersParser._extract_team("All Players To Wear Number 12") is None
        )


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestUniformNumbersParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ValueError, match="Could not find uniform_number table"):
            _uniform_numbers_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestUniformNumbersEndpointConfig:
    def test_config_with_team(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_uniform_numbers_config(number=6, team="pit")
        assert config.operation_id == "getUniformNumbers"
        assert config.query_params["number"] == "6"
        assert config.query_params["team"] == "pit"

    def test_config_without_team(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_uniform_numbers_config(number=12)
        assert config.operation_id == "getUniformNumbers"
        assert config.query_params["number"] == "12"
        assert "team" not in config.query_params

    def test_endpoint_via_mock(self, uniform_numbers_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=uniform_numbers_html,
        ):
            result = pfr.frivolities.get_uniform_numbers(number=6, team="pit")
        assert isinstance(result, UniformNumbers)
        assert result.number == 6
        assert result.team == "Pittsburgh Steelers"
        assert len(result.players) == 8


# #########################################################################
# QB WINS VS. FRANCHISES
# #########################################################################


@pytest.fixture(scope="module")
def qb_wins_html() -> str:
    return (FIXTURE_DIR / "qb_wins.html").read_text()


@pytest.fixture(scope="module")
def qb_wins_parsed(qb_wins_html: str) -> dict:
    return _qb_wins_parser.parse(qb_wins_html)


@pytest.fixture(scope="module")
def qb_wins_model(qb_wins_parsed: dict) -> QBWins:
    return QBWins.model_validate(qb_wins_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestQBWinsSmoke:
    def test_parse_returns_dict(self, qb_wins_parsed):
        assert isinstance(qb_wins_parsed, dict)

    def test_has_required_keys(self, qb_wins_parsed):
        assert "title" in qb_wins_parsed
        assert "entries" in qb_wins_parsed

    def test_model_validates(self, qb_wins_model):
        assert isinstance(qb_wins_model, QBWins)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestQBWinsMetadata:
    def test_title(self, qb_wins_model):
        assert qb_wins_model.title == "Quarterback Wins"


# =========================================================================
# Entries table
# =========================================================================


@pytest.mark.unit
class TestQBWinsEntries:
    def test_entry_count(self, qb_wins_model):
        assert len(qb_wins_model.entries) == 100

    def test_entry_types(self, qb_wins_model):
        for entry in qb_wins_model.entries:
            assert isinstance(entry, QBWinEntry)

    def test_first_entry_beat_all(self, qb_wins_model):
        """Brett Favre beat all 32 teams."""
        first = qb_wins_model.entries[0]
        assert first.player == "Brett Favre"
        assert first.player_href == "/players/F/FavrBr00.htm"
        assert first.player_id == "FavrBr00"
        assert first.teams_beat == 32
        assert first.teams_not_beat == []

    def test_entry_with_one_team_not_beat(self, qb_wins_model):
        """Roethlisberger didn't beat Pittsburgh Steelers (his own team)."""
        roethlisberger = qb_wins_model.entries[4]
        assert roethlisberger.player == "Ben Roethlisberger"
        assert roethlisberger.teams_beat == 31
        assert roethlisberger.teams_not_beat == ["Pittsburgh Steelers"]

    def test_entry_with_multiple_teams_not_beat(self, qb_wins_model):
        """Drew Bledsoe didn't beat 3 teams."""
        bledsoe = next(e for e in qb_wins_model.entries if e.player == "Drew Bledsoe")
        assert bledsoe.teams_beat == 29
        assert len(bledsoe.teams_not_beat) == 3
        assert "Atlanta Falcons" in bledsoe.teams_not_beat
        assert "Las Vegas/LA/Oakland Raiders" in bledsoe.teams_not_beat
        assert "Tampa Bay Buccaneers" in bledsoe.teams_not_beat

    def test_last_entry(self, qb_wins_model):
        last = qb_wins_model.entries[-1]
        assert isinstance(last, QBWinEntry)
        assert last.teams_beat > 0
        assert isinstance(last.teams_not_beat, list)


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestQBWinsParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ValueError, match="Could not find qb_wins table"):
            _qb_wins_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestQBWinsEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_qb_wins_vs_franchises_config()
        assert config.operation_id == "getQBWinsVsFranchises"
        assert config.path_template == "/friv/qb-wins.htm"
        assert config.wait_for_element == "#qb_wins"

    def test_endpoint_via_mock(self, qb_wins_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=qb_wins_html,
        ):
            result = pfr.frivolities.get_qb_wins_vs_franchises()
        assert isinstance(result, QBWins)
        assert result.title == "Quarterback Wins"
        assert len(result.entries) == 100
        assert result.entries[0].player == "Brett Favre"


# #########################################################################
# NON-QUARTERBACK PASSERS
# #########################################################################


@pytest.fixture(scope="module")
def non_qb_passers_html() -> str:
    return (FIXTURE_DIR / "non_qb_passers.html").read_text()


@pytest.fixture(scope="module")
def non_qb_passers_parsed(non_qb_passers_html: str) -> dict:
    return _non_qb_passers_parser.parse(non_qb_passers_html)


@pytest.fixture(scope="module")
def non_qb_passers_model(non_qb_passers_parsed: dict) -> NonQBPassers:
    return NonQBPassers.model_validate(non_qb_passers_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersSmoke:
    def test_parse_returns_dict(self, non_qb_passers_parsed):
        assert isinstance(non_qb_passers_parsed, dict)

    def test_has_required_keys(self, non_qb_passers_parsed):
        assert "title" in non_qb_passers_parsed
        assert "entries" in non_qb_passers_parsed

    def test_model_validates(self, non_qb_passers_model):
        assert isinstance(non_qb_passers_model, NonQBPassers)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersMetadata:
    def test_title(self, non_qb_passers_model):
        assert non_qb_passers_model.title == "Non-Quarterback Passing"


# =========================================================================
# Entries table
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersEntries:
    def test_entry_count(self, non_qb_passers_model):
        assert len(non_qb_passers_model.entries) == 1576

    def test_entry_types(self, non_qb_passers_model):
        for entry in non_qb_passers_model.entries:
            assert isinstance(entry, NonQBPasserEntry)

    def test_first_entry_old_era(self, non_qb_passers_model):
        """Duke Abbruzzi — 1946 HB, some modern stats are None."""
        first = non_qb_passers_model.entries[0]
        assert first.player == "Duke Abbruzzi"
        assert first.player_href == "/players/A/AbbrDu20.htm"
        assert first.player_id == "AbbrDu20"
        assert first.pos == "HB"
        assert first.year_min == 1946
        assert first.year_max == 1946
        assert first.pass_cmp == 1
        assert first.pass_att == 1
        assert first.pass_cmp_perc == 100.0
        assert first.pass_yds == 11
        assert first.pass_td == 0
        assert first.pass_long == 11
        assert first.pass_rating == 112.5
        # Old era — no QBR or sack data
        assert first.qbr is None
        assert first.pass_sacked is None
        assert first.pass_sacked_yds is None

    def test_entry_with_full_modern_stats(self, non_qb_passers_model):
        """Odell Beckham Jr. — WR with QBR, sack data, and all stats."""
        beckham = next(
            e for e in non_qb_passers_model.entries if e.player == "Odell Beckham Jr."
        )
        assert beckham.pos == "WR"
        assert beckham.year_min == 2014
        assert beckham.year_max == 2024
        assert beckham.pass_cmp == 4
        assert beckham.pass_att == 6
        assert beckham.pass_cmp_perc == 66.7
        assert beckham.pass_yds == 144
        assert beckham.pass_td == 2
        assert beckham.pass_td_perc == 33.3
        assert beckham.pass_int == 0
        assert beckham.pass_long == 57
        assert beckham.pass_yds_per_att == 24.0
        assert beckham.pass_adj_yds_per_att == 30.7
        assert beckham.pass_yds_per_cmp == 36.0
        assert beckham.pass_rating == 149.3
        assert beckham.qbr == 1.3
        assert beckham.pass_sacked == 1
        assert beckham.pass_sacked_yds == 6
        assert beckham.pass_sacked_perc == 14.3
        assert beckham.pass_net_yds_per_att == 19.71
        assert beckham.pass_adj_net_yds_per_att == 25.43

    def test_last_entry(self, non_qb_passers_model):
        last = non_qb_passers_model.entries[-1]
        assert last.player == "Brandon Zylstra"
        assert last.player_id == "ZylsBr00"
        assert last.pos == "WR"
        assert last.pass_att == 1
        assert last.pass_cmp == 0
        assert last.pass_yds == 0


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ValueError, match="Could not find nonqb_passers table"):
            _non_qb_passers_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_non_qb_passers_config()
        assert config.operation_id == "getNonQBPassers"
        assert config.path_template == "/friv/nonqb.htm"
        assert config.wait_for_element == "#nonqb_passers"

    def test_endpoint_via_mock(self, non_qb_passers_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=non_qb_passers_html,
        ):
            result = pfr.frivolities.get_non_qb_passers()
        assert isinstance(result, NonQBPassers)
        assert result.title == "Non-Quarterback Passing"
        assert len(result.entries) == 1576
        assert result.entries[0].player == "Duke Abbruzzi"


# #########################################################################
# NON-SKILL POSITION TD SCORERS
# #########################################################################


@pytest.fixture(scope="module")
def non_skill_pos_td_html() -> str:
    return (FIXTURE_DIR / "non_skill_pos_td.html").read_text()


@pytest.fixture(scope="module")
def non_skill_pos_td_parsed(non_skill_pos_td_html: str) -> dict:
    return _non_skill_pos_td_parser.parse(non_skill_pos_td_html)


@pytest.fixture(scope="module")
def non_skill_pos_td_model(non_skill_pos_td_parsed: dict) -> NonSkillPosTdScorers:
    return NonSkillPosTdScorers.model_validate(non_skill_pos_td_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdSmoke:
    def test_parse_returns_dict(self, non_skill_pos_td_parsed):
        assert isinstance(non_skill_pos_td_parsed, dict)

    def test_has_required_keys(self, non_skill_pos_td_parsed):
        assert "title" in non_skill_pos_td_parsed
        assert "entries" in non_skill_pos_td_parsed

    def test_model_validates(self, non_skill_pos_td_model):
        assert isinstance(non_skill_pos_td_model, NonSkillPosTdScorers)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdMetadata:
    def test_title(self, non_skill_pos_td_model):
        assert non_skill_pos_td_model.title == "Non-Skill Position TD Scorers"


# =========================================================================
# Entries table
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdEntries:
    def test_entry_count(self, non_skill_pos_td_model):
        assert len(non_skill_pos_td_model.entries) == 215

    def test_entry_types(self, non_skill_pos_td_model):
        for entry in non_skill_pos_td_model.entries:
            assert isinstance(entry, NonSkillPosTdEntry)

    def test_first_entry_home_game(self, non_skill_pos_td_model):
        """Frank Crum — OT, DEN home game, receiving TD."""
        first = non_skill_pos_td_model.entries[0]
        assert first.player == "Frank Crum"
        assert first.player_href == "/players/C/CrumFr00.htm"
        assert first.player_id == "CrumFr00"
        assert first.pos == "OT"
        assert first.week_num == 20
        assert first.game_day_of_week == "Sat"
        assert first.game_date == "Jan 17, 2026"
        assert first.boxscore_href == "/boxscores/202601170den.htm"
        assert first.game_outcome == "W"
        assert first.team == "DEN"
        assert first.team_href == "/teams/den/2025.htm"
        assert first.game_location is None
        assert first.opp == "BUF"
        assert first.opp_href == "/teams/buf/2025.htm"
        assert first.pts_off == 33
        assert first.pts_def == 30
        assert first.rush_att == 0
        assert first.rush_yds == 0
        assert first.rush_long == 0
        assert first.rush_yds_per_att is None
        assert first.rush_td == 0
        assert first.rec == 1
        assert first.rec_yds == 7
        assert first.rec_long == 7
        assert first.rec_yds_per_rec == 7.0
        assert first.rec_td == 1

    def test_entry_away_game(self, non_skill_pos_td_model):
        """Jeffery Simmons — DT, TEN away at SFO, receiving TD."""
        simmons = non_skill_pos_td_model.entries[1]
        assert simmons.player == "Jeffery Simmons"
        assert simmons.pos == "DT"
        assert simmons.game_location == "@"
        assert simmons.team == "TEN*"
        assert simmons.opp == "SFO"
        assert simmons.game_outcome == "L"
        assert simmons.pts_off == 24
        assert simmons.pts_def == 37
        assert simmons.rec_td == 1

    def test_entry_with_rushing_td(self, non_skill_pos_td_model):
        """Akiem Hicks — DE, scored via rushing TD (not receiving)."""
        hicks = next(
            e for e in non_skill_pos_td_model.entries if e.player == "Akiem Hicks"
        )
        assert hicks.pos == "DE"
        assert hicks.rush_att == 1
        assert hicks.rush_yds == 1
        assert hicks.rush_long == 1
        assert hicks.rush_yds_per_att == 1.0
        assert hicks.rush_td == 1
        assert hicks.rec == 0
        assert hicks.rec_td == 0

    def test_last_entry_old_era(self, non_skill_pos_td_model):
        """Bob Gonya — T, 1934, oldest entry, some stats empty."""
        last = non_skill_pos_td_model.entries[-1]
        assert last.player == "Bob Gonya"
        assert last.player_id == "GonyBo20"
        assert last.pos == "T"
        assert last.game_date == "Oct 7, 1934"
        assert last.team == "PHI"
        assert last.opp == "PIT"
        assert last.rush_long is None
        assert last.rush_yds_per_att is None
        assert last.rec_yds == 4
        assert last.rec_td == 1


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ValueError, match="Could not find odd_scorers table"):
            _non_skill_pos_td_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_non_skill_pos_td_scorers_config()
        assert config.operation_id == "getNonSkillPosTdScorers"
        assert config.path_template == "/friv/odd_td.htm"
        assert config.wait_for_element == "#odd_scorers"

    def test_endpoint_via_mock(self, non_skill_pos_td_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=non_skill_pos_td_html,
        ):
            result = pfr.frivolities.get_non_skill_pos_td_scorers()
        assert isinstance(result, NonSkillPosTdScorers)
        assert result.title == "Non-Skill Position TD Scorers"
        assert len(result.entries) == 215
        assert result.entries[0].player == "Frank Crum"


# #########################################################################
# OCTOPUS TRACKER
# #########################################################################


@pytest.fixture(scope="module")
def octopus_tracker_html() -> str:
    return (FIXTURE_DIR / "octopus_tracker.html").read_text()


@pytest.fixture(scope="module")
def octopus_tracker_parsed(octopus_tracker_html: str) -> dict:
    return _octopus_tracker_parser.parse(octopus_tracker_html)


@pytest.fixture(scope="module")
def octopus_tracker_model(octopus_tracker_parsed: dict) -> OctopusTracker:
    return OctopusTracker.model_validate(octopus_tracker_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestOctopusTrackerSmoke:
    def test_parse_returns_dict(self, octopus_tracker_parsed):
        assert isinstance(octopus_tracker_parsed, dict)

    def test_has_required_keys(self, octopus_tracker_parsed):
        assert "title" in octopus_tracker_parsed
        assert "entries" in octopus_tracker_parsed

    def test_model_validates(self, octopus_tracker_model):
        assert isinstance(octopus_tracker_model, OctopusTracker)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestOctopusTrackerMetadata:
    def test_title(self, octopus_tracker_model):
        assert (
            octopus_tracker_model.title
            == "Octopus Touchdown and Two Point Conversion Scorers"
        )


# =========================================================================
# Entries table
# =========================================================================


@pytest.mark.unit
class TestOctopusTrackerEntries:
    def test_entry_count(self, octopus_tracker_model):
        assert len(octopus_tracker_model.entries) == 200

    def test_entry_types(self, octopus_tracker_model):
        for entry in octopus_tracker_model.entries:
            assert isinstance(entry, OctopusEntry)

    def test_first_entry_pass_td(self, octopus_tracker_model):
        """Chris Godwin — TAM, pass TD + pass 2pt, loss."""
        first = octopus_tracker_model.entries[0]
        assert first.player == "Chris Godwin"
        assert first.player_href == "/players/G/GodwCh00.htm"
        assert first.player_id == "GodwCh00"
        assert first.week_num == 15
        assert first.game_day_of_week == "Thu"
        assert first.game_date == "Dec 11, 2025"
        assert first.boxscore_href == "/boxscores/202512110tam.htm"
        assert first.game_outcome == "L"
        assert first.team == "TAM"
        assert first.team_href == "/teams/tam/2025.htm"
        assert first.opp == "ATL"
        assert first.opp_href == "/teams/atl/2025.htm"
        assert first.margin == 14
        assert first.score_type == "Pass"
        assert first.xpa_type == "Pass"

    def test_entry_rush_td(self, octopus_tracker_model):
        """Jonathan Taylor — IND, rush TD + rush 2pt, win."""
        taylor = octopus_tracker_model.entries[2]
        assert taylor.player == "Jonathan Taylor"
        assert taylor.player_href == "/players/T/TaylJo02.htm"
        assert taylor.player_id == "TaylJo02"
        assert taylor.week_num == 5
        assert taylor.game_day_of_week == "Sun"
        assert taylor.game_date == "Oct 5, 2025"
        assert taylor.game_outcome == "W"
        assert taylor.team == "IND"
        assert taylor.opp == "LVR"
        assert taylor.margin == 37
        assert taylor.score_type == "Rush"
        assert taylor.xpa_type == "Rush"

    def test_entry_negative_margin(self, octopus_tracker_model):
        """Last entry — Torrance Small, negative margin, loss."""
        last = octopus_tracker_model.entries[-1]
        assert last.player == "Torrance Small"
        assert last.player_href == "/players/S/SmalTo00.htm"
        assert last.player_id == "SmalTo00"
        assert last.week_num == 2
        assert last.game_date == "Sep 11, 1994"
        assert last.game_outcome == "L"
        assert last.team == "NOR"
        assert last.opp == "WAS"
        assert last.margin == -21
        assert last.score_type == "Pass"
        assert last.xpa_type == "Pass"

    def test_middle_entry(self, octopus_tracker_model):
        """DeAndre Hopkins — row 100, HOU vs KAN."""
        mid = octopus_tracker_model.entries[99]
        assert mid.player == "DeAndre Hopkins"
        assert mid.player_id == "HopkDe00"
        assert mid.team == "HOU"
        assert mid.opp == "KAN"
        assert mid.margin == -10
        assert mid.game_outcome == "L"


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestOctopusTrackerParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ValueError, match="Could not find octopus table"):
            _octopus_tracker_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestOctopusTrackerEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_octopus_tracker_config()
        assert config.operation_id == "getOctopusTracker"
        assert config.path_template == "/friv/octopus-tracker.htm"
        assert config.wait_for_element == "#octopus"

    def test_endpoint_via_mock(self, octopus_tracker_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=octopus_tracker_html,
        ):
            result = pfr.frivolities.get_octopus_tracker()
        assert isinstance(result, OctopusTracker)
        assert result.title == "Octopus Touchdown and Two Point Conversion Scorers"
        assert len(result.entries) == 200
        assert result.entries[0].player == "Chris Godwin"
