from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel
from .coachesfilmvideo import CoachesFilmVideo, CoachesFilmVideoTypedDict
from .pagination import Pagination, PaginationTypedDict
from .responsemetadata import ResponseMetadata, ResponseMetadataTypedDict


class CoachesFilmResponseTypedDict(TypedDict):
    items: List[CoachesFilmVideoTypedDict]
    metadata: ResponseMetadataTypedDict
    pagination: NotRequired[PaginationTypedDict]


class CoachesFilmResponse(BaseModel):
    items: List[CoachesFilmVideo]

    metadata: ResponseMetadata

    pagination: Optional[Pagination] = None
