from __future__ import annotations

from typing import Optional

from typing_extensions import Annotated

from ...types import BaseModel
from ...utils import FieldMetadata, SecurityMetadata


class Security(BaseModel):
    """Security credentials for NFL API authentication."""

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
