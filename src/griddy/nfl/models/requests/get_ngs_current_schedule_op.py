"""Request model for NGS current schedule endpoint."""

from __future__ import annotations

from griddy.nfl.types import BaseModel


class GetNgsCurrentScheduleRequest(BaseModel):
    """Request model for getting the current NGS schedule.

    This endpoint takes no parameters.
    """

    pass
