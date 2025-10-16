from __future__ import annotations
from ..types import BaseModel
import pydantic
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TeamBoxscoreTypedDict(TypedDict):
    extra_points: NotRequired[List[Dict[str, Any]]]
    field_goals: NotRequired[List[Dict[str, Any]]]
    fumbles: NotRequired[List[Dict[str, Any]]]
    kick_return: NotRequired[List[Dict[str, Any]]]
    kicking: NotRequired[List[Dict[str, Any]]]
    passing: NotRequired[List[Dict[str, Any]]]
    punt_return: NotRequired[List[Dict[str, Any]]]
    punting: NotRequired[List[Dict[str, Any]]]
    receiving: NotRequired[List[Dict[str, Any]]]
    rushing: NotRequired[List[Dict[str, Any]]]
    tackles: NotRequired[List[Dict[str, Any]]]


class TeamBoxscore(BaseModel):
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
