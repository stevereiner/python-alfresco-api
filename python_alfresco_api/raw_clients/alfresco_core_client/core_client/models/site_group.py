from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.site_group_role import SiteGroupRole

if TYPE_CHECKING:
    from ..models.group_member import GroupMember


T = TypeVar("T", bound="SiteGroup")


@_attrs_define
class SiteGroup:
    """
    Attributes:
        group (GroupMember):
        id (str):
        role (SiteGroupRole):
    """

    group: "GroupMember"
    id: str
    role: SiteGroupRole
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group = self.group.to_dict()

        id = self.id

        role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group": group,
                "id": id,
                "role": role,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_member import GroupMember

        d = dict(src_dict)
        group = GroupMember.from_dict(d.pop("group"))

        id = d.pop("id")

        role = SiteGroupRole(d.pop("role"))

        site_group = cls(
            group=group,
            id=id,
            role=role,
        )

        site_group.additional_properties = d
        return site_group

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
