from typing import Optional

from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, QueryParamMetadata


class GetDraftPicksReportRequest(BaseModel):
    """Request parameters for fetching a draft picks report."""

    year: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
    r"""Draft year"""
    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1000
