from __future__ import annotations

from typing import List, Optional

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.types import BaseModel


class GameStatsResponseData(BaseModel):
    r"""Game statistics data"""


class GameStatsResponse(BaseModel):
    data: Optional[List[GameStatsResponseData]] = None

    pagination: Optional[Pagination] = None
