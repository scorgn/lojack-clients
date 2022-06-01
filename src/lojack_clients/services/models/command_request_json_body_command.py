from enum import Enum


class CommandRequestJsonBodyCommand(str, Enum):
    LOCATE = "locate"

    def __str__(self) -> str:
        return str(self.value)
