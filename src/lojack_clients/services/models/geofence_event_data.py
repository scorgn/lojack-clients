from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeofenceEventData")


@attr.s(auto_attribs=True)
class GeofenceEventData:
    """
    Attributes:
        geofence_id (Union[Unset, str]):  Example: 1140762987615GIDWGA.
    """

    geofence_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        geofence_id = self.geofence_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if geofence_id is not UNSET:
            field_dict["geofenceId"] = geofence_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        geofence_id = d.pop("geofenceId", UNSET)

        geofence_event_data = cls(
            geofence_id=geofence_id,
        )

        geofence_event_data.additional_properties = d
        return geofence_event_data

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
