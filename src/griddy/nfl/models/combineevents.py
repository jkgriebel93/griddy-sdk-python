from typing import List

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy.nfl.models.enums.combineenums import DesignationEnum
from griddy.nfl.types import BaseModel


class HasDesignationTypedDict(TypedDict):
    designation: DesignationEnum
    r"""Whether the result is official/unofficial"""


class HasDesignation(BaseModel):
    designation: DesignationEnum
    r"""Whether the result is official/unofficial"""


class BenchPressTypedDict(HasDesignationTypedDict):
    repetitions: int
    r"""Bench press reps"""


class BroadJumpTypedDict(HasDesignationTypedDict):
    inches: int
    r"""Broad jump distance in inches"""


class FortyYardDashTypedDict(HasDesignationTypedDict):
    seconds: float
    r"""40 yard dash time"""


class TenYardSplitTypedDict(HasDesignationTypedDict):
    seconds: float
    r"""Split time"""


class ThreeConeDrillTypedDict(HasDesignationTypedDict):
    seconds: float
    r"""Three cone drill time"""


class TwentyYardShuffleTypedDict(HasDesignationTypedDict):
    seconds: float
    r"""Twenty yard shuffle time"""


class VerticalJumpTypedDict(HasDesignationTypedDict):
    inches: float
    r"""Vertical jump height"""


class BenchPress(HasDesignation):
    repetitions: int
    r"""Bench press reps"""


class BroadJump(HasDesignation):
    inches: int
    r"""Broad jump distance in inches"""


class FortyYardDash(HasDesignation):
    seconds: float
    r"""40 yard dash time"""


class TenYardSplit(HasDesignation):
    seconds: float
    r"""Split time"""


class ThreeConeDrill(HasDesignation):
    seconds: float
    r"""Three cone drill time"""


class TwentyYardShuffle(HasDesignation):
    seconds: float
    r"""Twenty yard shuffle time"""


class VerticalJump(HasDesignation):
    inches: float
    r"""Vertical jump height"""
