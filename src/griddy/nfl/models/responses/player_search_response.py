from __future__ import annotations

from typing import List

from griddy.nfl.models.entities.player_search_result import PlayerSearchResult
from griddy.nfl.types import BaseModel


class PlayerSearchResponse(BaseModel):
    """Response containing player search results."""

    players: List[PlayerSearchResult]
    r"""Array of players matching search criteria"""

    term: str
    r"""Search term used"""
