from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.command_request_response_201_command import CommandRequestResponse201Command
from ..models.command_request_response_201_response_strategy import CommandRequestResponse201ResponseStrategy
from ..types import UNSET, Unset

T = TypeVar("T", bound="CommandRequestResponse201")


@attr.s(auto_attribs=True)
class CommandRequestResponse201:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 436tef1637vd7623g1.
        command (Union[Unset, CommandRequestResponse201Command]):  Example: locate.
        device_id (Union[Unset, str]): Device ID Example: 38261738B7DG937BXMQ3.
        asset_id (Union[Unset, str]): Asset ID Example: 272956057382HD3JBSD24.
        response_channel (Union[Unset, str]):  Example: consumerMobile_assetId_272956057382HD3JBSD24.
        response_strategy (Union[Unset, CommandRequestResponse201ResponseStrategy]):  Example: PUSH_NOTIFICATION.
        requested_by (Union[Unset, str]):  Example: username31.
    """

    id: Union[Unset, str] = UNSET
    command: Union[Unset, CommandRequestResponse201Command] = UNSET
    device_id: Union[Unset, str] = UNSET
    asset_id: Union[Unset, str] = UNSET
    response_channel: Union[Unset, str] = UNSET
    response_strategy: Union[Unset, CommandRequestResponse201ResponseStrategy] = UNSET
    requested_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        command: Union[Unset, str] = UNSET
        if not isinstance(self.command, Unset):
            command = self.command.value

        device_id = self.device_id
        asset_id = self.asset_id
        response_channel = self.response_channel
        response_strategy: Union[Unset, str] = UNSET
        if not isinstance(self.response_strategy, Unset):
            response_strategy = self.response_strategy.value

        requested_by = self.requested_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if command is not UNSET:
            field_dict["command"] = command
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if response_channel is not UNSET:
            field_dict["responseChannel"] = response_channel
        if response_strategy is not UNSET:
            field_dict["responseStrategy"] = response_strategy
        if requested_by is not UNSET:
            field_dict["requestedBy"] = requested_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _command = d.pop("command", UNSET)
        command: Union[Unset, CommandRequestResponse201Command]
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = CommandRequestResponse201Command(_command)

        device_id = d.pop("deviceId", UNSET)

        asset_id = d.pop("assetId", UNSET)

        response_channel = d.pop("responseChannel", UNSET)

        _response_strategy = d.pop("responseStrategy", UNSET)
        response_strategy: Union[Unset, CommandRequestResponse201ResponseStrategy]
        if isinstance(_response_strategy, Unset):
            response_strategy = UNSET
        else:
            response_strategy = CommandRequestResponse201ResponseStrategy(_response_strategy)

        requested_by = d.pop("requestedBy", UNSET)

        command_request_response_201 = cls(
            id=id,
            command=command,
            device_id=device_id,
            asset_id=asset_id,
            response_channel=response_channel,
            response_strategy=response_strategy,
            requested_by=requested_by,
        )

        command_request_response_201.additional_properties = d
        return command_request_response_201

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
