from enum import Enum


class AssetStatus(str, Enum):
    STOPPED = "Stopped"

    def __str__(self) -> str:
        return str(self.value)
