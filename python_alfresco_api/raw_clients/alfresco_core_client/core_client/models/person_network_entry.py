from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.person_network import PersonNetwork


T = TypeVar("T", bound="PersonNetworkEntry")


@_attrs_define
class PersonNetworkEntry:
    """
    Attributes:
        entry (PersonNetwork): A network is the group of users and sites that belong to an organization.
            Networks are organized by email domain. When a user signs up for an
            Alfresco account , their email domain becomes their Home Network.
    """

    entry: "PersonNetwork"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry = self.entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entry": entry,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person_network import PersonNetwork

        d = dict(src_dict)
        entry = PersonNetwork.from_dict(d.pop("entry"))

        person_network_entry = cls(
            entry=entry,
        )

        person_network_entry.additional_properties = d
        return person_network_entry

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
