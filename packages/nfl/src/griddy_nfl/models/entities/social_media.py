from __future__ import annotations

from typing import Optional

from typing_extensions import NotRequired, TypedDict

from ...types import BaseModel


class SocialMediaTypedDict(TypedDict):
    link: NotRequired[str]
    r"""URL to social media profile"""
    platform: NotRequired[str]
    r"""Social media platform name"""


class SocialMedia(BaseModel):
    link: Optional[str] = None
    r"""URL to social media profile"""

    platform: Optional[str] = None
    r"""Social media platform name"""
