from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestFacetSet")


@_attrs_define
class RequestFacetSet:
    """The interval to Set

    Attributes:
        end (Union[Unset, str]): The end of the range
        end_inclusive (Union[Unset, bool]): When true, the set will include values less than or equal to "end" Default:
            True.
        label (Union[Unset, str]): A label to use to identify the set
        start (Union[Unset, str]): The start of the range
        start_inclusive (Union[Unset, bool]): When true, the set will include values greater or equal to "start"
            Default: True.
    """

    end: Union[Unset, str] = UNSET
    end_inclusive: Union[Unset, bool] = True
    label: Union[Unset, str] = UNSET
    start: Union[Unset, str] = UNSET
    start_inclusive: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        end_inclusive = self.end_inclusive

        label = self.label

        start = self.start

        start_inclusive = self.start_inclusive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if end_inclusive is not UNSET:
            field_dict["endInclusive"] = end_inclusive
        if label is not UNSET:
            field_dict["label"] = label
        if start is not UNSET:
            field_dict["start"] = start
        if start_inclusive is not UNSET:
            field_dict["startInclusive"] = start_inclusive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end", UNSET)

        end_inclusive = d.pop("endInclusive", UNSET)

        label = d.pop("label", UNSET)

        start = d.pop("start", UNSET)

        start_inclusive = d.pop("startInclusive", UNSET)

        request_facet_set = cls(
            end=end,
            end_inclusive=end_inclusive,
            label=label,
            start=start,
            start_inclusive=start_inclusive,
        )

        request_facet_set.additional_properties = d
        return request_facet_set

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
