"""Tests for Multi-Sport Players endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import MultiSportPlayer, MultiSportPlayers
from griddy.pfr.sdk import GriddyPFR

from .conftest import (
    FIXTURE_DIR,
    assert_endpoint_via_mock,
    assert_smoke,
)
from .conftest import multi_sport_players_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def multi_sport_players_html() -> str:
    return (FIXTURE_DIR / "multi_sport_players.html").read_text()


@pytest.fixture(scope="module")
def multi_sport_players_parsed(multi_sport_players_html: str) -> dict:
    return _parser.parse(multi_sport_players_html)


@pytest.fixture(scope="module")
def multi_sport_players_model(
    multi_sport_players_parsed: dict,
) -> MultiSportPlayers:
    return MultiSportPlayers.model_validate(multi_sport_players_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersSmoke:
    def test_parse_returns_dict(self, multi_sport_players_parsed):
        assert isinstance(multi_sport_players_parsed, dict)

    def test_has_required_keys(self, multi_sport_players_parsed):
        assert_smoke(multi_sport_players_parsed, ["title", "entries"])

    def test_model_validates(self, multi_sport_players_model):
        assert isinstance(multi_sport_players_model, MultiSportPlayers)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersMetadata:
    def test_title(self, multi_sport_players_model):
        assert multi_sport_players_model.title == "Multisport Athletes"


# =========================================================================
# Entries table
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersEntries:
    def test_entry_count(self, multi_sport_players_model):
        assert len(multi_sport_players_model.entries) == 450

    def test_entry_types(self, multi_sport_players_model):
        for entry in multi_sport_players_model.entries:
            assert isinstance(entry, MultiSportPlayer)

    def test_first_entry(self, multi_sport_players_model):
        """Mo Alie-Cox — TE, 2018–2025, college basketball."""
        first = multi_sport_players_model.entries[0]
        assert first.player == "Mo Alie-Cox"
        assert first.player_href == "/players/A/AlieMo00.htm"
        assert first.player_id == "AlieMo00"
        assert first.pos == "TE"
        assert first.year_min == 2018
        assert first.year_max == 2025
        assert first.all_pros_first_team == 0
        assert first.pro_bowls == 0
        assert first.years_as_primary_starter == 2
        assert first.career_av == 12
        assert first.g == 125
        assert first.rec == 127
        assert first.rec_yds == 1550
        assert first.rec_td == 16
        assert first.rec_long == 45
        assert len(first.other_links) == 1
        assert first.other_links[0].text == "College Basketball at Sports-Reference.com"
        assert "sports-reference.com/cbb" in first.other_links[0].href

    def test_last_entry(self, multi_sport_players_model):
        """George Magerkurth — T, 1920, pre-sack era."""
        last = multi_sport_players_model.entries[-1]
        assert last.player == "George Magerkurth"
        assert last.player_id == "MageGe20"
        assert last.pos == "T"
        assert last.year_min == 1920
        assert last.year_max == 1920
        assert last.g == 1
        assert last.pass_sacked is None
        assert last.pass_sacked_yds is None
        assert len(last.other_links) == 1

    def test_entry_with_multiple_links(self, multi_sport_players_model):
        """Drew Henson — had both Baseball-Reference and Minors links."""
        henson = next(
            e for e in multi_sport_players_model.entries if e.player == "Drew Henson"
        )
        assert len(henson.other_links) == 2
        link_texts = [link.text for link in henson.other_links]
        assert "Baseball-Reference.com" in link_texts
        assert "Minors at Baseball-Reference.com" in link_texts

    def test_entry_with_negative_rush_yds(self, multi_sport_players_model):
        """Drake London — negative rush_yds (-3)."""
        london = next(
            e for e in multi_sport_players_model.entries if e.player == "Drake London"
        )
        assert london.rush_yds == -3

    def test_entry_with_empty_sack_fields(self, multi_sport_players_model):
        """Reggie Carolan — 1962, pre-sack era, empty sack cells."""
        carolan = next(
            e for e in multi_sport_players_model.entries if e.player == "Reggie Carolan"
        )
        assert carolan.year_min == 1962
        assert carolan.pass_sacked is None
        assert carolan.pass_sacked_yds is None

    def test_tom_brady(self, multi_sport_players_model):
        """Tom Brady — QB, 2000–2022, significant passing stats."""
        brady = next(
            e for e in multi_sport_players_model.entries if e.player == "Tom Brady"
        )
        assert brady.pos == "QB"
        assert brady.year_min == 2000
        assert brady.year_max == 2022
        assert brady.all_pros_first_team == 3
        assert brady.pro_bowls == 15
        assert brady.career_av == 184
        assert brady.g == 335
        assert brady.pass_cmp == 7753
        assert brady.pass_yds == 89214
        assert brady.pass_td == 649
        assert brady.pass_sacked == 565
        assert len(brady.other_links) == 1
        assert "baseball-reference.com" in brady.other_links[0].href


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ParsingError, match="Could not find multisport table"):
            _parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestMultiSportPlayersEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_multi_sport_players_config()
        assert config.operation_id == "getMultiSportPlayers"
        assert config.path_template == "/friv/multisport.htm"
        assert config.wait_for_element == "#multisport"

    def test_endpoint_via_mock(self, multi_sport_players_html):
        result = assert_endpoint_via_mock(
            multi_sport_players_html,
            "get_multi_sport_players",
            MultiSportPlayers,
        )
        assert result.title == "Multisport Athletes"
        assert len(result.entries) == 450
        assert result.entries[0].player == "Mo Alie-Cox"
