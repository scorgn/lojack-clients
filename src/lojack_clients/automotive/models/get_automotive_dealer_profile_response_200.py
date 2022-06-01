from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_automotive_dealer_profile_response_200_dealership_address import (
    GetAutomotiveDealerProfileResponse200DealershipAddress,
)
from ..models.get_automotive_dealer_profile_response_200_vehicle_valuation import (
    GetAutomotiveDealerProfileResponse200VehicleValuation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAutomotiveDealerProfileResponse200")


@attr.s(auto_attribs=True)
class GetAutomotiveDealerProfileResponse200:
    """
    Attributes:
        dealership_id (Union[Unset, str]):  Example: 38262739272BDQYAS2GA.
        dealership_name (Union[Unset, str]):  Example: Frank's Toyota Brimington.
        dealership_address (Union[Unset, GetAutomotiveDealerProfileResponse200DealershipAddress]):
        main_phone_number (Union[Unset, str]):  Example: 508193371.
        service_phone_number (Union[Unset, str]):  Example: 508128492.
        primary_franchise (Union[Unset, str]):  Example: Ford.
        website_url (Union[Unset, str]):
        service_url (Union[Unset, str]):
        profile_image_url (Union[Unset, str]):
        vehicle_valuation (Union[Unset, GetAutomotiveDealerProfileResponse200VehicleValuation]):
        repair_order_history_disabled (Union[Unset, bool]):
        map_box_enabled (Union[Unset, bool]):  Example: True.
        allows_iap (Union[Unset, bool]):
        car_pay_enabled (Union[Unset, bool]):  Example: True.
        repair_pal_enabled (Union[Unset, bool]):  Example: True.
    """

    dealership_id: Union[Unset, str] = UNSET
    dealership_name: Union[Unset, str] = UNSET
    dealership_address: Union[Unset, GetAutomotiveDealerProfileResponse200DealershipAddress] = UNSET
    main_phone_number: Union[Unset, str] = UNSET
    service_phone_number: Union[Unset, str] = UNSET
    primary_franchise: Union[Unset, str] = UNSET
    website_url: Union[Unset, str] = UNSET
    service_url: Union[Unset, str] = UNSET
    profile_image_url: Union[Unset, str] = UNSET
    vehicle_valuation: Union[Unset, GetAutomotiveDealerProfileResponse200VehicleValuation] = UNSET
    repair_order_history_disabled: Union[Unset, bool] = UNSET
    map_box_enabled: Union[Unset, bool] = UNSET
    allows_iap: Union[Unset, bool] = UNSET
    car_pay_enabled: Union[Unset, bool] = UNSET
    repair_pal_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dealership_id = self.dealership_id
        dealership_name = self.dealership_name
        dealership_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dealership_address, Unset):
            dealership_address = self.dealership_address.to_dict()

        main_phone_number = self.main_phone_number
        service_phone_number = self.service_phone_number
        primary_franchise = self.primary_franchise
        website_url = self.website_url
        service_url = self.service_url
        profile_image_url = self.profile_image_url
        vehicle_valuation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.vehicle_valuation, Unset):
            vehicle_valuation = self.vehicle_valuation.to_dict()

        repair_order_history_disabled = self.repair_order_history_disabled
        map_box_enabled = self.map_box_enabled
        allows_iap = self.allows_iap
        car_pay_enabled = self.car_pay_enabled
        repair_pal_enabled = self.repair_pal_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dealership_id is not UNSET:
            field_dict["dealershipId"] = dealership_id
        if dealership_name is not UNSET:
            field_dict["dealershipName"] = dealership_name
        if dealership_address is not UNSET:
            field_dict["dealershipAddress"] = dealership_address
        if main_phone_number is not UNSET:
            field_dict["mainPhoneNumber"] = main_phone_number
        if service_phone_number is not UNSET:
            field_dict["servicePhoneNumber"] = service_phone_number
        if primary_franchise is not UNSET:
            field_dict["primaryFranchise"] = primary_franchise
        if website_url is not UNSET:
            field_dict["websiteUrl"] = website_url
        if service_url is not UNSET:
            field_dict["serviceUrl"] = service_url
        if profile_image_url is not UNSET:
            field_dict["profileImageUrl"] = profile_image_url
        if vehicle_valuation is not UNSET:
            field_dict["vehicleValuation"] = vehicle_valuation
        if repair_order_history_disabled is not UNSET:
            field_dict["repairOrderHistoryDisabled"] = repair_order_history_disabled
        if map_box_enabled is not UNSET:
            field_dict["mapBoxEnabled"] = map_box_enabled
        if allows_iap is not UNSET:
            field_dict["allowsIAP"] = allows_iap
        if car_pay_enabled is not UNSET:
            field_dict["carPayEnabled"] = car_pay_enabled
        if repair_pal_enabled is not UNSET:
            field_dict["repairPalEnabled"] = repair_pal_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dealership_id = d.pop("dealershipId", UNSET)

        dealership_name = d.pop("dealershipName", UNSET)

        _dealership_address = d.pop("dealershipAddress", UNSET)
        dealership_address: Union[Unset, GetAutomotiveDealerProfileResponse200DealershipAddress]
        if isinstance(_dealership_address, Unset):
            dealership_address = UNSET
        else:
            dealership_address = GetAutomotiveDealerProfileResponse200DealershipAddress.from_dict(_dealership_address)

        main_phone_number = d.pop("mainPhoneNumber", UNSET)

        service_phone_number = d.pop("servicePhoneNumber", UNSET)

        primary_franchise = d.pop("primaryFranchise", UNSET)

        website_url = d.pop("websiteUrl", UNSET)

        service_url = d.pop("serviceUrl", UNSET)

        profile_image_url = d.pop("profileImageUrl", UNSET)

        _vehicle_valuation = d.pop("vehicleValuation", UNSET)
        vehicle_valuation: Union[Unset, GetAutomotiveDealerProfileResponse200VehicleValuation]
        if isinstance(_vehicle_valuation, Unset):
            vehicle_valuation = UNSET
        else:
            vehicle_valuation = GetAutomotiveDealerProfileResponse200VehicleValuation.from_dict(_vehicle_valuation)

        repair_order_history_disabled = d.pop("repairOrderHistoryDisabled", UNSET)

        map_box_enabled = d.pop("mapBoxEnabled", UNSET)

        allows_iap = d.pop("allowsIAP", UNSET)

        car_pay_enabled = d.pop("carPayEnabled", UNSET)

        repair_pal_enabled = d.pop("repairPalEnabled", UNSET)

        get_automotive_dealer_profile_response_200 = cls(
            dealership_id=dealership_id,
            dealership_name=dealership_name,
            dealership_address=dealership_address,
            main_phone_number=main_phone_number,
            service_phone_number=service_phone_number,
            primary_franchise=primary_franchise,
            website_url=website_url,
            service_url=service_url,
            profile_image_url=profile_image_url,
            vehicle_valuation=vehicle_valuation,
            repair_order_history_disabled=repair_order_history_disabled,
            map_box_enabled=map_box_enabled,
            allows_iap=allows_iap,
            car_pay_enabled=car_pay_enabled,
            repair_pal_enabled=repair_pal_enabled,
        )

        get_automotive_dealer_profile_response_200.additional_properties = d
        return get_automotive_dealer_profile_response_200

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
