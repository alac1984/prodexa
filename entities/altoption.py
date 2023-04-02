from dataclasses import dataclass

from .image import Image


@dataclass
class AltOption:
    letter: str
    text: str
    image: Image | None = None
    _complete: bool = False

    @property
    def is_complete(self):
        return self._complete
