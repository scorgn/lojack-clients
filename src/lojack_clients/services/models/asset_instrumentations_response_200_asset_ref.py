from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetInstrumentationsResponse200AssetRef")


@attr.s(auto_attribs=True)
class AssetInstrumentationsResponse200AssetRef:
    """
    Attributes:
        id (Union[Unset, str]): Asset ID Example: 272956057382HD3JBSD24.
        name (Union[Unset, str]):  Example: Consumer Asset VINNUMBER12356,.
        vin (Union[Unset, str]):  Example: VINNUMBER12345.
        href (Union[Unset, str]):  Example: /assets/272956057382HD3JBSD24.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    vin: Union[Unset, str] = UNSET
    href: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        vin = self.vin
        href = self.href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if vin is not UNSET:
            field_dict["vin"] = vin
        if href is not UNSET:
            field_dict["href"] = href

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        vin = d.pop("vin", UNSET)

        href = d.pop("href", UNSET)

        asset_instrumentations_response_200_asset_ref = cls(
            id=id,
            name=name,
            vin=vin,
            href=href,
        )

        asset_instrumentations_response_200_asset_ref.additional_properties = d
        return asset_instrumentations_response_200_asset_ref

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
