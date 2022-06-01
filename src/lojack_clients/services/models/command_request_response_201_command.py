from enum import Enum


class CommandRequestResponse201Command(str, Enum):
    LOCATE = "locate"

    def __str__(self) -> str:
        return str(self.value)
