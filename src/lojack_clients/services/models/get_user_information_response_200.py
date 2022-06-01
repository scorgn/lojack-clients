from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_user_information_response_200_account import GetUserInformationResponse200Account
from ..models.get_user_information_response_200_user import GetUserInformationResponse200User
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUserInformationResponse200")


@attr.s(auto_attribs=True)
class GetUserInformationResponse200:
    """
    Attributes:
        user (Union[Unset, GetUserInformationResponse200User]):
        account (Union[Unset, GetUserInformationResponse200Account]):
    """

    user: Union[Unset, GetUserInformationResponse200User] = UNSET
    account: Union[Unset, GetUserInformationResponse200Account] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        account: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if account is not UNSET:
            field_dict["account"] = account

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[Unset, GetUserInformationResponse200User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = GetUserInformationResponse200User.from_dict(_user)

        _account = d.pop("account", UNSET)
        account: Union[Unset, GetUserInformationResponse200Account]
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = GetUserInformationResponse200Account.from_dict(_account)

        get_user_information_response_200 = cls(
            user=user,
            account=account,
        )

        get_user_information_response_200.additional_properties = d
        return get_user_information_response_200

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
