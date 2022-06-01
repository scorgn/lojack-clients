from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.event_gps_fix_quality import EventGpsFixQuality
from ..models.event_type import EventType
from ..models.geofence_event_data import GeofenceEventData
from ..models.location import Location
from ..models.null_value import NullValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="Event")


@attr.s(auto_attribs=True)
class Event:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 9085a727-a00f-4ee6-9363-603a6266b0d5.
        type (Union[Unset, EventType]):
        location (Union[Unset, Location]):
        date (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        odometer (Union[Unset, float]):  Example: 324.19.
        battery_voltage (Union[Unset, float]):  Example: 15.124.
        heading (Union[Unset, int]):  Example: 250.
        speed (Union[Unset, int]):
        engine_hours (Union[Unset, int]):
        distance_driven (Union[Unset, float]):  Example: 724.241.
        signal_strength (Union[Unset, float]):  Example: 0.815.
        gps_fix_quality (Union[Unset, EventGpsFixQuality]):
        event_data (Union[GeofenceEventData, NullValue, Unset]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, EventType] = UNSET
    location: Union[Unset, Location] = UNSET
    date: Union[Unset, str] = UNSET
    odometer: Union[Unset, float] = UNSET
    battery_voltage: Union[Unset, float] = UNSET
    heading: Union[Unset, int] = UNSET
    speed: Union[Unset, int] = UNSET
    engine_hours: Union[Unset, int] = UNSET
    distance_driven: Union[Unset, float] = UNSET
    signal_strength: Union[Unset, float] = UNSET
    gps_fix_quality: Union[Unset, EventGpsFixQuality] = UNSET
    event_data: Union[GeofenceEventData, NullValue, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        date = self.date
        odometer = self.odometer
        battery_voltage = self.battery_voltage
        heading = self.heading
        speed = self.speed
        engine_hours = self.engine_hours
        distance_driven = self.distance_driven
        signal_strength = self.signal_strength
        gps_fix_quality: Union[Unset, str] = UNSET
        if not isinstance(self.gps_fix_quality, Unset):
            gps_fix_quality = self.gps_fix_quality.value

        event_data: Union[Dict[str, Any], Unset, str]
        if isinstance(self.event_data, Unset):
            event_data = UNSET

        elif isinstance(self.event_data, GeofenceEventData):
            event_data = UNSET
            if not isinstance(self.event_data, Unset):
                event_data = self.event_data.to_dict()

        else:
            event_data = UNSET
            if not isinstance(self.event_data, Unset):
                event_data = self.event_data.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if location is not UNSET:
            field_dict["location"] = location
        if date is not UNSET:
            field_dict["date"] = date
        if odometer is not UNSET:
            field_dict["odometer"] = odometer
        if battery_voltage is not UNSET:
            field_dict["batteryVoltage"] = battery_voltage
        if heading is not UNSET:
            field_dict["heading"] = heading
        if speed is not UNSET:
            field_dict["speed"] = speed
        if engine_hours is not UNSET:
            field_dict["engineHours"] = engine_hours
        if distance_driven is not UNSET:
            field_dict["distanceDriven"] = distance_driven
        if signal_strength is not UNSET:
            field_dict["signalStrength"] = signal_strength
        if gps_fix_quality is not UNSET:
            field_dict["gpsFixQuality"] = gps_fix_quality
        if event_data is not UNSET:
            field_dict["eventData"] = event_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EventType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EventType(_type)

        _location = d.pop("location", UNSET)
        location: Union[Unset, Location]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = Location.from_dict(_location)

        date = d.pop("date", UNSET)

        odometer = d.pop("odometer", UNSET)

        battery_voltage = d.pop("batteryVoltage", UNSET)

        heading = d.pop("heading", UNSET)

        speed = d.pop("speed", UNSET)

        engine_hours = d.pop("engineHours", UNSET)

        distance_driven = d.pop("distanceDriven", UNSET)

        signal_strength = d.pop("signalStrength", UNSET)

        _gps_fix_quality = d.pop("gpsFixQuality", UNSET)
        gps_fix_quality: Union[Unset, EventGpsFixQuality]
        if isinstance(_gps_fix_quality, Unset):
            gps_fix_quality = UNSET
        else:
            gps_fix_quality = EventGpsFixQuality(_gps_fix_quality)

        def _parse_event_data(data: object) -> Union[GeofenceEventData, NullValue, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _event_data_type_0 = data
                event_data_type_0: Union[Unset, GeofenceEventData]
                if isinstance(_event_data_type_0, Unset):
                    event_data_type_0 = UNSET
                else:
                    event_data_type_0 = GeofenceEventData.from_dict(_event_data_type_0)

                return event_data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            _event_data_type_1 = data
            event_data_type_1: Union[Unset, NullValue]
            if isinstance(_event_data_type_1, Unset):
                event_data_type_1 = UNSET
            else:
                event_data_type_1 = NullValue(_event_data_type_1)

            return event_data_type_1

        event_data = _parse_event_data(d.pop("eventData", UNSET))

        event = cls(
            id=id,
            type=type,
            location=location,
            date=date,
            odometer=odometer,
            battery_voltage=battery_voltage,
            heading=heading,
            speed=speed,
            engine_hours=engine_hours,
            distance_driven=distance_driven,
            signal_strength=signal_strength,
            gps_fix_quality=gps_fix_quality,
            event_data=event_data,
        )

        event.additional_properties = d
        return event

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
