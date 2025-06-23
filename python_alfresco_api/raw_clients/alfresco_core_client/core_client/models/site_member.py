from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.site_member_role import SiteMemberRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person import Person


T = TypeVar("T", bound="SiteMember")


@_attrs_define
class SiteMember:
    """
    Attributes:
        id (str):
        person (Person):
        role (SiteMemberRole):
        is_member_of_group (Union[Unset, bool]):
    """

    id: str
    person: "Person"
    role: SiteMemberRole
    is_member_of_group: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        person = self.person.to_dict()

        role = self.role.value

        is_member_of_group = self.is_member_of_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "person": person,
                "role": role,
            }
        )
        if is_member_of_group is not UNSET:
            field_dict["isMemberOfGroup"] = is_member_of_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person import Person

        d = dict(src_dict)
        id = d.pop("id")

        person = Person.from_dict(d.pop("person"))

        role = SiteMemberRole(d.pop("role"))

        is_member_of_group = d.pop("isMemberOfGroup", UNSET)

        site_member = cls(
            id=id,
            person=person,
            role=role,
            is_member_of_group=is_member_of_group,
        )

        site_member.additional_properties = d
        return site_member

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
