"""Tests for Overtime Ties endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import OvertimeTieEntry, OvertimeTies
from griddy.pfr.sdk import GriddyPFR

from .conftest import FIXTURE_DIR, assert_endpoint_via_mock, assert_smoke
from .conftest import overtime_ties_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def overtime_ties_html() -> str:
    return (FIXTURE_DIR / "overtime_ties.html").read_text()


@pytest.fixture(scope="module")
def overtime_ties_parsed(overtime_ties_html: str) -> dict:
    return _parser.parse(overtime_ties_html)


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
        assert_smoke(overtime_ties_parsed, ["title", "entries"])

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
            _parser.parse("<html><body>No tables</body></html>")


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
        result = assert_endpoint_via_mock(
            overtime_ties_html,
            "get_overtime_ties",
            OvertimeTies,
        )
        assert isinstance(result, OvertimeTies)
        assert result.title == "Overtime Ties"
        assert len(result.entries) == 30
        assert result.entries[0].year == 2025
