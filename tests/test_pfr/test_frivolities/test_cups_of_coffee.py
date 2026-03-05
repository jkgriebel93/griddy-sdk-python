"""Tests for Cups of Coffee endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import CoffeeEntry, CupsOfCoffee
from griddy.pfr.sdk import GriddyPFR

from .conftest import (
    FIXTURE_DIR,
    assert_endpoint_via_mock,
    assert_smoke,
)
from .conftest import cups_of_coffee_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def cups_of_coffee_html() -> str:
    return (FIXTURE_DIR / "cups_of_coffee.html").read_text()


@pytest.fixture(scope="module")
def cups_of_coffee_parsed(cups_of_coffee_html: str) -> dict:
    return _parser.parse(cups_of_coffee_html)


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
        assert_smoke(cups_of_coffee_parsed, ["title", "entries"])

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
            _parser.parse("<html><body>No tables here</body></html>")


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
        result = assert_endpoint_via_mock(
            cups_of_coffee_html,
            "get_cups_of_coffee",
            CupsOfCoffee,
        )
        assert result.title == "Cups of Coffee"
        assert len(result.entries) == 1481
        assert result.entries[0].player == "Nate Abrams"
