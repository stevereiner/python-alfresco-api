from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="NetworkQuota")


@_attrs_define
class NetworkQuota:
    """Limits and usage of each quota. A network will have quotas for File space,
    the number of sites in the network, the number of people in the network,
    and the number of network administrators

        Attributes:
            id (str):
            limit (int):
            usage (int):
    """

    id: str
    limit: int
    usage: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        limit = self.limit

        usage = self.usage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "limit": limit,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        limit = d.pop("limit")

        usage = d.pop("usage")

        network_quota = cls(
            id=id,
            limit=limit,
            usage=usage,
        )

        network_quota.additional_properties = d
        return network_quota

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
