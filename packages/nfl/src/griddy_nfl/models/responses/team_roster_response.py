from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.player import Player, PlayerTypedDict
from griddy_nfl.models.entities.team_info import TeamInfo, TeamInfoTypedDict
from griddy_nfl.types import BaseModel


class TeamRosterResponseTypedDict(TypedDict):
    season: NotRequired[int]
    r"""Season year"""
    team: NotRequired[TeamInfoTypedDict]
    r"""Basic team information included in roster responses"""
    team_players: NotRequired[List[PlayerTypedDict]]


class TeamRosterResponse(BaseModel):
    season: Optional[int] = None
    r"""Season year"""

    team: Optional[TeamInfo] = None
    r"""Basic team information included in roster responses"""

    team_players: Annotated[
        Optional[List[Player]], pydantic.Field(alias="teamPlayers")
    ] = None
