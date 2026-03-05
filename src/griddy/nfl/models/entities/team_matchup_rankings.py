from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, Nullable, OptionalNullable


class TeamMatchupRankings(BaseModel):
    r"""Comprehensive team rankings across multiple statistical categories"""

    passing_blitz_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingBlitzAdvantage")
    ] = None

    passing_blitz_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingBlitzZDiff")
    ] = None

    passing_deep_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingDeepAdvantage")
    ] = None

    passing_deep_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingDeepZDiff")
    ] = None

    passing_intermediate_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingIntermediateAdvantage")
    ] = None

    passing_intermediate_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingIntermediateZDiff")
    ] = None

    passing_long_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingLongAdvantage")
    ] = None

    passing_long_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingLongZDiff")
    ] = None

    passing_no_blitz_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingNoBlitzAdvantage")
    ] = None

    passing_no_blitz_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingNoBlitzZDiff")
    ] = None

    passing_no_play_action_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingNoPlayActionAdvantage")
    ] = None

    passing_no_play_action_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingNoPlayActionZDiff")
    ] = None

    passing_no_pressure_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingNoPressureAdvantage")
    ] = None

    passing_no_pressure_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingNoPressureZDiff")
    ] = None

    passing_overall_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingOverallAdvantage")
    ] = None
    r"""Advantage rating (-4 to 4)"""

    passing_overall_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingOverallZDiff")
    ] = None
    r"""Z-score differential for passing offense vs defense"""

    passing_play_action_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingPlayActionAdvantage")
    ] = None

    passing_play_action_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingPlayActionZDiff")
    ] = None

    passing_pressure_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingPressureAdvantage")
    ] = None

    passing_pressure_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingPressureZDiff")
    ] = None

    passing_quick_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingQuickAdvantage")
    ] = None

    passing_quick_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingQuickZDiff")
    ] = None

    passing_short_advantage: Annotated[
        Optional[str], pydantic.Field(alias="passingShortAdvantage")
    ] = None

    passing_short_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="passingShortZDiff")
    ] = None

    pressure_rate_advantage: Annotated[
        Optional[str], pydantic.Field(alias="pressureRateAdvantage")
    ] = None

    pressure_rate_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="pressureRateZDiff")
    ] = None

    rushing_designed_runs_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingDesignedRunsAdvantage")
    ] = None

    rushing_designed_runs_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="rushingDesignedRunsZDiff")
    ] = None

    rushing_inside_tackles_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingInsideTacklesAdvantage")
    ] = None

    rushing_inside_tackles_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="rushingInsideTacklesZDiff")
    ] = None

    rushing_light_box_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingLightBoxAdvantage")
    ] = None

    rushing_light_box_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="rushingLightBoxZDiff")
    ] = None

    rushing_outside_tackles_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingOutsideTacklesAdvantage")
    ] = None

    rushing_outside_tackles_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="rushingOutsideTacklesZDiff")
    ] = None

    rushing_overall_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingOverallAdvantage")
    ] = None

    rushing_overall_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="rushingOverallZDiff")
    ] = None

    rushing_qb_scrambles_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingQBScramblesAdvantage")
    ] = None

    rushing_qb_scrambles_z_diff: Annotated[
        OptionalNullable[float], pydantic.Field(alias="rushingQBScramblesZDiff")
    ] = UNSET

    rushing_red_zone_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingRedZoneAdvantage")
    ] = None

    rushing_red_zone_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="rushingRedZoneZDiff")
    ] = None

    rushing_shotgun_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingShotgunAdvantage")
    ] = None

    rushing_shotgun_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="rushingShotgunZDiff")
    ] = None

    rushing_stacked_box_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingStackedBoxAdvantage")
    ] = None

    rushing_stacked_box_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="rushingStackedBoxZDiff")
    ] = None

    rushing_under_center_advantage: Annotated[
        Optional[str], pydantic.Field(alias="rushingUnderCenterAdvantage")
    ] = None

    rushing_under_center_z_diff: Annotated[
        Optional[float], pydantic.Field(alias="rushingUnderCenterZDiff")
    ] = None

    team_defense_passing_blitz_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingBlitzRank")
    ] = None

    team_defense_passing_blitz_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingBlitzZ")
    ] = None

    team_defense_passing_deep_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingDeepRank")
    ] = None

    team_defense_passing_deep_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingDeepZ")
    ] = None

    team_defense_passing_intermediate_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingIntermediateRank")
    ] = None

    team_defense_passing_intermediate_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingIntermediateZ")
    ] = None

    team_defense_passing_long_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingLongRank")
    ] = None

    team_defense_passing_long_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingLongZ")
    ] = None

    team_defense_passing_no_blitz_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingNoBlitzRank")
    ] = None

    team_defense_passing_no_blitz_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingNoBlitzZ")
    ] = None

    team_defense_passing_no_play_action_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingNoPlayActionRank")
    ] = None

    team_defense_passing_no_play_action_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingNoPlayActionZ")
    ] = None

    team_defense_passing_no_pressure_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingNoPressureRank")
    ] = None

    team_defense_passing_no_pressure_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingNoPressureZ")
    ] = None

    team_defense_passing_overall_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingOverallRank")
    ] = None

    team_defense_passing_overall_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingOverallZ")
    ] = None

    team_defense_passing_play_action_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingPlayActionRank")
    ] = None

    team_defense_passing_play_action_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingPlayActionZ")
    ] = None

    team_defense_passing_pressure_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingPressureRank")
    ] = None

    team_defense_passing_pressure_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingPressureZ")
    ] = None

    team_defense_passing_quick_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingQuickRank")
    ] = None

    team_defense_passing_quick_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingQuickZ")
    ] = None

    team_defense_passing_short_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePassingShortRank")
    ] = None

    team_defense_passing_short_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePassingShortZ")
    ] = None

    team_defense_pressure_rate_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefensePressureRateRank")
    ] = None

    team_defense_pressure_rate_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefensePressureRateZ")
    ] = None

    team_defense_rushing_designed_runs_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingDesignedRunsRank")
    ] = None

    team_defense_rushing_designed_runs_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingDesignedRunsZ")
    ] = None

    team_defense_rushing_inside_tackles_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingInsideTacklesRank")
    ] = None

    team_defense_rushing_inside_tackles_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingInsideTacklesZ")
    ] = None

    team_defense_rushing_light_box_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingLightBoxRank")
    ] = None

    team_defense_rushing_light_box_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingLightBoxZ")
    ] = None

    team_defense_rushing_outside_tackles_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingOutsideTacklesRank")
    ] = None

    team_defense_rushing_outside_tackles_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingOutsideTacklesZ")
    ] = None

    team_defense_rushing_overall_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingOverallRank")
    ] = None

    team_defense_rushing_overall_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingOverallZ")
    ] = None

    team_defense_rushing_qb_scrambles_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingQBScramblesRank")
    ] = None

    team_defense_rushing_qb_scrambles_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingQBScramblesZ")
    ] = None

    team_defense_rushing_red_zone_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingRedZoneRank")
    ] = None

    team_defense_rushing_red_zone_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingRedZoneZ")
    ] = None

    team_defense_rushing_shotgun_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingShotgunRank")
    ] = None

    team_defense_rushing_shotgun_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingShotgunZ")
    ] = None

    team_defense_rushing_stacked_box_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingStackedBoxRank")
    ] = None

    team_defense_rushing_stacked_box_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingStackedBoxZ")
    ] = None

    team_defense_rushing_under_center_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamDefenseRushingUnderCenterRank")
    ] = None

    team_defense_rushing_under_center_z: Annotated[
        Optional[float], pydantic.Field(alias="teamDefenseRushingUnderCenterZ")
    ] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None

    team_passing_blitz_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingBlitzRank")
    ] = None

    team_passing_blitz_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingBlitzZ")
    ] = None

    team_passing_deep_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingDeepRank")
    ] = None

    team_passing_deep_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingDeepZ")
    ] = None

    team_passing_intermediate_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingIntermediateRank")
    ] = None

    team_passing_intermediate_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingIntermediateZ")
    ] = None

    team_passing_long_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingLongRank")
    ] = None

    team_passing_long_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingLongZ")
    ] = None

    team_passing_no_blitz_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingNoBlitzRank")
    ] = None

    team_passing_no_blitz_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingNoBlitzZ")
    ] = None

    team_passing_no_play_action_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingNoPlayActionRank")
    ] = None

    team_passing_no_play_action_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingNoPlayActionZ")
    ] = None

    team_passing_no_pressure_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingNoPressureRank")
    ] = None

    team_passing_no_pressure_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingNoPressureZ")
    ] = None

    team_passing_overall_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingOverallRank")
    ] = None
    r"""Overall passing offense rank (1-32)"""

    team_passing_overall_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingOverallZ")
    ] = None
    r"""Z-score for passing offense"""

    team_passing_play_action_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingPlayActionRank")
    ] = None

    team_passing_play_action_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingPlayActionZ")
    ] = None

    team_passing_pressure_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingPressureRank")
    ] = None

    team_passing_pressure_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingPressureZ")
    ] = None

    team_passing_quick_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingQuickRank")
    ] = None

    team_passing_quick_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingQuickZ")
    ] = None

    team_passing_short_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPassingShortRank")
    ] = None

    team_passing_short_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPassingShortZ")
    ] = None

    team_pressure_rate_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamPressureRateRank")
    ] = None

    team_pressure_rate_z: Annotated[
        Optional[float], pydantic.Field(alias="teamPressureRateZ")
    ] = None

    team_rushing_designed_runs_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingDesignedRunsRank")
    ] = None

    team_rushing_designed_runs_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingDesignedRunsZ")
    ] = None

    team_rushing_inside_tackles_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingInsideTacklesRank")
    ] = None

    team_rushing_inside_tackles_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingInsideTacklesZ")
    ] = None

    team_rushing_light_box_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingLightBoxRank")
    ] = None

    team_rushing_light_box_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingLightBoxZ")
    ] = None

    team_rushing_outside_tackles_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingOutsideTacklesRank")
    ] = None

    team_rushing_outside_tackles_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingOutsideTacklesZ")
    ] = None

    team_rushing_overall_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingOverallRank")
    ] = None

    team_rushing_overall_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingOverallZ")
    ] = None

    team_rushing_qb_scrambles_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingQBScramblesRank")
    ] = None

    team_rushing_qb_scrambles_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingQBScramblesZ")
    ] = None

    team_rushing_red_zone_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingRedZoneRank")
    ] = None

    team_rushing_red_zone_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingRedZoneZ")
    ] = None

    team_rushing_shotgun_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingShotgunRank")
    ] = None

    team_rushing_shotgun_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingShotgunZ")
    ] = None

    team_rushing_stacked_box_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingStackedBoxRank")
    ] = None

    team_rushing_stacked_box_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingStackedBoxZ")
    ] = None

    team_rushing_under_center_rank: Annotated[
        Optional[int], pydantic.Field(alias="teamRushingUnderCenterRank")
    ] = None

    team_rushing_under_center_z: Annotated[
        Optional[float], pydantic.Field(alias="teamRushingUnderCenterZ")
    ] = None
