from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy.nfl import models
from griddy.nfl.types import BaseModel
from griddy.nfl.utils.unmarshal_json_response import int_to_str


class PersonTypedDict(TypedDict):
    id_: str
    r"""UUUID assigned by the NFL"""
    college_names: NotRequired[List[str]]
    r"""Colleges the person attended"""
    display_name: str
    r"""First and last name"""
    birth_date: NotRequired[str]
    r"""Person's date of birth as YYYY-MM-DD"""
    first_name: str
    r"""Person's formal first name"""
    common_first_name: str
    r"""e.g. Mike instead of Michael"""
    esb_id: str
    r"""Another form of ID tracked by the NFL"""
    gsis_id: NotRequired[str]
    r"""Yet another ID"""
    headshot: NotRequired[str]
    r"""A URL for the person's headshot used in Media"""
    height: int
    r"""Person's height rounded to nearest whole inch"""
    internation_exempt: bool
    r"""Not sure what this is"""
    jersey_number: NotRequired[str]
    r"""Number the player wears on the field."""
    last_name: str
    r"""Person's surname"""
    nfl_experience: int
    r"""Number of years the person has been a part of the NFL"""
    position: str
    # TODO: Make an enum for this
    r"""Player's position on the field"""
    position_group: str
    # TODO: Make an enum for this
    r"""Player's position group"""
    status: str
    # TODO: Make an enum
    r"""Whether the player is active or retired"""
    weight: int
    r"""Player's weight rounded to the nearest pound"""


class Person(BaseModel):
    id_: Annotated[str, pydantic.Field(alias="id")]
    r"""UUUID assigned by the NFL"""
    college_names: Annotated[Optional[List[str]], pydantic.Field(alias="collegeNames")]
    r"""Colleges the person attended"""
    display_name: Annotated[str, pydantic.Field(alias="displayName")]
    r"""First and last name"""
    birth_date: Annotated[Optional[str], pydantic.Field(alias="birthDate")] = None
    r"""Person's date of birth as YYYY-MM-DD"""
    first_name: Annotated[str, pydantic.Field(alias="firstName")]
    r"""Person's formal first name"""
    common_first_name: Annotated[str, pydantic.Field(alias="commonFirstName")]
    r"""e.g. Mike instead of Michael"""
    esb_id: Annotated[str, pydantic.Field(alias="esbId")]
    r"""Another form of ID tracked by the NFL"""
    gsis_id: Annotated[Optional[str], pydantic.Field(alias="gsisId")] = None
    r"""Yet another ID"""
    headshot: Optional[str] = None
    r"""A URL for the person's headshot used in Media"""
    height: int
    r"""Person's height rounded to nearest whole inch"""
    internation_exempt: Annotated[bool, pydantic.Field(alias="internationalExempt")]
    r"""Not sure what this is"""
    jersey_number: Annotated[
        Optional[str],
        pydantic.Field(alias="jerseyNumber"),
        pydantic.BeforeValidator(int_to_str),
    ] = None
    r"""Number the player wears on the field."""
    last_name: Annotated[str, pydantic.Field(alias="lastName")]
    r"""Person's surname"""
    nfl_experience: Annotated[int, pydantic.Field(alias="nflExperience")]
    r"""Number of years the person has been a part of the NFL"""
    position: str
    # TODO: Make an enum for this
    r"""Player's position on the field"""
    position_group: Annotated[str, pydantic.Field(alias="positionGroup")]
    # TODO: Make an enum for this
    r"""Player's position group"""
    status: str
    # TODO: Make an enum
    r"""Whether the player is active or retired"""
    weight: int
    r"""Player's weight rounded to the nearest pound"""
