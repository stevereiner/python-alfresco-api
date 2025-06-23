import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.favorite_properties import FavoriteProperties
    from ..models.favorite_target import FavoriteTarget


T = TypeVar("T", bound="Favorite")


@_attrs_define
class Favorite:
    """A favorite describes an Alfresco entity that a person has marked as a favorite.
    The target can be a site, file or folder.

        Attributes:
            target (FavoriteTarget):
            target_guid (str): The guid of the object that is a favorite.
            created_at (Union[Unset, datetime.datetime]): The time the object was made a favorite.
            properties (Union[Unset, FavoriteProperties]): A subset of the target favorite properties, system properties and
                properties already available in the target are excluded.
    """

    target: "FavoriteTarget"
    target_guid: str
    created_at: Union[Unset, datetime.datetime] = UNSET
    properties: Union[Unset, "FavoriteProperties"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target = self.target.to_dict()

        target_guid = self.target_guid

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
                "targetGuid": target_guid,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.favorite_properties import FavoriteProperties
        from ..models.favorite_target import FavoriteTarget

        d = dict(src_dict)
        target = FavoriteTarget.from_dict(d.pop("target"))

        target_guid = d.pop("targetGuid")

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, FavoriteProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = FavoriteProperties.from_dict(_properties)

        favorite = cls(
            target=target,
            target_guid=target_guid,
            created_at=created_at,
            properties=properties,
        )

        favorite.additional_properties = d
        return favorite

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
