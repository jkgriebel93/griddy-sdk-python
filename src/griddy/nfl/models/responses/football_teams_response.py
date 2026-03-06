from typing import List

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.team import Team
from griddy.nfl.types import BaseModel


class FootballTeamsResponse(BaseModel):
    """Response containing football teams."""

    teams: List[Team]
    pagination: Pagination
