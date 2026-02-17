"""Response model for NGS game center overview endpoint."""

from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.ngs_game_overview import (
    NgsGameLeaders,
    NgsGameLeadersTypedDict,
    NgsGameScheduleInfo,
    NgsGameScheduleInfoTypedDict,
    NgsPassersOverview,
    NgsPassersOverviewTypedDict,
    NgsPassRushersOverview,
    NgsPassRushersOverviewTypedDict,
    NgsReceiversOverview,
    NgsReceiversOverviewTypedDict,
    NgsRushersOverview,
    NgsRushersOverviewTypedDict,
)
from griddy_nfl.types import BaseModel


class NgsGameCenterOverviewResponseTypedDict(TypedDict):
    """Response from the NGS game center overview endpoint."""

    schedule: NotRequired[NgsGameScheduleInfoTypedDict]
    passers: NotRequired[NgsPassersOverviewTypedDict]
    rushers: NotRequired[NgsRushersOverviewTypedDict]
    receivers: NotRequired[NgsReceiversOverviewTypedDict]
    pass_rushers: NotRequired[NgsPassRushersOverviewTypedDict]
    leaders: NotRequired[NgsGameLeadersTypedDict]


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
