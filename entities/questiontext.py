from dataclasses import dataclass


@dataclass
class QuestionText:
    text: str
    _complete: bool

    @property
    def is_complete(self):
        return self.is_complete
