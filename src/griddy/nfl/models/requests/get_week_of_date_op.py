from typing import TypedDict

from typing_extensions import Annotated

from griddy.nfl.types import BaseModel
from griddy.nfl.utils import FieldMetadata, PathParamMetadata


class GetWeekOfDateRequestTypedDict(TypedDict):
    date: str
    r"""Date for which to fetch week information. YYYY-MM-DD"""


class GetWeekOfDateRequest(BaseModel):
    date: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""Date for which to fetch week information. YYYY-MM-DD"""
