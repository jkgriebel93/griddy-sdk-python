"""NGS News entity models for articles, videos, and content items."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.types import BaseModel


class NgsThumbnail(BaseModel):
    """Thumbnail for content items."""

    thumbnail_url: Annotated[Optional[str], pydantic.Field(alias="thumbnailUrl")] = None
    title: Optional[str] = None


class NgsContentTag(BaseModel):
    """Tag for content items."""

    title: Optional[str] = None
    slug: Optional[str] = None
    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    person_id: Annotated[Optional[str], pydantic.Field(alias="personId")] = None
    extra_data: Annotated[
        Optional[Dict[str, Any]], pydantic.Field(alias="extraData")
    ] = None


class NgsContentItem(BaseModel):
    """A content item (article or video)."""

    type: Optional[str] = None
    id: Optional[str] = None
    title: Optional[str] = None
    display_title: Annotated[Optional[str], pydantic.Field(alias="displayTitle")] = None
    mobile_title: Annotated[Optional[str], pydantic.Field(alias="mobileTitle")] = None
    description: Optional[str] = None
    summary: Optional[str] = None
    slug: Optional[str] = None
    publish_date: Annotated[Optional[datetime], pydantic.Field(alias="publishDate")] = (
        None
    )
    last_updated: Annotated[Optional[datetime], pydantic.Field(alias="lastUpdated")] = (
        None
    )
    web_link: Annotated[Optional[str], pydantic.Field(alias="webLink")] = None
    fantasy_link: Annotated[Optional[str], pydantic.Field(alias="fantasyLink")] = None
    mobile_link: Annotated[Optional[str], pydantic.Field(alias="mobileLink")] = None
    thumbnail: Optional[NgsThumbnail] = None
    tags: Optional[List[NgsContentTag]] = None
    # Video specific
    language: Optional[str] = None
    author: Optional[str] = None
    duration: Optional[int] = None
    clip_type: Annotated[Optional[str], pydantic.Field(alias="clipType")] = None
    mcp_playback_id: Annotated[Optional[str], pydantic.Field(alias="mcpPlaybackId")] = (
        None
    )
    external_id: Annotated[Optional[str], pydantic.Field(alias="externalId")] = None


class NgsContentMetadata(BaseModel):
    """Metadata for content responses."""

    generated_at: Annotated[Optional[datetime], pydantic.Field(alias="generatedAt")] = (
        None
    )


class NgsContentPagination(BaseModel):
    """Pagination for content responses."""

    token: Optional[str] = None
