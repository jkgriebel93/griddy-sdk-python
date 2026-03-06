from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata


class GetWeekOfDateRequest(BaseModel):
    """Request parameters for fetching the NFL week for a given date."""

    date: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Date for which to fetch week information. YYYY-MM-DD"""
