from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rating_body_id import RatingBodyId

T = TypeVar("T", bound="RatingBody")


@_attrs_define
class RatingBody:
    """
    Attributes:
        id (RatingBodyId): The rating scheme type. Possible values are likes and fiveStar. Default: RatingBodyId.LIKES.
        my_rating (str): The rating. The type is specific to the rating scheme, boolean for the likes and an integer for
            the fiveStar
    """

    my_rating: str
    id: RatingBodyId = RatingBodyId.LIKES
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id.value

        my_rating = self.my_rating

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "myRating": my_rating,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = RatingBodyId(d.pop("id"))

        my_rating = d.pop("myRating")

        rating_body = cls(
            id=id,
            my_rating=my_rating,
        )

        rating_body.additional_properties = d
        return rating_body

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
