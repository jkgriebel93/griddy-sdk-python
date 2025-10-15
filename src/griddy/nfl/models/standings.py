from __future__ import annotations
from .clinched import Clinched, ClinchedTypedDict
from .overallrecord import OverallRecord, OverallRecordTypedDict
from .pointsrecord import PointsRecord, PointsRecordTypedDict
from .record import Record, RecordTypedDict
from .standingsrecord import StandingsRecord, StandingsRecordTypedDict
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class StandingsTeamTypedDict(TypedDict):
    current_logo: NotRequired[str]
    full_name: NotRequired[str]
    id: NotRequired[str]


class StandingsTeam(BaseModel):
    current_logo: Annotated[Optional[str], pydantic.Field(alias="currentLogo")] = None

    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None

    id: Optional[str] = None


class StandingsTypedDict(TypedDict):
    clinched: NotRequired[ClinchedTypedDict]
    close_games: NotRequired[RecordTypedDict]
    conference: NotRequired[StandingsRecordTypedDict]
    division: NotRequired[StandingsRecordTypedDict]
    home: NotRequired[PointsRecordTypedDict]
    last5: NotRequired[PointsRecordTypedDict]
    overall: NotRequired[OverallRecordTypedDict]
    road: NotRequired[PointsRecordTypedDict]
    team: NotRequired[StandingsTeamTypedDict]


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
