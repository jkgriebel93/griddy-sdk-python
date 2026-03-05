from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.team import Team
from griddy.nfl.types import BaseModel


class FootballTeamsResponse(BaseModel):
    teams: List[Team]
    pagination: Pagination
