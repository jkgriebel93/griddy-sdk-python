from __future__ import annotations

from typing import List, Optional

from typing_extensions import NotRequired, TypedDict

from griddy_nfl.models.entities.coaches_film_video import (
    CoachesFilmVideo,
    CoachesFilmVideoTypedDict,
)
from griddy_nfl.models.entities.pagination import Pagination, PaginationTypedDict
from griddy_nfl.types import BaseModel

from ..response_metadata import ResponseMetadata, ResponseMetadataTypedDict


class CoachesFilmResponseTypedDict(TypedDict):
    items: List[CoachesFilmVideoTypedDict]
    metadata: ResponseMetadataTypedDict
    pagination: NotRequired[PaginationTypedDict]


class CoachesFilmResponse(BaseModel):
    items: List[CoachesFilmVideo]

    metadata: ResponseMetadata

    pagination: Optional[Pagination] = None
