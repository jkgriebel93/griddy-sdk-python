from typing import List

from typing_extensions import TypedDict

from griddy_nfl import models
from griddy_nfl.types import BaseModel


class FootballRostersResponseTypedDict(TypedDict):
    rosters: List[models.FootballRosterTypedDict]
    pagination: models.PaginationTypedDict


class FootballRostersResponse(BaseModel):
    rosters: List[models.FootballRoster]
    pagination: models.Pagination
