from typing import List, Optional

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.team_needs import TeamNeeds
from griddy.nfl.types import BaseModel


class TeamNeedsResponse(BaseModel):
    """Response containing team draft needs."""

    teams: List[TeamNeeds]
    r"""List of teams along with their needs analysis"""
    pagination: Optional[Pagination]
    r"""Pagination information"""
