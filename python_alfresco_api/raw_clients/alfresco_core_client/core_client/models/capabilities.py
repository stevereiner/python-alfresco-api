from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Capabilities")


@_attrs_define
class Capabilities:
    """
    Attributes:
        is_admin (Union[Unset, bool]):
        is_guest (Union[Unset, bool]):
        is_mutable (Union[Unset, bool]):
    """

    is_admin: Union[Unset, bool] = UNSET
    is_guest: Union[Unset, bool] = UNSET
    is_mutable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_admin = self.is_admin

        is_guest = self.is_guest

        is_mutable = self.is_mutable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_admin is not UNSET:
            field_dict["isAdmin"] = is_admin
        if is_guest is not UNSET:
            field_dict["isGuest"] = is_guest
        if is_mutable is not UNSET:
            field_dict["isMutable"] = is_mutable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_admin = d.pop("isAdmin", UNSET)

        is_guest = d.pop("isGuest", UNSET)

        is_mutable = d.pop("isMutable", UNSET)

        capabilities = cls(
            is_admin=is_admin,
            is_guest=is_guest,
            is_mutable=is_mutable,
        )

        capabilities.additional_properties = d
        return capabilities

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
