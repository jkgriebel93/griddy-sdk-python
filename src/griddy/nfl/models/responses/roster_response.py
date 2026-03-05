from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.player import Player
from griddy.nfl.models.entities.team import Team
from griddy.nfl.types import BaseModel


class Roster(BaseModel):
    defense: Optional[List[Player]] = None

    injured_reserve: Annotated[
        Optional[List[Player]], pydantic.Field(alias="injuredReserve")
    ] = None

    offense: Optional[List[Player]] = None

    practice_squad: Annotated[
        Optional[List[Player]], pydantic.Field(alias="practiceSquad")
    ] = None

    special_teams: Annotated[
        Optional[List[Player]], pydantic.Field(alias="specialTeams")
    ] = None


class RosterResponse(BaseModel):
    roster: Optional[Roster] = None

    season: Optional[int] = None

    team: Optional[Team] = None
