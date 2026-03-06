"""Test that enum types extracted from TODO comments are properly defined and usable.

Covers TGF-153: Extract enum types for model fields and request constants.
"""

import typing

import pydantic
import pytest

from griddy.nfl.models.enums.combine_enums import (
    CombinePositionEnum,
    CombinePositionGroupEnum,
)
from griddy.nfl.models.enums.play_state_enum import PlayStateEnum
from griddy.nfl.models.enums.player_position_enum import PlayerPositionEnum
from griddy.nfl.models.enums.player_position_group_enum import PlayerPositionGroupEnum
from griddy.nfl.models.enums.player_status_enum import PlayerStatusEnum
from griddy.nfl.models.enums.team_defense_stats_enums import (
    TeamDefenseStatsSortKeyEnum,
    TeamDefenseStatsSplitEnum,
)


def _get_literal_values(literal_type):
    """Extract the values from a Literal type."""
    return typing.get_args(literal_type)


@pytest.mark.unit
class TestPlayerPositionEnum:
    def test_contains_common_offensive_positions(self):
        values = _get_literal_values(PlayerPositionEnum)
        for pos in ("QB", "RB", "WR", "TE", "FB"):
            assert pos in values

    def test_contains_common_defensive_positions(self):
        values = _get_literal_values(PlayerPositionEnum)
        for pos in ("CB", "DE", "DT", "ILB", "OLB", "FS", "SS"):
            assert pos in values

    def test_contains_special_teams_positions(self):
        values = _get_literal_values(PlayerPositionEnum)
        for pos in ("K", "P", "LS"):
            assert pos in values

    def test_values_are_sorted(self):
        values = list(_get_literal_values(PlayerPositionEnum))
        assert values == sorted(values)


@pytest.mark.unit
class TestPlayerPositionGroupEnum:
    def test_contains_expected_groups(self):
        values = _get_literal_values(PlayerPositionGroupEnum)
        for group in ("QB", "RB", "WR", "TE", "OL", "DL", "LB", "DB", "SPEC"):
            assert group in values

    def test_values_are_sorted(self):
        values = list(_get_literal_values(PlayerPositionGroupEnum))
        assert values == sorted(values)


@pytest.mark.unit
class TestPlayerStatusEnum:
    def test_contains_common_statuses(self):
        values = _get_literal_values(PlayerStatusEnum)
        for status in ("ACT", "RES", "CUT", "RET"):
            assert status in values

    def test_values_are_sorted(self):
        values = list(_get_literal_values(PlayerStatusEnum))
        assert values == sorted(values)


@pytest.mark.unit
class TestPlayStateEnum:
    def test_contains_expected_states(self):
        values = _get_literal_values(PlayStateEnum)
        for state in ("PRE_SNAP", "IN_PROGRESS", "POST_PLAY"):
            assert state in values


@pytest.mark.unit
class TestCombinePositionEnum:
    def test_contains_combine_specific_positions(self):
        values = _get_literal_values(CombinePositionEnum)
        for pos in ("EDGE", "IOL", "S"):
            assert pos in values

    def test_contains_common_positions(self):
        values = _get_literal_values(CombinePositionEnum)
        for pos in ("QB", "RB", "WR", "TE", "CB"):
            assert pos in values

    def test_values_are_sorted(self):
        values = list(_get_literal_values(CombinePositionEnum))
        assert values == sorted(values)


@pytest.mark.unit
class TestCombinePositionGroupEnum:
    def test_contains_expected_groups(self):
        values = _get_literal_values(CombinePositionGroupEnum)
        for group in ("QB", "RB", "WR", "TE", "OL", "DL", "LB", "DB", "SPEC"):
            assert group in values


@pytest.mark.unit
class TestTeamDefenseStatsSortKeyEnum:
    def test_contains_expected_sort_keys(self):
        values = _get_literal_values(TeamDefenseStatsSortKeyEnum)
        for key in ("ypg", "total", "epa", "interception", "totalTakeaways"):
            assert key in values

    def test_has_expected_count(self):
        values = _get_literal_values(TeamDefenseStatsSortKeyEnum)
        assert len(values) == 34


@pytest.mark.unit
class TestTeamDefenseStatsSplitEnum:
    def test_contains_expected_splits(self):
        values = _get_literal_values(TeamDefenseStatsSplitEnum)
        for split in (
            "TEAM_DEFENSE_BASE",
            "TEAM_DEFENSE_RED_ZONE",
            "TEAM_DEFENSE_MOTION",
        ):
            assert split in values

    def test_has_expected_count(self):
        values = _get_literal_values(TeamDefenseStatsSplitEnum)
        assert len(values) == 12


@pytest.mark.unit
class TestModelFieldsUseEnums:
    """Verify the model fields now reference enum types instead of plain str."""

    def test_person_position_field_type(self):
        from griddy.nfl.models.entities.person import Person

        field = Person.model_fields["position"]
        assert field.annotation is PlayerPositionEnum

    def test_person_position_group_field_uses_enum(self):
        from griddy.nfl.models.entities.person import Person

        field = Person.model_fields["position_group"]
        flat = _flatten_type_args(field.annotation)
        assert (
            PlayerPositionGroupEnum in flat
            or field.annotation is PlayerPositionGroupEnum
        )

    def test_person_status_field_type(self):
        from griddy.nfl.models.entities.person import Person

        field = Person.model_fields["status"]
        assert field.annotation is PlayerStatusEnum

    def test_pro_play_play_state_uses_enum(self):
        from griddy.nfl.models.entities.pro_play import ProPlay

        field = ProPlay.model_fields["play_state"]
        args = typing.get_args(field.annotation)
        # Optional[PlayStateEnum] -> args should contain PlayStateEnum
        flat = _flatten_type_args(field.annotation)
        assert PlayStateEnum in flat

    def test_combine_profile_position_field_type(self):
        from griddy.nfl.models.entities.combine_profile import CombineProfile

        field = CombineProfile.model_fields["position"]
        assert field.annotation is CombinePositionEnum

    def test_combine_profile_position_group_uses_enum(self):
        from griddy.nfl.models.entities.combine_profile import CombineProfile

        field = CombineProfile.model_fields["position_group"]
        flat = _flatten_type_args(field.annotation)
        assert CombinePositionGroupEnum in flat

    def test_defense_request_sort_key_uses_enum(self):
        from griddy.nfl.models.requests.get_team_defense_stats_by_week_op import (
            GetTeamDefenseStatsByWeekRequest,
        )

        field = GetTeamDefenseStatsByWeekRequest.model_fields["sort_key"]
        flat = _flatten_type_args(field.annotation)
        assert TeamDefenseStatsSortKeyEnum in flat

    def test_defense_request_split_uses_enum(self):
        from griddy.nfl.models.requests.get_team_defense_stats_by_week_op import (
            GetTeamDefenseStatsByWeekRequest,
        )

        field = GetTeamDefenseStatsByWeekRequest.model_fields["split"]
        flat = _flatten_type_args(field.annotation)
        assert TeamDefenseStatsSplitEnum in flat


@pytest.mark.unit
class TestEnumExportsFromModelsInit:
    """Verify new enums are accessible from the models package."""

    def test_team_defense_sort_key_enum_importable(self):
        from griddy.nfl import models

        assert hasattr(models, "TeamDefenseStatsSortKeyEnum")

    def test_team_defense_split_enum_importable(self):
        from griddy.nfl import models

        assert hasattr(models, "TeamDefenseStatsSplitEnum")


def _flatten_type_args(tp):
    """Recursively extract all type args from a (possibly nested) generic type."""
    result = set()
    args = typing.get_args(tp)
    if not args:
        result.add(tp)
    for arg in args:
        result.add(arg)
        result.update(_flatten_type_args(arg))
    return result
