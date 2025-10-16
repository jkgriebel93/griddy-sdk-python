from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from ..types import BaseModel


class MoneyLineTypedDict(TypedDict):
    r"""Money line betting odds"""

    away_price: NotRequired[str]
    r"""Away team money line odds (American format)"""
    home_price: NotRequired[str]
    r"""Home team money line odds (American format)"""


class MoneyLine(BaseModel):
    r"""Money line betting odds"""

    away_price: Annotated[Optional[str], pydantic.Field(alias="awayPrice")] = None
    r"""Away team money line odds (American format)"""

    home_price: Annotated[Optional[str], pydantic.Field(alias="homePrice")] = None
    r"""Home team money line odds (American format)"""
