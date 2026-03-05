"""Tests for Birthplaces endpoints (landing and filtered)."""

from unittest.mock import patch

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import (
    BirthplaceFiltered,
    BirthplaceLanding,
    BirthplaceLocation,
    BirthplacePlayer,
)
from griddy.pfr.parsers.birthplaces import BirthplacesParser
from griddy.pfr.sdk import GriddyPFR

from .conftest import (
    FIXTURE_DIR,
    assert_endpoint_via_mock,
    assert_smoke,
)
from .conftest import birthplaces_parser as _parser

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
    return _parser.parse_landing(birthplaces_landing_html)


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
        assert_smoke(birthplaces_landing_parsed, ["title", "locations"])

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
            _parser.parse_landing("<html><body>No tables here</body></html>")


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
        result = assert_endpoint_via_mock(
            html=birthplaces_landing_html,
            method_name="get_birthplaces",
            model_class=BirthplaceLanding,
        )
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
    return _parser.parse_filtered(birthplaces_filtered_html)


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
        assert_smoke(
            birthplaces_filtered_parsed, ["title", "country", "state", "players"]
        )

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
            _parser.parse_filtered("<html><body>No tables here</body></html>")


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
        result = assert_endpoint_via_mock(
            html=birthplaces_filtered_html,
            method_name="get_birthplace_players",
            model_class=BirthplaceFiltered,
            method_kwargs={"country": "USA", "state": "PA"},
        )
        assert result.country == "USA"
        assert result.state == "Pennsylvania"
        assert len(result.players) == 200
