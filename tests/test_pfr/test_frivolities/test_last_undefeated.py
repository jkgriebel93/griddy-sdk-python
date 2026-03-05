"""Tests for Last Undefeated Team endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import LastUndefeated, LastUndefeatedEntry
from griddy.pfr.sdk import GriddyPFR

from .conftest import (
    FIXTURE_DIR,
    assert_endpoint_via_mock,
    assert_smoke,
)
from .conftest import last_undefeated_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def last_undefeated_html() -> str:
    return (FIXTURE_DIR / "last_undefeated.html").read_text()


@pytest.fixture(scope="module")
def last_undefeated_parsed(last_undefeated_html: str) -> dict:
    return _parser.parse(last_undefeated_html)


@pytest.fixture(scope="module")
def last_undefeated_model(last_undefeated_parsed: dict) -> LastUndefeated:
    return LastUndefeated.model_validate(last_undefeated_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestLastUndefeatedSmoke:
    def test_parse_returns_dict(self, last_undefeated_parsed):
        assert isinstance(last_undefeated_parsed, dict)

    def test_has_required_keys(self, last_undefeated_parsed):
        assert_smoke(last_undefeated_parsed, ["title", "entries"])

    def test_model_validates(self, last_undefeated_model):
        assert isinstance(last_undefeated_model, LastUndefeated)


# =========================================================================
# Title and metadata
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
            _parser.parse("<html><body>No tables</body></html>")


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
        result = assert_endpoint_via_mock(
            last_undefeated_html,
            "get_last_undefeated",
            LastUndefeated,
        )
        assert result.title == "Last Undefeated Team"
        assert len(result.entries) == 149
        assert result.entries[0].year == 2025
