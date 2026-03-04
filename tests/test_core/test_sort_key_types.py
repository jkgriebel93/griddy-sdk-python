"""Verify that all stats endpoint sort_key parameters use proper Literal types.

Guards against two regressions:
1. Using bare ``Optional[str]`` instead of a typed Literal from ``models``
2. Weekly config methods using a Season-variant sort key type
"""

import annotationlib

import pytest

from griddy.nfl.endpoints.pro.stats.defense import PlayerDefenseStats
from griddy.nfl.endpoints.pro.stats.fantasy import Fantasy
from griddy.nfl.endpoints.pro.stats.passing import PlayerPassingStats
from griddy.nfl.endpoints.pro.stats.receiving import PlayerReceivingStats
from griddy.nfl.endpoints.pro.stats.rushing import PlayerRushingStats
from griddy.nfl.endpoints.pro.stats.team_defense import TeamDefenseStats
from griddy.nfl.endpoints.pro.stats.team_offense import TeamOffenseStats

ALL_STATS_CLASSES = [
    PlayerPassingStats,
    PlayerRushingStats,
    PlayerReceivingStats,
    PlayerDefenseStats,
    Fantasy,
    TeamDefenseStats,
    TeamOffenseStats,
]


def _get_sort_key_annotation_str(cls, method_name):
    """Return the string-form annotation for the sort_key parameter."""
    method = getattr(cls, method_name)
    annotations = annotationlib.get_annotations(
        method, format=annotationlib.Format.STRING
    )
    return annotations.get("sort_key")


def _collect_config_methods():
    """Yield (cls, method_name) for all _get_*_config methods across stats classes."""
    for cls in ALL_STATS_CLASSES:
        for name in sorted(dir(cls)):
            if name.startswith("_get_") and name.endswith("_config"):
                yield cls, name


_ALL_METHODS = list(_collect_config_methods())
_ALL_IDS = [f"{c.__name__}.{m}" for c, m in _ALL_METHODS]

_WEEKLY_METHODS = [(c, m) for c, m in _ALL_METHODS if "weekly" in m or "by_week" in m]
_WEEKLY_IDS = [f"{c.__name__}.{m}" for c, m in _WEEKLY_METHODS]


@pytest.mark.unit
class TestSortKeyTypesAreNotBareStr:
    """No sort_key parameter should use bare ``Optional[str]``."""

    @pytest.mark.parametrize("cls,method_name", _ALL_METHODS, ids=_ALL_IDS)
    def test_sort_key_is_not_bare_str(self, cls, method_name):
        ann = _get_sort_key_annotation_str(cls, method_name)
        if ann is None:
            pytest.skip(f"{cls.__name__}.{method_name} has no sort_key param")
        assert "Optional[str]" not in ann, (
            f"{cls.__name__}.{method_name} uses Optional[str] for sort_key; "
            f"should use a typed Literal from models"
        )


@pytest.mark.unit
class TestWeeklyMethodsUseWeekSortKeyTypes:
    """Weekly config methods should reference Week-variant sort key types."""

    @pytest.mark.parametrize("cls,method_name", _WEEKLY_METHODS, ids=_WEEKLY_IDS)
    def test_weekly_sort_key_uses_week_variant(self, cls, method_name):
        ann = _get_sort_key_annotation_str(cls, method_name)
        if ann is None:
            pytest.skip(f"{cls.__name__}.{method_name} has no sort_key param")
        assert "BySeason" not in ann, (
            f"{cls.__name__}.{method_name} uses Season-variant sort key type "
            f"in annotation '{ann}'; should use the Week variant"
        )
