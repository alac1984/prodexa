from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .question import Question


@dataclass
class Image:
    path: Path
    created: date
    question: Question
