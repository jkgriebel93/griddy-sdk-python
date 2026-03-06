from __future__ import annotations

from typing import Optional

from ...types import BaseModel


class SocialMedia(BaseModel):
    """Social media account links for an NFL entity."""

    link: Optional[str] = None
    r"""URL to social media profile"""

    platform: Optional[str] = None
    r"""Social media platform name"""
