from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.futures_market import FuturesMarket
from griddy.nfl.types import BaseModel


class FuturesOddsResponseData(BaseModel):
    """Futures odds data grouped by market."""

    conference: Optional[List[FuturesMarket]] = None

    division: Optional[List[FuturesMarket]] = None

    super_bowl: Annotated[
        Optional[List[FuturesMarket]], pydantic.Field(alias="superBowl")
    ] = None


class FuturesOddsResponse(BaseModel):
    """Response containing futures betting odds."""

    data: Optional[FuturesOddsResponseData] = None
