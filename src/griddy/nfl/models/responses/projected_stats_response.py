from __future__ import annotations

from typing import List, Optional, Union

from typing_extensions import TypeAliasType

from griddy.nfl.models.entities.player_projection import PlayerProjection
from griddy.nfl.models.entities.player_week_projected_points import (
    PlayerWeekProjectedPoints,
)
from griddy.nfl.models.entities.player_week_projected_stats import (
    PlayerWeekProjectedStats,
)
from griddy.nfl.types import BaseModel

Included = TypeAliasType(
    "Included", Union[PlayerWeekProjectedPoints, PlayerWeekProjectedStats]
)


class Page(BaseModel):
    number: Optional[int] = None
    r"""Current page number"""

    size: Optional[int] = None
    r"""Page size"""


class Meta(BaseModel):
    page: Optional[Page] = None


class ProjectedStatsResponsePagination(BaseModel):
    token: Optional[str] = None
    r"""Token for next page of results"""


class ProjectedStatsResponse(BaseModel):
    r"""JSON:API formatted response for projected statistics"""

    data: List[PlayerProjection]
    r"""Primary player data with relationships"""

    included: List[Included]
    r"""Related data included in response"""

    meta: Optional[Meta] = None

    pagination: Optional[ProjectedStatsResponsePagination] = None
