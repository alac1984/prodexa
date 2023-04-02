from dataclasses import dataclass


@dataclass
class Text:
    raw: str
    _complete: bool = False

    def is_complete(self):
        return self._complete
