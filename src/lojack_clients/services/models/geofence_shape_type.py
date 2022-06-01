from enum import Enum


class GeofenceShapeType(str, Enum):
    RECTANGLE = "RECTANGLE"

    def __str__(self) -> str:
        return str(self.value)
