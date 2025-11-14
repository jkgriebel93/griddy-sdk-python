from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.player import Player, PlayerTypedDict
from griddy.nfl.models.team import Team, TeamTypedDict
from griddy.nfl.types import BaseModel


class PlayerStatsResponsePaginationTypedDict(TypedDict):
    limit: NotRequired[int]
    offset: NotRequired[int]
    total: NotRequired[int]


class PlayerStatsResponsePagination(BaseModel):
    limit: Optional[int] = None

    offset: Optional[int] = None

    total: Optional[int] = None


class PlayerStatsResponseStatsTypedDict(TypedDict):
    r"""Statistics object varies by category"""


class PlayerStatsResponseStats(BaseModel):
    r"""Statistics object varies by category"""


class PlayerStatsResponsePlayerTypedDict(TypedDict):
    player: NotRequired[PlayerTypedDict]
    stats: NotRequired[PlayerStatsResponseStatsTypedDict]
    r"""Statistics object varies by category"""
    team: NotRequired[TeamTypedDict]


class PlayerStatsResponsePlayer(BaseModel):
    player: Optional[Player] = None

    stats: Optional[PlayerStatsResponseStats] = None
    r"""Statistics object varies by category"""

    team: Optional[Team] = None


class PlayerStatsResponseTypedDict(TypedDict):
    pagination: NotRequired[PlayerStatsResponsePaginationTypedDict]
    players: NotRequired[List[PlayerStatsResponsePlayerTypedDict]]
    season: NotRequired[int]
    season_type: NotRequired[str]
    stat_category: NotRequired[str]


class PlayerStatsResponse(BaseModel):
    pagination: Optional[PlayerStatsResponsePagination] = None

    players: Optional[List[PlayerStatsResponsePlayer]] = None

    season: Optional[int] = None

    season_type: Annotated[Optional[str], pydantic.Field(alias="seasonType")] = None

    stat_category: Annotated[Optional[str], pydantic.Field(alias="statCategory")] = None
