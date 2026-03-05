from __future__ import annotations

from typing import Optional

from ...types import BaseModel


class ExternalID(BaseModel):
    id: Optional[str] = None
    r"""ID in external system"""

    source: Optional[str] = None
    r"""External system name"""
