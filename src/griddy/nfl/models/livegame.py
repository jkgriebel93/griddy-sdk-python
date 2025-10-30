
from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AwayTeamTypedDict(TypedDict):
    abbreviation: NotRequired[str]
    score: NotRequired[int]
    team_id: NotRequired[str]


class AwayTeam(BaseModel):
    abbreviation: Optional[str] = None

    score: Optional[int] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None


class HomeTeamTypedDict(TypedDict):
    abbreviation: NotRequired[str]
    score: NotRequired[int]
    team_id: NotRequired[str]


class HomeTeam(BaseModel):
    abbreviation: Optional[str] = None

    score: Optional[int] = None

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None


LiveGameStatus = Literal[
    "SCHEDULED",
    "IN_PROGRESS",
    "HALFTIME",
    "FINAL",
    "POSTPONED",
    "CANCELLED",
]


class LiveGameTypedDict(TypedDict):
    r"""Live game scoring and status information"""

    away_team: NotRequired[AwayTeamTypedDict]
    game_id: NotRequired[str]
    r"""Game identifier"""
    home_team: NotRequired[HomeTeamTypedDict]
    last_play: NotRequired[str]
    r"""Description of last play"""
    possession: NotRequired[str]
    r"""Team abbreviation with current possession"""
    quarter: NotRequired[str]
    r"""Current quarter/period"""
    red_zone: NotRequired[bool]
    r"""Whether team is in red zone"""
    status: NotRequired[LiveGameStatus]
    time_remaining: NotRequired[str]
    r"""Time remaining in current period"""


class LiveGame(BaseModel):
    r"""Live game scoring and status information"""

    away_team: Annotated[Optional[AwayTeam], pydantic.Field(alias="awayTeam")] = None

    game_id: Annotated[Optional[str], pydantic.Field(alias="gameId")] = None
    r"""Game identifier"""

    home_team: Annotated[Optional[HomeTeam], pydantic.Field(alias="homeTeam")] = None

    last_play: Annotated[Optional[str], pydantic.Field(alias="lastPlay")] = None
    r"""Description of last play"""

    possession: Optional[str] = None
    r"""Team abbreviation with current possession"""

    quarter: Optional[str] = None
    r"""Current quarter/period"""

    red_zone: Annotated[Optional[bool], pydantic.Field(alias="redZone")] = None
    r"""Whether team is in red zone"""

    status: Optional[LiveGameStatus] = None

    time_remaining: Annotated[Optional[str], pydantic.Field(alias="timeRemaining")] = (
        None
    )
    r"""Time remaining in current period"""
