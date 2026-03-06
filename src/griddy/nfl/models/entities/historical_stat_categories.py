from __future__ import annotations

from typing import Any, Dict, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel

# ---------------------------------------------------------------------------
# Defense
# ---------------------------------------------------------------------------


class HistoricalDefenseStats(BaseModel):
    """Historical defensive statistics for a player or team."""

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


class HistoricalPassingStats(BaseModel):
    """Historical passing statistics for a player or team."""

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


class HistoricalRushingStats(BaseModel):
    """Historical rushing statistics for a player or team."""

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


class HistoricalReceivingStats(BaseModel):
    """Historical receiving statistics for a player or team."""

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


class HistoricalKickReturnsStats(BaseModel):
    """Historical kick return statistics."""

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


class HistoricalPuntReturnsStats(BaseModel):
    """Historical punt return statistics."""

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
    """Detailed kicking breakdown by distance range."""

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
    made_per_game: Annotated[Optional[float], pydantic.Field(alias="madePerGame")] = (
        None
    )


class HistoricalKickingStats(BaseModel):
    """Historical kicking statistics."""

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


class HistoricalKickoffsStats(BaseModel):
    """Historical kickoff statistics."""

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


class HistoricalPuntingStats(BaseModel):
    """Historical punting statistics."""

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


class HistoricalPenaltiesStats(BaseModel):
    """Historical penalty statistics."""

    total: Optional[int] = None

    yards: Optional[int] = None


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


class HistoricalScoringStats(BaseModel):
    """Historical scoring statistics."""

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


class HistoricalDownAndDistanceStats(BaseModel):
    """Historical down-and-distance conversion statistics."""

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


class HistoricalRedzoneStats(BaseModel):
    """Historical red zone statistics."""

    attempts: Optional[int] = None

    field_goals: Annotated[Optional[int], pydantic.Field(alias="fieldGoals")] = None

    good: Optional[int] = None


# ---------------------------------------------------------------------------
# Goal to Go
# ---------------------------------------------------------------------------


class HistoricalGoalToGoStats(BaseModel):
    """Historical goal-to-go statistics."""

    attempts: Optional[int] = None

    good: Optional[int] = None


# ---------------------------------------------------------------------------
# Time of Possession
# ---------------------------------------------------------------------------


class HistoricalTimeOfPossessionStats(BaseModel):
    """Historical time of possession statistics."""

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


class HistoricalStatCategories(BaseModel):
    """Container for all historical stat categories."""

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
