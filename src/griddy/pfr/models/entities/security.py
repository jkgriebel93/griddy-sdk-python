"""Security model for PFR SDK authentication.

Carries bearer-token credentials used by the SDK when making
authenticated requests.
"""

from __future__ import annotations

from typing import Optional

from typing_extensions import Annotated

from ...utils import FieldMetadata, SecurityMetadata
from ..base import PFRBaseModel


class Security(PFRBaseModel):
    """Bearer-token authentication model for the PFR SDK."""

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
