from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .season_type_enum import SeasonTypeEnum
from .team_info import TeamInfo, TeamInfoTypedDict
from .weekly_player import WeeklyPlayer, WeeklyPlayerTypedDict


class WeeklyRosterResponseTypedDict(TypedDict):
    season: NotRequired[int]
    r"""Season year"""
    season_type: NotRequired[SeasonTypeEnum]
    r"""Type of NFL season"""
    team: NotRequired[TeamInfoTypedDict]
    r"""Basic team information included in roster responses"""
    team_players: NotRequired[List[WeeklyPlayerTypedDict]]
    week: NotRequired[int]
    r"""Week number"""


class WeeklyRosterResponse(BaseModel):
    season: Optional[int] = None
    r"""Season year"""

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    team: Optional[TeamInfo] = None
    r"""Basic team information included in roster responses"""

    team_players: Annotated[
        Optional[List[WeeklyPlayer]], pydantic.Field(alias="teamPlayers")
    ] = None

    week: Optional[int] = None
    r"""Week number"""
