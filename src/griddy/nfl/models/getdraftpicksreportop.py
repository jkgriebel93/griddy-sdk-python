from typing import Optional, TypedDict

import pydantic
from typing_extensions import Annotated, NotRequired

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata


class GetDraftPicksReportRequestTypedDict(TypedDict):
    year: int
    r"""Draft year"""
    limit: NotRequired[int]
    r"""Maximum picks to return"""


class GetDraftPicksReportRequest(BaseModel):
    year: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Draft year"""
    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1000
