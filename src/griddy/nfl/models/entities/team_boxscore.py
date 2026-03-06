from __future__ import annotations

from typing import Any, Dict, List, Optional

import pydantic
from typing_extensions import Annotated

from ...types import BaseModel


class TeamBoxscore(BaseModel):
    """Team-level boxscore statistics for a game."""

    extra_points: Annotated[
        Optional[List[Dict[str, Any]]], pydantic.Field(alias="extraPoints")
    ] = None

    field_goals: Annotated[
        Optional[List[Dict[str, Any]]], pydantic.Field(alias="fieldGoals")
    ] = None

    fumbles: Optional[List[Dict[str, Any]]] = None

    kick_return: Annotated[
        Optional[List[Dict[str, Any]]], pydantic.Field(alias="kickReturn")
    ] = None

    kicking: Optional[List[Dict[str, Any]]] = None

    passing: Optional[List[Dict[str, Any]]] = None

    punt_return: Annotated[
        Optional[List[Dict[str, Any]]], pydantic.Field(alias="puntReturn")
    ] = None

    punting: Optional[List[Dict[str, Any]]] = None

    receiving: Optional[List[Dict[str, Any]]] = None

    rushing: Optional[List[Dict[str, Any]]] = None

    tackles: Optional[List[Dict[str, Any]]] = None
