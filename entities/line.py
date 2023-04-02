from dataclasses import dataclass
from enum import auto
from enum import Enum

from protocols import Composable


class LineType(Enum):
    TEXT = auto()
    QUESTION = auto()
    BLANK = auto()
    IMAGE = auto()
    OPTION = auto()
    FILL = auto()
    ALT_OPTION = auto()
    TF_OPTION = auto()
    SOURCE = auto()


@dataclass
class Line:
    type: LineType
    content: str
    composed: bool
    composables: list[Composable]
