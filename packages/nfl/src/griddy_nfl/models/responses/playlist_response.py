from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.pro_play import ProPlay, ProPlayTypedDict
from griddy_nfl.types import BaseModel
from griddy_nfl.utils.unmarshal_json_response import int_to_str


class PlaylistResponseTypedDict(TypedDict):
    game_id: str
    r"""Ten digit game ID"""
    game_key: int
    r"""Another ID looking value, not sure what it is."""
    plays: List[ProPlayTypedDict]


class PlaylistResponse(BaseModel):
    game_id: Annotated[
        Optional[str],
        pydantic.Field(alias="gameId"),
        pydantic.BeforeValidator(int_to_str),
    ] = None
    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    plays: List[ProPlay]
