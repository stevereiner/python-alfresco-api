from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.favorite_body_create_target import FavoriteBodyCreateTarget


T = TypeVar("T", bound="FavoriteBodyCreate")


@_attrs_define
class FavoriteBodyCreate:
    """
    Attributes:
        target (FavoriteBodyCreateTarget):
    """

    target: "FavoriteBodyCreateTarget"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target = self.target.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target": target,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.favorite_body_create_target import FavoriteBodyCreateTarget

        d = dict(src_dict)
        target = FavoriteBodyCreateTarget.from_dict(d.pop("target"))

        favorite_body_create = cls(
            target=target,
        )

        favorite_body_create.additional_properties = d
        return favorite_body_create

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
