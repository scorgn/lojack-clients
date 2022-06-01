from enum import Enum


class CommandRequestResponse201ResponseStrategy(str, Enum):
    PUSH_NOTIFICATION = "PUSH_NOTIFICATION"

    def __str__(self) -> str:
        return str(self.value)
