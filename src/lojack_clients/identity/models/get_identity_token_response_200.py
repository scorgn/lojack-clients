from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetIdentityTokenResponse200")


@attr.s(auto_attribs=True)
class GetIdentityTokenResponse200:
    """
    Attributes:
        token (Union[Unset, str]):  Example: {jwt}.
        scope (Union[Unset, str]): scope Example: ACCOUNT_USER_SCOPE.
        expires_on (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        refresh_by (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        refresh_in_seconds (Union[Unset, float]):  Example: 86340.
    """

    token: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    expires_on: Union[Unset, str] = UNSET
    refresh_by: Union[Unset, str] = UNSET
    refresh_in_seconds: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        scope = self.scope
        expires_on = self.expires_on
        refresh_by = self.refresh_by
        refresh_in_seconds = self.refresh_in_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if token is not UNSET:
            field_dict["token"] = token
        if scope is not UNSET:
            field_dict["scope"] = scope
        if expires_on is not UNSET:
            field_dict["expiresOn"] = expires_on
        if refresh_by is not UNSET:
            field_dict["refreshBy"] = refresh_by
        if refresh_in_seconds is not UNSET:
            field_dict["refreshInSeconds"] = refresh_in_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token", UNSET)

        scope = d.pop("scope", UNSET)

        expires_on = d.pop("expiresOn", UNSET)

        refresh_by = d.pop("refreshBy", UNSET)

        refresh_in_seconds = d.pop("refreshInSeconds", UNSET)

        get_identity_token_response_200 = cls(
            token=token,
            scope=scope,
            expires_on=expires_on,
            refresh_by=refresh_by,
            refresh_in_seconds=refresh_in_seconds,
        )

        get_identity_token_response_200.additional_properties = d
        return get_identity_token_response_200

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
