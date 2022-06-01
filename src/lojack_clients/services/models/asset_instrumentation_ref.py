from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetInstrumentationRef")


@attr.s(auto_attribs=True)
class AssetInstrumentationRef:
    """
    Attributes:
        id (Union[Unset, str]): Asset ID Example: 272956057382HD3JBSD24.
        device_id (Union[Unset, str]): Device ID Example: 38261738B7DG937BXMQ3.
    """

    id: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        device_id = self.device_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        device_id = d.pop("deviceId", UNSET)

        asset_instrumentation_ref = cls(
            id=id,
            device_id=device_id,
        )

        asset_instrumentation_ref.additional_properties = d
        return asset_instrumentation_ref

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
