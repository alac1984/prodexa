from dataclasses import dataclass


@dataclass
class QuestionNumber:
    raw: str
    number: int
    decorator: str

    def normalized(self):
        return f"{self.number}. "
