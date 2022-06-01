from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserInformationResponse200User")


@attr.s(auto_attribs=True)
class GetUserInformationResponse200User:
    """
    Attributes:
        id (Union[Unset, float]):  Example: 1854583.
        global_id (Union[Unset, str]):  Example: 9085a727-a00f-4ee6-9363-603a6266b0d5.
        username (Union[Unset, str]):  Example: username31.
        first_name (Union[Unset, str]):  Example: John,.
        last_name (Union[Unset, str]):  Example: Doe,.
        email (Union[Unset, str]): Your email address Example: email@provider.com.
        phone (Union[Unset, str]): Your phone number Example: (502) 820-1852.
        date_created (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        last_updated (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        created_by (Union[Unset, str]):  Example: InvitationAuthenticationProvider.
        updated_by (Union[Unset, str]):  Example: username31.
        active (Union[Unset, bool]):  Example: True.
    """

    id: Union[Unset, float] = UNSET
    global_id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        global_id = self.global_id
        username = self.username
        first_name = self.first_name
        last_name = self.last_name
        email = self.email
        phone = self.phone
        date_created = self.date_created
        last_updated = self.last_updated
        created_by = self.created_by
        updated_by = self.updated_by
        active = self.active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if username is not UNSET:
            field_dict["username"] = username
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if active is not UNSET:
            field_dict["active"] = active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        global_id = d.pop("globalId", UNSET)

        username = d.pop("username", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        created_by = d.pop("createdBy", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        active = d.pop("active", UNSET)

        get_user_information_response_200_user = cls(
            id=id,
            global_id=global_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            date_created=date_created,
            last_updated=last_updated,
            created_by=created_by,
            updated_by=updated_by,
            active=active,
        )

        get_user_information_response_200_user.additional_properties = d
        return get_user_information_response_200_user

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
