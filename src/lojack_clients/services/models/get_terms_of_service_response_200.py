from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTermsOfServiceResponse200")


@attr.s(auto_attribs=True)
class GetTermsOfServiceResponse200:
    """
    Attributes:
        id (Union[Unset, str]):  Example: SBDGFVBAGWGVQ352521.
        name (Union[Unset, str]):  Example: LoJack SSA.
        content (Union[Unset, str]): Long HTML output with terms of service
        accepted (Union[Unset, bool]):  Example: True.
        can_accept (Union[Unset, bool]):
        date_created (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        last_updated (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        created_by (Union[Unset, str]):  Example: email@spireon.com.
        ttl_days (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    accepted: Union[Unset, bool] = UNSET
    can_accept: Union[Unset, bool] = UNSET
    date_created: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    ttl_days: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        content = self.content
        accepted = self.accepted
        can_accept = self.can_accept
        date_created = self.date_created
        last_updated = self.last_updated
        created_by = self.created_by
        ttl_days = self.ttl_days

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if content is not UNSET:
            field_dict["content"] = content
        if accepted is not UNSET:
            field_dict["accepted"] = accepted
        if can_accept is not UNSET:
            field_dict["canAccept"] = can_accept
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if ttl_days is not UNSET:
            field_dict["ttlDays"] = ttl_days

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        content = d.pop("content", UNSET)

        accepted = d.pop("accepted", UNSET)

        can_accept = d.pop("canAccept", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        created_by = d.pop("createdBy", UNSET)

        ttl_days = d.pop("ttlDays", UNSET)

        get_terms_of_service_response_200 = cls(
            id=id,
            name=name,
            content=content,
            accepted=accepted,
            can_accept=can_accept,
            date_created=date_created,
            last_updated=last_updated,
            created_by=created_by,
            ttl_days=ttl_days,
        )

        get_terms_of_service_response_200.additional_properties = d
        return get_terms_of_service_response_200

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
