from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.standings import Standings
from griddy.nfl.models.enums.season_type_enum import SeasonTypeEnum
from griddy.nfl.types import BaseModel


class StandingsResponseWeek(BaseModel):
    """Week metadata within a standings response."""

    standings: Optional[List[Standings]] = None

    week: Optional[int] = None


class StandingsResponse(BaseModel):
    """Response containing standings data."""

    pagination: Optional[Pagination] = None

    season: Optional[int] = None

    season_type: Annotated[
        Optional[SeasonTypeEnum], pydantic.Field(alias="seasonType")
    ] = None
    r"""Type of NFL season"""

    week: Optional[int] = None
    r"""Current week for standings"""

    weeks: Optional[List[StandingsResponseWeek]] = None
