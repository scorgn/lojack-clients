from enum import Enum


class CommandRequestJsonBodyResponseStrategy(str, Enum):
    PUSH_NOTIFICATION = "PUSH_NOTIFICATION"

    def __str__(self) -> str:
        return str(self.value)
