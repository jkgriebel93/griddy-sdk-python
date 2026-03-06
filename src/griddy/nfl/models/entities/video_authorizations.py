from __future__ import annotations

from typing import List, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class NflPlusPlusRequirements(BaseModel):
    """Requirements for NFL+ Plus tier access."""

    country_code: Annotated[
        Optional[List[str]], pydantic.Field(alias="countryCode")
    ] = None


class NFLPLUSPLUSNFLPLUSCOACHESFILM(BaseModel):
    """NFL+ Plus coaches film authorization."""

    requirements: Optional[NflPlusPlusRequirements] = None


class NflPlusPlus(BaseModel):
    """NFL+ Plus subscription tier details."""

    nfl_plus_coaches_film: Annotated[
        Optional[NFLPLUSPLUSNFLPLUSCOACHESFILM],
        pydantic.Field(alias="NFL PLUS - COACHES FILM"),
    ] = None


class NflPlusPremiumRequirements(BaseModel):
    """Requirements for NFL+ Premium tier access."""

    country_code: Annotated[
        Optional[List[str]], pydantic.Field(alias="countryCode")
    ] = None


class NFLPLUSPremiumNFLPLUSCOACHESFILM(BaseModel):
    """NFL+ Premium coaches film authorization."""

    requirements: Optional[NflPlusPremiumRequirements] = None


class NflPlusPremium(BaseModel):
    """NFL+ Premium subscription tier details."""

    nfl_plus_coaches_film: Annotated[
        Optional[NFLPLUSPremiumNFLPLUSCOACHESFILM],
        pydantic.Field(alias="NFL PLUS - COACHES FILM"),
    ] = None


class ProPremiumRequirements(BaseModel):
    """Requirements for Pro Premium tier access."""

    country_code: Annotated[
        Optional[List[str]], pydantic.Field(alias="countryCode")
    ] = None


class ProPremiumNFLPLUSCOACHESFILM(BaseModel):
    """Pro Premium coaches film authorization."""

    requirements: Optional[ProPremiumRequirements] = None


class ProPremium(BaseModel):
    """Pro Premium subscription tier details."""

    nfl_plus_coaches_film: Annotated[
        Optional[ProPremiumNFLPLUSCOACHESFILM],
        pydantic.Field(alias="NFL PLUS - COACHES FILM"),
    ] = None


class VideoAuthorizations(BaseModel):
    r"""Authorization requirements for video access"""

    nfl_plus_plus: Optional[List[NflPlusPlus]] = None

    nfl_plus_premium: Optional[List[NflPlusPremium]] = None

    pro_premium: Optional[List[ProPremium]] = None
