from __future__ import annotations

from typing import Literal

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, Nullable, OptionalNullable


class PlayerWeekProjectedPointsAttributes(BaseModel):
    player_id: Annotated[str, pydantic.Field(alias="playerId")]
    r"""Player SMART ID"""

    season: int
    r"""Season year"""

    settings_code: Annotated[str, pydantic.Field(alias="settingsCode")]
    r"""Fantasy settings code"""

    week: int
    r"""Week number"""

    points: OptionalNullable[float] = UNSET
    r"""Projected fantasy points"""


PlayerWeekProjectedPointsType = Literal["player-week-projected-points",]


class PlayerWeekProjectedPoints(BaseModel):
    attributes: PlayerWeekProjectedPointsAttributes

    id: str
    r"""Unique identifier for this projection"""

    type: PlayerWeekProjectedPointsType
