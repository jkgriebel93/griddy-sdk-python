"""Response models for NGS news endpoints (articles, videos, mixed content)."""

from __future__ import annotations

from typing import List, Optional

from griddy.nfl.models.entities.ngs_news import (
    NgsContentItem,
    NgsContentMetadata,
    NgsContentPagination,
)
from griddy.nfl.types import BaseModel


class NgsMixedContentResponse(BaseModel):
    """Response from the NGS mixed content endpoint."""

    items: Optional[List[NgsContentItem]] = None
    metadata: Optional[NgsContentMetadata] = None
    pagination: Optional[NgsContentPagination] = None


class NgsArticlesResponse(BaseModel):
    """Response from the NGS articles endpoint."""

    items: Optional[List[NgsContentItem]] = None
    metadata: Optional[NgsContentMetadata] = None
    pagination: Optional[NgsContentPagination] = None


class NgsVideosResponse(BaseModel):
    """Response from the NGS videos endpoint."""

    items: Optional[List[NgsContentItem]] = None
    metadata: Optional[NgsContentMetadata] = None
    pagination: Optional[NgsContentPagination] = None
