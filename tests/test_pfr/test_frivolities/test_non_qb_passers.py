"""Tests for Non-Quarterback Passers endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import NonQBPasserEntry, NonQBPassers
from griddy.pfr.sdk import GriddyPFR

from .conftest import FIXTURE_DIR, assert_endpoint_via_mock, assert_smoke
from .conftest import non_qb_passers_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def non_qb_passers_html() -> str:
    return (FIXTURE_DIR / "non_qb_passers.html").read_text()


@pytest.fixture(scope="module")
def non_qb_passers_parsed(non_qb_passers_html: str) -> dict:
    return _parser.parse(non_qb_passers_html)


@pytest.fixture(scope="module")
def non_qb_passers_model(non_qb_passers_parsed: dict) -> NonQBPassers:
    return NonQBPassers.model_validate(non_qb_passers_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersSmoke:
    def test_parse_returns_dict(self, non_qb_passers_parsed):
        assert isinstance(non_qb_passers_parsed, dict)

    def test_has_required_keys(self, non_qb_passers_parsed):
        assert_smoke(non_qb_passers_parsed, ["title", "entries"])

    def test_model_validates(self, non_qb_passers_model):
        assert isinstance(non_qb_passers_model, NonQBPassers)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersMetadata:
    def test_title(self, non_qb_passers_model):
        assert non_qb_passers_model.title == "Non-Quarterback Passing"


# =========================================================================
# Entries table
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersEntries:
    def test_entry_count(self, non_qb_passers_model):
        assert len(non_qb_passers_model.entries) == 1576

    def test_entry_types(self, non_qb_passers_model):
        for entry in non_qb_passers_model.entries:
            assert isinstance(entry, NonQBPasserEntry)

    def test_first_entry_old_era(self, non_qb_passers_model):
        """Duke Abbruzzi — 1946 HB, some modern stats are None."""
        first = non_qb_passers_model.entries[0]
        assert first.player == "Duke Abbruzzi"
        assert first.player_href == "/players/A/AbbrDu20.htm"
        assert first.player_id == "AbbrDu20"
        assert first.pos == "HB"
        assert first.year_min == 1946
        assert first.year_max == 1946
        assert first.pass_cmp == 1
        assert first.pass_att == 1
        assert first.pass_cmp_perc == 100.0
        assert first.pass_yds == 11
        assert first.pass_td == 0
        assert first.pass_long == 11
        assert first.pass_rating == 112.5
        # Old era — no QBR or sack data
        assert first.qbr is None
        assert first.pass_sacked is None
        assert first.pass_sacked_yds is None

    def test_entry_with_full_modern_stats(self, non_qb_passers_model):
        """Odell Beckham Jr. — WR with QBR, sack data, and all stats."""
        beckham = next(
            e for e in non_qb_passers_model.entries if e.player == "Odell Beckham Jr."
        )
        assert beckham.pos == "WR"
        assert beckham.year_min == 2014
        assert beckham.year_max == 2024
        assert beckham.pass_cmp == 4
        assert beckham.pass_att == 6
        assert beckham.pass_cmp_perc == 66.7
        assert beckham.pass_yds == 144
        assert beckham.pass_td == 2
        assert beckham.pass_td_perc == 33.3
        assert beckham.pass_int == 0
        assert beckham.pass_long == 57
        assert beckham.pass_yds_per_att == 24.0
        assert beckham.pass_adj_yds_per_att == 30.7
        assert beckham.pass_yds_per_cmp == 36.0
        assert beckham.pass_rating == 149.3
        assert beckham.qbr == 1.3
        assert beckham.pass_sacked == 1
        assert beckham.pass_sacked_yds == 6
        assert beckham.pass_sacked_perc == 14.3
        assert beckham.pass_net_yds_per_att == 19.71
        assert beckham.pass_adj_net_yds_per_att == 25.43

    def test_last_entry(self, non_qb_passers_model):
        last = non_qb_passers_model.entries[-1]
        assert last.player == "Brandon Zylstra"
        assert last.player_id == "ZylsBr00"
        assert last.pos == "WR"
        assert last.pass_att == 1
        assert last.pass_cmp == 0
        assert last.pass_yds == 0


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ParsingError, match="Could not find nonqb_passers table"):
            _parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestNonQBPassersEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_non_qb_passers_config()
        assert config.operation_id == "getNonQBPassers"
        assert config.path_template == "/friv/nonqb.htm"
        assert config.wait_for_element == "#nonqb_passers"

    def test_endpoint_via_mock(self, non_qb_passers_html):
        result = assert_endpoint_via_mock(
            non_qb_passers_html,
            "get_non_qb_passers",
            NonQBPassers,
        )
        assert result.title == "Non-Quarterback Passing"
        assert len(result.entries) == 1576
        assert result.entries[0].player == "Duke Abbruzzi"
