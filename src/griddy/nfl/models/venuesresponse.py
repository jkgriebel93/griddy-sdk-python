from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .pagination import Pagination, PaginationTypedDict
from .venue import Venue, VenueTypedDict


class VenuesResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    venues: NotRequired[List[VenueTypedDict]]


class VenuesResponse(BaseModel):
    pagination: Optional[Pagination] = None

    venues: Optional[List[Venue]] = None
