from enum import Enum


class GetSpecificUserPreferencesNamespace(str, Enum):
    CONSUMERMOBILE_SKYLINK = "consumerMobile.SkyLink"

    def __str__(self) -> str:
        return str(self.value)
