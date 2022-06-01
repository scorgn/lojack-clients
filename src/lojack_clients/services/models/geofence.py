from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.geofence_shape import GeofenceShape
from ..types import UNSET, Unset

T = TypeVar("T", bound="Geofence")


@attr.s(auto_attribs=True)
class Geofence:
    """
    Attributes:
        id (Union[Unset, str]):  Example: 1140762987615GIDWGA.
        name (Union[Unset, str]):  Example: My Home.
        shape (Union[Unset, GeofenceShape]):
        date_created (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        last_updated (Union[Unset, str]):  Example: 2022-05-10T03:59:59.999+0000.
        created_by (Union[Unset, str]):  Example: username31.
        updated_by (Union[Unset, str]):  Example: username31.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    shape: Union[Unset, GeofenceShape] = UNSET
    date_created: Union[Unset, str] = UNSET
    last_updated: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    updated_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        shape: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.shape, Unset):
            shape = self.shape.to_dict()

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
        if shape is not UNSET:
            field_dict["shape"] = shape
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

        _shape = d.pop("shape", UNSET)
        shape: Union[Unset, GeofenceShape]
        if isinstance(_shape, Unset):
            shape = UNSET
        else:
            shape = GeofenceShape.from_dict(_shape)

        date_created = d.pop("dateCreated", UNSET)

        last_updated = d.pop("lastUpdated", UNSET)

        created_by = d.pop("createdBy", UNSET)

        updated_by = d.pop("updatedBy", UNSET)

        geofence = cls(
            id=id,
            name=name,
            shape=shape,
            date_created=date_created,
            last_updated=last_updated,
            created_by=created_by,
            updated_by=updated_by,
        )

        geofence.additional_properties = d
        return geofence

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
