from __future__ import annotations

from typing import Literal

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, OptionalNullable


class PlayerWeekProjectedStatsAttributes(BaseModel):
    """Projected statistical attributes for a player-week."""

    player_id: Annotated[str, pydantic.Field(alias="playerId")]

    season: int

    week: int

    assisted_tackles: Annotated[
        OptionalNullable[float], pydantic.Field(alias="assistedTackles")
    ] = UNSET

    defense_interceptions: Annotated[
        OptionalNullable[float], pydantic.Field(alias="defenseInterceptions")
    ] = UNSET

    dt_blocked_kicks: Annotated[
        OptionalNullable[float], pydantic.Field(alias="dtBlockedKicks")
    ] = UNSET

    dt_fumbles_forced: Annotated[
        OptionalNullable[float], pydantic.Field(alias="dtFumblesForced")
    ] = UNSET

    dt_fumbles_recovered: Annotated[
        OptionalNullable[float], pydantic.Field(alias="dtFumblesRecovered")
    ] = UNSET

    dt_interceptions: Annotated[
        OptionalNullable[float], pydantic.Field(alias="dtInterceptions")
    ] = UNSET

    dt_kickoff_return_yards: Annotated[
        OptionalNullable[float], pydantic.Field(alias="dtKickoffReturnYards")
    ] = UNSET

    dt_points_allowed: Annotated[
        OptionalNullable[float], pydantic.Field(alias="dtPointsAllowed")
    ] = UNSET

    dt_sacks: Annotated[OptionalNullable[float], pydantic.Field(alias="dtSacks")] = (
        UNSET
    )

    dt_safeties: Annotated[
        OptionalNullable[float], pydantic.Field(alias="dtSafeties")
    ] = UNSET

    dt_touchdowns: Annotated[
        OptionalNullable[float], pydantic.Field(alias="dtTouchdowns")
    ] = UNSET

    dt_yards_allowed: Annotated[
        OptionalNullable[float], pydantic.Field(alias="dtYardsAllowed")
    ] = UNSET

    fg_attempts: Annotated[
        OptionalNullable[float], pydantic.Field(alias="fgAttempts")
    ] = UNSET

    fg_made20to29: Annotated[
        OptionalNullable[float], pydantic.Field(alias="fgMade20to29")
    ] = UNSET

    fg_made30to39: Annotated[
        OptionalNullable[float], pydantic.Field(alias="fgMade30to39")
    ] = UNSET

    fg_made40to49: Annotated[
        OptionalNullable[float], pydantic.Field(alias="fgMade40to49")
    ] = UNSET

    fg_made50: Annotated[OptionalNullable[float], pydantic.Field(alias="fgMade50")] = (
        UNSET
    )

    forced_fumbles: Annotated[
        OptionalNullable[float], pydantic.Field(alias="forcedFumbles")
    ] = UNSET

    fumbles: OptionalNullable[float] = UNSET

    fumbles_lost: Annotated[
        OptionalNullable[float], pydantic.Field(alias="fumblesLost")
    ] = UNSET

    fumbles_recovered: Annotated[
        OptionalNullable[float], pydantic.Field(alias="fumblesRecovered")
    ] = UNSET

    games_played: Annotated[
        OptionalNullable[int], pydantic.Field(alias="gamesPlayed")
    ] = UNSET

    interceptions_thrown: Annotated[
        OptionalNullable[float], pydantic.Field(alias="interceptionsThrown")
    ] = UNSET

    kickoff_return_touchdowns: Annotated[
        OptionalNullable[float], pydantic.Field(alias="kickoffReturnTouchdowns")
    ] = UNSET

    kickoff_return_yards: Annotated[
        OptionalNullable[float], pydantic.Field(alias="kickoffReturnYards")
    ] = UNSET

    pass_defended: Annotated[
        OptionalNullable[float], pydantic.Field(alias="passDefended")
    ] = UNSET

    passing_attempts: Annotated[
        OptionalNullable[float], pydantic.Field(alias="passingAttempts")
    ] = UNSET

    passing_completions: Annotated[
        OptionalNullable[float], pydantic.Field(alias="passingCompletions")
    ] = UNSET

    passing_touchdowns: Annotated[
        OptionalNullable[float], pydantic.Field(alias="passingTouchdowns")
    ] = UNSET

    passing_yards: Annotated[
        OptionalNullable[float], pydantic.Field(alias="passingYards")
    ] = UNSET

    pat_made: Annotated[OptionalNullable[float], pydantic.Field(alias="patMade")] = (
        UNSET
    )

    pat_missed: Annotated[
        OptionalNullable[float], pydantic.Field(alias="patMissed")
    ] = UNSET

    receiving_touchdowns: Annotated[
        OptionalNullable[float], pydantic.Field(alias="receivingTouchdowns")
    ] = UNSET

    receiving_yards: Annotated[
        OptionalNullable[float], pydantic.Field(alias="receivingYards")
    ] = UNSET

    receptions: OptionalNullable[float] = UNSET

    rushing_attempts: Annotated[
        OptionalNullable[float], pydantic.Field(alias="rushingAttempts")
    ] = UNSET

    rushing_touchdowns: Annotated[
        OptionalNullable[float], pydantic.Field(alias="rushingTouchdowns")
    ] = UNSET

    rushing_yards: Annotated[
        OptionalNullable[float], pydantic.Field(alias="rushingYards")
    ] = UNSET

    sacks: OptionalNullable[float] = UNSET

    tackles: OptionalNullable[float] = UNSET


PlayerWeekProjectedStatsType = Literal["player-week-projected-stats",]


class PlayerWeekProjectedStats(BaseModel):
    """Weekly projected statistics for a player."""

    attributes: PlayerWeekProjectedStatsAttributes

    id: str
    r"""Unique identifier for these stats"""

    type: PlayerWeekProjectedStatsType
