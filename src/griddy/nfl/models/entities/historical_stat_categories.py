from __future__ import annotations

from typing import Any, Dict, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel

# ---------------------------------------------------------------------------
# Defense
# ---------------------------------------------------------------------------


class HistoricalDefenseStatsTypedDict(TypedDict):
    assists: NotRequired[int]
    all_kick_blocked: NotRequired[int]
    batted_down: NotRequired[int]
    combine_tackles: NotRequired[int]
    fg_blocked: NotRequired[int]
    forced_fumble: NotRequired[int]
    misc_assists: NotRequired[int]
    misc_ffum: NotRequired[int]
    misc_tackles: NotRequired[float]
    passes_defensed: NotRequired[int]
    punt_blocked: NotRequired[int]
    qb_hits: NotRequired[int]
    reg_assists: NotRequired[int]
    reg_combined: NotRequired[float]
    reg_ffum: NotRequired[int]
    reg_tackles: NotRequired[float]
    sack_yards: NotRequired[float]
    sacks: NotRequired[float]
    safeties: NotRequired[int]
    solo_tackles: NotRequired[int]
    spec_assists: NotRequired[int]
    spec_ffum: NotRequired[int]
    spec_tackles: NotRequired[float]
    stuff: NotRequired[float]
    stuff_yards: NotRequired[int]
    tackles: NotRequired[float]
    tfl: NotRequired[float]
    tfl_yards: NotRequired[float]
    total_assists: NotRequired[int]
    total_combined: NotRequired[float]
    total_tackles: NotRequired[float]
    xp_blocked: NotRequired[int]


class HistoricalDefenseStats(BaseModel):
    assists: Optional[int] = None

    all_kick_blocked: Annotated[
        Optional[int], pydantic.Field(alias="allKickBlocked")
    ] = None

    batted_down: Annotated[Optional[int], pydantic.Field(alias="battedDown")] = None

    combine_tackles: Annotated[
        Optional[int], pydantic.Field(alias="combineTackles")
    ] = None

    fg_blocked: Annotated[Optional[int], pydantic.Field(alias="fgBlocked")] = None

    forced_fumble: Annotated[Optional[int], pydantic.Field(alias="forcedFumble")] = None

    misc_assists: Annotated[Optional[int], pydantic.Field(alias="miscAssists")] = None

    misc_ffum: Annotated[Optional[int], pydantic.Field(alias="miscFfum")] = None

    misc_tackles: Annotated[Optional[float], pydantic.Field(alias="miscTackles")] = None

    passes_defensed: Annotated[
        Optional[int], pydantic.Field(alias="passesDefensed")
    ] = None

    punt_blocked: Annotated[Optional[int], pydantic.Field(alias="puntBlocked")] = None

    qb_hits: Annotated[Optional[int], pydantic.Field(alias="qbHits")] = None

    reg_assists: Annotated[Optional[int], pydantic.Field(alias="regAssists")] = None

    reg_combined: Annotated[Optional[float], pydantic.Field(alias="regCombined")] = None

    reg_ffum: Annotated[Optional[int], pydantic.Field(alias="regFfum")] = None

    reg_tackles: Annotated[Optional[float], pydantic.Field(alias="regTackles")] = None

    sack_yards: Annotated[Optional[float], pydantic.Field(alias="sackYards")] = None

    sacks: Optional[float] = None

    safeties: Optional[int] = None

    solo_tackles: Annotated[Optional[int], pydantic.Field(alias="soloTackles")] = None

    spec_assists: Annotated[Optional[int], pydantic.Field(alias="specAssists")] = None

    spec_ffum: Annotated[Optional[int], pydantic.Field(alias="specFfum")] = None

    spec_tackles: Annotated[Optional[float], pydantic.Field(alias="specTackles")] = None

    stuff: Optional[float] = None

    stuff_yards: Annotated[Optional[int], pydantic.Field(alias="stuffYards")] = None

    tackles: Optional[float] = None

    tfl: Optional[float] = None

    tfl_yards: Annotated[Optional[float], pydantic.Field(alias="tflYards")] = None

    total_assists: Annotated[Optional[int], pydantic.Field(alias="totalAssists")] = None

    total_combined: Annotated[
        Optional[float], pydantic.Field(alias="totalCombined")
    ] = None

    total_tackles: Annotated[Optional[float], pydantic.Field(alias="totalTackles")] = (
        None
    )

    xp_blocked: Annotated[Optional[int], pydantic.Field(alias="xpBlocked")] = None


# ---------------------------------------------------------------------------
# Passing
# ---------------------------------------------------------------------------


class HistoricalPassingStatsTypedDict(TypedDict):
    distance_20_plus: NotRequired[int]
    distance_40_plus: NotRequired[int]
    attempts: NotRequired[int]
    attempts_per_game: NotRequired[Optional[float]]
    average_yards: NotRequired[float]
    completion_percentage: NotRequired[float]
    completions: NotRequired[int]
    extra_point_attempts: NotRequired[int]
    extra_point_good: NotRequired[int]
    first_down_percentage: NotRequired[float]
    first_downs: NotRequired[int]
    fumbles: NotRequired[int]
    fumbles_lost: NotRequired[int]
    interception_percentage: NotRequired[float]
    interceptions: NotRequired[int]
    lgtd: NotRequired[bool]
    long: NotRequired[int]
    net_yards: NotRequired[int]
    passer_rating: NotRequired[float]
    sacked: NotRequired[int]
    sacked_yards_lost: NotRequired[int]
    touchdown_percentage: NotRequired[float]
    touchdowns: NotRequired[int]
    touchdowns_per_game: NotRequired[Optional[float]]
    yards: NotRequired[int]
    yards_after_catch: NotRequired[int]


class HistoricalPassingStats(BaseModel):
    distance_20_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance20Plus")
    ] = None

    distance_40_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance40Plus")
    ] = None

    attempts: Optional[int] = None

    attempts_per_game: Annotated[
        Optional[float], pydantic.Field(alias="attemptsPerGame")
    ] = None

    average_yards: Annotated[Optional[float], pydantic.Field(alias="averageYards")] = (
        None
    )

    completion_percentage: Annotated[
        Optional[float], pydantic.Field(alias="completionPercentage")
    ] = None

    completions: Optional[int] = None

    extra_point_attempts: Annotated[
        Optional[int], pydantic.Field(alias="extraPointAttempts")
    ] = None

    extra_point_good: Annotated[
        Optional[int], pydantic.Field(alias="extraPointGood")
    ] = None

    first_down_percentage: Annotated[
        Optional[float], pydantic.Field(alias="firstDownPercentage")
    ] = None

    first_downs: Annotated[Optional[int], pydantic.Field(alias="firstDowns")] = None

    fumbles: Optional[int] = None

    fumbles_lost: Annotated[Optional[int], pydantic.Field(alias="fumblesLost")] = None

    interception_percentage: Annotated[
        Optional[float], pydantic.Field(alias="interceptionPercentage")
    ] = None

    interceptions: Optional[int] = None

    lgtd: Optional[bool] = None

    long: Optional[int] = None

    net_yards: Annotated[Optional[int], pydantic.Field(alias="netYards")] = None

    passer_rating: Annotated[Optional[float], pydantic.Field(alias="passerRating")] = (
        None
    )

    sacked: Optional[int] = None

    sacked_yards_lost: Annotated[
        Optional[int], pydantic.Field(alias="sackedYardsLost")
    ] = None

    touchdown_percentage: Annotated[
        Optional[float], pydantic.Field(alias="touchdownPercentage")
    ] = None

    touchdowns: Optional[int] = None

    touchdowns_per_game: Annotated[
        Optional[float], pydantic.Field(alias="touchdownsPerGame")
    ] = None

    yards: Optional[int] = None

    yards_after_catch: Annotated[
        Optional[int], pydantic.Field(alias="yardsAfterCatch")
    ] = None


# ---------------------------------------------------------------------------
# Rushing
# ---------------------------------------------------------------------------


class HistoricalRushingStatsTypedDict(TypedDict):
    distance_20_plus: NotRequired[int]
    distance_40_plus: NotRequired[int]
    attempts: NotRequired[int]
    attempts_per_game: NotRequired[Optional[float]]
    average_yards: NotRequired[float]
    extra_point_attempts: NotRequired[int]
    extra_point_good: NotRequired[int]
    first_down_percentage: NotRequired[float]
    first_downs: NotRequired[int]
    fumbles: NotRequired[int]
    fumbles_lost: NotRequired[int]
    lgtd: NotRequired[bool]
    long: NotRequired[int]
    stuff: NotRequired[int]
    stuff_yards: NotRequired[int]
    touchdowns: NotRequired[int]
    touchdowns_per_game: NotRequired[Optional[float]]
    yards: NotRequired[int]


class HistoricalRushingStats(BaseModel):
    distance_20_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance20Plus")
    ] = None

    distance_40_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance40Plus")
    ] = None

    attempts: Optional[int] = None

    attempts_per_game: Annotated[
        Optional[float], pydantic.Field(alias="attemptsPerGame")
    ] = None

    average_yards: Annotated[Optional[float], pydantic.Field(alias="averageYards")] = (
        None
    )

    extra_point_attempts: Annotated[
        Optional[int], pydantic.Field(alias="extraPointAttempts")
    ] = None

    extra_point_good: Annotated[
        Optional[int], pydantic.Field(alias="extraPointGood")
    ] = None

    first_down_percentage: Annotated[
        Optional[float], pydantic.Field(alias="firstDownPercentage")
    ] = None

    first_downs: Annotated[Optional[int], pydantic.Field(alias="firstDowns")] = None

    fumbles: Optional[int] = None

    fumbles_lost: Annotated[Optional[int], pydantic.Field(alias="fumblesLost")] = None

    lgtd: Optional[bool] = None

    long: Optional[int] = None

    stuff: Optional[int] = None

    stuff_yards: Annotated[Optional[int], pydantic.Field(alias="stuffYards")] = None

    touchdowns: Optional[int] = None

    touchdowns_per_game: Annotated[
        Optional[float], pydantic.Field(alias="touchdownsPerGame")
    ] = None

    yards: Optional[int] = None


# ---------------------------------------------------------------------------
# Receiving
# ---------------------------------------------------------------------------


class HistoricalReceivingStatsTypedDict(TypedDict):
    average_yards: NotRequired[float]
    distance_20_plus: NotRequired[int]
    distance_40_plus: NotRequired[int]
    extra_point_attempts: NotRequired[int]
    extra_point_good: NotRequired[int]
    first_down_percentage: NotRequired[float]
    first_downs: NotRequired[int]
    fumbles: NotRequired[int]
    fumbles_lost: NotRequired[int]
    lgtd: NotRequired[bool]
    long: NotRequired[int]
    receptions: NotRequired[int]
    receptions_per_game: NotRequired[Optional[float]]
    target: NotRequired[int]
    touchdowns: NotRequired[int]
    touchdowns_per_game: NotRequired[Optional[float]]
    yards: NotRequired[int]
    yards_after_catch: NotRequired[int]
    yards_per_game: NotRequired[Optional[float]]


class HistoricalReceivingStats(BaseModel):
    average_yards: Annotated[Optional[float], pydantic.Field(alias="averageYards")] = (
        None
    )

    distance_20_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance20Plus")
    ] = None

    distance_40_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance40Plus")
    ] = None

    extra_point_attempts: Annotated[
        Optional[int], pydantic.Field(alias="extraPointAttempts")
    ] = None

    extra_point_good: Annotated[
        Optional[int], pydantic.Field(alias="extraPointGood")
    ] = None

    first_down_percentage: Annotated[
        Optional[float], pydantic.Field(alias="firstDownPercentage")
    ] = None

    first_downs: Annotated[Optional[int], pydantic.Field(alias="firstDowns")] = None

    fumbles: Optional[int] = None

    fumbles_lost: Annotated[Optional[int], pydantic.Field(alias="fumblesLost")] = None

    lgtd: Optional[bool] = None

    long: Optional[int] = None

    receptions: Optional[int] = None

    receptions_per_game: Annotated[
        Optional[float], pydantic.Field(alias="receptionsPerGame")
    ] = None

    target: Optional[int] = None

    touchdowns: Optional[int] = None

    touchdowns_per_game: Annotated[
        Optional[float], pydantic.Field(alias="touchdownsPerGame")
    ] = None

    yards: Optional[int] = None

    yards_after_catch: Annotated[
        Optional[int], pydantic.Field(alias="yardsAfterCatch")
    ] = None

    yards_per_game: Annotated[Optional[float], pydantic.Field(alias="yardsPerGame")] = (
        None
    )


# ---------------------------------------------------------------------------
# Kick Returns
# ---------------------------------------------------------------------------


class HistoricalKickReturnsStatsTypedDict(TypedDict):
    attempts: NotRequired[int]
    average_yards: NotRequired[float]
    distance_20_plus: NotRequired[int]
    distance_40_plus: NotRequired[int]
    fair_catches: NotRequired[int]
    fumbles: NotRequired[int]
    fumbles_lost: NotRequired[int]
    lgtd: NotRequired[bool]
    long: NotRequired[int]
    touchdowns: NotRequired[int]
    yards: NotRequired[int]


class HistoricalKickReturnsStats(BaseModel):
    attempts: Optional[int] = None

    average_yards: Annotated[Optional[float], pydantic.Field(alias="averageYards")] = (
        None
    )

    distance_20_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance20Plus")
    ] = None

    distance_40_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance40Plus")
    ] = None

    fair_catches: Annotated[Optional[int], pydantic.Field(alias="fairCatches")] = None

    fumbles: Optional[int] = None

    fumbles_lost: Annotated[Optional[int], pydantic.Field(alias="fumblesLost")] = None

    lgtd: Optional[bool] = None

    long: Optional[int] = None

    touchdowns: Optional[int] = None

    yards: Optional[int] = None


# ---------------------------------------------------------------------------
# Punt Returns
# ---------------------------------------------------------------------------


class HistoricalPuntReturnsStatsTypedDict(TypedDict):
    attempts: NotRequired[int]
    average_yards: NotRequired[float]
    distance_20_plus: NotRequired[int]
    distance_40_plus: NotRequired[int]
    fair_catches: NotRequired[int]
    fumbles: NotRequired[int]
    fumbles_lost: NotRequired[int]
    lgtd: NotRequired[bool]
    long: NotRequired[int]
    start_in_10: NotRequired[int]
    start_in_20: NotRequired[int]
    touchdowns: NotRequired[int]
    yards: NotRequired[int]


class HistoricalPuntReturnsStats(BaseModel):
    attempts: Optional[int] = None

    average_yards: Annotated[Optional[float], pydantic.Field(alias="averageYards")] = (
        None
    )

    distance_20_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance20Plus")
    ] = None

    distance_40_plus: Annotated[
        Optional[int], pydantic.Field(alias="distance40Plus")
    ] = None

    fair_catches: Annotated[Optional[int], pydantic.Field(alias="fairCatches")] = None

    fumbles: Optional[int] = None

    fumbles_lost: Annotated[Optional[int], pydantic.Field(alias="fumblesLost")] = None

    lgtd: Optional[bool] = None

    long: Optional[int] = None

    start_in_10: Annotated[Optional[int], pydantic.Field(alias="startIn10")] = None

    start_in_20: Annotated[Optional[int], pydantic.Field(alias="startIn20")] = None

    touchdowns: Optional[int] = None

    yards: Optional[int] = None


# ---------------------------------------------------------------------------
# Kicking
# ---------------------------------------------------------------------------

class KickingDetails(BaseModel):
    # These are provided for each range
    attempts: Optional[int] = None
    made: Optional[int] = None
    percentage: Optional[float] = None

    # These are only on "FieldGoals" or "extraPoints"
    attempted_yards: Annotated[
        Optional[int], pydantic.Field(alias="attemptedYards")
    ] = None
    blocked: Optional[int] = None
    long: Optional[int] = None
    made_per_game: Annotated[
        Optional[float], pydantic.Field(alias="madePerGame")
    ] = None


class HistoricalKickingStatsTypedDict(TypedDict):
    attempts_1_to_19: NotRequired[int]
    attempts_20_to_29: NotRequired[int]
    attempts_30_to_39: NotRequired[int]
    attempts_40_to_49: NotRequired[int]
    attempts_50_to_59: NotRequired[int]
    attempts_60_plus: NotRequired[int]
    extra_points: NotRequired[Dict[str, Any]]
    field_goals: NotRequired[Dict[str, Any]]


class HistoricalKickingStats(BaseModel):
    attempts_1_to_19: Annotated[
        Optional[KickingDetails], pydantic.Field(alias="attempts1To19")
    ] = None

    attempts_20_to_29: Annotated[
        Optional[KickingDetails], pydantic.Field(alias="attempts20To29")
    ] = None

    attempts_30_to_39: Annotated[
        Optional[KickingDetails], pydantic.Field(alias="attempts30To39")
    ] = None

    attempts_40_to_49: Annotated[
        Optional[KickingDetails], pydantic.Field(alias="attempts40To49")
    ] = None

    attempts_50_to_59: Annotated[
        Optional[KickingDetails], pydantic.Field(alias="attempts50To59")
    ] = None

    attempts_60_plus: Annotated[
        Optional[KickingDetails], pydantic.Field(alias="attempts60Plus")
    ] = None

    extra_points: Annotated[
        Optional[Dict[str, Any]], pydantic.Field(alias="extraPoints")
    ] = None

    field_goals: Annotated[
        Optional[Dict[str, Any]], pydantic.Field(alias="fieldGoals")
    ] = None


# ---------------------------------------------------------------------------
# Kickoffs
# ---------------------------------------------------------------------------


class HistoricalKickoffsStatsTypedDict(TypedDict):
    attempts: NotRequired[int]
    average_yards: NotRequired[float]
    endzone: NotRequired[int]
    fair_caught: NotRequired[int]
    onside: NotRequired[int]
    onside_recovered: NotRequired[int]
    out_of_bounds: NotRequired[int]
    return_average_yards: NotRequired[float]
    return_touchdowns: NotRequired[int]
    return_yards: NotRequired[int]
    returns: NotRequired[int]
    touchbacks: NotRequired[int]
    touchbacks_percentage: NotRequired[float]
    yards: NotRequired[int]


class HistoricalKickoffsStats(BaseModel):
    attempts: Optional[int] = None

    average_yards: Annotated[Optional[float], pydantic.Field(alias="averageYards")] = (
        None
    )

    endzone: Optional[int] = None

    fair_caught: Annotated[Optional[int], pydantic.Field(alias="fairCaught")] = None

    onside: Optional[int] = None

    onside_recovered: Annotated[
        Optional[int], pydantic.Field(alias="onsideRecovered")
    ] = None

    out_of_bounds: Annotated[Optional[int], pydantic.Field(alias="outOfBounds")] = None

    return_average_yards: Annotated[
        Optional[float], pydantic.Field(alias="returnAverageYards")
    ] = None

    return_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="returnTouchdowns")
    ] = None

    return_yards: Annotated[Optional[int], pydantic.Field(alias="returnYards")] = None

    returns: Optional[int] = None

    touchbacks: Optional[int] = None

    touchbacks_percentage: Annotated[
        Optional[float], pydantic.Field(alias="touchbacksPercentage")
    ] = None

    yards: Optional[int] = None


# ---------------------------------------------------------------------------
# Punting
# ---------------------------------------------------------------------------


class HistoricalPuntingStatsTypedDict(TypedDict):
    attempts: NotRequired[int]
    average_yards: NotRequired[float]
    blocked: NotRequired[int]
    downed: NotRequired[int]
    fair_caught: NotRequired[int]
    inside_10: NotRequired[int]
    inside_20: NotRequired[int]
    long: NotRequired[int]
    net_average: NotRequired[float]
    net_yardage: NotRequired[int]
    out_of_bounds: NotRequired[int]
    punts_and_blocked: NotRequired[int]
    return_touchdowns: NotRequired[int]
    return_yards: NotRequired[int]
    returns: NotRequired[int]
    touchbacks: NotRequired[int]
    yards: NotRequired[int]


class HistoricalPuntingStats(BaseModel):
    attempts: Optional[int] = None

    average_yards: Annotated[Optional[float], pydantic.Field(alias="averageYards")] = (
        None
    )

    blocked: Optional[int] = None

    downed: Optional[int] = None

    fair_caught: Annotated[Optional[int], pydantic.Field(alias="fairCaught")] = None

    inside_10: Annotated[Optional[int], pydantic.Field(alias="inside10")] = None

    inside_20: Annotated[Optional[int], pydantic.Field(alias="inside20")] = None

    long: Optional[int] = None

    net_average: Annotated[Optional[float], pydantic.Field(alias="netAverage")] = None

    net_yardage: Annotated[Optional[int], pydantic.Field(alias="netYardage")] = None

    out_of_bounds: Annotated[Optional[int], pydantic.Field(alias="outOfBounds")] = None

    punts_and_blocked: Annotated[
        Optional[int], pydantic.Field(alias="puntsAndBlocked")
    ] = None

    return_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="returnTouchdowns")
    ] = None

    return_yards: Annotated[Optional[int], pydantic.Field(alias="returnYards")] = None

    returns: Optional[int] = None

    touchbacks: Optional[int] = None

    yards: Optional[int] = None


# ---------------------------------------------------------------------------
# Penalties
# ---------------------------------------------------------------------------


class HistoricalPenaltiesStatsTypedDict(TypedDict):
    total: NotRequired[int]
    yards: NotRequired[int]


class HistoricalPenaltiesStats(BaseModel):
    total: Optional[int] = None

    yards: Optional[int] = None


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


class HistoricalScoringStatsTypedDict(TypedDict):
    average_margin_of_victory: NotRequired[Optional[float]]
    average_points_scored: NotRequired[Optional[float]]
    defensive_touchdowns: NotRequired[int]
    offensive_touchdowns: NotRequired[int]
    return_touchdowns: NotRequired[int]
    special_teams_touchdowns: NotRequired[int]
    total_points_scored: NotRequired[int]
    total_touchdowns: NotRequired[int]


class HistoricalScoringStats(BaseModel):
    average_margin_of_victory: Annotated[
        Optional[float], pydantic.Field(alias="averageMarginOfVictory")
    ] = None

    average_points_scored: Annotated[
        Optional[float], pydantic.Field(alias="averagePointsScored")
    ] = None

    defensive_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="defensiveTouchdowns")
    ] = None

    offensive_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="offensiveTouchdowns")
    ] = None

    return_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="returnTouchdowns")
    ] = None

    special_teams_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="specialTeamsTouchdowns")
    ] = None

    total_points_scored: Annotated[
        Optional[int], pydantic.Field(alias="totalPointsScored")
    ] = None

    total_touchdowns: Annotated[
        Optional[int], pydantic.Field(alias="totalTouchdowns")
    ] = None


# ---------------------------------------------------------------------------
# Down and Distance
# ---------------------------------------------------------------------------


class HistoricalDownAndDistanceStatsTypedDict(TypedDict):
    downs_1st_attempts: NotRequired[int]
    downs_1st_made: NotRequired[int]
    downs_2nd_attempts: NotRequired[int]
    downs_2nd_made: NotRequired[int]
    downs_3rd_attempts: NotRequired[int]
    downs_3rd_made: NotRequired[int]
    downs_4th_attempts: NotRequired[int]
    downs_4th_made: NotRequired[int]
    passing: NotRequired[int]
    penalty: NotRequired[int]
    rushing: NotRequired[int]
    total: NotRequired[int]


class HistoricalDownAndDistanceStats(BaseModel):
    downs_1st_attempts: Annotated[
        Optional[int], pydantic.Field(alias="downs1stAttempts")
    ] = None

    downs_1st_made: Annotated[Optional[int], pydantic.Field(alias="downs1stMade")] = (
        None
    )

    downs_2nd_attempts: Annotated[
        Optional[int], pydantic.Field(alias="downs2ndAttempts")
    ] = None

    downs_2nd_made: Annotated[Optional[int], pydantic.Field(alias="downs2ndMade")] = (
        None
    )

    downs_3rd_attempts: Annotated[
        Optional[int], pydantic.Field(alias="downs3rdAttempts")
    ] = None

    downs_3rd_made: Annotated[Optional[int], pydantic.Field(alias="downs3rdMade")] = (
        None
    )

    downs_4th_attempts: Annotated[
        Optional[int], pydantic.Field(alias="downs4thAttempts")
    ] = None

    downs_4th_made: Annotated[Optional[int], pydantic.Field(alias="downs4thMade")] = (
        None
    )

    passing: Optional[int] = None

    penalty: Optional[int] = None

    rushing: Optional[int] = None

    total: Optional[int] = None


# ---------------------------------------------------------------------------
# Red Zone
# ---------------------------------------------------------------------------


class HistoricalRedzoneStatsTypedDict(TypedDict):
    attempts: NotRequired[int]
    field_goals: NotRequired[int]
    good: NotRequired[int]


class HistoricalRedzoneStats(BaseModel):
    attempts: Optional[int] = None

    field_goals: Annotated[Optional[int], pydantic.Field(alias="fieldGoals")] = None

    good: Optional[int] = None


# ---------------------------------------------------------------------------
# Goal to Go
# ---------------------------------------------------------------------------


class HistoricalGoalToGoStatsTypedDict(TypedDict):
    attempts: NotRequired[int]
    good: NotRequired[int]


class HistoricalGoalToGoStats(BaseModel):
    attempts: Optional[int] = None

    good: Optional[int] = None


# ---------------------------------------------------------------------------
# Time of Possession
# ---------------------------------------------------------------------------


class HistoricalTimeOfPossessionStatsTypedDict(TypedDict):
    display: NotRequired[str]
    seconds_per_game: NotRequired[Optional[float]]
    seconds_per_game_display: NotRequired[Optional[str]]
    total_seconds: NotRequired[int]


class HistoricalTimeOfPossessionStats(BaseModel):
    display: Optional[str] = None

    seconds_per_game: Annotated[
        Optional[float], pydantic.Field(alias="secondsPerGame")
    ] = None

    seconds_per_game_display: Annotated[
        Optional[str], pydantic.Field(alias="secondsPerGameDisplay")
    ] = None

    total_seconds: Annotated[Optional[int], pydantic.Field(alias="totalSeconds")] = None


# ---------------------------------------------------------------------------
# Container: HistoricalStatCategories
# ---------------------------------------------------------------------------


class HistoricalStatCategoriesTypedDict(TypedDict):
    defense: NotRequired[HistoricalDefenseStatsTypedDict]
    passing: NotRequired[HistoricalPassingStatsTypedDict]
    rushing: NotRequired[HistoricalRushingStatsTypedDict]
    receiving: NotRequired[HistoricalReceivingStatsTypedDict]
    kick_returns: NotRequired[HistoricalKickReturnsStatsTypedDict]
    punt_returns: NotRequired[HistoricalPuntReturnsStatsTypedDict]
    kicking: NotRequired[HistoricalKickingStatsTypedDict]
    kickoffs: NotRequired[HistoricalKickoffsStatsTypedDict]
    punting: NotRequired[HistoricalPuntingStatsTypedDict]
    penalties: NotRequired[HistoricalPenaltiesStatsTypedDict]
    scoring: NotRequired[HistoricalScoringStatsTypedDict]
    down_and_distance: NotRequired[HistoricalDownAndDistanceStatsTypedDict]
    redzone: NotRequired[HistoricalRedzoneStatsTypedDict]
    goal_to_go: NotRequired[HistoricalGoalToGoStatsTypedDict]
    time_of_possession: NotRequired[HistoricalTimeOfPossessionStatsTypedDict]
    fumbles: NotRequired[Optional[Dict[str, Any]]]
    interceptions: NotRequired[Optional[Dict[str, Any]]]
    misc: NotRequired[Optional[Dict[str, Any]]]
    offense: NotRequired[Optional[Dict[str, Any]]]
    opponent_fumble_recoveries: NotRequired[Optional[Dict[str, Any]]]
    own_fumble_recoveries: NotRequired[Optional[Dict[str, Any]]]


class HistoricalStatCategories(BaseModel):
    defense: Optional[HistoricalDefenseStats] = None

    passing: Optional[HistoricalPassingStats] = None

    rushing: Optional[HistoricalRushingStats] = None

    receiving: Optional[HistoricalReceivingStats] = None

    kick_returns: Annotated[
        Optional[HistoricalKickReturnsStats], pydantic.Field(alias="kickReturns")
    ] = None

    punt_returns: Annotated[
        Optional[HistoricalPuntReturnsStats], pydantic.Field(alias="puntReturns")
    ] = None

    kicking: Optional[HistoricalKickingStats] = None

    kickoffs: Optional[HistoricalKickoffsStats] = None

    punting: Optional[HistoricalPuntingStats] = None

    penalties: Optional[HistoricalPenaltiesStats] = None

    scoring: Optional[HistoricalScoringStats] = None

    down_and_distance: Annotated[
        Optional[HistoricalDownAndDistanceStats],
        pydantic.Field(alias="downAndDistance"),
    ] = None

    redzone: Optional[HistoricalRedzoneStats] = None

    goal_to_go: Annotated[
        Optional[HistoricalGoalToGoStats], pydantic.Field(alias="goalToGo")
    ] = None

    time_of_possession: Annotated[
        Optional[HistoricalTimeOfPossessionStats],
        pydantic.Field(alias="timeOfPossession"),
    ] = None

    fumbles: Optional[Dict[str, Any]] = None

    interceptions: Optional[Dict[str, Any]] = None

    misc: Optional[Dict[str, Any]] = None

    offense: Optional[Dict[str, Any]] = None

    opponent_fumble_recoveries: Annotated[
        Optional[Dict[str, Any]], pydantic.Field(alias="opponentFumbleRecoveries")
    ] = None

    own_fumble_recoveries: Annotated[
        Optional[Dict[str, Any]], pydantic.Field(alias="ownFumbleRecoveries")
    ] = None
