from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.asset_attributes import AssetAttributes
from ..models.asset_custom_attributes import AssetCustomAttributes
from ..models.asset_instrumentation_ref import AssetInstrumentationRef
from ..models.asset_status import AssetStatus
from ..models.location import Location
from ..types import UNSET, Unset

T = TypeVar("T", bound="Asset")


@attr.s(auto_attribs=True)
class Asset:
    """
    Attributes:
        id (Union[Unset, str]): Asset ID Example: 272956057382HD3JBSD24.
        active (Union[Unset, bool]):  Example: True.
        name (Union[Unset, str]):  Example: Consumer Asset VINNUMBER12345.
        make (Union[Unset, str]):  Example: Ford.
        model (Union[Unset, str]):  Example: Explorer.
        year (Union[Unset, int]):  Example: 2022.
        vin (Union[Unset, str]):  Example: VINNUMBER12345.
        initial_odometer (Union[Unset, float]):  Example: 9.
        odometer (Union[Unset, float]):  Example: 516.83.
        distance_driven (Union[Unset, float]):  Example: 525.83.
        internal_battery_voltage (Union[Unset, float]):
        attributes (Union[Unset, AssetAttributes]):
        custom_attributes (Union[Unset, AssetCustomAttributes]):
        last_location (Union[Unset, Location]):
        location_last_reported (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        speed (Union[Unset, float]):
        status (Union[Unset, AssetStatus]):  Example: Stopped.
        status_start_date (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        battery_voltage (Union[Unset, float]):  Example: 12.941.
        created_by (Union[Unset, str]):  Example: enterpriseIntegrationServices@spireon.com.
        updated_by (Union[Unset, str]):  Example: username31.
        date_created (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        last_updated (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        instrumentation_ref (Union[Unset, AssetInstrumentationRef]):
    """

    id: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    make: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    year: Union[Unset, int] = UNSET
    vin: Union[Unset, str] = UNSET
    initial_odometer: Union[Unset, float] = UNSET
    odometer: Union[Unset, float] = UNSET
    distance_driven: Union[Unset, float] = UNSET
    internal_battery_voltage: Union[Unset, float] = UNSET
    attributes: Union[Unset, AssetAttributes] = UNSET
    custom_attributes: Union[Unset, AssetCustomAttributes] = UNSET
    last_location: Union[Unset, Location] = UNSET
    location_last_reported: Union[Unset, str] = UNSET
    speed: Union[Unset, float] = UNSET
    status: Union[Unset, AssetStatus] = UNSET
    status_start_date: Union[Unset, str] = UNSET
    battery_voltage: Union[Unset, float] = UNSET
    created_by: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    instrumentation_ref: Union[Unset, AssetInstrumentationRef] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        active = self.active
        name = self.name
        make = self.make
        model = self.model
        year = self.year
        vin = self.vin
        initial_odometer = self.initial_odometer
        odometer = self.odometer
        distance_driven = self.distance_driven
        internal_battery_voltage = self.internal_battery_voltage
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        custom_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_attributes, Unset):
            custom_attributes = self.custom_attributes.to_dict()

        last_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_location, Unset):
            last_location = self.last_location.to_dict()

        location_last_reported = self.location_last_reported
        speed = self.speed
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_start_date = self.status_start_date
        battery_voltage = self.battery_voltage
        created_by = self.created_by
        updated_by = self.updated_by
        date_created = self.date_created
        last_updated = self.last_updated
        instrumentation_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.instrumentation_ref, Unset):
            instrumentation_ref = self.instrumentation_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if active is not UNSET:
            field_dict["active"] = active
        if name is not UNSET:
            field_dict["name"] = name
        if make is not UNSET:
            field_dict["make"] = make
        if model is not UNSET:
            field_dict["model"] = model
        if year is not UNSET:
            field_dict["year"] = year
        if vin is not UNSET:
            field_dict["vin"] = vin
        if initial_odometer is not UNSET:
            field_dict["initialOdometer"] = initial_odometer
        if odometer is not UNSET:
            field_dict["odometer"] = odometer
        if distance_driven is not UNSET:
            field_dict["distanceDriven"] = distance_driven
        if internal_battery_voltage is not UNSET:
            field_dict["internalBatteryVoltage"] = internal_battery_voltage
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if custom_attributes is not UNSET:
            field_dict["customAttributes"] = custom_attributes
        if last_location is not UNSET:
            field_dict["lastLocation"] = last_location
        if location_last_reported is not UNSET:
            field_dict["locationLastReported"] = location_last_reported
        if speed is not UNSET:
            field_dict["speed"] = speed
        if status is not UNSET:
            field_dict["status"] = status
        if status_start_date is not UNSET:
            field_dict["statusStartDate"] = status_start_date
        if battery_voltage is not UNSET:
            field_dict["batteryVoltage"] = battery_voltage
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if instrumentation_ref is not UNSET:
            field_dict["instrumentationRef"] = instrumentation_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        active = d.pop("active", UNSET)

        name = d.pop("name", UNSET)

        make = d.pop("make", UNSET)

        model = d.pop("model", UNSET)

        year = d.pop("year", UNSET)

        vin = d.pop("vin", UNSET)

        initial_odometer = d.pop("initialOdometer", UNSET)

        odometer = d.pop("odometer", UNSET)

        distance_driven = d.pop("distanceDriven", UNSET)

        internal_battery_voltage = d.pop("internalBatteryVoltage", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, AssetAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = AssetAttributes.from_dict(_attributes)

        _custom_attributes = d.pop("customAttributes", UNSET)
        custom_attributes: Union[Unset, AssetCustomAttributes]
        if isinstance(_custom_attributes, Unset):
            custom_attributes = UNSET
        else:
            custom_attributes = AssetCustomAttributes.from_dict(_custom_attributes)

        _last_location = d.pop("lastLocation", UNSET)
        last_location: Union[Unset, Location]
        if isinstance(_last_location, Unset):
            last_location = UNSET
        else:
            last_location = Location.from_dict(_last_location)

        location_last_reported = d.pop("locationLastReported", UNSET)

        speed = d.pop("speed", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, AssetStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = AssetStatus(_status)

        status_start_date = d.pop("statusStartDate", UNSET)

        battery_voltage = d.pop("batteryVoltage", UNSET)

        created_by = d.pop("createdBy", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        _instrumentation_ref = d.pop("instrumentationRef", UNSET)
        instrumentation_ref: Union[Unset, AssetInstrumentationRef]
        if isinstance(_instrumentation_ref, Unset):
            instrumentation_ref = UNSET
        else:
            instrumentation_ref = AssetInstrumentationRef.from_dict(_instrumentation_ref)

        asset = cls(
            id=id,
            active=active,
            name=name,
            make=make,
            model=model,
            year=year,
            vin=vin,
            initial_odometer=initial_odometer,
            odometer=odometer,
            distance_driven=distance_driven,
            internal_battery_voltage=internal_battery_voltage,
            attributes=attributes,
            custom_attributes=custom_attributes,
            last_location=last_location,
            location_last_reported=location_last_reported,
            speed=speed,
            status=status,
            status_start_date=status_start_date,
            battery_voltage=battery_voltage,
            created_by=created_by,
            updated_by=updated_by,
            date_created=date_created,
            last_updated=last_updated,
            instrumentation_ref=instrumentation_ref,
        )

        asset.additional_properties = d
        return asset

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
