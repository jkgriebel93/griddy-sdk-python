from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.player import Player
from griddy.nfl.models.entities.team_info import TeamInfo
from griddy.nfl.types import BaseModel


class TeamRosterResponse(BaseModel):
    season: Optional[int] = None
    r"""Season year"""

    team: Optional[TeamInfo] = None
    r"""Basic team information included in roster responses"""

    team_players: Annotated[
        Optional[List[Player]], pydantic.Field(alias="teamPlayers")
    ] = None
