from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.asset_instrumentations_response_200_asset_ref import AssetInstrumentationsResponse200AssetRef
from ..models.asset_instrumentations_response_200_device_ref import AssetInstrumentationsResponse200DeviceRef
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetInstrumentationsResponse200")


@attr.s(auto_attribs=True)
class AssetInstrumentationsResponse200:
    """
    Attributes:
        id (Union[Unset, str]): Asset ID Example: 272956057382HD3JBSD24.
        asset_id (Union[Unset, str]): Asset ID Example: 272956057382HD3JBSD24.
        device_id (Union[Unset, str]): Device ID Example: 38261738B7DG937BXMQ3.
        device_ref (Union[Unset, AssetInstrumentationsResponse200DeviceRef]):
        asset_ref (Union[Unset, AssetInstrumentationsResponse200AssetRef]):
    """

    id: Union[Unset, str] = UNSET
    asset_id: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    device_ref: Union[Unset, AssetInstrumentationsResponse200DeviceRef] = UNSET
    asset_ref: Union[Unset, AssetInstrumentationsResponse200AssetRef] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        asset_id = self.asset_id
        device_id = self.device_id
        device_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.device_ref, Unset):
            device_ref = self.device_ref.to_dict()

        asset_ref: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.asset_ref, Unset):
            asset_ref = self.asset_ref.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if device_ref is not UNSET:
            field_dict["deviceRef"] = device_ref
        if asset_ref is not UNSET:
            field_dict["assetRef"] = asset_ref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        asset_id = d.pop("assetId", UNSET)

        device_id = d.pop("deviceId", UNSET)

        _device_ref = d.pop("deviceRef", UNSET)
        device_ref: Union[Unset, AssetInstrumentationsResponse200DeviceRef]
        if isinstance(_device_ref, Unset):
            device_ref = UNSET
        else:
            device_ref = AssetInstrumentationsResponse200DeviceRef.from_dict(_device_ref)

        _asset_ref = d.pop("assetRef", UNSET)
        asset_ref: Union[Unset, AssetInstrumentationsResponse200AssetRef]
        if isinstance(_asset_ref, Unset):
            asset_ref = UNSET
        else:
            asset_ref = AssetInstrumentationsResponse200AssetRef.from_dict(_asset_ref)

        asset_instrumentations_response_200 = cls(
            id=id,
            asset_id=asset_id,
            device_id=device_id,
            device_ref=device_ref,
            asset_ref=asset_ref,
        )

        asset_instrumentations_response_200.additional_properties = d
        return asset_instrumentations_response_200

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
