"""Request model for NGS teams endpoint."""

from __future__ import annotations

from griddy.nfl.types import BaseModel


class GetNgsTeamsRequest(BaseModel):
    """Request model for getting NGS teams.

    This endpoint takes no parameters.
    """

    pass
