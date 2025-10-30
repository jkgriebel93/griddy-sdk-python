
from __future__ import annotations
from .pagination import Pagination, PaginationTypedDict
from .venue import Venue, VenueTypedDict
from ..types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class VenuesResponseTypedDict(TypedDict):
    pagination: NotRequired[PaginationTypedDict]
    venues: NotRequired[List[VenueTypedDict]]


class VenuesResponse(BaseModel):
    pagination: Optional[Pagination] = None

    venues: Optional[List[Venue]] = None
