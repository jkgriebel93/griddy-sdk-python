from __future__ import annotations

from typing import List, Optional

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.week import Week
from griddy.nfl.types import BaseModel


class SeasonWeeksResponse(BaseModel):
    """Response containing season week data."""

    pagination: Optional[Pagination] = None

    season: Optional[str] = None
    r"""Season year"""

    weeks: Optional[List[Week]] = None
