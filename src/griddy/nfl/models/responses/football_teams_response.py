from typing import List

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.team import Team
from griddy.nfl.types import BaseModel


class FootballTeamsResponse(BaseModel):
    teams: List[Team]
    pagination: Pagination
