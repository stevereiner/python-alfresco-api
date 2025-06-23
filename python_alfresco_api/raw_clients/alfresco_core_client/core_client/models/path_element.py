from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PathElement")


@_attrs_define
class PathElement:
    """
    Attributes:
        aspect_names (Union[Unset, list[str]]):
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        node_type (Union[Unset, str]):
    """

    aspect_names: Union[Unset, list[str]] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    node_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aspect_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aspect_names, Unset):
            aspect_names = self.aspect_names

        id = self.id

        name = self.name

        node_type = self.node_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_names is not UNSET:
            field_dict["aspectNames"] = aspect_names
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aspect_names = cast(list[str], d.pop("aspectNames", UNSET))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        node_type = d.pop("nodeType", UNSET)

        path_element = cls(
            aspect_names=aspect_names,
            id=id,
            name=name,
            node_type=node_type,
        )

        path_element.additional_properties = d
        return path_element

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
