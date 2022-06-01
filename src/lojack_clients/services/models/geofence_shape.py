from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.coordinates import Coordinates
from ..models.geofence_shape_type import GeofenceShapeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GeofenceShape")


@attr.s(auto_attribs=True)
class GeofenceShape:
    """
    Attributes:
        type (Union[Unset, GeofenceShapeType]):
        point1 (Union[Unset, Coordinates]):
        point2 (Union[Unset, Coordinates]):
    """

    type: Union[Unset, GeofenceShapeType] = UNSET
    point1: Union[Unset, Coordinates] = UNSET
    point2: Union[Unset, Coordinates] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        point1: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.point1, Unset):
            point1 = self.point1.to_dict()

        point2: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.point2, Unset):
            point2 = self.point2.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if point1 is not UNSET:
            field_dict["point1"] = point1
        if point2 is not UNSET:
            field_dict["point2"] = point2

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, GeofenceShapeType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GeofenceShapeType(_type)

        _point1 = d.pop("point1", UNSET)
        point1: Union[Unset, Coordinates]
        if isinstance(_point1, Unset):
            point1 = UNSET
        else:
            point1 = Coordinates.from_dict(_point1)

        _point2 = d.pop("point2", UNSET)
        point2: Union[Unset, Coordinates]
        if isinstance(_point2, Unset):
            point2 = UNSET
        else:
            point2 = Coordinates.from_dict(_point2)

        geofence_shape = cls(
            type=type,
            point1=point1,
            point2=point2,
        )

        geofence_shape.additional_properties = d
        return geofence_shape

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
