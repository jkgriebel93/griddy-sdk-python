from __future__ import annotations

from typing import List, Union

import pydantic
from typing_extensions import Annotated, TypeAliasType, TypedDict

from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
from .winprobabilityresponse import (
    WinProbabilityResponse,
    WinProbabilityResponseTypedDict,
)

GameIDTypedDict = TypeAliasType("GameIDTypedDict", Union[str, List[str]])
r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
Can be a single game ID or multiple game IDs for batch retrieval.

"""


GameID = TypeAliasType("GameID", Union[str, List[str]])
r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
Can be a single game ID or multiple game IDs for batch retrieval.

"""


class GetPlaysWinProbabilityRequestTypedDict(TypedDict):
    game_id: GameIDTypedDict
    r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
    Can be a single game ID or multiple game IDs for batch retrieval.

    """


class GetPlaysWinProbabilityRequest(BaseModel):
    game_id: Annotated[
        GameID,
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
    Can be a single game ID or multiple game IDs for batch retrieval.

    """


GetPlaysWinProbabilityResponseTypedDict = TypeAliasType(
    "GetPlaysWinProbabilityResponseTypedDict",
    Union[WinProbabilityResponseTypedDict, List[WinProbabilityResponseTypedDict]],
)
r"""Successfully retrieved win probability data"""


GetPlaysWinProbabilityResponse = TypeAliasType(
    "GetPlaysWinProbabilityResponse",
    Union[WinProbabilityResponse, List[WinProbabilityResponse]],
)
r"""Successfully retrieved win probability data"""
