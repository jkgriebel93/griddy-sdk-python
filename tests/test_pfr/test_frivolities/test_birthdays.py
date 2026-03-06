"""Tests for Birthdays endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import BirthdayPlayer, Birthdays
from griddy.pfr.parsers.birthdays import BirthdaysParser
from griddy.pfr.sdk import GriddyPFR

from .conftest import FIXTURE_DIR, assert_endpoint_via_mock, assert_smoke
from .conftest import birthdays_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def birthdays_html() -> str:
    return (FIXTURE_DIR / "birthdays.html").read_text()


@pytest.fixture(scope="module")
def birthdays_parsed(birthdays_html: str) -> dict:
    return _parser.parse(birthdays_html)


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
        assert_smoke(birthdays_parsed, ["title", "month", "day", "players"])

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
            _parser.parse("<html><body>No tables here</body></html>")


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
        result = assert_endpoint_via_mock(
            birthdays_html,
            "get_birthdays",
            Birthdays,
            method_kwargs={"month": 3, "day": 2},
        )
        assert result.month == 3
        assert result.day == 2
        assert len(result.players) == 90
