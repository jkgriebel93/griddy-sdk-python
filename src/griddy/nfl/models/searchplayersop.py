from __future__ import annotations
from ..types import BaseModel
from ..utils import FieldMetadata, QueryParamMetadata
from typing_extensions import Annotated, TypedDict


class SearchPlayersRequestTypedDict(TypedDict):
    term: str
    r"""Search term for player name (first or last name)"""


class SearchPlayersRequest(BaseModel):
    term: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Search term for player name (first or last name)"""
