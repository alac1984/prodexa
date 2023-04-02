from dataclasses import dataclass
from datetime import date

from .question import Question
from protocols import ComposableOption


@dataclass
class Test:
    created: date
    questions: list[Question]

    def get_all_answers(self) -> list[ComposableOption]:
        answers = []
        for question in self.questions:
            answers.append(question.get_answer())

        return answers
