from __future__ import annotations

from typing import List

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetWinProbabilityMinRequest(BaseModel):
    """Request parameters for fetching minute-level win probability."""

    fapi_game_id: Annotated[
        List[str],
        pydantic.Field(alias="fapiGameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Football API game identifiers (UUID format). Supports multiple game IDs
    to retrieve win probability data for multiple games simultaneously.

    """
