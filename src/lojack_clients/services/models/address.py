from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@attr.s(auto_attribs=True)
class Address:
    """
    Attributes:
        line1 (Union[Unset, str]):  Example: 123 Street Name.
        city (Union[Unset, str]):  Example: City Name.
        state_or_province (Union[Unset, str]):  Example: ST.
        postal_code (Union[Unset, str]):  Example: 30098.
    """

    line1: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state_or_province: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        line1 = self.line1
        city = self.city
        state_or_province = self.state_or_province
        postal_code = self.postal_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line1 is not UNSET:
            field_dict["line1"] = line1
        if city is not UNSET:
            field_dict["city"] = city
        if state_or_province is not UNSET:
            field_dict["stateOrProvince"] = state_or_province
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        line1 = d.pop("line1", UNSET)

        city = d.pop("city", UNSET)

        state_or_province = d.pop("stateOrProvince", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        address = cls(
            line1=line1,
            city=city,
            state_or_province=state_or_province,
            postal_code=postal_code,
        )

        address.additional_properties = d
        return address

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
