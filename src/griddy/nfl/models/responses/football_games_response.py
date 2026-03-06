from __future__ import annotations

from typing import List, Optional

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.weekly_game_detail import WeeklyGameDetail
from griddy.nfl.types import BaseModel


class FootballGamesResponse(BaseModel):
    games: Optional[List[WeeklyGameDetail]] = None

    pagination: Optional[Pagination] = None
