from dataclasses import dataclass


@dataclass
class QuestionNumber:
    raw: str
    number: int
    decorator: str
    _complete: bool

    def normalized(self):
        return f"{self.number}. "

    @property
    def is_complete(self):
        return self._complete
