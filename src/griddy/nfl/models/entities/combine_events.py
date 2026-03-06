from griddy.nfl.models.enums.combine_enums import DesignationEnum
from griddy.nfl.types import BaseModel


class HasDesignation(BaseModel):
    """Combine event participation flag."""

    designation: DesignationEnum
    r"""Whether the result is official/unofficial"""


class BenchPress(HasDesignation):
    """NFL Combine bench press results."""

    repetitions: int
    r"""Bench press reps"""


class BroadJump(HasDesignation):
    """NFL Combine broad jump results."""

    inches: int
    r"""Broad jump distance in inches"""


class FortyYardDash(HasDesignation):
    """NFL Combine 40-yard dash results."""

    seconds: float
    r"""40 yard dash time"""


class TenYardSplit(HasDesignation):
    """NFL Combine 10-yard split results."""

    seconds: float
    r"""Split time"""


class ThreeConeDrill(HasDesignation):
    """NFL Combine three-cone drill results."""

    seconds: float
    r"""Three cone drill time"""


class TwentyYardShuffle(HasDesignation):
    """NFL Combine 20-yard shuttle results."""

    seconds: float
    r"""Twenty yard shuffle time"""


class VerticalJump(HasDesignation):
    """NFL Combine vertical jump results."""

    inches: float
    r"""Vertical jump height"""
