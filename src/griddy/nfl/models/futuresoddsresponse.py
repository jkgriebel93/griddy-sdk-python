from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel
from .futuresmarket import FuturesMarket, FuturesMarketTypedDict


class FuturesOddsResponseDataTypedDict(TypedDict):
    conference: NotRequired[List[FuturesMarketTypedDict]]
    division: NotRequired[List[FuturesMarketTypedDict]]
    super_bowl: NotRequired[List[FuturesMarketTypedDict]]


class FuturesOddsResponseData(BaseModel):
    conference: Optional[List[FuturesMarket]] = None

    division: Optional[List[FuturesMarket]] = None

    super_bowl: Annotated[
        Optional[List[FuturesMarket]], pydantic.Field(alias="superBowl")
    ] = None


class FuturesOddsResponseTypedDict(TypedDict):
    data: NotRequired[FuturesOddsResponseDataTypedDict]


class FuturesOddsResponse(BaseModel):
    data: Optional[FuturesOddsResponseData] = None
