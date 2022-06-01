from enum import Enum


class EventType(str, Enum):
    EXT_PWR_LOW = "EXT_PWR_LOW"
    SPEED = "SPEED"
    MOVE_START = "MOVE_START"
    MOVE_STOP = "MOVE_STOP"
    MOVE_PER = "MOVE_PER"
    TRIP_START = "TRIP_START"
    TRIP_STOP = "TRIP_STOP"
    SLEEP_ENTER = "SLEEP_ENTER"
    CFG_RESP = "CFG_RESP"
    USER_LOC = "USER_LOC"
    AUTO_LOC = "AUTO_LOC"
    GEO_ENTER = "GEO_ENTER"
    GEO_EXIT = "GEO_EXIT"

    def __str__(self) -> str:
        return str(self.value)
