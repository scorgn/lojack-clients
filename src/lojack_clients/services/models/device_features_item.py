from enum import Enum


class DeviceFeaturesItem(str, Enum):
    QUICK_LOCATE = "QUICK_LOCATE"
    NSPIRE_V2 = "NSPIRE_V2"

    def __str__(self) -> str:
        return str(self.value)
