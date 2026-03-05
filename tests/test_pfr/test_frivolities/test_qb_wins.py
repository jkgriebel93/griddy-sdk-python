"""Tests for QB Wins vs. Franchises endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import QBWinEntry, QBWins
from griddy.pfr.sdk import GriddyPFR

from .conftest import (
    FIXTURE_DIR,
    assert_endpoint_via_mock,
    assert_smoke,
)
from .conftest import qb_wins_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def qb_wins_html() -> str:
    return (FIXTURE_DIR / "qb_wins.html").read_text()


@pytest.fixture(scope="module")
def qb_wins_parsed(qb_wins_html: str) -> dict:
    return _parser.parse(qb_wins_html)


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
        assert_smoke(qb_wins_parsed, ["title", "entries"])

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
            _parser.parse("<html><body>No tables here</body></html>")


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
        result = assert_endpoint_via_mock(
            qb_wins_html,
            "get_qb_wins_vs_franchises",
            QBWins,
        )
        assert result.title == "Quarterback Wins"
        assert len(result.entries) == 100
        assert result.entries[0].player == "Brett Favre"
