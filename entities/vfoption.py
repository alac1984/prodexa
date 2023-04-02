from dataclasses import dataclass


@dataclass
class VFOption:
    text: str
    _complete: bool

    def is_complete(self):
        return self._complete
