from __future__ import annotations

from typing import Optional

from ...types import BaseModel


class ExternalID(BaseModel):
    """External identifier mapping for an NFL entity."""

    id: Optional[str] = None
    r"""ID in external system"""

    source: Optional[str] = None
    r"""External system name"""
