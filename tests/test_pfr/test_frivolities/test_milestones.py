"""Tests for Statistical Milestones and Upcoming Milestones endpoints."""

import pytest

from griddy.pfr.basesdk import BaseSDK as PfrBaseSDK
from griddy.pfr.errors import ParsingError
from griddy.pfr.models import (
    CareerLeader,
    MilestoneEntry,
    StatisticalMilestones,
    UpcomingLeaderboardEntry,
    UpcomingMilestoneEntry,
    UpcomingMilestones,
)
from griddy.pfr.sdk import GriddyPFR

from .conftest import (
    FIXTURE_DIR,
    assert_endpoint_via_mock,
    assert_smoke,
)
from .conftest import statistical_milestones_parser as _milestones_parser
from .conftest import upcoming_milestones_parser as _upcoming_parser

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
    preprocessed = PfrBaseSDK._preprocess_html(milestones_html)
    return _milestones_parser.parse(preprocessed)


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
        assert_smoke(
            milestones_parsed, ["title", "stat", "milestones", "career_leaders"]
        )

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
        result = assert_endpoint_via_mock(
            milestones_html,
            "get_statistical_milestones",
            StatisticalMilestones,
            method_kwargs={"stat": "pass_td"},
        )
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
        assert_smoke(
            upcoming_parsed, ["title", "description", "milestones", "leaderboards"]
        )

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
        result = assert_endpoint_via_mock(
            upcoming_html,
            "get_upcoming_milestones",
            UpcomingMilestones,
        )
        assert len(result.milestones) == 17
        assert len(result.leaderboards) == 43
