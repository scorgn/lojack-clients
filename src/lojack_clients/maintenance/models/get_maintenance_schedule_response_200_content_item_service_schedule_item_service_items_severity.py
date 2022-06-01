from enum import Enum


class GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItemsSeverity(str, Enum):
    NORMAL = "Normal"
    SEVERE = "Severe"

    def __str__(self) -> str:
        return str(self.value)
