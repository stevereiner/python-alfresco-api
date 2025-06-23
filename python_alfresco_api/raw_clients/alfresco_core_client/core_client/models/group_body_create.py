from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupBodyCreate")


@_attrs_define
class GroupBodyCreate:
    """
    Attributes:
        display_name (str):
        id (str):
        parent_ids (Union[Unset, list[str]]):
    """

    display_name: str
    id: str
    parent_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        id = self.id

        parent_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.parent_ids, Unset):
            parent_ids = self.parent_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "id": id,
            }
        )
        if parent_ids is not UNSET:
            field_dict["parentIds"] = parent_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("displayName")

        id = d.pop("id")

        parent_ids = cast(list[str], d.pop("parentIds", UNSET))

        group_body_create = cls(
            display_name=display_name,
            id=id,
            parent_ids=parent_ids,
        )

        group_body_create.additional_properties = d
        return group_body_create

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
