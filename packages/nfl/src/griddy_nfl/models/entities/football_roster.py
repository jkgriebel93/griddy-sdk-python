from typing import List

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy_nfl import models
from griddy_nfl.types import BaseModel


class FootballRosterTypedDict(TypedDict):
    season: int
    r"""Season the roster reflects"""
    season_type: models.SeasonTypeEnum
    r"""Season type"""
    team: models.TeamTypedDict
    r"""Team info"""
    persons: List[models.PersonTypedDict]
    r"""List of players on the team roster"""


class FootballRoster(BaseModel):
    season: int
    r"""Season the roster reflects"""
    season_type: Annotated[models.SeasonTypeEnum, pydantic.Field(alias="seasonType")]
    r"""Season type"""
    team: models.Team
    r"""Team info"""
    persons: List[models.Person]
    r"""List of players on the team roster"""
