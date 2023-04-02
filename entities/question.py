from dataclasses import dataclass
from enum import auto
from enum import Enum

from protocols import Composable
from protocols import ComposableOption


class QuestionType(Enum):
    OBJ = auto()
    SUB = auto()
    OBJ_ALT = auto()
    OBJ_VF = auto()


@dataclass
class Question:
    type: QuestionType
    text: Composable
    number: Composable
    options: list[ComposableOption]
    altoptions: list[Composable]
    vfoptions: list[Composable]
    images: list[Composable]
    answer: int

    def get_answer(self) -> ComposableOption:
        for option in self.options:
            if option.is_answer:
                return option
        # TODO: it should raise an specific error
        raise NotImplementedError
