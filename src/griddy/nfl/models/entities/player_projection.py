from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel

RelationshipsTypePlayerWeekProjectedPoints = Literal["player-week-projected-points",]


class WeekPoint(BaseModel):
    """Projected fantasy points for a single week."""

    id: Optional[str] = None
    r"""Reference to projected points"""

    type: Optional[RelationshipsTypePlayerWeekProjectedPoints] = None


RelationshipsTypePlayerWeekProjectedStats = Literal["player-week-projected-stats",]


class WeekStat(BaseModel):
    """Projected statistical output for a single week."""

    id: Optional[str] = None
    r"""Reference to projected stats"""

    type: Optional[RelationshipsTypePlayerWeekProjectedStats] = None


class Relationships(BaseModel):
    """Related entities for a player projection."""

    week_points: Annotated[
        Optional[List[WeekPoint]], pydantic.Field(alias="weekPoints")
    ] = None

    week_stats: Annotated[
        Optional[List[WeekStat]], pydantic.Field(alias="weekStats")
    ] = None


TypePlayer = Literal["player",]
r"""Resource type"""


class PlayerProjection(BaseModel):
    """Fantasy projection data for a player."""

    id: str
    r"""Player SMART ID"""

    relationships: Relationships

    type: TypePlayer
    r"""Resource type"""
