from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.asset_instrumentations_response_200_device_ref_features_item import (
    AssetInstrumentationsResponse200DeviceRefFeaturesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetInstrumentationsResponse200DeviceRef")


@attr.s(auto_attribs=True)
class AssetInstrumentationsResponse200DeviceRef:
    """
    Attributes:
        id (Union[Unset, str]): Asset ID Example: 272956057382HD3JBSD24.
        serial_number (Union[Unset, str]):  Example: BSHA638QKNB1,.
        features (Union[Unset, List[AssetInstrumentationsResponse200DeviceRefFeaturesItem]]):
        href (Union[Unset, str]):  Example: /devices/38261738B7DG937BXMQ3.
    """

    id: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    features: Union[Unset, List[AssetInstrumentationsResponse200DeviceRefFeaturesItem]] = UNSET
    href: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        serial_number = self.serial_number
        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.value

                features.append(features_item)

        href = self.href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if features is not UNSET:
            field_dict["features"] = features
        if href is not UNSET:
            field_dict["href"] = href

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        features = []
        _features = d.pop("features", UNSET)
        for features_item_data in _features or []:
            features_item = AssetInstrumentationsResponse200DeviceRefFeaturesItem(features_item_data)

            features.append(features_item)

        href = d.pop("href", UNSET)

        asset_instrumentations_response_200_device_ref = cls(
            id=id,
            serial_number=serial_number,
            features=features,
            href=href,
        )

        asset_instrumentations_response_200_device_ref.additional_properties = d
        return asset_instrumentations_response_200_device_ref

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
