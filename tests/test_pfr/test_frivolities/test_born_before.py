"""Tests for Players Born Before endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import PlayerBornBefore, PlayersBornBefore
from griddy.pfr.parsers.players_born_before import PlayersBornBeforeParser
from griddy.pfr.sdk import GriddyPFR

from .conftest import FIXTURE_DIR, assert_endpoint_via_mock, assert_smoke
from .conftest import born_before_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def born_before_html() -> str:
    return (FIXTURE_DIR / "players_born_before.html").read_text()


@pytest.fixture(scope="module")
def born_before_parsed(born_before_html: str) -> dict:
    return _parser.parse(born_before_html)


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
        assert_smoke(
            born_before_parsed,
            ["title", "month", "day", "year", "players"],
        )

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
            _parser.parse("<html><body>No tables here</body></html>")


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
        result = assert_endpoint_via_mock(
            born_before_html,
            "get_players_born_before",
            PlayersBornBefore,
            method_kwargs={"month": 8, "day": 5, "year": 1993},
        )
        assert isinstance(result, PlayersBornBefore)
        assert result.month == 8
        assert result.day == 5
        assert result.year == 1993
        assert len(result.players) == 150
