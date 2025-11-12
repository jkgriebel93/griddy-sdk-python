from typing import List

import pydantic
from typing_extensions import Annotated, TypedDict

from griddy.nfl.models.combineevents import (
    BenchPress,
    BenchPressTypedDict,
    BroadJump,
    BroadJumpTypedDict,
    FortyYardDash,
    FortyYardDashTypedDict,
    TenYardSplit,
    TenYardSplitTypedDict,
    ThreeConeDrill,
    ThreeConeDrillTypedDict,
    TwentyYardShuffle,
    TwentyYardShuffleTypedDict,
    VerticalJump,
    VerticalJumpTypedDict,
)
from griddy.nfl.models.enums.combineenums import CollegeClassEnum
from griddy.nfl.types import BaseModel


class CombinePersonTypedDict(TypedDict):
    id_: str
    r"""UUID assigned to the prospect by the NFL"""
    display_name: str
    r"""Fist and last name"""
    esb_id: str
    r"""String ID containing first three letters of surname followed by a number"""
    first_name: str
    r"""Prospect's given name"""
    last_name: str
    r"""Prospect's last name"""
    hometown: str
    r"""Prospect's hometown"""
    college_names: List[str]
    r"""College(s) the prospect attended"""


class CombinePerson(BaseModel):
    id_: Annotated[str, pydantic.Field(alias="id")]
    r"""UUID assigned to the prospect by the NFL"""
    display_name: str
    r"""Fist and last name"""
    esb_id: Annotated[str, pydantic.Field(alias="esbId")]
    r"""String ID containing first three letters of surname followed by a number"""
    first_name: Annotated[str, pydantic.Field(alias="fisrtName")]
    r"""Prospect's given name"""
    last_name: Annotated[str, pydantic.Field(alias="lastName")]
    r"""Prospect's last name"""
    hometown: str
    r"""Prospect's hometown"""
    college_names: Annotated[List[str], pydantic.Field(alias="collegeNames")]
    r"""College(s) the prospect attended"""


class CombineProfileTypedDict(TypedDict):
    id_: str
    r"""UUID assigned by the NFL"""
    year: int
    r"""Draft year of the combine testing"""
    person: CombinePersonTypedDict
    r"""Bio information about the prospect"""
    arm_length: float
    r"""Arm length in inches precise to 1/8 inch, represented as a float"""
    athletic_score: float
    r"""A 0-100 grade of the prospect's overall athleticism"""
    bench_press: BenchPressTypedDict
    r"""Bench press results"""
    broad_jump: BroadJumpTypedDict
    r"""Broad jump results"""
    bio: str
    r"""HTML formatted snippet containing brief summary of prospect's background"""
    college_class: CollegeClassEnum
    r"""College year of the prospect"""
    draft_grade: float
    r"""0-100 overall grade"""
    draft_projection: str
    r"""Anticipated draft outcome for the prospect"""
    forty_yard_dash: FortyYardDashTypedDict
    r"""Forty yard dash outcome"""
    grade: float
    r""""""
    hand_size: float
    r"""Thumb to pinky tip measurement, precise to 1/8 inch"""
    headshot: str
    r"""URL to the prospect's headshot"""
    height: float
    r"""Prospect height in inches"""
    nfl_comparison: str
    r"""Name of an NFL player with a similar profile"""
    overview: str
    r"""HTML formatted snippet with scouting elevator pitch"""
    production_score: float
    r"""0-100 grade of player's on-field statistical profile"""
    profile_author: str
    r"""Name of the person who wrote the scouting profile"""
    pro_forty_yard_dash: FortyYardDashTypedDict
    r"""Forty yard dash from prospect's pro day"""
    sources_tell_us: str
    r"""HTML - Comments on the prospect from talent evaluators around the league"""
    strengths: str
    r"""HTML - Prospect strengths"""
    ten_yard_split: TenYardSplitTypedDict
    r"""Ten yard split time in 40 yd dash"""
    three_cone_drill: ThreeConeDrillTypedDict
    r"""Three cone drill result"""
    twenty_yard_shuffle: TwentyYardShuffleTypedDict
    r"""Twenty yard shuffle result"""
    weaknesses: str
    r"""HTML - Prospect weaknesses"""
    combine_attendance: bool
    r"""Whether or not the prospect attended the official scouting combine"""
    position: str
    # TODO: Make this field a complete enum
    r"""Player's position in college"""
    position_group: str
    # TODO: Create complete enum
    r"""Position group in college"""
    vertical_jump: VerticalJumpTypedDict
    r"""Vertical jump result"""
    weight: float
    r"""Weight in pounds"""


class CombineProfile(BaseModel):
    id_: Annotated[str, pydantic.Field(alias="id")]
    r"""UUID assigned by the NFL"""
    year: int
    r"""Draft year of the combine testing"""
    person: CombinePerson
    r"""Bio information about the prospect"""
    arm_length: Annotated[float, pydantic.Field(alias="armLength")]
    r"""Arm length in inches precise to 1/8 inch, represented as a float"""
    athletic_score: Annotated[float, pydantic.Field(alias="athleticScore")]
    r"""A 0-100 grade of the prospect's overall athleticism"""
    bench_press: Annotated[BenchPress, pydantic.Field(alias="benchPress")]
    r"""Bench press results"""
    broad_jump: Annotated[BroadJump, pydantic.Field(alias="broadJump")]
    r"""Broad jump results"""
    bio: str
    r"""HTML formatted snippet containing brief summary of prospect's background"""
    college_class: Annotated[CollegeClassEnum, pydantic.Field(alias="collegeClass")]
    r"""College year of the prospect"""
    draft_grade: Annotated[float, pydantic.Field(alias="draftGrade")]
    r"""0-100 overall grade"""
    draft_projection: Annotated[str, pydantic.Field(alias="draftProjection")]
    r"""Anticipated draft outcome for the prospect"""
    forty_yard_dash: Annotated[FortyYardDash, pydantic.Field(alias="fortyYardDash")]
    r"""Forty yard dash outcome"""
    grade: float
    r""""""
    hand_size: Annotated[float, pydantic.Field(alias="handSize")]
    r"""Thumb to pinky tip measurement, precise to 1/8 inch"""
    headshot: str
    r"""URL to the prospect's headshot"""
    height: float
    r"""Prospect height in inches"""
    nfl_comparison: Annotated[str, pydantic.Field(alias="nflComparison")]
    r"""Name of an NFL player with a similar profile"""
    overview: str
    r"""HTML formatted snippet with scouting elevator pitch"""
    production_score: Annotated[float, pydantic.Field(alias="productionScore")]
    r"""0-100 grade of player's on-field statistical profile"""
    profile_author: Annotated[str, pydantic.Field(alias="profileAuthor")]
    r"""Name of the person who wrote the scouting profile"""
    pro_forty_yard_dash: Annotated[
        FortyYardDash, pydantic.Field(alias="proFortyYardDash")
    ]
    r"""Forty yard dash from prospect's pro day"""
    sources_tell_us: Annotated[str, pydantic.Field(alias="sourcesTellUs")]
    r"""HTML - Comments on the prospect from talent evaluators around the league"""
    strengths: str
    r"""HTML - Prospect strengths"""
    ten_yard_split: Annotated[TenYardSplit, pydantic.Field(alias="tenYardSplit")]
    r"""Ten yard split time in 40 yd dash"""
    three_cone_drill: Annotated[ThreeConeDrill, pydantic.Field(alias="threeConeDrill")]
    r"""Three cone drill result"""
    twenty_yard_shuffle: Annotated[
        TwentyYardShuffle, pydantic.Field(alias="twentyYardShuffle")
    ]
    r"""Twenty yard shuffle result"""
    weaknesses: str
    r"""HTML - Prospect weaknesses"""
    combine_attendance: Annotated[bool, pydantic.Field(alias="combineAttendance")]
    r"""Whether or not the prospect attended the official scouting combine"""
    position: str
    # TODO: Make this field a complete enum
    r"""Player's position in college"""
    position_group: Annotated[str, pydantic.Field(alias="positionGroup")]
    # TODO: Create complete enum
    r"""Position group in college"""
    vertical_jump: Annotated[VerticalJump, pydantic.Field(alias="verticalJump")]
    r"""Vertical jump result"""
    weight: float
    r"""Weight in pounds"""
