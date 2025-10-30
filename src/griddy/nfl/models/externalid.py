from __future__ import annotations

from typing import Optional

from typing_extensions import NotRequired, TypedDict

from ..types import BaseModel


class ExternalIDTypedDict(TypedDict):
    id: NotRequired[str]
    r"""ID in external system"""
    source: NotRequired[str]
    r"""External system name"""


class ExternalID(BaseModel):
    id: Optional[str] = None
    r"""ID in external system"""

    source: Optional[str] = None
    r"""External system name"""
