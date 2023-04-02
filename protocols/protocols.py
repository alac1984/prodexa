from typing import Protocol


class Composable(Protocol):
    @property
    def is_complete(self) -> bool:
        """
        Returns True if Composable is complete, False otherwise
        """


class ComposableOption(Protocol):
    @property
    def is_complete(self) -> bool:
        """
        Returns True if ComposableQuestion is complete, False otherwise
        """

    @property
    def is_answer(self) -> bool:
        """
        Returns a question answer
        """
