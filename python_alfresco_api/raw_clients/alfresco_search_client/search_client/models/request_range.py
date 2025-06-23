from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestRange")


@_attrs_define
class RequestRange:
    """Facet range

    Attributes:
        end (Union[Unset, str]): The end of the range
        exclude_filters (Union[Unset, list[str]]): Filter queries to exclude when calculating statistics
        field (Union[Unset, str]): The name of the field to perform range
        gap (Union[Unset, str]): Bucket size
        hardend (Union[Unset, bool]): If true means that the last bucket will end at “end” even if it is less than “gap”
            wide.
        include (Union[Unset, list[str]]): lower, upper, edge, outer, all
        label (Union[Unset, str]): A label to include as a pivot reference
        other (Union[Unset, list[str]]): before, after, between, non, all
        start (Union[Unset, str]): The start of the range
    """

    end: Union[Unset, str] = UNSET
    exclude_filters: Union[Unset, list[str]] = UNSET
    field: Union[Unset, str] = UNSET
    gap: Union[Unset, str] = UNSET
    hardend: Union[Unset, bool] = UNSET
    include: Union[Unset, list[str]] = UNSET
    label: Union[Unset, str] = UNSET
    other: Union[Unset, list[str]] = UNSET
    start: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end = self.end

        exclude_filters: Union[Unset, list[str]] = UNSET
        if not isinstance(self.exclude_filters, Unset):
            exclude_filters = self.exclude_filters

        field = self.field

        gap = self.gap

        hardend = self.hardend

        include: Union[Unset, list[str]] = UNSET
        if not isinstance(self.include, Unset):
            include = self.include

        label = self.label

        other: Union[Unset, list[str]] = UNSET
        if not isinstance(self.other, Unset):
            other = self.other

        start = self.start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end is not UNSET:
            field_dict["end"] = end
        if exclude_filters is not UNSET:
            field_dict["excludeFilters"] = exclude_filters
        if field is not UNSET:
            field_dict["field"] = field
        if gap is not UNSET:
            field_dict["gap"] = gap
        if hardend is not UNSET:
            field_dict["hardend"] = hardend
        if include is not UNSET:
            field_dict["include"] = include
        if label is not UNSET:
            field_dict["label"] = label
        if other is not UNSET:
            field_dict["other"] = other
        if start is not UNSET:
            field_dict["start"] = start

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end = d.pop("end", UNSET)

        exclude_filters = cast(list[str], d.pop("excludeFilters", UNSET))

        field = d.pop("field", UNSET)

        gap = d.pop("gap", UNSET)

        hardend = d.pop("hardend", UNSET)

        include = cast(list[str], d.pop("include", UNSET))

        label = d.pop("label", UNSET)

        other = cast(list[str], d.pop("other", UNSET))

        start = d.pop("start", UNSET)

        request_range = cls(
            end=end,
            exclude_filters=exclude_filters,
            field=field,
            gap=gap,
            hardend=hardend,
            include=include,
            label=label,
            other=other,
            start=start,
        )

        request_range.additional_properties = d
        return request_range

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
