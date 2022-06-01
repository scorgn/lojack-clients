from enum import Enum


class PreferenceKey(str, Enum):
    APPTHEME = "appTheme"
    GEOFENCEALERT_EMAIL = "GeofenceAlert.email"
    GEOFENCEALERT_PUSHNOTIFICATION = "GeofenceAlert.pushNotification"
    LOWBATTERYALERT_EMAIL = "LowBatteryAlert.email"
    LOWBATTERYALERT_PUSHNOTIFICATION = "LowBatteryAlert.pushNotification"
    SERVICEALERTS_EMAIL = "ServiceAlerts.email"
    SERVICEALERTS_PUSHNOTIFICATION = "ServiceAlerts.pushNotification"
    SPEEDALERT_EMAIL = "SpeedAlert.email"
    SPEEDALERT_PUSHNOTIFICATION = "SpeedAlert.pushNotification"

    def __str__(self) -> str:
        return str(self.value)
