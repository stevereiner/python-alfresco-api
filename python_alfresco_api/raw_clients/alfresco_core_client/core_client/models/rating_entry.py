from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.rating import Rating


T = TypeVar("T", bound="RatingEntry")


@_attrs_define
class RatingEntry:
    """
    Attributes:
        entry (Rating): A person can rate an item of content by liking it. They can also remove
            their like of an item of content. API methods exist to get a list of
            ratings and to add a new rating.
    """

    entry: "Rating"
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
        from ..models.rating import Rating

        d = dict(src_dict)
        entry = Rating.from_dict(d.pop("entry"))

        rating_entry = cls(
            entry=entry,
        )

        rating_entry.additional_properties = d
        return rating_entry

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
