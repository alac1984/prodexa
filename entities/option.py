from dataclasses import dataclass

from .image import Image


@dataclass
class Option:
    letter: str
    text: str
    image: Image | None = None
    _complete: bool = False
    _answer: bool = False

    @property
    def is_complete(self):
        return self._complete

    @property
    def is_answer(self):
        return self._answer
