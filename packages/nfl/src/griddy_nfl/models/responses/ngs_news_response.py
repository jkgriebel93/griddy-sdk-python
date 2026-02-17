"""Response models for NGS news endpoints (articles, videos, mixed content)."""

from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.ngs_news import (
    NgsContentItem,
    NgsContentItemTypedDict,
    NgsContentMetadata,
    NgsContentMetadataTypedDict,
    NgsContentPagination,
    NgsContentPaginationTypedDict,
)
from griddy_nfl.types import BaseModel


class NgsMixedContentResponseTypedDict(TypedDict):
    """Response from the NGS mixed content endpoint."""

    items: NotRequired[List[NgsContentItemTypedDict]]
    metadata: NotRequired[NgsContentMetadataTypedDict]
    pagination: NotRequired[NgsContentPaginationTypedDict]


class NgsMixedContentResponse(BaseModel):
    """Response from the NGS mixed content endpoint."""

    items: Optional[List[NgsContentItem]] = None
    metadata: Optional[NgsContentMetadata] = None
    pagination: Optional[NgsContentPagination] = None


class NgsArticlesResponseTypedDict(TypedDict):
    """Response from the NGS articles endpoint."""

    items: NotRequired[List[NgsContentItemTypedDict]]
    metadata: NotRequired[NgsContentMetadataTypedDict]
    pagination: NotRequired[NgsContentPaginationTypedDict]


class NgsArticlesResponse(BaseModel):
    """Response from the NGS articles endpoint."""

    items: Optional[List[NgsContentItem]] = None
    metadata: Optional[NgsContentMetadata] = None
    pagination: Optional[NgsContentPagination] = None


class NgsVideosResponseTypedDict(TypedDict):
    """Response from the NGS videos endpoint."""

    items: NotRequired[List[NgsContentItemTypedDict]]
    metadata: NotRequired[NgsContentMetadataTypedDict]
    pagination: NotRequired[NgsContentPaginationTypedDict]


class NgsVideosResponse(BaseModel):
    """Response from the NGS videos endpoint."""

    items: Optional[List[NgsContentItem]] = None
    metadata: Optional[NgsContentMetadata] = None
    pagination: Optional[NgsContentPagination] = None
