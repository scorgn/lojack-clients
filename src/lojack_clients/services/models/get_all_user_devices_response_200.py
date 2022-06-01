from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.device import Device
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAllUserDevicesResponse200")


@attr.s(auto_attribs=True)
class GetAllUserDevicesResponse200:
    """
    Attributes:
        content (Union[Unset, List[Device]]):
    """

    content: Union[Unset, List[Device]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()

                content.append(content_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content = []
        _content = d.pop("content", UNSET)
        for content_item_data in _content or []:
            content_item = Device.from_dict(content_item_data)

            content.append(content_item)

        get_all_user_devices_response_200 = cls(
            content=content,
        )

        get_all_user_devices_response_200.additional_properties = d
        return get_all_user_devices_response_200

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
