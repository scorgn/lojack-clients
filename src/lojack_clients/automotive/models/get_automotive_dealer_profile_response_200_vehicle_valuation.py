from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAutomotiveDealerProfileResponse200VehicleValuation")


@attr.s(auto_attribs=True)
class GetAutomotiveDealerProfileResponse200VehicleValuation:
    """
    Attributes:
        url (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        threshold_in_months (Union[Unset, float]):  Example: 12.
    """

    url: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    threshold_in_months: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        enabled = self.enabled
        threshold_in_months = self.threshold_in_months

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if threshold_in_months is not UNSET:
            field_dict["thresholdInMonths"] = threshold_in_months

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        url = d.pop("url", UNSET)

        enabled = d.pop("enabled", UNSET)

        threshold_in_months = d.pop("thresholdInMonths", UNSET)

        get_automotive_dealer_profile_response_200_vehicle_valuation = cls(
            url=url,
            enabled=enabled,
            threshold_in_months=threshold_in_months,
        )

        get_automotive_dealer_profile_response_200_vehicle_valuation.additional_properties = d
        return get_automotive_dealer_profile_response_200_vehicle_valuation

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
