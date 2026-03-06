from typing import Literal

DesignationEnum = Literal["OFFICIAL", "UNOFFICIAL"]


CollegeClassEnum = Literal["R-Sophomore", "R-Junior", "R-Senior", "Junior", "Senior"]

CombinePositionEnum = Literal[
    "C",
    "CB",
    "DE",
    "DT",
    "EDGE",
    "FB",
    "FS",
    "G",
    "ILB",
    "IOL",
    "K",
    "LB",
    "LS",
    "NT",
    "OG",
    "OLB",
    "OT",
    "P",
    "QB",
    "RB",
    "S",
    "SS",
    "T",
    "TE",
    "WR",
]
r"""NFL Combine prospect position"""

CombinePositionGroupEnum = Literal[
    "DB",
    "DL",
    "LB",
    "OL",
    "QB",
    "RB",
    "SPEC",
    "TE",
    "WR",
]
r"""NFL Combine prospect position group"""

EventFilterEnum = Literal[
    "FORTY_YARD_DASH",
    "TEN_YARD_SPLIT",
    "VERTICAL_JUMP",
    "BROAD_JUMP",
    "THREE_CONE_DRILL",
    "TWENTY_YARD_SHUTTLE",
    "BENCH_PRESS",
]
