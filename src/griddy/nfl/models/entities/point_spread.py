from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


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
