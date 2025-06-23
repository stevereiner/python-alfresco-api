from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.site_membership_body_create_role import SiteMembershipBodyCreateRole

T = TypeVar("T", bound="SiteMembershipBodyCreate")


@_attrs_define
class SiteMembershipBodyCreate:
    """
    Attributes:
        id (str):
        role (SiteMembershipBodyCreateRole):
    """

    id: str
    role: SiteMembershipBodyCreateRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        role = SiteMembershipBodyCreateRole(d.pop("role"))

        site_membership_body_create = cls(
            id=id,
            role=role,
        )

        site_membership_body_create.additional_properties = d
        return site_membership_body_create

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
