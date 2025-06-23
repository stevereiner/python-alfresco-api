import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rating_aggregate import RatingAggregate


T = TypeVar("T", bound="Rating")


@_attrs_define
class Rating:
    """A person can rate an item of content by liking it. They can also remove
    their like of an item of content. API methods exist to get a list of
    ratings and to add a new rating.

        Attributes:
            aggregate (RatingAggregate):
            id (str):
            my_rating (Union[Unset, str]): The rating. The type is specific to the rating scheme, boolean for the likes and
                an integer for the fiveStar.
            rated_at (Union[Unset, datetime.datetime]):
    """

    aggregate: "RatingAggregate"
    id: str
    my_rating: Union[Unset, str] = UNSET
    rated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregate = self.aggregate.to_dict()

        id = self.id

        my_rating = self.my_rating

        rated_at: Union[Unset, str] = UNSET
        if not isinstance(self.rated_at, Unset):
            rated_at = self.rated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "aggregate": aggregate,
                "id": id,
            }
        )
        if my_rating is not UNSET:
            field_dict["myRating"] = my_rating
        if rated_at is not UNSET:
            field_dict["ratedAt"] = rated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rating_aggregate import RatingAggregate

        d = dict(src_dict)
        aggregate = RatingAggregate.from_dict(d.pop("aggregate"))

        id = d.pop("id")

        my_rating = d.pop("myRating", UNSET)

        _rated_at = d.pop("ratedAt", UNSET)
        rated_at: Union[Unset, datetime.datetime]
        if isinstance(_rated_at, Unset):
            rated_at = UNSET
        else:
            rated_at = isoparse(_rated_at)

        rating = cls(
            aggregate=aggregate,
            id=id,
            my_rating=my_rating,
            rated_at=rated_at,
        )

        rating.additional_properties = d
        return rating

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
