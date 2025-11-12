from typing import TypedDict

from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetFootballTeamsRequestTypedDict(TypedDict):
    limit: int
    r"""Maximum number of teams to fetch"""
    season: int
    r"""Which season to fetch the teams for"""


class GetFootballTeamsRequest(BaseModel):
    limit: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Maximum number of teams to fetch"""
    season: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Season year"""
