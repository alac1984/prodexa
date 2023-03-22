import re
from enum import auto
from enum import Enum
from typing import Protocol
from typing import TextIO

# Loop throught the file
# At each line, check its type
# If a line is the beggining of a question, start question extraction
# Gets question number and text
# If next line is more text, join it with previous question text
# If next line is extendend options
# If next line is question option, gets option value and text
# If is not blank, the code categorize


class Token(Protocol):
    @property
    def normalize(self) -> str:
        """Property that normalize the current token"""


class LineType(Enum):
    BLANK = auto()
    QUESTION_NUM = auto()
    QUESTION_OPT = auto()
    EXTENDEND_OPT = auto()
    TRUE_FALSE_OPT = auto()
    IMG_REF = auto()
    TEXT = auto()


class Line:
    def __init__(self, text: str):
        self.text = text
        self.type: LineType | None = None
        self.tokens: list[Token] = []

    @property
    def is_processed(self):
        """Return if a line was already processed (typed)"""
        return self.type is not None


class QuestionNumber:
    def __init__(self, value: str):
        self.value = value

    @property
    def normalize(self):
        """Function that normalize the question number format"""
        ...


class Lexer:
    def __init__(self, file: TextIO):
        self.file = file

    def check_line(self, line: str):
        """
        Check the current line and return if:
            - Line is blank
            - Line starts with question number
            - Line starts with text
            - Line starts with option
        """
        ...


with open("sample.txt") as f:
    breakpoint()
    for line in f:
        match = re.search("Imagine", line)
        if match:
            print(match.group())
