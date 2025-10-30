from typing import List, Union

import pydantic
from typing_extensions import Annotated, TypeAliasType, TypedDict

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata

GameIDTypedDict = TypeAliasType("GameIDTypedDict", Union[str, List[str]])
r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
Can be a single game ID or multiple game IDs for batch retrieval.

"""


GameID = TypeAliasType("GameID", Union[str, List[str]])
r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
Can be a single game ID or multiple game IDs for batch retrieval.

"""


class GetPlayListRequestTypedDict(TypedDict):
    game_id: GameIDTypedDict
    r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
    Can be a single game ID or multiple game IDs for batch retrieval.

    """


class GetPlayListRequest(BaseModel):
    game_id: Annotated[
        GameID,
        pydantic.Field(alias="gameId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ]
    r"""Game identifier(s) in 10-digit format (YYYYMMDDNN).
    Can be a single game ID or multiple game IDs for batch retrieval.

    """
