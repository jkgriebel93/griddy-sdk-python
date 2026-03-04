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
- Cups of Coffee
  (``/friv/coffee.htm``)
- Multi-Sport Players
  (``/friv/multisport.htm``)
- Pronunciation Guide
  (``/friv/pronunciation-guide.htm``)
- Overtime Ties
  (``/friv/nfl-ties.htm``)
- Last Undefeated Team
  (``/friv/last-undefeated.htm``)
- Standings on Any Date
  (``/boxscores/standings.cgi``)
"""

from unittest.mock import patch

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import (
    BirthdayPlayer,
    Birthdays,
    BirthplaceFiltered,
    BirthplaceLanding,
    BirthplaceLocation,
    BirthplacePlayer,
    CareerLeader,
    CoffeeEntry,
    CupsOfCoffee,
    LastUndefeated,
    LastUndefeatedEntry,
    MilestoneEntry,
    MultiSportPlayer,
    MultiSportPlayers,
    MultiTeamPlayers,
    MultiTeamPlayerStats,
    NonQBPasserEntry,
    NonQBPassers,
    NonSkillPosTdEntry,
    NonSkillPosTdScorers,
    OctopusEntry,
    OctopusTracker,
    OvertimeTieEntry,
    OvertimeTies,
    PlayerBornBefore,
    PlayersBornBefore,
    PronunciationEntry,
    PronunciationGuide,
    QBWinEntry,
    QBWins,
    StandingsOnDate,
    StandingsTeamEntry,
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
from griddy.pfr.parsers.cups_of_coffee import CupsOfCoffeeParser
from griddy.pfr.parsers.last_undefeated import LastUndefeatedParser
from griddy.pfr.parsers.multi_sport_players import MultiSportPlayersParser
from griddy.pfr.parsers.multi_team_players import MultiTeamPlayersParser
from griddy.pfr.parsers.non_qb_passers import NonQBPassersParser
from griddy.pfr.parsers.non_skill_pos_td import NonSkillPosTdParser
from griddy.pfr.parsers.octopus_tracker import OctopusTrackerParser
from griddy.pfr.parsers.overtime_ties import OvertimeTiesParser
from griddy.pfr.parsers.players_born_before import PlayersBornBeforeParser
from griddy.pfr.parsers.pronunciation_guide import PronunciationGuideParser
from griddy.pfr.parsers.qb_wins import QBWinsParser
from griddy.pfr.parsers.standings_on_date import StandingsOnDateParser
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
_cups_of_coffee_parser = CupsOfCoffeeParser()
_multi_sport_players_parser = MultiSportPlayersParser()
_pronunciation_guide_parser = PronunciationGuideParser()
_overtime_ties_parser = OvertimeTiesParser()
_last_undefeated_parser = LastUndefeatedParser()
_standings_on_date_parser = StandingsOnDateParser()

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
        with pytest.raises(ParsingError, match="Could not find"):
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
        with pytest.raises(ParsingError, match="Could not find milestones table"):
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
            ParsingError, match="Could not find upcoming milestones table"
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
        with pytest.raises(ParsingError, match="Could not find birthdays table"):
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
        with pytest.raises(ParsingError, match="Could not find birthplaces table"):
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
        with pytest.raises(ParsingError, match="Could not find birthplaces table"):
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
        with pytest.raises(ParsingError, match="Could not find players table"):
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
        with pytest.raises(ParsingError, match="Could not find uniform_number table"):
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
        with pytest.raises(ParsingError, match="Could not find qb_wins table"):
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
        with pytest.raises(ParsingError, match="Could not find nonqb_passers table"):
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
        with pytest.raises(ParsingError, match="Could not find odd_scorers table"):
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
        with pytest.raises(ParsingError, match="Could not find octopus table"):
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


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║  Cups of Coffee                                                       ║
# ╚═════════════════════════════════════════════════════════════════════════╝

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def cups_of_coffee_html() -> str:
    return (FIXTURE_DIR / "cups_of_coffee.html").read_text()


@pytest.fixture(scope="module")
def cups_of_coffee_parsed(cups_of_coffee_html: str) -> dict:
    return _cups_of_coffee_parser.parse(cups_of_coffee_html)


@pytest.fixture(scope="module")
def cups_of_coffee_model(cups_of_coffee_parsed: dict) -> CupsOfCoffee:
    return CupsOfCoffee.model_validate(cups_of_coffee_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestCupsOfCoffeeSmoke:
    def test_parse_returns_dict(self, cups_of_coffee_parsed):
        assert isinstance(cups_of_coffee_parsed, dict)

    def test_has_required_keys(self, cups_of_coffee_parsed):
        assert "title" in cups_of_coffee_parsed
        assert "entries" in cups_of_coffee_parsed

    def test_model_validates(self, cups_of_coffee_model):
        assert isinstance(cups_of_coffee_model, CupsOfCoffee)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestCupsOfCoffeeMetadata:
    def test_title(self, cups_of_coffee_model):
        assert cups_of_coffee_model.title == "Cups of Coffee"


# =========================================================================
# Entries table
# =========================================================================


@pytest.mark.unit
class TestCupsOfCoffeeEntries:
    def test_entry_count(self, cups_of_coffee_model):
        assert len(cups_of_coffee_model.entries) == 1481

    def test_entry_types(self, cups_of_coffee_model):
        for entry in cups_of_coffee_model.entries:
            assert isinstance(entry, CoffeeEntry)

    def test_first_entry(self, cups_of_coffee_model):
        """Nate Abrams — E, 1921, all stats zero, pass_sacked empty."""
        first = cups_of_coffee_model.entries[0]
        assert first.player == "Nate Abrams"
        assert first.player_href == "/players/A/AbraNa20.htm"
        assert first.player_id == "AbraNa20"
        assert first.pos == "E"
        assert first.year_id == "1921"
        assert first.all_pros_first_team == 0
        assert first.pro_bowls == 0
        assert first.years_as_primary_starter == 0
        assert first.career_av == 0
        assert first.g == 1
        assert first.pass_cmp == 0
        assert first.pass_att == 0
        assert first.pass_yds == 0
        assert first.pass_td == 0
        assert first.pass_long == 0
        assert first.pass_int == 0
        # Pre-sack-tracking era — empty cells
        assert first.pass_sacked is None
        assert first.pass_sacked_yds is None
        assert first.rush_att == 0
        assert first.rush_yds == 0
        assert first.rush_td == 0
        assert first.rush_long == 0
        assert first.rec == 0
        assert first.rec_yds == 0
        assert first.rec_td == 0
        assert first.rec_long == 0

    def test_entry_with_rushing_stats(self, cups_of_coffee_model):
        """Vincent Alexander — RB, 1987, career_av=1, meaningful rushing."""
        entry = cups_of_coffee_model.entries[8]
        assert entry.player == "Vincent Alexander"
        assert entry.pos == "RB"
        assert entry.year_id == "1987"
        assert entry.career_av == 1
        assert entry.g == 1
        assert entry.rush_att == 21
        assert entry.rush_yds == 71
        assert entry.rush_td == 1
        assert entry.rush_long == 16
        assert entry.rec == 2
        assert entry.rec_yds == 15

    def test_entry_with_negative_rush_yds(self, cups_of_coffee_model):
        """Verify negative rushing yards are parsed correctly."""
        negatives = [
            e
            for e in cups_of_coffee_model.entries
            if e.rush_yds is not None and e.rush_yds < 0
        ]
        assert len(negatives) > 0
        # Buddy Allen is the first with negative rush yards
        buddy = next(
            e for e in cups_of_coffee_model.entries if e.player == "Buddy Allen"
        )
        assert buddy.rush_yds == -4

    def test_last_entry(self, cups_of_coffee_model):
        """Marty Zoll — G, 1921, all stats zero, pre-sack era."""
        last = cups_of_coffee_model.entries[-1]
        assert last.player == "Marty Zoll"
        assert last.player_id == "ZollMa20"
        assert last.pos == "G"
        assert last.year_id == "1921"
        assert last.g == 1
        assert last.pass_sacked is None
        assert last.pass_sacked_yds is None

    def test_all_games_equal_one(self, cups_of_coffee_model):
        """Every player on this page played exactly 1 game."""
        for entry in cups_of_coffee_model.entries:
            assert entry.g == 1


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestCupsOfCoffeeParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ParsingError, match="Could not find coffee table"):
            _cups_of_coffee_parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestCupsOfCoffeeEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_cups_of_coffee_config()
        assert config.operation_id == "getCupsOfCoffee"
        assert config.path_template == "/friv/coffee.htm"
        assert config.wait_for_element == "#coffee"

    def test_endpoint_via_mock(self, cups_of_coffee_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=cups_of_coffee_html,
        ):
            result = pfr.frivolities.get_cups_of_coffee()
        assert isinstance(result, CupsOfCoffee)
        assert result.title == "Cups of Coffee"
        assert len(result.entries) == 1481
        assert result.entries[0].player == "Nate Abrams"


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║  Multi-Sport Players                                                   ║
# ╚═════════════════════════════════════════════════════════════════════════╝

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def multi_sport_players_html() -> str:
    return (FIXTURE_DIR / "multi_sport_players.html").read_text()


@pytest.fixture(scope="module")
def multi_sport_players_parsed(multi_sport_players_html: str) -> dict:
    return _multi_sport_players_parser.parse(multi_sport_players_html)


@pytest.fixture(scope="module")
def multi_sport_players_model(
    multi_sport_players_parsed: dict,
) -> MultiSportPlayers:
    return MultiSportPlayers.model_validate(multi_sport_players_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersSmoke:
    def test_parse_returns_dict(self, multi_sport_players_parsed):
        assert isinstance(multi_sport_players_parsed, dict)

    def test_has_required_keys(self, multi_sport_players_parsed):
        assert "title" in multi_sport_players_parsed
        assert "entries" in multi_sport_players_parsed

    def test_model_validates(self, multi_sport_players_model):
        assert isinstance(multi_sport_players_model, MultiSportPlayers)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersMetadata:
    def test_title(self, multi_sport_players_model):
        assert multi_sport_players_model.title == "Multisport Athletes"


# =========================================================================
# Entries table
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersEntries:
    def test_entry_count(self, multi_sport_players_model):
        assert len(multi_sport_players_model.entries) == 450

    def test_entry_types(self, multi_sport_players_model):
        for entry in multi_sport_players_model.entries:
            assert isinstance(entry, MultiSportPlayer)

    def test_first_entry(self, multi_sport_players_model):
        """Mo Alie-Cox — TE, 2018–2025, college basketball."""
        first = multi_sport_players_model.entries[0]
        assert first.player == "Mo Alie-Cox"
        assert first.player_href == "/players/A/AlieMo00.htm"
        assert first.player_id == "AlieMo00"
        assert first.pos == "TE"
        assert first.year_min == 2018
        assert first.year_max == 2025
        assert first.all_pros_first_team == 0
        assert first.pro_bowls == 0
        assert first.years_as_primary_starter == 2
        assert first.career_av == 12
        assert first.g == 125
        assert first.rec == 127
        assert first.rec_yds == 1550
        assert first.rec_td == 16
        assert first.rec_long == 45
        assert len(first.other_links) == 1
        assert first.other_links[0].text == "College Basketball at Sports-Reference.com"
        assert "sports-reference.com/cbb" in first.other_links[0].href

    def test_last_entry(self, multi_sport_players_model):
        """George Magerkurth — T, 1920, pre-sack era."""
        last = multi_sport_players_model.entries[-1]
        assert last.player == "George Magerkurth"
        assert last.player_id == "MageGe20"
        assert last.pos == "T"
        assert last.year_min == 1920
        assert last.year_max == 1920
        assert last.g == 1
        assert last.pass_sacked is None
        assert last.pass_sacked_yds is None
        assert len(last.other_links) == 1

    def test_entry_with_multiple_links(self, multi_sport_players_model):
        """Drew Henson — had both Baseball-Reference and Minors links."""
        henson = next(
            e for e in multi_sport_players_model.entries if e.player == "Drew Henson"
        )
        assert len(henson.other_links) == 2
        link_texts = [link.text for link in henson.other_links]
        assert "Baseball-Reference.com" in link_texts
        assert "Minors at Baseball-Reference.com" in link_texts

    def test_entry_with_negative_rush_yds(self, multi_sport_players_model):
        """Drake London — negative rush_yds (-3)."""
        london = next(
            e for e in multi_sport_players_model.entries if e.player == "Drake London"
        )
        assert london.rush_yds == -3

    def test_entry_with_empty_sack_fields(self, multi_sport_players_model):
        """Reggie Carolan — 1962, pre-sack era, empty sack cells."""
        carolan = next(
            e for e in multi_sport_players_model.entries if e.player == "Reggie Carolan"
        )
        assert carolan.year_min == 1962
        assert carolan.pass_sacked is None
        assert carolan.pass_sacked_yds is None

    def test_tom_brady(self, multi_sport_players_model):
        """Tom Brady — QB, 2000–2022, significant passing stats."""
        brady = next(
            e for e in multi_sport_players_model.entries if e.player == "Tom Brady"
        )
        assert brady.pos == "QB"
        assert brady.year_min == 2000
        assert brady.year_max == 2022
        assert brady.all_pros_first_team == 3
        assert brady.pro_bowls == 15
        assert brady.career_av == 184
        assert brady.g == 335
        assert brady.pass_cmp == 7753
        assert brady.pass_yds == 89214
        assert brady.pass_td == 649
        assert brady.pass_sacked == 565
        assert len(brady.other_links) == 1
        assert "baseball-reference.com" in brady.other_links[0].href


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ParsingError, match="Could not find multisport table"):
            _multi_sport_players_parser.parse(
                "<html><body>No tables here</body></html>"
            )


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_multi_sport_players_config()
        assert config.operation_id == "getMultiSportPlayers"
        assert config.path_template == "/friv/multisport.htm"
        assert config.wait_for_element == "#multisport"

    def test_endpoint_via_mock(self, multi_sport_players_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=multi_sport_players_html,
        ):
            result = pfr.frivolities.get_multi_sport_players()
        assert isinstance(result, MultiSportPlayers)
        assert result.title == "Multisport Athletes"
        assert len(result.entries) == 450
        assert result.entries[0].player == "Mo Alie-Cox"


# =========================================================================
# Pronunciation Guide
# =========================================================================


@pytest.fixture(scope="module")
def pronunciation_guide_html() -> str:
    return (FIXTURE_DIR / "pronunciation_guide.html").read_text()


@pytest.fixture(scope="module")
def pronunciation_guide_parsed(pronunciation_guide_html: str) -> dict:
    return _pronunciation_guide_parser.parse(pronunciation_guide_html)


@pytest.fixture(scope="module")
def pronunciation_guide_model(
    pronunciation_guide_parsed: dict,
) -> PronunciationGuide:
    return PronunciationGuide.model_validate(pronunciation_guide_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideSmoke:
    def test_parse_returns_dict(self, pronunciation_guide_parsed):
        assert isinstance(pronunciation_guide_parsed, dict)

    def test_has_required_keys(self, pronunciation_guide_parsed):
        assert "title" in pronunciation_guide_parsed
        assert "entries" in pronunciation_guide_parsed

    def test_model_validates(self, pronunciation_guide_model):
        assert isinstance(pronunciation_guide_model, PronunciationGuide)


# =========================================================================
# Metadata
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideMetadata:
    def test_title(self, pronunciation_guide_model):
        assert (
            pronunciation_guide_model.title
            == "Current and Former Player Name Pronunciation Guide"
        )


# =========================================================================
# Entries
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideEntries:
    def test_entry_count(self, pronunciation_guide_model):
        assert len(pronunciation_guide_model.entries) == 2093

    def test_all_entries_are_pronunciation_entry(self, pronunciation_guide_model):
        for entry in pronunciation_guide_model.entries:
            assert isinstance(entry, PronunciationEntry)

    def test_first_entry(self, pronunciation_guide_model):
        first = pronunciation_guide_model.entries[0]
        assert first.player == "Isaako Aaitui"
        assert first.player_href == "/players/A/AaitIs00.htm"
        assert first.player_id == "AaitIs00"
        assert first.pronunciation == "e-saw-AH-co ah-ah-TWO-e"

    def test_last_entry(self, pronunciation_guide_model):
        last = pronunciation_guide_model.entries[-1]
        assert last.player == "Shane Zylstra"
        assert last.player_id == "ZylsSh00"
        assert last.pronunciation == "ZILL-struh"

    def test_parenthetical_pronunciation(self, pronunciation_guide_model):
        """David Blough uses parenthetical clarification."""
        blough = next(
            e for e in pronunciation_guide_model.entries if e.player == "David Blough"
        )
        assert 'BLAU (like "cow")' in blough.pronunciation

    def test_apostrophe_in_name(self, pronunciation_guide_model):
        """De'Von Achane has an apostrophe in first name."""
        achane = next(
            e for e in pronunciation_guide_model.entries if e.player == "De'Von Achane"
        )
        assert achane.player_id == "AchaDe00"
        assert achane.pronunciation == "duh-VAHN AY-chan"

    def test_name_with_suffix(self, pronunciation_guide_model):
        """Dorance Armstrong Jr. has a name suffix."""
        armstrong = next(
            e
            for e in pronunciation_guide_model.entries
            if e.player == "Dorance Armstrong Jr."
        )
        assert armstrong.pronunciation == "DOOR-intz"

    def test_tua_tagovailoa(self, pronunciation_guide_model):
        """Tua Tagovailoa is a well-known pronunciation example."""
        tua = next(
            e for e in pronunciation_guide_model.entries if e.player == "Tua Tagovailoa"
        )
        assert tua.player_id == "TagoTu00"
        assert tua.pronunciation == "TWO-uh TUNG-oh-vai-LO-uh"

    def test_all_entries_have_pronunciation(self, pronunciation_guide_model):
        for entry in pronunciation_guide_model.entries:
            assert entry.pronunciation, f"{entry.player} has empty pronunciation"

    def test_all_entries_have_player_href(self, pronunciation_guide_model):
        for entry in pronunciation_guide_model.entries:
            assert entry.player_href is not None
            assert entry.player_href.startswith("/players/")


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideParserErrors:
    def test_raises_on_missing_content_div(self):
        with pytest.raises(ParsingError, match="Could not find #content div"):
            _pronunciation_guide_parser.parse("<html><body>No content</body></html>")

    def test_raises_on_missing_list(self):
        with pytest.raises(ParsingError, match="Could not find pronunciation list"):
            _pronunciation_guide_parser.parse(
                '<html><body><div id="content"><h1>Title</h1></div></body></html>'
            )


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestPronunciationGuideEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_pronunciation_guide_config()
        assert config.operation_id == "getPronunciationGuide"
        assert config.path_template == "/friv/pronunciation-guide.htm"
        assert config.wait_for_element == "#content ul"

    def test_endpoint_via_mock(self, pronunciation_guide_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=pronunciation_guide_html,
        ):
            result = pfr.frivolities.get_pronunciation_guide()
        assert isinstance(result, PronunciationGuide)
        assert result.title == "Current and Former Player Name Pronunciation Guide"
        assert len(result.entries) == 2093
        assert result.entries[0].player == "Isaako Aaitui"


# ╔═════════════════════════════════════════════════════════════════════════╗
# ║ Overtime Ties                                                         ║
# ╚═════════════════════════════════════════════════════════════════════════╝

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def overtime_ties_html() -> str:
    return (FIXTURE_DIR / "overtime_ties.html").read_text()


@pytest.fixture(scope="module")
def overtime_ties_parsed(overtime_ties_html: str) -> dict:
    return _overtime_ties_parser.parse(overtime_ties_html)


@pytest.fixture(scope="module")
def overtime_ties_model(overtime_ties_parsed: dict) -> OvertimeTies:
    return OvertimeTies.model_validate(overtime_ties_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestOvertimeTiesSmoke:
    def test_parse_returns_dict(self, overtime_ties_parsed):
        assert isinstance(overtime_ties_parsed, dict)

    def test_has_required_keys(self, overtime_ties_parsed):
        assert "title" in overtime_ties_parsed
        assert "entries" in overtime_ties_parsed

    def test_model_validates(self, overtime_ties_model):
        assert isinstance(overtime_ties_model, OvertimeTies)


# =========================================================================
# Metadata
# =========================================================================


@pytest.mark.unit
class TestOvertimeTiesMetadata:
    def test_title(self, overtime_ties_model):
        assert overtime_ties_model.title == "Overtime Ties"


# =========================================================================
# Entry details
# =========================================================================


@pytest.mark.unit
class TestOvertimeTiesEntries:
    def test_entry_count(self, overtime_ties_model):
        assert len(overtime_ties_model.entries) == 30

    def test_all_entry_types(self, overtime_ties_model):
        for entry in overtime_ties_model.entries:
            assert isinstance(entry, OvertimeTieEntry)

    def test_first_entry(self, overtime_ties_model):
        first = overtime_ties_model.entries[0]
        assert first.year == 2025
        assert first.game_date == "Sep 28, 2025"
        assert first.team == "Green Bay Packers"
        assert first.team_href == "/teams/gnb/2025.htm"
        assert first.points == 40
        assert first.opp == "Dallas Cowboys"
        assert first.opp_href == "/teams/dal/2025.htm"
        assert first.points_opp == 40
        assert first.boxscore_href == "/boxscores/202509280dal.htm"

    def test_last_entry(self, overtime_ties_model):
        last = overtime_ties_model.entries[-1]
        assert last.year == 1974
        assert last.game_date == "Sep 22, 1974"
        assert last.team == "Pittsburgh Steelers"
        assert last.team_href == "/teams/pit/1974.htm"
        assert last.points == 35
        assert last.opp == "Denver Broncos"
        assert last.opp_href == "/teams/den/1974.htm"
        assert last.points_opp == 35
        assert last.boxscore_href == "/boxscores/197409220den.htm"

    def test_all_entries_have_equal_scores(self, overtime_ties_model):
        """Ties always have equal scores."""
        for entry in overtime_ties_model.entries:
            assert entry.points == entry.points_opp

    def test_all_entries_have_team_href(self, overtime_ties_model):
        for entry in overtime_ties_model.entries:
            assert entry.team_href is not None
            assert entry.team_href.startswith("/teams/")

    def test_all_entries_have_opp_href(self, overtime_ties_model):
        for entry in overtime_ties_model.entries:
            assert entry.opp_href is not None
            assert entry.opp_href.startswith("/teams/")

    def test_all_entries_have_boxscore_href(self, overtime_ties_model):
        for entry in overtime_ties_model.entries:
            assert entry.boxscore_href is not None
            assert entry.boxscore_href.startswith("/boxscores/")

    def test_all_entries_have_game_date(self, overtime_ties_model):
        for entry in overtime_ties_model.entries:
            assert entry.game_date is not None


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestOvertimeTiesParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ParsingError, match="Could not find ot_ties table"):
            _overtime_ties_parser.parse("<html><body>No tables</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestOvertimeTiesEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_overtime_ties_config()
        assert config.operation_id == "getOvertimeTies"
        assert config.path_template == "/friv/nfl-ties.htm"
        assert config.wait_for_element == "#ot_ties"

    def test_endpoint_via_mock(self, overtime_ties_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=overtime_ties_html,
        ):
            result = pfr.frivolities.get_overtime_ties()
        assert isinstance(result, OvertimeTies)
        assert result.title == "Overtime Ties"
        assert len(result.entries) == 30
        assert result.entries[0].year == 2025


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  Last Undefeated Team                                                    ║
# ╚═══════════════════════════════════════════════════════════════════════════╝


@pytest.fixture(scope="module")
def last_undefeated_html() -> str:
    return (FIXTURE_DIR / "last_undefeated.html").read_text()


@pytest.fixture(scope="module")
def last_undefeated_parsed(last_undefeated_html: str) -> dict:
    return _last_undefeated_parser.parse(last_undefeated_html)


@pytest.fixture(scope="module")
def last_undefeated_model(last_undefeated_parsed: dict) -> LastUndefeated:
    return LastUndefeated.model_validate(last_undefeated_parsed)


# =========================================================================
# Smoke
# =========================================================================


@pytest.mark.unit
class TestLastUndefeatedSmoke:
    def test_parse_returns_dict(self, last_undefeated_parsed):
        assert isinstance(last_undefeated_parsed, dict)

    def test_has_required_keys(self, last_undefeated_parsed):
        assert "title" in last_undefeated_parsed
        assert "entries" in last_undefeated_parsed

    def test_model_validates(self, last_undefeated_model):
        assert isinstance(last_undefeated_model, LastUndefeated)


# =========================================================================
# Metadata
# =========================================================================


@pytest.mark.unit
class TestLastUndefeatedMetadata:
    def test_title(self, last_undefeated_model):
        assert last_undefeated_model.title == "Last Undefeated Team"


# =========================================================================
# Entry details
# =========================================================================


@pytest.mark.unit
class TestLastUndefeatedEntries:
    def test_entry_count(self, last_undefeated_model):
        assert len(last_undefeated_model.entries) == 149

    def test_all_entry_types(self, last_undefeated_model):
        for entry in last_undefeated_model.entries:
            assert isinstance(entry, LastUndefeatedEntry)

    def test_first_entry(self, last_undefeated_model):
        first = last_undefeated_model.entries[0]
        assert first.year == 2025
        assert first.year_href == "/years/2025/"
        assert first.league_id == "NFL"
        assert first.team == "Bills"
        assert first.team_href == "/teams/buf/2025.htm"
        assert first.record == "4-0-0"
        assert first.first_loss == "23-20 vs. Patriots"
        assert first.first_loss_href == "/boxscores/202510050buf.htm"
        assert first.final_record is None
        assert first.playoff_result is None
        assert first.playoff_result_href is None

    def test_continuation_row(self, last_undefeated_model):
        """Second entry is a continuation row (same year, year is None)."""
        second = last_undefeated_model.entries[1]
        assert second.year is None
        assert second.year_href is None
        assert second.league_id == "NFL"
        assert second.team == "Eagles"
        assert second.team_href == "/teams/phi/2025.htm"
        assert second.record == "4-0-0"

    def test_entry_with_playoff_result(self, last_undefeated_model):
        """2024 Chiefs had a playoff result."""
        third = last_undefeated_model.entries[2]
        assert third.year == 2024
        assert third.team == "Chiefs"
        assert third.record == "9-0-0"
        assert third.final_record == "17-3-0"
        assert third.playoff_result == "Lost SB"
        assert third.playoff_result_href == "/boxscores/202502090phi.htm"

    def test_last_entry(self, last_undefeated_model):
        last = last_undefeated_model.entries[-1]
        assert last.year == 1920
        assert last.year_href == "/years/1920_APFA/"
        assert last.league_id == "APFA"
        assert last.team == "Pros"
        assert last.team_href == "/teams/akr/1920.htm"
        assert last.record == "8-0-3"
        assert last.first_loss == "Undefeated"
        assert last.first_loss_href is None
        assert last.final_record == "8-0-3"

    def test_all_entries_have_team(self, last_undefeated_model):
        for entry in last_undefeated_model.entries:
            assert entry.team is not None

    def test_all_entries_have_team_href(self, last_undefeated_model):
        for entry in last_undefeated_model.entries:
            assert entry.team_href is not None
            assert entry.team_href.startswith("/teams/")

    def test_all_entries_have_league_id(self, last_undefeated_model):
        for entry in last_undefeated_model.entries:
            assert entry.league_id is not None

    def test_undefeated_seasons(self, last_undefeated_model):
        """Six teams went fully undefeated."""
        undefeated = [
            e for e in last_undefeated_model.entries if e.first_loss == "Undefeated"
        ]
        assert len(undefeated) == 6

    def test_continuation_row_count(self, last_undefeated_model):
        """29 continuation rows have no year."""
        no_year = [e for e in last_undefeated_model.entries if e.year is None]
        assert len(no_year) == 29


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestLastUndefeatedParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ParsingError, match="Could not find undefeated_teams table"):
            _last_undefeated_parser.parse("<html><body>No tables</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestLastUndefeatedEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_last_undefeated_config()
        assert config.operation_id == "getLastUndefeated"
        assert config.path_template == "/friv/last-undefeated.htm"
        assert config.wait_for_element == "#undefeated_teams"

    def test_endpoint_via_mock(self, last_undefeated_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=last_undefeated_html,
        ):
            result = pfr.frivolities.get_last_undefeated()
        assert isinstance(result, LastUndefeated)
        assert result.title == "Last Undefeated Team"
        assert len(result.entries) == 149
        assert result.entries[0].year == 2025


# =========================================================================
# Standings on Any Date
# =========================================================================


@pytest.fixture(scope="module")
def standings_on_date_html() -> str:
    return (FIXTURE_DIR / "standings_on_date.html").read_text()


@pytest.fixture(scope="module")
def standings_on_date_parsed(standings_on_date_html: str) -> dict:
    return _standings_on_date_parser.parse(standings_on_date_html)


@pytest.fixture(scope="module")
def standings_on_date_model(standings_on_date_parsed: dict) -> StandingsOnDate:
    return StandingsOnDate.model_validate(standings_on_date_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateSmoke:
    def test_parse_returns_dict(self, standings_on_date_parsed):
        assert isinstance(standings_on_date_parsed, dict)

    def test_has_required_keys(self, standings_on_date_parsed):
        assert "title" in standings_on_date_parsed
        assert "teams" in standings_on_date_parsed

    def test_model_validates(self, standings_on_date_model):
        assert isinstance(standings_on_date_model, StandingsOnDate)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateMetadata:
    def test_title(self, standings_on_date_model):
        assert standings_on_date_model.title == "NFL Standings As Of October 10, 2016"


# =========================================================================
# Team entries
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateEntries:
    def test_team_count(self, standings_on_date_model):
        assert len(standings_on_date_model.teams) == 32

    def test_all_are_standings_team_entry(self, standings_on_date_model):
        for team in standings_on_date_model.teams:
            assert isinstance(team, StandingsTeamEntry)

    def test_first_team(self, standings_on_date_model):
        """First team is New England Patriots (AFC East)."""
        first = standings_on_date_model.teams[0]
        assert first.conference == "AFC"
        assert first.division == "AFC East"
        assert first.team == "New England Patriots"
        assert first.team_href == "/teams/nwe/2016.htm"
        assert first.playoff_marker == "*"
        assert first.wins == 4
        assert first.losses == 1
        assert first.ties == 0
        assert first.win_loss_perc == pytest.approx(0.8)
        assert first.points_for == 114
        assert first.points_against == 74
        assert first.points_diff == 40
        assert first.margin_of_victory == pytest.approx(8.0)

    def test_last_team(self, standings_on_date_model):
        """Last team is San Francisco 49ers (NFC West)."""
        last = standings_on_date_model.teams[-1]
        assert last.conference == "NFC"
        assert last.division == "NFC West"
        assert last.team == "San Francisco 49ers"
        assert last.team_href == "/teams/sfo/2016.htm"
        assert last.playoff_marker is None
        assert last.wins == 1
        assert last.losses == 4
        assert last.points_diff == -29
        assert last.margin_of_victory == pytest.approx(-5.8)

    def test_conferences(self, standings_on_date_model):
        conferences = {t.conference for t in standings_on_date_model.teams}
        assert conferences == {"AFC", "NFC"}

    def test_afc_team_count(self, standings_on_date_model):
        afc = [t for t in standings_on_date_model.teams if t.conference == "AFC"]
        assert len(afc) == 16

    def test_nfc_team_count(self, standings_on_date_model):
        nfc = [t for t in standings_on_date_model.teams if t.conference == "NFC"]
        assert len(nfc) == 16

    def test_divisions(self, standings_on_date_model):
        divisions = {t.division for t in standings_on_date_model.teams}
        assert len(divisions) == 8
        assert "AFC East" in divisions
        assert "NFC West" in divisions

    def test_all_teams_have_team_name(self, standings_on_date_model):
        for team in standings_on_date_model.teams:
            assert team.team is not None

    def test_all_teams_have_team_href(self, standings_on_date_model):
        for team in standings_on_date_model.teams:
            assert team.team_href is not None
            assert team.team_href.startswith("/teams/")

    def test_playoff_marker_count(self, standings_on_date_model):
        """12 teams have playoff markers."""
        markers = [t for t in standings_on_date_model.teams if t.playoff_marker]
        assert len(markers) == 12

    def test_division_winner_marker(self, standings_on_date_model):
        """Patriots are a division winner (*)."""
        pats = next(
            t for t in standings_on_date_model.teams if t.team == "New England Patriots"
        )
        assert pats.playoff_marker == "*"

    def test_wild_card_marker(self, standings_on_date_model):
        """Wild card teams have + marker."""
        wc = [t for t in standings_on_date_model.teams if t.playoff_marker == "+"]
        assert len(wc) > 0

    def test_zero_ties(self, standings_on_date_model):
        """All teams have 0 ties in this fixture."""
        for team in standings_on_date_model.teams:
            assert team.ties == 0

    def test_negative_points_diff(self, standings_on_date_model):
        """Cleveland has negative point differential."""
        cle = next(
            t for t in standings_on_date_model.teams if t.team == "Cleveland Browns"
        )
        assert cle.points_diff < 0
        assert cle.wins == 0


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateParserErrors:
    def test_raises_on_missing_tables(self):
        with pytest.raises(ParsingError, match="Could not find AFC or NFC"):
            _standings_on_date_parser.parse("<html><body>No tables</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateEndpointConfig:
    def test_config_with_date(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_standings_on_date_config(
            year=2016, month=10, day=10
        )
        assert config.operation_id == "getStandingsOnDate"
        assert config.path_template == "/boxscores/standings.cgi"
        assert config.wait_for_element == "#AFC"
        assert config.query_params == {
            "month": "10",
            "day": "10",
            "year": "2016",
        }

    def test_config_with_week(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_standings_on_date_config(year=2024, week=5)
        assert config.query_params == {"week": "5", "year": "2024"}

    def test_config_raises_without_params(self):
        pfr = GriddyPFR()
        with pytest.raises(ValueError, match="Provide either"):
            pfr.frivolities._get_standings_on_date_config(year=2024)

    def test_endpoint_via_mock(self, standings_on_date_html):
        pfr = GriddyPFR()
        with patch.object(
            pfr.frivolities.browserless,
            "get_page_content",
            return_value=standings_on_date_html,
        ):
            result = pfr.frivolities.get_standings_on_date(year=2016, month=10, day=10)
        assert isinstance(result, StandingsOnDate)
        assert result.title == "NFL Standings As Of October 10, 2016"
        assert len(result.teams) == 32
