from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.team_info import TeamInfo
from griddy.nfl.models.entities.weekly_player import WeeklyPlayer
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel


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
