from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models.entities.pro_play import ProPlay
from griddy.nfl.types import BaseModel
from griddy.nfl.utils.unmarshal_json_response import int_to_str


class PlaylistResponse(BaseModel):
    game_id: Annotated[
        Optional[str],
        pydantic.Field(alias="gameId"),
        pydantic.BeforeValidator(int_to_str),
    ] = None
    game_key: Annotated[Optional[int], pydantic.Field(alias="gameKey")] = None
    plays: List[ProPlay]
