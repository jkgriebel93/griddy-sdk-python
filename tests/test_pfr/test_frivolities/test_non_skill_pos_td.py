"""Tests for Non-Skill Position TD Scorers endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import NonSkillPosTdEntry, NonSkillPosTdScorers
from griddy.pfr.sdk import GriddyPFR

from .conftest import FIXTURE_DIR, assert_endpoint_via_mock, assert_smoke
from .conftest import non_skill_pos_td_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def non_skill_pos_td_html() -> str:
    return (FIXTURE_DIR / "non_skill_pos_td.html").read_text()


@pytest.fixture(scope="module")
def non_skill_pos_td_parsed(non_skill_pos_td_html: str) -> dict:
    return _parser.parse(non_skill_pos_td_html)


@pytest.fixture(scope="module")
def non_skill_pos_td_model(non_skill_pos_td_parsed: dict) -> NonSkillPosTdScorers:
    return NonSkillPosTdScorers.model_validate(non_skill_pos_td_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdSmoke:
    def test_parse_returns_dict(self, non_skill_pos_td_parsed):
        assert isinstance(non_skill_pos_td_parsed, dict)

    def test_has_required_keys(self, non_skill_pos_td_parsed):
        assert_smoke(non_skill_pos_td_parsed, ["title", "entries"])

    def test_model_validates(self, non_skill_pos_td_model):
        assert isinstance(non_skill_pos_td_model, NonSkillPosTdScorers)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdMetadata:
    def test_title(self, non_skill_pos_td_model):
        assert non_skill_pos_td_model.title == "Non-Skill Position TD Scorers"


# =========================================================================
# Entries table
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdEntries:
    def test_entry_count(self, non_skill_pos_td_model):
        assert len(non_skill_pos_td_model.entries) == 215

    def test_entry_types(self, non_skill_pos_td_model):
        for entry in non_skill_pos_td_model.entries:
            assert isinstance(entry, NonSkillPosTdEntry)

    def test_first_entry_home_game(self, non_skill_pos_td_model):
        """Frank Crum — OT, DEN home game, receiving TD."""
        first = non_skill_pos_td_model.entries[0]
        assert first.player == "Frank Crum"
        assert first.player_href == "/players/C/CrumFr00.htm"
        assert first.player_id == "CrumFr00"
        assert first.pos == "OT"
        assert first.week_num == 20
        assert first.game_day_of_week == "Sat"
        assert first.game_date == "Jan 17, 2026"
        assert first.boxscore_href == "/boxscores/202601170den.htm"
        assert first.game_outcome == "W"
        assert first.team == "DEN"
        assert first.team_href == "/teams/den/2025.htm"
        assert first.game_location is None
        assert first.opp == "BUF"
        assert first.opp_href == "/teams/buf/2025.htm"
        assert first.pts_off == 33
        assert first.pts_def == 30
        assert first.rush_att == 0
        assert first.rush_yds == 0
        assert first.rush_long == 0
        assert first.rush_yds_per_att is None
        assert first.rush_td == 0
        assert first.rec == 1
        assert first.rec_yds == 7
        assert first.rec_long == 7
        assert first.rec_yds_per_rec == 7.0
        assert first.rec_td == 1

    def test_entry_away_game(self, non_skill_pos_td_model):
        """Jeffery Simmons — DT, TEN away at SFO, receiving TD."""
        simmons = non_skill_pos_td_model.entries[1]
        assert simmons.player == "Jeffery Simmons"
        assert simmons.pos == "DT"
        assert simmons.game_location == "@"
        assert simmons.team == "TEN*"
        assert simmons.opp == "SFO"
        assert simmons.game_outcome == "L"
        assert simmons.pts_off == 24
        assert simmons.pts_def == 37
        assert simmons.rec_td == 1

    def test_entry_with_rushing_td(self, non_skill_pos_td_model):
        """Akiem Hicks — DE, scored via rushing TD (not receiving)."""
        hicks = next(
            e for e in non_skill_pos_td_model.entries if e.player == "Akiem Hicks"
        )
        assert hicks.pos == "DE"
        assert hicks.rush_att == 1
        assert hicks.rush_yds == 1
        assert hicks.rush_long == 1
        assert hicks.rush_yds_per_att == 1.0
        assert hicks.rush_td == 1
        assert hicks.rec == 0
        assert hicks.rec_td == 0

    def test_last_entry_old_era(self, non_skill_pos_td_model):
        """Bob Gonya — T, 1934, oldest entry, some stats empty."""
        last = non_skill_pos_td_model.entries[-1]
        assert last.player == "Bob Gonya"
        assert last.player_id == "GonyBo20"
        assert last.pos == "T"
        assert last.game_date == "Oct 7, 1934"
        assert last.team == "PHI"
        assert last.opp == "PIT"
        assert last.rush_long is None
        assert last.rush_yds_per_att is None
        assert last.rec_yds == 4
        assert last.rec_td == 1


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdParserErrors:
    def test_raises_on_missing_table(self):
        with pytest.raises(ParsingError, match="Could not find odd_scorers table"):
            _parser.parse("<html><body>No tables here</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestNonSkillPosTdEndpointConfig:
    def test_config(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_non_skill_pos_td_scorers_config()
        assert config.operation_id == "getNonSkillPosTdScorers"
        assert config.path_template == "/friv/odd_td.htm"
        assert config.wait_for_element == "#odd_scorers"

    def test_endpoint_via_mock(self, non_skill_pos_td_html):
        result = assert_endpoint_via_mock(
            non_skill_pos_td_html,
            "get_non_skill_pos_td_scorers",
            NonSkillPosTdScorers,
        )
        assert result.title == "Non-Skill Position TD Scorers"
        assert len(result.entries) == 215
        assert result.entries[0].player == "Frank Crum"
