from __future__ import annotations

from typing import List, Optional

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.pro_week import ProWeek
from griddy.nfl.types import BaseModel


class WeeksResponse(BaseModel):
    """Response containing weeks data."""

    pagination: Optional[Pagination] = None

    weeks: Optional[List[ProWeek]] = None
