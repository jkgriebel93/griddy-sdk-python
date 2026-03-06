from __future__ import annotations

from typing import List

from griddy.nfl.models.entities.film_room_play import FilmroomPlay
from griddy.nfl.types import BaseModel


class FilmroomPlaysResponse(BaseModel):
    """Response containing Film Room plays."""

    count: int
    r"""Total number of plays matching the filter criteria"""

    plays: List[FilmroomPlay]
    r"""Array of play data matching the filter criteria"""
