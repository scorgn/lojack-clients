from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.device_features_item import DeviceFeaturesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Device")


@attr.s(auto_attribs=True)
class Device:
    """
    Attributes:
        id (Union[Unset, str]): Device ID Example: 38261738B7DG937BXMQ3.
        account_id (Union[Unset, str]):  Example: 83628362941HDHQQ63V1.
        active (Union[Unset, bool]):  Example: True.
        type (Union[Unset, str]):  Example: UNKNOWN.
        features (Union[Unset, List[DeviceFeaturesItem]]):
        serial_number (Union[Unset, str]):  Example: BSHA638QKNB1.
        date_created (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        last_updated (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        created_by (Union[Unset, str]):  Example: O2C.
        updated_by (Union[Unset, str]):  Example: otaService@spireon.com.
    """

    id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    type: Union[Unset, str] = UNSET
    features: Union[Unset, List[DeviceFeaturesItem]] = UNSET
    serial_number: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        account_id = self.account_id
        active = self.active
        type = self.type
        features: Union[Unset, List[str]] = UNSET
        if not isinstance(self.features, Unset):
            features = []
            for features_item_data in self.features:
                features_item = features_item_data.value

                features.append(features_item)

        serial_number = self.serial_number
        date_created = self.date_created
        last_updated = self.last_updated
        created_by = self.created_by
        updated_by = self.updated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if active is not UNSET:
            field_dict["active"] = active
        if type is not UNSET:
            field_dict["type"] = type
        if features is not UNSET:
            field_dict["features"] = features
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        account_id = d.pop("accountId", UNSET)

        active = d.pop("active", UNSET)

        type = d.pop("type", UNSET)

        features = []
        _features = d.pop("features", UNSET)
        for features_item_data in _features or []:
            features_item = DeviceFeaturesItem(features_item_data)

            features.append(features_item)

        serial_number = d.pop("serialNumber", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        created_by = d.pop("createdBy", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        device = cls(
            id=id,
            account_id=account_id,
            active=active,
            type=type,
            features=features,
            serial_number=serial_number,
            date_created=date_created,
            last_updated=last_updated,
            created_by=created_by,
            updated_by=updated_by,
        )

        device.additional_properties = d
        return device

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
