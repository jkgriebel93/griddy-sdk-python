"""Tests for Standings on Date endpoint."""

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.models import StandingsOnDate, StandingsTeamEntry
from griddy.pfr.sdk import GriddyPFR

from .conftest import FIXTURE_DIR, assert_endpoint_via_mock, assert_smoke
from .conftest import standings_on_date_parser as _parser

# -------------------------------------------------------------------------
# Fixtures
# -------------------------------------------------------------------------


@pytest.fixture(scope="module")
def standings_on_date_html() -> str:
    return (FIXTURE_DIR / "standings_on_date.html").read_text()


@pytest.fixture(scope="module")
def standings_on_date_parsed(standings_on_date_html: str) -> dict:
    return _parser.parse(standings_on_date_html)


@pytest.fixture(scope="module")
def standings_on_date_model(standings_on_date_parsed: dict) -> StandingsOnDate:
    return StandingsOnDate.model_validate(standings_on_date_parsed)


# =========================================================================
# Smoke tests
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateSmoke:
    def test_parse_returns_dict(self, standings_on_date_parsed):
        assert isinstance(standings_on_date_parsed, dict)

    def test_has_required_keys(self, standings_on_date_parsed):
        assert_smoke(standings_on_date_parsed, ["title", "teams"])

    def test_model_validates(self, standings_on_date_model):
        assert isinstance(standings_on_date_model, StandingsOnDate)


# =========================================================================
# Title and metadata
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateMetadata:
    def test_title(self, standings_on_date_model):
        assert standings_on_date_model.title == "NFL Standings As Of October 10, 2016"


# =========================================================================
# Team entries
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateEntries:
    def test_team_count(self, standings_on_date_model):
        assert len(standings_on_date_model.teams) == 32

    def test_all_are_standings_team_entry(self, standings_on_date_model):
        for team in standings_on_date_model.teams:
            assert isinstance(team, StandingsTeamEntry)

    def test_first_team(self, standings_on_date_model):
        """First team is New England Patriots (AFC East)."""
        first = standings_on_date_model.teams[0]
        assert first.conference == "AFC"
        assert first.division == "AFC East"
        assert first.team == "New England Patriots"
        assert first.team_href == "/teams/nwe/2016.htm"
        assert first.playoff_marker == "*"
        assert first.wins == 4
        assert first.losses == 1
        assert first.ties == 0
        assert first.win_loss_perc == pytest.approx(0.8)
        assert first.points_for == 114
        assert first.points_against == 74
        assert first.points_diff == 40
        assert first.margin_of_victory == pytest.approx(8.0)

    def test_last_team(self, standings_on_date_model):
        """Last team is San Francisco 49ers (NFC West)."""
        last = standings_on_date_model.teams[-1]
        assert last.conference == "NFC"
        assert last.division == "NFC West"
        assert last.team == "San Francisco 49ers"
        assert last.team_href == "/teams/sfo/2016.htm"
        assert last.playoff_marker is None
        assert last.wins == 1
        assert last.losses == 4
        assert last.points_diff == -29
        assert last.margin_of_victory == pytest.approx(-5.8)

    def test_conferences(self, standings_on_date_model):
        conferences = {t.conference for t in standings_on_date_model.teams}
        assert conferences == {"AFC", "NFC"}

    def test_afc_team_count(self, standings_on_date_model):
        afc = [t for t in standings_on_date_model.teams if t.conference == "AFC"]
        assert len(afc) == 16

    def test_nfc_team_count(self, standings_on_date_model):
        nfc = [t for t in standings_on_date_model.teams if t.conference == "NFC"]
        assert len(nfc) == 16

    def test_divisions(self, standings_on_date_model):
        divisions = {t.division for t in standings_on_date_model.teams}
        assert len(divisions) == 8
        assert "AFC East" in divisions
        assert "NFC West" in divisions

    def test_all_teams_have_team_name(self, standings_on_date_model):
        for team in standings_on_date_model.teams:
            assert team.team is not None

    def test_all_teams_have_team_href(self, standings_on_date_model):
        for team in standings_on_date_model.teams:
            assert team.team_href is not None
            assert team.team_href.startswith("/teams/")

    def test_playoff_marker_count(self, standings_on_date_model):
        """12 teams have playoff markers."""
        markers = [t for t in standings_on_date_model.teams if t.playoff_marker]
        assert len(markers) == 12

    def test_division_winner_marker(self, standings_on_date_model):
        """Patriots are a division winner (*)."""
        pats = next(
            t for t in standings_on_date_model.teams if t.team == "New England Patriots"
        )
        assert pats.playoff_marker == "*"

    def test_wild_card_marker(self, standings_on_date_model):
        """Wild card teams have + marker."""
        wc = [t for t in standings_on_date_model.teams if t.playoff_marker == "+"]
        assert len(wc) > 0

    def test_zero_ties(self, standings_on_date_model):
        """All teams have 0 ties in this fixture."""
        for team in standings_on_date_model.teams:
            assert team.ties == 0

    def test_negative_points_diff(self, standings_on_date_model):
        """Cleveland has negative point differential."""
        cle = next(
            t for t in standings_on_date_model.teams if t.team == "Cleveland Browns"
        )
        assert cle.points_diff < 0
        assert cle.wins == 0


# =========================================================================
# Parser error handling
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateParserErrors:
    def test_raises_on_missing_tables(self):
        with pytest.raises(ParsingError, match="Could not find AFC or NFC"):
            _parser.parse("<html><body>No tables</body></html>")


# =========================================================================
# Endpoint config
# =========================================================================


@pytest.mark.unit
class TestStandingsOnDateEndpointConfig:
    def test_config_with_date(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_standings_on_date_config(
            year=2016, month=10, day=10
        )
        assert config.operation_id == "getStandingsOnDate"
        assert config.path_template == "/boxscores/standings.cgi"
        assert config.wait_for_element == "#AFC"
        assert config.query_params == {
            "month": "10",
            "day": "10",
            "year": "2016",
        }

    def test_config_with_week(self):
        pfr = GriddyPFR()
        config = pfr.frivolities._get_standings_on_date_config(year=2024, week=5)
        assert config.query_params == {"week": "5", "year": "2024"}

    def test_config_raises_without_params(self):
        pfr = GriddyPFR()
        with pytest.raises(ValueError, match="Provide either"):
            pfr.frivolities._get_standings_on_date_config(year=2024)

    def test_endpoint_via_mock(self, standings_on_date_html):
        result = assert_endpoint_via_mock(
            html=standings_on_date_html,
            method_name="get_standings_on_date",
            model_class=StandingsOnDate,
            method_kwargs={"year": 2016, "month": 10, "day": 10},
        )
        assert isinstance(result, StandingsOnDate)
        assert result.title == "NFL Standings As Of October 10, 2016"
        assert len(result.teams) == 32
