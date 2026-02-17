from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy_nfl.models.entities.pagination import Pagination, PaginationTypedDict
from griddy_nfl.models.entities.venue import Venue, VenueTypedDict
from griddy_nfl.types import BaseModel


class VenuesResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    venues: NotRequired[List[VenueTypedDict]]


class VenuesResponse(BaseModel):
    pagination: Optional[Pagination] = None

    venues: Optional[List[Venue]] = None
