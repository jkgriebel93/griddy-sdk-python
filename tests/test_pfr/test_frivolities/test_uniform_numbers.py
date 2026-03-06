"""Tests for Uniform Numbers endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import UniformNumberPlayer, UniformNumbers
from griddy.pfr.parsers.uniform_numbers import UniformNumbersParser
from griddy.pfr.sdk import GriddyPFR

from .conftest import FIXTURE_DIR, assert_endpoint_via_mock, assert_smoke
from .conftest import uniform_numbers_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def uniform_numbers_html() -> str:
    return (FIXTURE_DIR / "uniform_numbers.html").read_text()


@pytest.fixture(scope="module")
def uniform_numbers_parsed(uniform_numbers_html: str) -> dict:
    return _parser.parse(uniform_numbers_html)


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
        assert_smoke(uniform_numbers_parsed, ["title", "number", "team", "players"])

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
            _parser.parse("<html><body>No tables here</body></html>")


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
        result = assert_endpoint_via_mock(
            uniform_numbers_html,
            "get_uniform_numbers",
            UniformNumbers,
            method_kwargs={"number": 6, "team": "pit"},
        )
        assert result.number == 6
        assert result.team == "Pittsburgh Steelers"
        assert len(result.players) == 8
