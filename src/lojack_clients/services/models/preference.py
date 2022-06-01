from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.preference_key import PreferenceKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="Preference")


@attr.s(auto_attribs=True)
class Preference:
    """
    Attributes:
        key (Union[Unset, PreferenceKey]):
        value (Union[Unset, bool]):
        namespace (Union[Unset, str]):  Example: consumerMobile.SkyLink.
    """

    key: Union[Unset, PreferenceKey] = UNSET
    value: Union[Unset, bool] = UNSET
    namespace: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key: Union[Unset, str] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.value

        value = self.value
        namespace = self.namespace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if namespace is not UNSET:
            field_dict["namespace"] = namespace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _key = d.pop("key", UNSET)
        key: Union[Unset, PreferenceKey]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = PreferenceKey(_key)

        value = d.pop("value", UNSET)

        namespace = d.pop("namespace", UNSET)

        preference = cls(
            key=key,
            value=value,
            namespace=namespace,
        )

        preference.additional_properties = d
        return preference

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
