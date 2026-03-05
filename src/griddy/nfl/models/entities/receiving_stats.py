from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class ReceivingStats(BaseModel):
    drops: Optional[int] = None

    long_reception: Annotated[Optional[int], pydantic.Field(alias="longReception")] = (
        None
    )

    receptions: Optional[int] = None

    targets: Optional[int] = None

    touchdowns: Optional[int] = None

    yards: Optional[int] = None

    yards_per_reception: Annotated[
        Optional[float], pydantic.Field(alias="yardsPerReception")
    ] = None
