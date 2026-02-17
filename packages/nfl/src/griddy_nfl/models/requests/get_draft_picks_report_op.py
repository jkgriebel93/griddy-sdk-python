from typing import Optional, TypedDict

from typing_extensions import Annotated, NotRequired

from griddy_nfl.types import BaseModel
from griddy_nfl.utils import FieldMetadata, QueryParamMetadata


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
