"""Shared fixtures and helpers for PFR Frivolities tests."""

from __future__ import annotations

from typing import Any
from unittest.mock import patch

import pytest

from griddy.pfr.errors import ParsingError
from griddy.pfr.parsers.birthdays import BirthdaysParser
from griddy.pfr.parsers.birthplaces import BirthplacesParser
from griddy.pfr.parsers.cups_of_coffee import CupsOfCoffeeParser
from griddy.pfr.parsers.last_undefeated import LastUndefeatedParser
from griddy.pfr.parsers.multi_sport_players import MultiSportPlayersParser
from griddy.pfr.parsers.multi_team_players import MultiTeamPlayersParser
from griddy.pfr.parsers.non_qb_passers import NonQBPassersParser
from griddy.pfr.parsers.non_skill_pos_td import NonSkillPosTdParser
from griddy.pfr.parsers.octopus_tracker import OctopusTrackerParser
from griddy.pfr.parsers.overtime_ties import OvertimeTiesParser
from griddy.pfr.parsers.players_born_before import PlayersBornBeforeParser
from griddy.pfr.parsers.pronunciation_guide import PronunciationGuideParser
from griddy.pfr.parsers.qb_wins import QBWinsParser
from griddy.pfr.parsers.standings_on_date import StandingsOnDateParser
from griddy.pfr.parsers.statistical_milestones import StatisticalMilestonesParser
from griddy.pfr.parsers.uniform_numbers import UniformNumbersParser
from griddy.pfr.parsers.upcoming_milestones import UpcomingMilestonesParser
from griddy.pfr.sdk import GriddyPFR
from griddy.settings import FIXTURE_DIR as _FIXTURE_DIR

FIXTURE_DIR = _FIXTURE_DIR / "pfr" / "frivolities"

# ---------------------------------------------------------------------------
# Shared parser singletons
# ---------------------------------------------------------------------------
multi_team_players_parser = MultiTeamPlayersParser()
statistical_milestones_parser = StatisticalMilestonesParser()
upcoming_milestones_parser = UpcomingMilestonesParser()
birthdays_parser = BirthdaysParser()
birthplaces_parser = BirthplacesParser()
born_before_parser = PlayersBornBeforeParser()
uniform_numbers_parser = UniformNumbersParser()
qb_wins_parser = QBWinsParser()
non_qb_passers_parser = NonQBPassersParser()
non_skill_pos_td_parser = NonSkillPosTdParser()
octopus_tracker_parser = OctopusTrackerParser()
cups_of_coffee_parser = CupsOfCoffeeParser()
multi_sport_players_parser = MultiSportPlayersParser()
pronunciation_guide_parser = PronunciationGuideParser()
overtime_ties_parser = OvertimeTiesParser()
last_undefeated_parser = LastUndefeatedParser()
standings_on_date_parser = StandingsOnDateParser()


# ---------------------------------------------------------------------------
# Shared assertion helpers
# ---------------------------------------------------------------------------


def assert_smoke(parsed: dict, required_keys: list[str]) -> None:
    """Common smoke-test assertions for parsed dicts."""
    assert isinstance(parsed, dict)
    for key in required_keys:
        assert key in parsed, f"Missing required key: {key}"


def assert_parser_error(parser: Any, html: str, match: str) -> None:
    """Assert that a parser raises ``ParsingError`` with *match*."""
    with pytest.raises(ParsingError, match=match):
        parser.parse(html)


def assert_endpoint_via_mock(
    html: str,
    method_name: str,
    model_class: type,
    method_kwargs: dict | None = None,
) -> Any:
    """Invoke *method_name* on a fresh ``GriddyPFR().frivolities`` with mocked HTML."""
    pfr = GriddyPFR()
    with patch.object(
        pfr.frivolities.browserless,
        "get_page_content",
        return_value=html,
    ):
        method = getattr(pfr.frivolities, method_name)
        result = method(**(method_kwargs or {}))
    assert isinstance(result, model_class)
    return result
