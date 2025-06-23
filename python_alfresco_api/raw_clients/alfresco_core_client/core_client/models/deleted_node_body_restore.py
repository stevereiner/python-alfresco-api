from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeletedNodeBodyRestore")


@_attrs_define
class DeletedNodeBodyRestore:
    """
    Attributes:
        assoc_type (Union[Unset, str]):
        target_parent_id (Union[Unset, str]):
    """

    assoc_type: Union[Unset, str] = UNSET
    target_parent_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assoc_type = self.assoc_type

        target_parent_id = self.target_parent_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if assoc_type is not UNSET:
            field_dict["assocType"] = assoc_type
        if target_parent_id is not UNSET:
            field_dict["targetParentId"] = target_parent_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assoc_type = d.pop("assocType", UNSET)

        target_parent_id = d.pop("targetParentId", UNSET)

        deleted_node_body_restore = cls(
            assoc_type=assoc_type,
            target_parent_id=target_parent_id,
        )

        deleted_node_body_restore.additional_properties = d
        return deleted_node_body_restore

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
