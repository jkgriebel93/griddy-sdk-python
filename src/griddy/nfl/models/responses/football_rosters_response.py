from typing import List

from griddy.nfl import models
from griddy.nfl.types import BaseModel


class FootballRostersResponse(BaseModel):
    rosters: List[models.FootballRoster]
    pagination: models.Pagination
