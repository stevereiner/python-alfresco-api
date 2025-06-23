from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_membership_body_create_member_type import GroupMembershipBodyCreateMemberType

T = TypeVar("T", bound="GroupMembershipBodyCreate")


@_attrs_define
class GroupMembershipBodyCreate:
    """
    Attributes:
        id (str):
        member_type (GroupMembershipBodyCreateMemberType):
    """

    id: str
    member_type: GroupMembershipBodyCreateMemberType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        member_type = self.member_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "memberType": member_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        member_type = GroupMembershipBodyCreateMemberType(d.pop("memberType"))

        group_membership_body_create = cls(
            id=id,
            member_type=member_type,
        )

        group_membership_body_create.additional_properties = d
        return group_membership_body_create

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
