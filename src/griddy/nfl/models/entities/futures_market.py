from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, OptionalNullable
from .odds_selection import OddsSelection


class Fixture(BaseModel):
    r"""Associated fixture information"""


class FuturesMarket(BaseModel):
    fixture: OptionalNullable[Fixture] = UNSET
    r"""Associated fixture information"""

    fixture_id: Annotated[OptionalNullable[str], pydantic.Field(alias="fixtureId")] = (
        UNSET
    )
    r"""Associated fixture ID if applicable"""

    hierarchy: Optional[str] = None
    r"""Full betting hierarchy path"""

    is_available: Annotated[Optional[bool], pydantic.Field(alias="isAvailable")] = None
    r"""Whether market is currently available"""

    is_suspended: Annotated[Optional[bool], pydantic.Field(alias="isSuspended")] = None
    r"""Whether market is currently suspended"""

    name: Optional[str] = None
    r"""Market name (e.g., \"Winner\", \"Division Winner\")"""

    selections: Optional[List[OddsSelection]] = None

    source_id: Annotated[Optional[str], pydantic.Field(alias="sourceId")] = None
    r"""Source identifier for the market"""
