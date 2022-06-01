from enum import Enum


class EventGpsFixQuality(str, Enum):
    GOOD = "GOOD"
    BAD = "BAD"
    HISTORIC = "HISTORIC"

    def __str__(self) -> str:
        return str(self.value)
