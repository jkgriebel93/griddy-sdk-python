from __future__ import annotations

from typing import List

from typing_extensions import TypedDict

from griddy_nfl.models.entities.player_search_result import (
    PlayerSearchResult,
    PlayerSearchResultTypedDict,
)
from griddy_nfl.types import BaseModel


class PlayerSearchResponseTypedDict(TypedDict):
    players: List[PlayerSearchResultTypedDict]
    r"""Array of players matching search criteria"""
    term: str
    r"""Search term used"""


class PlayerSearchResponse(BaseModel):
    players: List[PlayerSearchResult]
    r"""Array of players matching search criteria"""

    term: str
    r"""Search term used"""
