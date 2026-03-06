"""Tests verifying docstrings and type annotations for the nfl/endpoints/pro module (TGF-161)."""

import inspect

import pytest

from griddy.nfl.endpoints.pro import ProSDK
from griddy.nfl.endpoints.pro.content import Content
from griddy.nfl.endpoints.pro.games import ProGames
from griddy.nfl.endpoints.pro.players import Players
from griddy.nfl.endpoints.pro.stats import StatsSDK
from griddy.nfl.endpoints.pro.stats.base import PlayerStatsBase
from griddy.nfl.endpoints.pro.stats.defense import PlayerDefenseStats
from griddy.nfl.endpoints.pro.stats.passing import PlayerPassingStats
from griddy.nfl.endpoints.pro.stats.receiving import PlayerReceivingStats
from griddy.nfl.endpoints.pro.stats.rushing import PlayerRushingStats
from griddy.nfl.endpoints.pro.stats.team_defense import TeamDefenseStats
from griddy.nfl.endpoints.pro.teams import Teams
from griddy.nfl.endpoints.pro.transactions import Transactions

_ITEMS_NEEDING_DOCSTRINGS = [
    # pro/__init__.py
    (ProSDK, "ProSDK"),
    (ProSDK.__init__, "ProSDK.__init__"),
    # pro/content.py
    (Content, "Content"),
    # pro/games.py
    (ProGames, "ProGames"),
    # pro/players.py
    (Players, "Players"),
    # pro/stats/__init__.py
    (StatsSDK.__init__, "StatsSDK.__init__"),
    # pro/stats/defense.py
    (PlayerDefenseStats, "PlayerDefenseStats"),
    # pro/stats/passing.py
    (PlayerPassingStats, "PlayerPassingStats"),
    # pro/stats/receiving.py
    (PlayerReceivingStats, "PlayerReceivingStats"),
    # pro/stats/rushing.py
    (PlayerRushingStats, "PlayerRushingStats"),
    # pro/stats/team_defense.py
    (TeamDefenseStats, "TeamDefenseStats"),
    # pro/teams.py
    (Teams, "Teams"),
    # pro/transactions.py
    (Transactions, "Transactions"),
]


@pytest.mark.unit
class TestDocstringsExist:
    @pytest.mark.parametrize(
        "obj,name",
        [pytest.param(obj, name, id=name) for obj, name in _ITEMS_NEEDING_DOCSTRINGS],
    )
    def test_has_docstring(self, obj, name):
        assert obj.__doc__ is not None, f"{name} is missing a docstring"
        assert len(obj.__doc__.strip()) > 0, f"{name} has an empty docstring"


@pytest.mark.unit
class TestParamTypeAnnotations:
    def test_make_stats_config_kwargs_has_type(self):
        hints = inspect.get_annotations(PlayerStatsBase._make_stats_config)
        assert "kwargs" in hints, (
            "PlayerStatsBase._make_stats_config is missing type annotation for **kwargs"
        )
