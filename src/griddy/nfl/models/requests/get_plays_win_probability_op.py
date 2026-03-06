from __future__ import annotations

from typing import List, Union

import pydantic
from typing_extensions import Annotated, TypeAliasType

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata

GameID = TypeAliasType("GameID", Union[str, List[str]])
r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
Can be a single game ID or multiple game IDs for batch retrieval.

"""


class GetPlaysWinProbabilityRequest(BaseModel):
    """Request parameters for fetching play win probabilities."""

    game_id: Annotated[
        GameID,
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
    Can be a single game ID or multiple game IDs for batch retrieval.

    """
