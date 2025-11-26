from __future__ import annotations

from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl.models.enums.play_type_enum import PlayTypeEnum
from griddy.nfl.types import BaseModel
from griddy.nfl.utils.unmarshal_json_response import int_to_str

from .penalty import Penalty, PenaltyTypedDict
from .play_participant import PlayParticipant, PlayParticipantTypedDict


class PlayTypedDict(TypedDict):
    description: NotRequired[str]
    distance: NotRequired[int]
    down: NotRequired[int]
    game_clock: NotRequired[str]
    penalties: NotRequired[List[PenaltyTypedDict]]
    play_id: NotRequired[str]
    play_number: NotRequired[int]
    play_type: NotRequired[PlayTypeEnum]
    players: NotRequired[List[PlayParticipantTypedDict]]
    quarter: NotRequired[int]
    result: NotRequired[str]
    yard_line: NotRequired[str]
    yards_gained: NotRequired[int]


class Play(BaseModel):
    description: Optional[str] = None

    distance: Optional[int] = None

    down: Optional[int] = None

    game_clock: Annotated[Optional[str], pydantic.Field(alias="gameClock")] = None

    penalties: Optional[List[Penalty]] = None

    play_id: Annotated[
        Optional[str],
        pydantic.Field(alias="playId"),
        pydantic.BeforeValidator(int_to_str),
    ] = None

    play_number: Annotated[Optional[int], pydantic.Field(alias="playNumber")] = None

    play_type: Annotated[Optional[PlayTypeEnum], pydantic.Field(alias="playType")] = (
        None
    )

    players: Optional[List[PlayParticipant]] = None

    quarter: Optional[int] = None

    result: Optional[str] = None

    yard_line: Annotated[Optional[str], pydantic.Field(alias="yardLine")] = None

    yards_gained: Annotated[Optional[int], pydantic.Field(alias="yardsGained")] = None
