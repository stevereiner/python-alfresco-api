from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_facet_intervals_intervals_item import RequestFacetIntervalsIntervalsItem
    from ..models.request_facet_set import RequestFacetSet


T = TypeVar("T", bound="RequestFacetIntervals")


@_attrs_define
class RequestFacetIntervals:
    """Facet Intervals

    Attributes:
        intervals (Union[Unset, list['RequestFacetIntervalsIntervalsItem']]): Specifies the fields to facet by interval.
        sets (Union[Unset, list['RequestFacetSet']]): Sets the intervals for all fields.
    """

    intervals: Union[Unset, list["RequestFacetIntervalsIntervalsItem"]] = UNSET
    sets: Union[Unset, list["RequestFacetSet"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        intervals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.intervals, Unset):
            intervals = []
            for intervals_item_data in self.intervals:
                intervals_item = intervals_item_data.to_dict()
                intervals.append(intervals_item)

        sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sets, Unset):
            sets = []
            for sets_item_data in self.sets:
                sets_item = sets_item_data.to_dict()
                sets.append(sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if intervals is not UNSET:
            field_dict["intervals"] = intervals
        if sets is not UNSET:
            field_dict["sets"] = sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_facet_intervals_intervals_item import RequestFacetIntervalsIntervalsItem
        from ..models.request_facet_set import RequestFacetSet

        d = dict(src_dict)
        intervals = []
        _intervals = d.pop("intervals", UNSET)
        for intervals_item_data in _intervals or []:
            intervals_item = RequestFacetIntervalsIntervalsItem.from_dict(intervals_item_data)

            intervals.append(intervals_item)

        sets = []
        _sets = d.pop("sets", UNSET)
        for sets_item_data in _sets or []:
            sets_item = RequestFacetSet.from_dict(sets_item_data)

            sets.append(sets_item)

        request_facet_intervals = cls(
            intervals=intervals,
            sets=sets,
        )

        request_facet_intervals.additional_properties = d
        return request_facet_intervals

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
