from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """
    Attributes:
        display_name (str):
        id (str):
        is_root (bool):  Default: True.
        parent_ids (Union[Unset, list[str]]):
        zones (Union[Unset, list[str]]):
    """

    display_name: str
    id: str
    is_root: bool = True
    parent_ids: Union[Unset, list[str]] = UNSET
    zones: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        id = self.id

        is_root = self.is_root

        parent_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.parent_ids, Unset):
            parent_ids = self.parent_ids

        zones: Union[Unset, list[str]] = UNSET
        if not isinstance(self.zones, Unset):
            zones = self.zones

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "id": id,
                "isRoot": is_root,
            }
        )
        if parent_ids is not UNSET:
            field_dict["parentIds"] = parent_ids
        if zones is not UNSET:
            field_dict["zones"] = zones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName")

        id = d.pop("id")

        is_root = d.pop("isRoot")

        parent_ids = cast(list[str], d.pop("parentIds", UNSET))

        zones = cast(list[str], d.pop("zones", UNSET))

        group = cls(
            display_name=display_name,
            id=id,
            is_root=is_root,
            parent_ids=parent_ids,
            zones=zones,
        )

        group.additional_properties = d
        return group

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
