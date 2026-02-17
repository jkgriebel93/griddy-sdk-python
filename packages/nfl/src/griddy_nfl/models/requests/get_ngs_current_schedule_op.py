"""Request model for NGS current schedule endpoint."""

from __future__ import annotations

from typing_extensions import TypedDict

from griddy_nfl.types import BaseModel


class GetNgsCurrentScheduleRequestTypedDict(TypedDict):
    """Request parameters for getting the current NGS schedule.

    This endpoint takes no parameters.
    """

    pass


class GetNgsCurrentScheduleRequest(BaseModel):
    """Request model for getting the current NGS schedule.

    This endpoint takes no parameters.
    """

    pass
