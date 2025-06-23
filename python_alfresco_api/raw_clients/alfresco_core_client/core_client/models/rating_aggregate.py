from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RatingAggregate")


@_attrs_define
class RatingAggregate:
    """
    Attributes:
        average (Union[Unset, int]):
        number_of_ratings (Union[Unset, int]):
    """

    average: Union[Unset, int] = UNSET
    number_of_ratings: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average = self.average

        number_of_ratings = self.number_of_ratings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average is not UNSET:
            field_dict["average"] = average
        if number_of_ratings is not UNSET:
            field_dict["numberOfRatings"] = number_of_ratings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        average = d.pop("average", UNSET)

        number_of_ratings = d.pop("numberOfRatings", UNSET)

        rating_aggregate = cls(
            average=average,
            number_of_ratings=number_of_ratings,
        )

        rating_aggregate.additional_properties = d
        return rating_aggregate

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
