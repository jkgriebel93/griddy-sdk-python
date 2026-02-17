from typing import Optional, TypedDict

from typing_extensions import Annotated, NotRequired

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, QueryParamMetadata


class GetTeamNeedsRequestTypedDict(TypedDict):
    year: int
    r"""Draft year"""
    limit: NotRequired[int]
    r"""Maximum picks to return"""


class GetTeamNeedsRequest(BaseModel):
    year: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Draft year"""
    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 32
