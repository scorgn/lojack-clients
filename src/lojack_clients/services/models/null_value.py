from enum import Enum


class NullValue(str, Enum):
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
