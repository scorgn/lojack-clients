from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_maintenance_schedule_response_200_content_item_service_schedule_item import (
    GetMaintenanceScheduleResponse200ContentItemServiceScheduleItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMaintenanceScheduleResponse200ContentItem")


@attr.s(auto_attribs=True)
class GetMaintenanceScheduleResponse200ContentItem:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 8e4cd954-41a3-4a1f-98d4-ab6b306614d9.
        service_interval (Union[Unset, float]): The mileage interval at which services are recommend (eg. new services
            every 5000 miles) Example: 5000.
        service_schedule (Union[Unset, List[GetMaintenanceScheduleResponse200ContentItemServiceScheduleItem]]):
    """

    id: Union[Unset, str] = UNSET
    service_interval: Union[Unset, float] = UNSET
    service_schedule: Union[Unset, List[GetMaintenanceScheduleResponse200ContentItemServiceScheduleItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        service_interval = self.service_interval
        service_schedule: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.service_schedule, Unset):
            service_schedule = []
            for service_schedule_item_data in self.service_schedule:
                service_schedule_item = service_schedule_item_data.to_dict()

                service_schedule.append(service_schedule_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if service_interval is not UNSET:
            field_dict["serviceInterval"] = service_interval
        if service_schedule is not UNSET:
            field_dict["serviceSchedule"] = service_schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        service_interval = d.pop("serviceInterval", UNSET)

        service_schedule = []
        _service_schedule = d.pop("serviceSchedule", UNSET)
        for service_schedule_item_data in _service_schedule or []:
            service_schedule_item = GetMaintenanceScheduleResponse200ContentItemServiceScheduleItem.from_dict(
                service_schedule_item_data
            )

            service_schedule.append(service_schedule_item)

        get_maintenance_schedule_response_200_content_item = cls(
            id=id,
            service_interval=service_interval,
            service_schedule=service_schedule,
        )

        get_maintenance_schedule_response_200_content_item.additional_properties = d
        return get_maintenance_schedule_response_200_content_item

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
