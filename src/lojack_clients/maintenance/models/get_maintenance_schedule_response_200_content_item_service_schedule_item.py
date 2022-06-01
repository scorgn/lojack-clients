from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_maintenance_schedule_response_200_content_item_service_schedule_item_service_items import (
    GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItems,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMaintenanceScheduleResponse200ContentItemServiceScheduleItem")


@attr.s(auto_attribs=True)
class GetMaintenanceScheduleResponse200ContentItemServiceScheduleItem:
    """
    Attributes:
        mileage (Union[Unset, float]):  Example: 15000.
        service_items (Union[Unset, GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItems]):
    """

    mileage: Union[Unset, float] = UNSET
    service_items: Union[Unset, GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItems] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mileage = self.mileage
        service_items: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service_items, Unset):
            service_items = self.service_items.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mileage is not UNSET:
            field_dict["mileage"] = mileage
        if service_items is not UNSET:
            field_dict["serviceItems"] = service_items

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mileage = d.pop("mileage", UNSET)

        _service_items = d.pop("serviceItems", UNSET)
        service_items: Union[Unset, GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItems]
        if isinstance(_service_items, Unset):
            service_items = UNSET
        else:
            service_items = GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItems.from_dict(
                _service_items
            )

        get_maintenance_schedule_response_200_content_item_service_schedule_item = cls(
            mileage=mileage,
            service_items=service_items,
        )

        get_maintenance_schedule_response_200_content_item_service_schedule_item.additional_properties = d
        return get_maintenance_schedule_response_200_content_item_service_schedule_item

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
