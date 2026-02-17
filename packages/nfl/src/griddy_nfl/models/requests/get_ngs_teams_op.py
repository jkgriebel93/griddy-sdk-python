"""Request model for NGS teams endpoint."""

from __future__ import annotations

from typing_extensions import TypedDict

from griddy_nfl.types import BaseModel


class GetNgsTeamsRequestTypedDict(TypedDict):
    """Request parameters for getting NGS teams.

    This endpoint takes no parameters.
    """

    pass


class GetNgsTeamsRequest(BaseModel):
    """Request model for getting NGS teams.

    This endpoint takes no parameters.
    """

    pass
