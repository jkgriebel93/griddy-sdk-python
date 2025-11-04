from typing import Literal

DefensePositionEnum = Literal[
    "FS",
    "SS",
    "CB",
    "SCB",
    "ILB",
    "OLB",
    "MLB",
    "DE",
    "DT",
    "NT",
]

DefensePositionGroupEnum = Literal[
    "DB",
    "DL",
    "LB",
]

DefenseNGSPositionEnum = Literal[
    "S",
    "CB",
    "SCB",
    "LB",
    "DE",
    "DT",
]
r"""Next Gen Stats position"""


DefenseNGSPositionGroupEnum = Literal["DL", "LB", "DB"]
