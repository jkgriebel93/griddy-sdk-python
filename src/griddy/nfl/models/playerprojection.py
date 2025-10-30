
from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import List, Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


RelationshipsTypePlayerWeekProjectedPoints = Literal["player-week-projected-points",]


class WeekPointTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Reference to projected points"""
    type: NotRequired[RelationshipsTypePlayerWeekProjectedPoints]


class WeekPoint(BaseModel):
    id: Optional[str] = None
    r"""Reference to projected points"""

    type: Optional[RelationshipsTypePlayerWeekProjectedPoints] = None


RelationshipsTypePlayerWeekProjectedStats = Literal["player-week-projected-stats",]


class WeekStatTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Reference to projected stats"""
    type: NotRequired[RelationshipsTypePlayerWeekProjectedStats]


class WeekStat(BaseModel):
    id: Optional[str] = None
    r"""Reference to projected stats"""

    type: Optional[RelationshipsTypePlayerWeekProjectedStats] = None


class RelationshipsTypedDict(TypedDict):
    week_points: NotRequired[List[WeekPointTypedDict]]
    week_stats: NotRequired[List[WeekStatTypedDict]]


class Relationships(BaseModel):
    week_points: Annotated[
        Optional[List[WeekPoint]], pydantic.Field(alias="weekPoints")
    ] = None

    week_stats: Annotated[
        Optional[List[WeekStat]], pydantic.Field(alias="weekStats")
    ] = None


TypePlayer = Literal["player",]
r"""Resource type"""


class PlayerProjectionTypedDict(TypedDict):
    id: str
    r"""Player SMART ID"""
    relationships: RelationshipsTypedDict
    type: TypePlayer
    r"""Resource type"""


class PlayerProjection(BaseModel):
    id: str
    r"""Player SMART ID"""

    relationships: Relationships

    type: TypePlayer
    r"""Resource type"""
