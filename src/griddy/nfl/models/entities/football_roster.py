from typing import List

import pydantic
from typing_extensions import Annotated

from griddy.nfl import models
from griddy.nfl.types import BaseModel


class FootballRoster(BaseModel):
    """Player entry within a team roster."""

    season: int
    r"""Season the roster reflects"""
    season_type: Annotated[models.SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Season type"""
    team: models.Team
    r"""Team info"""
    persons: List[models.Person]
    r"""List of players on the team roster"""
