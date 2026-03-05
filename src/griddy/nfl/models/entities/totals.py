from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class Totals(BaseModel):
    r"""Over/Under (totals) betting odds"""

    over_handicap: Annotated[Optional[float], pydantic.Field(alias="overHandicap")] = (
        None
    )
    r"""Total points line for over"""

    over_price: Annotated[Optional[int], pydantic.Field(alias="overPrice")] = None
    r"""Over odds (American format)"""

    under_handicap: Annotated[
        Optional[float], pydantic.Field(alias="underHandicap")
    ] = None
    r"""Total points line for under"""

    under_price: Annotated[Optional[int], pydantic.Field(alias="underPrice")] = None
    r"""Under odds (American format)"""
