from __future__ import annotations

from typing import Optional

from typing_extensions import Annotated

from ...utils import FieldMetadata, SecurityMetadata
from ..base import PFRBaseModel


class Security(PFRBaseModel):
    pfr_auth: Annotated[
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
