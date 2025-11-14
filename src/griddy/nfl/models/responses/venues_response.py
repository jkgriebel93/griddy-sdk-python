from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy.nfl.models.pagination import Pagination, PaginationTypedDict
from griddy.nfl.models.venue import Venue, VenueTypedDict
from griddy.nfl.types import BaseModel


class VenuesResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    venues: NotRequired[List[VenueTypedDict]]


class VenuesResponse(BaseModel):
    pagination: Optional[Pagination] = None

    venues: Optional[List[Venue]] = None
