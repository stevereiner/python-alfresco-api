from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeBodyMove")


@_attrs_define
class NodeBodyMove:
    r"""
    Attributes:
        target_parent_id (str):
        name (Union[Unset, str]): The name must not contain spaces or the following special characters: * " < > \ / ? :
            and |.
            The character . must not be used at the end of the name.
    """

    target_parent_id: str
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_parent_id = self.target_parent_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetParentId": target_parent_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        target_parent_id = d.pop("targetParentId")

        name = d.pop("name", UNSET)

        node_body_move = cls(
            target_parent_id=target_parent_id,
            name=name,
        )

        node_body_move.additional_properties = d
        return node_body_move

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
