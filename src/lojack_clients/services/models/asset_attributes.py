from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetAttributes")


@attr.s(auto_attribs=True)
class AssetAttributes:
    """
    Attributes:
        color (Union[Unset, str]):  Example: Black.
        installation_date (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        device_status (Union[Unset, str]):  Example: Installed.
    """

    color: Union[Unset, str] = UNSET
    installation_date: Union[Unset, str] = UNSET
    device_status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        color = self.color
        installation_date = self.installation_date
        device_status = self.device_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if color is not UNSET:
            field_dict["color"] = color
        if installation_date is not UNSET:
            field_dict["installationDate"] = installation_date
        if device_status is not UNSET:
            field_dict["deviceStatus"] = device_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        color = d.pop("color", UNSET)

        installation_date = d.pop("installationDate", UNSET)

        device_status = d.pop("deviceStatus", UNSET)

        asset_attributes = cls(
            color=color,
            installation_date=installation_date,
            device_status=device_status,
        )

        asset_attributes.additional_properties = d
        return asset_attributes

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
