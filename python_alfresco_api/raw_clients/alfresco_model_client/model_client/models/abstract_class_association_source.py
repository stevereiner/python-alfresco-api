from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbstractClassAssociationSource")


@_attrs_define
class AbstractClassAssociationSource:
    """
    Attributes:
        cls (Union[Unset, str]):
        is_mandatory (Union[Unset, bool]):
        is_mandatory_enforced (Union[Unset, bool]):
        is_many (Union[Unset, bool]):
        role (Union[Unset, str]):
    """

    cls: Union[Unset, str] = UNSET
    is_mandatory: Union[Unset, bool] = UNSET
    is_mandatory_enforced: Union[Unset, bool] = UNSET
    is_many: Union[Unset, bool] = UNSET
    role: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cls = self.cls

        is_mandatory = self.is_mandatory

        is_mandatory_enforced = self.is_mandatory_enforced

        is_many = self.is_many

        role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cls is not UNSET:
            field_dict["cls"] = cls
        if is_mandatory is not UNSET:
            field_dict["isMandatory"] = is_mandatory
        if is_mandatory_enforced is not UNSET:
            field_dict["isMandatoryEnforced"] = is_mandatory_enforced
        if is_many is not UNSET:
            field_dict["isMany"] = is_many
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cls = d.pop("cls", UNSET)

        is_mandatory = d.pop("isMandatory", UNSET)

        is_mandatory_enforced = d.pop("isMandatoryEnforced", UNSET)

        is_many = d.pop("isMany", UNSET)

        role = d.pop("role", UNSET)

        abstract_class_association_source = cls(
            cls=cls,
            is_mandatory=is_mandatory,
            is_mandatory_enforced=is_mandatory_enforced,
            is_many=is_many,
            role=role,
        )

        abstract_class_association_source.additional_properties = d
        return abstract_class_association_source

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
