from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserInformationResponse200Account")


@attr.s(auto_attribs=True)
class GetUserInformationResponse200Account:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 32732835623VGHSVWH.
        name (Union[Unset, str]):  Example: Consumer - 9529ae2e-8a56-4493-b9fb-3cc1edba8aae.
        description (Union[Unset, str]):  Example: Driver account.
        brand_name (Union[Unset, str]):  Example: LoJack.
        brand_code (Union[Unset, str]):  Example: consumerMobile.SkyLink.
        login_enabled (Union[Unset, bool]):  Example: True.
        alternate_ids (Union[Unset, List[str]]):
        date_created (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        last_updated (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        created_by (Union[Unset, str]):  Example: enterpriseIntegrationServices@spireon.com.
        updated_by (Union[Unset, str]):  Example: enterpriseIntegrationServices@spireon.com.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    brand_name: Union[Unset, str] = UNSET
    brand_code: Union[Unset, str] = UNSET
    login_enabled: Union[Unset, bool] = UNSET
    alternate_ids: Union[Unset, List[str]] = UNSET
    date_created: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        brand_name = self.brand_name
        brand_code = self.brand_code
        login_enabled = self.login_enabled
        alternate_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.alternate_ids, Unset):
            alternate_ids = self.alternate_ids

        date_created = self.date_created
        last_updated = self.last_updated
        created_by = self.created_by
        updated_by = self.updated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if brand_name is not UNSET:
            field_dict["brandName"] = brand_name
        if brand_code is not UNSET:
            field_dict["brandCode"] = brand_code
        if login_enabled is not UNSET:
            field_dict["loginEnabled"] = login_enabled
        if alternate_ids is not UNSET:
            field_dict["alternateIds"] = alternate_ids
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

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        brand_name = d.pop("brandName", UNSET)

        brand_code = d.pop("brandCode", UNSET)

        login_enabled = d.pop("loginEnabled", UNSET)

        alternate_ids = cast(List[str], d.pop("alternateIds", UNSET))

        date_created = d.pop("dateCreated", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        created_by = d.pop("createdBy", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        get_user_information_response_200_account = cls(
            id=id,
            name=name,
            description=description,
            brand_name=brand_name,
            brand_code=brand_code,
            login_enabled=login_enabled,
            alternate_ids=alternate_ids,
            date_created=date_created,
            last_updated=last_updated,
            created_by=created_by,
            updated_by=updated_by,
        )

        get_user_information_response_200_account.additional_properties = d
        return get_user_information_response_200_account

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
