from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.pagination import Pagination, PaginationTypedDict
from griddy.nfl.models.team import Team, TeamTypedDict
from griddy.nfl.types import BaseModel


class FootballTeamsResponseTypedDict(TypedDict):
    teams: List[TeamTypedDict]
    r"""List of teams"""
    pagination: PaginationTypedDict
    r"""Pagination information"""


class FootballTeamsResponse(BaseModel):
    teams: List[Team]
    pagination: Pagination
