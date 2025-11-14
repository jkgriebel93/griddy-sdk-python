from __future__ import annotations

from typing import Literal

import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import UNSET, UNSET_SENTINEL, BaseModel, Nullable, OptionalNullable


class PlayerWeekProjectedStatsAttributesTypedDict(TypedDict):
    player_id: str
    season: int
    week: int
    assisted_tackles: NotRequired[Nullable[float]]
    defense_interceptions: NotRequired[Nullable[float]]
    dt_blocked_kicks: NotRequired[Nullable[float]]
    dt_fumbles_forced: NotRequired[Nullable[float]]
    dt_fumbles_recovered: NotRequired[Nullable[float]]
    dt_interceptions: NotRequired[Nullable[float]]
    dt_kickoff_return_yards: NotRequired[Nullable[float]]
    dt_points_allowed: NotRequired[Nullable[float]]
    dt_sacks: NotRequired[Nullable[float]]
    dt_safeties: NotRequired[Nullable[float]]
    dt_touchdowns: NotRequired[Nullable[float]]
    dt_yards_allowed: NotRequired[Nullable[float]]
    fg_attempts: NotRequired[Nullable[float]]
    fg_made20to29: NotRequired[Nullable[float]]
    fg_made30to39: NotRequired[Nullable[float]]
    fg_made40to49: NotRequired[Nullable[float]]
    fg_made50: NotRequired[Nullable[float]]
    forced_fumbles: NotRequired[Nullable[float]]
    fumbles: NotRequired[Nullable[float]]
    fumbles_lost: NotRequired[Nullable[float]]
    fumbles_recovered: NotRequired[Nullable[float]]
    games_played: NotRequired[Nullable[int]]
    interceptions_thrown: NotRequired[Nullable[float]]
    kickoff_return_touchdowns: NotRequired[Nullable[float]]
    kickoff_return_yards: NotRequired[Nullable[float]]
    pass_defended: NotRequired[Nullable[float]]
    passing_attempts: NotRequired[Nullable[float]]
    passing_completions: NotRequired[Nullable[float]]
    passing_touchdowns: NotRequired[Nullable[float]]
    passing_yards: NotRequired[Nullable[float]]
    pat_made: NotRequired[Nullable[float]]
    pat_missed: NotRequired[Nullable[float]]
    receiving_touchdowns: NotRequired[Nullable[float]]
    receiving_yards: NotRequired[Nullable[float]]
    receptions: NotRequired[Nullable[float]]
    rushing_attempts: NotRequired[Nullable[float]]
    rushing_touchdowns: NotRequired[Nullable[float]]
    rushing_yards: NotRequired[Nullable[float]]
    sacks: NotRequired[Nullable[float]]
    tackles: NotRequired[Nullable[float]]


class PlayerWeekProjectedStatsAttributes(BaseModel):
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

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "assistedTackles",
            "defenseInterceptions",
            "dtBlockedKicks",
            "dtFumblesForced",
            "dtFumblesRecovered",
            "dtInterceptions",
            "dtKickoffReturnYards",
            "dtPointsAllowed",
            "dtSacks",
            "dtSafeties",
            "dtTouchdowns",
            "dtYardsAllowed",
            "fgAttempts",
            "fgMade20to29",
            "fgMade30to39",
            "fgMade40to49",
            "fgMade50",
            "forcedFumbles",
            "fumbles",
            "fumblesLost",
            "fumblesRecovered",
            "gamesPlayed",
            "interceptionsThrown",
            "kickoffReturnTouchdowns",
            "kickoffReturnYards",
            "passDefended",
            "passingAttempts",
            "passingCompletions",
            "passingTouchdowns",
            "passingYards",
            "patMade",
            "patMissed",
            "receivingTouchdowns",
            "receivingYards",
            "receptions",
            "rushingAttempts",
            "rushingTouchdowns",
            "rushingYards",
            "sacks",
            "tackles",
        ]
        nullable_fields = [
            "assistedTackles",
            "defenseInterceptions",
            "dtBlockedKicks",
            "dtFumblesForced",
            "dtFumblesRecovered",
            "dtInterceptions",
            "dtKickoffReturnYards",
            "dtPointsAllowed",
            "dtSacks",
            "dtSafeties",
            "dtTouchdowns",
            "dtYardsAllowed",
            "fgAttempts",
            "fgMade20to29",
            "fgMade30to39",
            "fgMade40to49",
            "fgMade50",
            "forcedFumbles",
            "fumbles",
            "fumblesLost",
            "fumblesRecovered",
            "gamesPlayed",
            "interceptionsThrown",
            "kickoffReturnTouchdowns",
            "kickoffReturnYards",
            "passDefended",
            "passingAttempts",
            "passingCompletions",
            "passingTouchdowns",
            "passingYards",
            "patMade",
            "patMissed",
            "receivingTouchdowns",
            "receivingYards",
            "receptions",
            "rushingAttempts",
            "rushingTouchdowns",
            "rushingYards",
            "sacks",
            "tackles",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(n)  # FIX: Use field name, not alias
            serialized.pop(n, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


PlayerWeekProjectedStatsType = Literal["player-week-projected-stats",]


class PlayerWeekProjectedStatsTypedDict(TypedDict):
    attributes: PlayerWeekProjectedStatsAttributesTypedDict
    id: str
    r"""Unique identifier for these stats"""
    type: PlayerWeekProjectedStatsType


class PlayerWeekProjectedStats(BaseModel):
    attributes: PlayerWeekProjectedStatsAttributes

    id: str
    r"""Unique identifier for these stats"""

    type: PlayerWeekProjectedStatsType
