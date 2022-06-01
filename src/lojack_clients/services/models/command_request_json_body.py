from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.command_request_json_body_command import CommandRequestJsonBodyCommand
from ..models.command_request_json_body_response_strategy import CommandRequestJsonBodyResponseStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommandRequestJsonBody")


@attr.s(auto_attribs=True)
class CommandRequestJsonBody:
    """
    Attributes:
        asset_id (Union[Unset, str]): Asset ID Example: 272956057382HD3JBSD24.
        command (Union[Unset, CommandRequestJsonBodyCommand]):  Example: locate.
        response_channel (Union[Unset, str]):  Example: consumerMobile_assetId_272956057382HD3JBSD24.
        response_strategy (Union[Unset, CommandRequestJsonBodyResponseStrategy]):  Example: PUSH_NOTIFICATION.
    """

    asset_id: Union[Unset, str] = UNSET
    command: Union[Unset, CommandRequestJsonBodyCommand] = UNSET
    response_channel: Union[Unset, str] = UNSET
    response_strategy: Union[Unset, CommandRequestJsonBodyResponseStrategy] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset_id = self.asset_id
        command: Union[Unset, str] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command.value

        response_channel = self.response_channel
        response_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.response_strategy, Unset):
            response_strategy = self.response_strategy.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if command is not UNSET:
            field_dict["command"] = command
        if response_channel is not UNSET:
            field_dict["responseChannel"] = response_channel
        if response_strategy is not UNSET:
            field_dict["responseStrategy"] = response_strategy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asset_id = d.pop("assetId", UNSET)

        _command = d.pop("command", UNSET)
        command: Union[Unset, CommandRequestJsonBodyCommand]
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = CommandRequestJsonBodyCommand(_command)

        response_channel = d.pop("responseChannel", UNSET)

        _response_strategy = d.pop("responseStrategy", UNSET)
        response_strategy: Union[Unset, CommandRequestJsonBodyResponseStrategy]
        if isinstance(_response_strategy, Unset):
            response_strategy = UNSET
        else:
            response_strategy = CommandRequestJsonBodyResponseStrategy(_response_strategy)

        command_request_json_body = cls(
            asset_id=asset_id,
            command=command,
            response_channel=response_channel,
            response_strategy=response_strategy,
        )

        command_request_json_body.additional_properties = d
        return command_request_json_body

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
