from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.utils.unmarshal_json_response import int_to_str

from ...types import BaseModel


class ZoneTypedDict(TypedDict):
    pass


class Zone(BaseModel):
    pass


class PasserStatsTypedDict(TypedDict):
    attempts: NotRequired[int]
    completions: NotRequired[int]
    game_id: NotRequired[str]
    interceptions: NotRequired[int]
    pass_yards: NotRequired[int]
    touchdowns: NotRequired[int]
    zones: NotRequired[List[ZoneTypedDict]]


class PasserStats(BaseModel):
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
