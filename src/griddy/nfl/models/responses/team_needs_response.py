from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.entities.pagination import Pagination, PaginationTypedDict
from griddy.nfl.models.entities.team_needs import TeamNeeds, TeamNeedsTypedDict
from griddy.nfl.types import BaseModel


class TeamNeedsResponseTypedDict(TypedDict):
    teams: List[TeamNeedsTypedDict]
    r"""List of teams along with their needs analysis"""
    pagination: NotRequired[PaginationTypedDict]
    r"""Pagination information"""


class TeamNeedsResponse(BaseModel):
    teams: List[TeamNeeds]
    r"""List of teams along with their needs analysis"""
    pagination: Optional[Pagination]
    r"""Pagination information"""
