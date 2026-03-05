"""Tests for Octopus Tracker endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import OctopusEntry, OctopusTracker
from griddy.pfr.sdk import GriddyPFR

from .conftest import (
    FIXTURE_DIR,
    assert_endpoint_via_mock,
    assert_smoke,
)
from .conftest import octopus_tracker_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def octopus_tracker_html() -> str:
    return (FIXTURE_DIR / "octopus_tracker.html").read_text()


@pytest.fixture(scope="module")
def octopus_tracker_parsed(octopus_tracker_html: str) -> dict:
    return _parser.parse(octopus_tracker_html)


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
        assert_smoke(octopus_tracker_parsed, ["title", "entries"])

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
            _parser.parse("<html><body>No tables here</body></html>")


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
        result = assert_endpoint_via_mock(
            octopus_tracker_html,
            "get_octopus_tracker",
            OctopusTracker,
        )
        assert result.title == "Octopus Touchdown and Two Point Conversion Scorers"
        assert len(result.entries) == 200
        assert result.entries[0].player == "Chris Godwin"
