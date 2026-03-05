from __future__ import annotations

from datetime import datetime
from typing import List, Literal, Optional

import pydantic
from typing_extensions import Annotated

from ...types import UNSET, BaseModel, OptionalNullable
from .video_authorizations import VideoAuthorizations
from .video_game_play_ids import VideoGamePlayIds
from .video_tag import VideoTag
from .video_thumbnail import VideoThumbnail


class Background(BaseModel):
    r"""Background configuration"""


CameraSource = Literal[
    "Endzone",
    "Sideline",
    "Broadcast",
]
r"""Camera angle/source for the video"""


class Cta(BaseModel):
    pass


class Image(BaseModel):
    pass


class PromoAsset(BaseModel):
    pass


SubType = Literal[
    "Coaches Film",
    "Coaches Film Pro",
]
r"""Video subtype classification"""


CoachesFilmVideoType = Literal["video",]
r"""Content type (always \"video\")"""


class Video(BaseModel):
    pass


class CoachesFilmVideo(BaseModel):
    camera_source: Annotated[CameraSource, pydantic.Field(alias="cameraSource")]
    r"""Camera angle/source for the video"""

    description: str
    r"""Play description"""

    duration: str
    r"""Video duration in seconds"""

    external_id: Annotated[str, pydantic.Field(alias="externalId")]
    r"""External video identifier"""

    ids: VideoGamePlayIds

    title: str
    r"""Video title"""

    type: CoachesFilmVideoType
    r"""Content type (always \"video\")"""

    advertiser_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="advertiserId")
    ] = UNSET
    r"""Associated advertiser ID"""

    author: OptionalNullable[str] = UNSET
    r"""Content author"""

    authorizations: Optional[VideoAuthorizations] = None
    r"""Authorization requirements for video access"""

    background: Optional[Background] = None
    r"""Background configuration"""

    clip_type: Annotated[OptionalNullable[str], pydantic.Field(alias="clipType")] = (
        UNSET
    )
    r"""Type of video clip"""

    cta_link: Annotated[OptionalNullable[str], pydantic.Field(alias="ctaLink")] = UNSET
    r"""Call-to-action link"""

    cta_target: Annotated[OptionalNullable[str], pydantic.Field(alias="ctaTarget")] = (
        UNSET
    )
    r"""Call-to-action target"""

    cta_text: Annotated[OptionalNullable[str], pydantic.Field(alias="ctaText")] = UNSET
    r"""Call-to-action text"""

    ctas: Optional[List[Cta]] = None
    r"""Call-to-action elements"""

    display_title: Annotated[
        OptionalNullable[str], pydantic.Field(alias="displayTitle")
    ] = UNSET
    r"""Display title override"""

    end_date: Annotated[OptionalNullable[datetime], pydantic.Field(alias="endDate")] = (
        UNSET
    )
    r"""Content end date"""

    entitlement: OptionalNullable[str] = UNSET
    r"""Entitlement information"""

    episode_number: Annotated[
        OptionalNullable[int], pydantic.Field(alias="episodeNumber")
    ] = UNSET
    r"""Episode number if part of series"""

    expiration_date: Annotated[
        Optional[datetime], pydantic.Field(alias="expirationDate")
    ] = None
    r"""Content expiration date"""

    fantasy_link: Annotated[
        OptionalNullable[str], pydantic.Field(alias="fantasyLink")
    ] = UNSET
    r"""Related fantasy content link"""

    host_network: Annotated[
        OptionalNullable[str], pydantic.Field(alias="hostNetwork")
    ] = UNSET
    r"""Broadcasting network"""

    id: OptionalNullable[str] = UNSET
    r"""Internal content ID"""

    images: Optional[List[Image]] = None
    r"""Associated images"""

    intended_audience: Annotated[
        OptionalNullable[str], pydantic.Field(alias="intendedAudience")
    ] = UNSET
    r"""Target audience"""

    intro_end: Annotated[OptionalNullable[str], pydantic.Field(alias="introEnd")] = (
        UNSET
    )
    r"""Introduction end timestamp"""

    language: OptionalNullable[str] = UNSET
    r"""Content language"""

    last_updated: Annotated[
        OptionalNullable[datetime], pydantic.Field(alias="lastUpdated")
    ] = UNSET
    r"""Last update timestamp"""

    mcp_playback_id: Annotated[Optional[str], pydantic.Field(alias="mcpPlaybackId")] = (
        None
    )
    r"""Media control platform playback ID"""

    mobile_link: Annotated[
        OptionalNullable[str], pydantic.Field(alias="mobileLink")
    ] = UNSET
    r"""Mobile-specific link"""

    mobile_title: Annotated[
        OptionalNullable[str], pydantic.Field(alias="mobileTitle")
    ] = UNSET
    r"""Mobile-specific title"""

    original_air_date: Annotated[
        Optional[datetime], pydantic.Field(alias="originalAirDate")
    ] = None
    r"""Original broadcast air date"""

    outro_start: Annotated[
        OptionalNullable[str], pydantic.Field(alias="outroStart")
    ] = UNSET
    r"""Outro start timestamp"""

    play_ids: Annotated[Optional[List[str]], pydantic.Field(alias="playIds")] = None
    r"""Play identifiers associated with this video"""

    pre_roll_disabled: Annotated[
        Optional[bool], pydantic.Field(alias="preRollDisabled")
    ] = False
    r"""Whether pre-roll ads are disabled"""

    promo_assets: Annotated[
        Optional[List[PromoAsset]], pydantic.Field(alias="promoAssets")
    ] = None
    r"""Promotional assets"""

    promo_link: Annotated[OptionalNullable[str], pydantic.Field(alias="promoLink")] = (
        UNSET
    )
    r"""Promotional link"""

    promo_target: Annotated[Optional[str], pydantic.Field(alias="promoTarget")] = (
        "_self"
    )
    r"""Promotional link target"""

    promo_text: Annotated[OptionalNullable[str], pydantic.Field(alias="promoText")] = (
        UNSET
    )
    r"""Promotional text"""

    publish_date: Annotated[Optional[datetime], pydantic.Field(alias="publishDate")] = (
        None
    )
    r"""Content publish date"""

    radio_station: Annotated[
        OptionalNullable[str], pydantic.Field(alias="radioStation")
    ] = UNSET
    r"""Associated radio station"""

    series: OptionalNullable[str] = UNSET
    r"""Series information"""

    series_season: Annotated[
        OptionalNullable[str], pydantic.Field(alias="seriesSeason")
    ] = UNSET
    r"""Series season if applicable"""

    series_title: Annotated[
        OptionalNullable[str], pydantic.Field(alias="seriesTitle")
    ] = UNSET
    r"""Series title if part of series"""

    slug: OptionalNullable[str] = UNSET
    r"""URL slug"""

    start_date: Annotated[
        OptionalNullable[datetime], pydantic.Field(alias="startDate")
    ] = UNSET
    r"""Content start date"""

    sub_type: Annotated[Optional[SubType], pydantic.Field(alias="subType")] = None
    r"""Video subtype classification"""

    summary: OptionalNullable[str] = UNSET
    r"""Content summary"""

    tags: Optional[List[VideoTag]] = None
    r"""Content tags and metadata"""

    thumbnail: Optional[VideoThumbnail] = None

    videos: Optional[List[Video]] = None
    r"""Additional video information"""

    web_link: Annotated[OptionalNullable[str], pydantic.Field(alias="webLink")] = UNSET
    r"""Web-specific link"""
