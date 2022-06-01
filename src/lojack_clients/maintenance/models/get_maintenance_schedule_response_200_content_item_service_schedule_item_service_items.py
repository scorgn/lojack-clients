from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_maintenance_schedule_response_200_content_item_service_schedule_item_service_items_severity import (
    GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItemsSeverity,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItems")


@attr.s(auto_attribs=True)
class GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItems:
    """
    Attributes:
        severity (Union[Unset, GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItemsSeverity]):
            Example: Normal.
        action (Union[Unset, str]):  Example: Inspect.
        literal_name (Union[Unset, str]):  Example: Floor Mat Inspect.
    """

    severity: Union[Unset, GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItemsSeverity] = UNSET
    action: Union[Unset, str] = UNSET
    literal_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        severity: Union[Unset, str] = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        action = self.action
        literal_name = self.literal_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if severity is not UNSET:
            field_dict["severity"] = severity
        if action is not UNSET:
            field_dict["action"] = action
        if literal_name is not UNSET:
            field_dict["literalName"] = literal_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _severity = d.pop("severity", UNSET)
        severity: Union[Unset, GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItemsSeverity]
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = GetMaintenanceScheduleResponse200ContentItemServiceScheduleItemServiceItemsSeverity(_severity)

        action = d.pop("action", UNSET)

        literal_name = d.pop("literalName", UNSET)

        get_maintenance_schedule_response_200_content_item_service_schedule_item_service_items = cls(
            severity=severity,
            action=action,
            literal_name=literal_name,
        )

        get_maintenance_schedule_response_200_content_item_service_schedule_item_service_items.additional_properties = d
        return get_maintenance_schedule_response_200_content_item_service_schedule_item_service_items

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
