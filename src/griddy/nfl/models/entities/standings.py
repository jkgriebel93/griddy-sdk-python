from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel
from .clinched import Clinched
from .overall_record import OverallRecord
from .points_record import PointsRecord
from .record import Record
from .standings_record import StandingsRecord


class StandingsTeam(BaseModel):
    current_logo: Annotated[Optional[str], pydantic.Field(alias="currentLogo")] = None

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None

    id: Optional[str] = None


class Standings(BaseModel):
    clinched: Optional[Clinched] = None

    close_games: Annotated[Optional[Record], pydantic.Field(alias="closeGames")] = None

    conference: Optional[StandingsRecord] = None

    division: Optional[StandingsRecord] = None

    home: Optional[PointsRecord] = None

    last5: Optional[PointsRecord] = None

    overall: Optional[OverallRecord] = None

    road: Optional[PointsRecord] = None

    team: Optional[StandingsTeam] = None
