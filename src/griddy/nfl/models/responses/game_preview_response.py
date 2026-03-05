from __future__ import annotations

from griddy.nfl.types import (
    UNSET,
    BaseModel,
    Nullable,
    OptionalNullable,
)


class Preview(BaseModel):
    r"""Preview content and analysis"""


class GamePreviewResponse(BaseModel):
    r"""Game preview content (may be empty if no preview available)"""

    preview: OptionalNullable[Preview] = UNSET
    r"""Preview content and analysis"""
