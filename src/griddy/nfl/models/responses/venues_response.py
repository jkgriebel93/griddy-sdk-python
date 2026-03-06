from __future__ import annotations

from typing import List, Optional

from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.models.entities.venue import Venue
from griddy.nfl.types import BaseModel


class VenuesResponse(BaseModel):
    """Response containing venue information."""

    pagination: Optional[Pagination] = None

    venues: Optional[List[Venue]] = None
