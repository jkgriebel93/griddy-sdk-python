"""Response model for NGS game center overview endpoint."""

from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.ngs_game_overview import (
    NgsGameLeaders,
    NgsGameScheduleInfo,
    NgsPassersOverview,
    NgsPassRushersOverview,
    NgsReceiversOverview,
    NgsRushersOverview,
)
from griddy.nfl.types import BaseModel


class NgsGameCenterOverviewResponse(BaseModel):
    """Response from the NGS game center overview endpoint."""

    schedule: Optional[NgsGameScheduleInfo] = None
    passers: Optional[NgsPassersOverview] = None
    rushers: Optional[NgsRushersOverview] = None
    receivers: Optional[NgsReceiversOverview] = None
    pass_rushers: Annotated[
        Optional[NgsPassRushersOverview], pydantic.Field(alias="passRushers")
    ] = None
    leaders: Optional[NgsGameLeaders] = None
