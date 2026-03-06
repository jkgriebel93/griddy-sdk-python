from __future__ import annotations

from typing_extensions import Annotated

from ...types import BaseModel
from ...utils import FieldMetadata, QueryParamMetadata


class SearchPlayersRequest(BaseModel):
    """Request parameters for searching NFL players."""

    term: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Search term for player name (first or last name)"""
