from __future__ import annotations

from typing import Optional

from typing_extensions import Annotated, NotRequired, TypedDict

from ...types import BaseModel
from ...utils import FieldMetadata, SecurityMetadata


class SecurityTypedDict(TypedDict):
    nfl_auth: NotRequired[str]


class Security(BaseModel):
    nfl_auth: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ] = None
