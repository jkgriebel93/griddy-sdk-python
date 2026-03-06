from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from griddy.nfl.models import SiteRoofTypeEnum
from griddy.nfl.types import UNSET, BaseModel, OptionalNullable


class GameSite(BaseModel):
    """Venue and site information for a game."""

    postal_code: Annotated[
        OptionalNullable[str], pydantic.Field(alias="postalCode")
    ] = UNSET

    roof_type: Annotated[
        Optional[SiteRoofTypeEnum], pydantic.Field(alias="roofType")
    ] = None

    site_city: Annotated[Optional[str], pydantic.Field(alias="siteCity")] = None

    site_full_name: Annotated[Optional[str], pydantic.Field(alias="siteFullName")] = (
        None
    )
    r"""Stadium name"""

    site_id: Annotated[Optional[int], pydantic.Field(alias="siteId")] = None

    site_state: Annotated[OptionalNullable[str], pydantic.Field(alias="siteState")] = (
        UNSET
    )

    smart_id: Annotated[Optional[str], pydantic.Field(alias="smartId")] = None
