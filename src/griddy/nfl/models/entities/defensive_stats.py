from __future__ import annotations

from typing import Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class DefensiveStats(BaseModel):
    assisted_tackles: Annotated[
        Optional[int], pydantic.Field(alias="assistedTackles")
    ] = None

    forced_fumbles: Annotated[Optional[int], pydantic.Field(alias="forcedFumbles")] = (
        None
    )

    fumble_recoveries: Annotated[
        Optional[int], pydantic.Field(alias="fumbleRecoveries")
    ] = None

    interceptions: Optional[int] = None

    passes_defended: Annotated[
        Optional[int], pydantic.Field(alias="passesDefended")
    ] = None

    qb_hits: Annotated[Optional[int], pydantic.Field(alias="qbHits")] = None

    sacks: Optional[float] = None

    safeties: Optional[int] = None

    solo_tackles: Annotated[Optional[int], pydantic.Field(alias="soloTackles")] = None

    tackles: Optional[int] = None

    tackles_for_loss: Annotated[
        Optional[int], pydantic.Field(alias="tacklesForLoss")
    ] = None
