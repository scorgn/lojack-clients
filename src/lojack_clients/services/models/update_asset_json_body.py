from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.update_asset_json_body_attributes import UpdateAssetJsonBodyAttributes
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAssetJsonBody")


@attr.s(auto_attribs=True)
class UpdateAssetJsonBody:
    """
    Attributes:
        attributes (Union[Unset, UpdateAssetJsonBodyAttributes]):
        id (Union[Unset, str]): Asset ID Example: 272956057382HD3JBSD24.
        make (Union[Unset, str]):  Example: Ford.
        model (Union[Unset, str]):  Example: Explorer.
        name (Union[Unset, str]):  Example: Consumer Asset VINNUMBER12345.
        odometer (Union[Unset, str]):  Example: 519.89.
        vin (Union[Unset, str]):  Example: VINNUMBER12345.
        year (Union[Unset, str]):  Example: 2022.
    """

    attributes: Union[Unset, UpdateAssetJsonBodyAttributes] = UNSET
    id: Union[Unset, str] = UNSET
    make: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    odometer: Union[Unset, str] = UNSET
    vin: Union[Unset, str] = UNSET
    year: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        id = self.id
        make = self.make
        model = self.model
        name = self.name
        odometer = self.odometer
        vin = self.vin
        year = self.year

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if id is not UNSET:
            field_dict["id"] = id
        if make is not UNSET:
            field_dict["make"] = make
        if model is not UNSET:
            field_dict["model"] = model
        if name is not UNSET:
            field_dict["name"] = name
        if odometer is not UNSET:
            field_dict["odometer"] = odometer
        if vin is not UNSET:
            field_dict["vin"] = vin
        if year is not UNSET:
            field_dict["year"] = year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, UpdateAssetJsonBodyAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = UpdateAssetJsonBodyAttributes.from_dict(_attributes)

        id = d.pop("id", UNSET)

        make = d.pop("make", UNSET)

        model = d.pop("model", UNSET)

        name = d.pop("name", UNSET)

        odometer = d.pop("odometer", UNSET)

        vin = d.pop("vin", UNSET)

        year = d.pop("year", UNSET)

        update_asset_json_body = cls(
            attributes=attributes,
            id=id,
            make=make,
            model=model,
            name=name,
            odometer=odometer,
            vin=vin,
            year=year,
        )

        update_asset_json_body.additional_properties = d
        return update_asset_json_body

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
