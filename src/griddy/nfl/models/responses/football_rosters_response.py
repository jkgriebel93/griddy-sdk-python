from typing import List

from griddy.nfl import models
from griddy.nfl.types import BaseModel


class FootballRostersResponse(BaseModel):
    """Response containing football rosters."""

    rosters: List[models.FootballRoster]
    pagination: models.Pagination
