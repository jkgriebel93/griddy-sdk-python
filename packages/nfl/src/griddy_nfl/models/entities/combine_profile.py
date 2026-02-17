from typing import List, Optional

import pydantic
from typing_extensions import Annotated, NotRequired, TypedDict

from griddy_nfl.models.entities.combine_events import (
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
from griddy_nfl.models.enums.combine_enums import CollegeClassEnum
from griddy_nfl.types import BaseModel


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
    hometown: NotRequired[str]
    r"""Prospect's hometown"""
    college_names: List[str]
    r"""College(s) the prospect attended"""


class CombinePerson(BaseModel):
    id_: Annotated[str, pydantic.Field(alias="id")]
    r"""UUID assigned to the prospect by the NFL"""
    display_name: Annotated[str, pydantic.Field(alias="displayName")]
    r"""Fist and last name"""
    esb_id: Annotated[str, pydantic.Field(alias="esbId")]
    r"""String ID containing first three letters of surname followed by a number"""
    first_name: Annotated[str, pydantic.Field(alias="firstName")]
    r"""Prospect's given name"""
    last_name: Annotated[str, pydantic.Field(alias="lastName")]
    r"""Prospect's last name"""
    hometown: Optional[str] = None
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
    arm_length: NotRequired[float]
    r"""Arm length in inches precise to 1/8 inch, represented as a float"""
    athletic_score: NotRequired[float]
    r"""A 0-100 grade of the prospect's overall athleticism"""
    bench_press: NotRequired[BenchPressTypedDict]
    r"""Bench press results"""
    broad_jump: NotRequired[BroadJumpTypedDict]
    r"""Broad jump results"""
    bio: NotRequired[str]
    r"""HTML formatted snippet containing brief summary of prospect's background"""
    college_class: CollegeClassEnum
    r"""College year of the prospect"""
    draft_grade: NotRequired[float]
    r"""0-100 overall grade"""
    draft_projection: NotRequired[str]
    r"""Anticipated draft outcome for the prospect"""
    forty_yard_dash: NotRequired[FortyYardDashTypedDict]
    r"""Forty yard dash outcome"""
    grade: NotRequired[float]
    r""""""
    hand_size: NotRequired[float]
    r"""Thumb to pinky tip measurement, precise to 1/8 inch"""
    headshot: NotRequired[str]
    r"""URL to the prospect's headshot"""
    height: float
    r"""Prospect height in inches"""
    nfl_comparison: NotRequired[str]
    r"""Name of an NFL player with a similar profile"""
    overview: NotRequired[str]
    r"""HTML formatted snippet with scouting elevator pitch"""
    production_score: NotRequired[float]
    r"""0-100 grade of player's on-field statistical profile"""
    profile_author: NotRequired[str]
    r"""Name of the person who wrote the scouting profile"""
    pro_forty_yard_dash: NotRequired[FortyYardDashTypedDict]
    r"""Forty yard dash from prospect's pro day"""
    sources_tell_us: NotRequired[str]
    r"""HTML - Comments on the prospect from talent evaluators around the league"""
    strengths: NotRequired[str]
    r"""HTML - Prospect strengths"""
    ten_yard_split: NotRequired[TenYardSplitTypedDict]
    r"""Ten yard split time in 40 yd dash"""
    three_cone_drill: NotRequired[ThreeConeDrillTypedDict]
    r"""Three cone drill result"""
    twenty_yard_shuffle: NotRequired[TwentyYardShuffleTypedDict]
    r"""Twenty yard shuffle result"""
    weaknesses: NotRequired[str]
    r"""HTML - Prospect weaknesses"""
    combine_attendance: bool
    r"""Whether or not the prospect attended the official scouting combine"""
    position: str
    # TODO: Make this field a complete enum
    r"""Player's position in college"""
    position_group: NotRequired[str]
    # TODO: Create complete enum
    r"""Position group in college"""
    vertical_jump: NotRequired[VerticalJumpTypedDict]
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
    arm_length: Annotated[Optional[float], pydantic.Field(alias="armLength")] = None
    r"""Arm length in inches precise to 1/8 inch, represented as a float"""
    athletic_score: Annotated[
        Optional[float], pydantic.Field(alias="athleticScore")
    ] = None
    r"""A 0-100 grade of the prospect's overall athleticism"""
    bench_press: Annotated[Optional[BenchPress], pydantic.Field(alias="benchPress")] = (
        None
    )
    r"""Bench press results"""
    broad_jump: Annotated[Optional[BroadJump], pydantic.Field(alias="broadJump")] = None
    r"""Broad jump results"""
    bio: Optional[str] = None
    r"""HTML formatted snippet containing brief summary of prospect's background"""
    college_class: Annotated[CollegeClassEnum, pydantic.Field(alias="collegeClass")]
    r"""College year of the prospect"""
    draft_grade: Annotated[Optional[float], pydantic.Field(alias="draftGrade")] = None
    r"""0-100 overall grade"""
    draft_projection: Annotated[
        Optional[str], pydantic.Field(alias="draftProjection")
    ] = None
    r"""Anticipated draft outcome for the prospect"""
    forty_yard_dash: Annotated[
        Optional[FortyYardDash], pydantic.Field(alias="fortyYardDash")
    ] = None
    r"""Forty yard dash outcome"""
    grade: Optional[float] = None
    r""""""
    hand_size: Annotated[Optional[float], pydantic.Field(alias="handSize")] = None
    r"""Thumb to pinky tip measurement, precise to 1/8 inch"""
    headshot: Optional[str] = None
    r"""URL to the prospect's headshot"""
    height: float
    r"""Prospect height in inches"""
    nfl_comparison: Annotated[Optional[str], pydantic.Field(alias="nflComparison")] = (
        None
    )
    r"""Name of an NFL player with a similar profile"""
    overview: Optional[str] = None
    r"""HTML formatted snippet with scouting elevator pitch"""
    production_score: Annotated[
        Optional[float], pydantic.Field(alias="productionScore")
    ] = None
    r"""0-100 grade of player's on-field statistical profile"""
    profile_author: Annotated[Optional[str], pydantic.Field(alias="profileAuthor")] = (
        None
    )
    r"""Name of the person who wrote the scouting profile"""
    pro_forty_yard_dash: Annotated[
        Optional[FortyYardDash], pydantic.Field(alias="proFortyYardDash")
    ] = None
    r"""Forty yard dash from prospect's pro day"""
    sources_tell_us: Annotated[Optional[str], pydantic.Field(alias="sourcesTellUs")] = (
        None
    )
    r"""HTML - Comments on the prospect from talent evaluators around the league"""
    strengths: Optional[str] = None
    r"""HTML - Prospect strengths"""
    ten_yard_split: Annotated[
        Optional[TenYardSplit], pydantic.Field(alias="tenYardSplit")
    ] = None
    r"""Ten yard split time in 40 yd dash"""
    three_cone_drill: Annotated[
        Optional[ThreeConeDrill], pydantic.Field(alias="threeConeDrill")
    ] = None
    r"""Three cone drill result"""
    twenty_yard_shuffle: Annotated[
        Optional[TwentyYardShuffle], pydantic.Field(alias="twentyYardShuffle")
    ] = None
    r"""Twenty yard shuffle result"""
    weaknesses: Optional[str] = None
    r"""HTML - Prospect weaknesses"""
    combine_attendance: Annotated[bool, pydantic.Field(alias="combineAttendance")]
    r"""Whether or not the prospect attended the official scouting combine"""
    position: str
    # TODO: Make this field a complete enum
    r"""Player's position in college"""
    position_group: Annotated[Optional[str], pydantic.Field(alias="positionGroup")] = (
        None
    )
    # TODO: Create complete enum
    r"""Position group in college"""
    vertical_jump: Annotated[
        Optional[VerticalJump], pydantic.Field(alias="verticalJump")
    ] = None
    r"""Vertical jump result"""
    weight: float
    r"""Weight in pounds"""
