from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PointSpreadTypedDict(TypedDict):
    r"""Point spread betting odds"""

    away_handicap: NotRequired[str]
    r"""Away team point spread"""
    away_price: NotRequired[str]
    r"""Away team spread odds (American format)"""
    home_handicap: NotRequired[str]
    r"""Home team point spread"""
    home_price: NotRequired[str]
    r"""Home team spread odds (American format)"""


class PointSpread(BaseModel):
    r"""Point spread betting odds"""

    away_handicap: Annotated[Optional[str], pydantic.Field(alias="awayHandicap")] = None
    r"""Away team point spread"""

    away_price: Annotated[Optional[str], pydantic.Field(alias="awayPrice")] = None
    r"""Away team spread odds (American format)"""

    home_handicap: Annotated[Optional[str], pydantic.Field(alias="homeHandicap")] = None
    r"""Home team point spread"""

    home_price: Annotated[Optional[str], pydantic.Field(alias="homePrice")] = None
    r"""Home team spread odds (American format)"""
