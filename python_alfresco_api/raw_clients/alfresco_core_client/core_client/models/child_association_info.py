from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChildAssociationInfo")


@_attrs_define
class ChildAssociationInfo:
    """
    Attributes:
        assoc_type (str):
        is_primary (bool):
    """

    assoc_type: str
    is_primary: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assoc_type = self.assoc_type

        is_primary = self.is_primary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assocType": assoc_type,
                "isPrimary": is_primary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assoc_type = d.pop("assocType")

        is_primary = d.pop("isPrimary")

        child_association_info = cls(
            assoc_type=assoc_type,
            is_primary=is_primary,
        )

        child_association_info.additional_properties = d
        return child_association_info

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
