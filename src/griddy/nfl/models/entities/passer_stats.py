from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.utils.unmarshal_json_response import int_to_str

from ...types import BaseModel


class Zone(BaseModel):
    """Passing zone identifier."""

    pass


class PasserStats(BaseModel):
    """Passer statistics by zone and game."""

    attempts: Optional[int] = None

    completions: Optional[int] = None

    game_id: Annotated[
        Optional[str],
        pydantic.Field(alias="gameId"),
        pydantic.BeforeValidator(int_to_str),
    ] = None

    interceptions: Optional[int] = None

    pass_yards: Annotated[Optional[int], pydantic.Field(alias="passYards")] = None

    touchdowns: Optional[int] = None

    zones: Optional[List[Zone]] = None
