from __future__ import annotations

from typing import List, Optional

from griddy.nfl.models.entities.coaches_film_video import (
    CoachesFilmVideo,
)
from griddy.nfl.models.entities.pagination import Pagination
from griddy.nfl.types import BaseModel

from ..response_metadata import ResponseMetadata


class CoachesFilmResponse(BaseModel):
    items: List[CoachesFilmVideo]

    metadata: ResponseMetadata

    pagination: Optional[Pagination] = None
