from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_buckets_buckets_item_display import ResultBucketsBucketsItemDisplay


T = TypeVar("T", bound="ResultBucketsBucketsItem")


@_attrs_define
class ResultBucketsBucketsItem:
    """
    Attributes:
        count (Union[Unset, int]): The count for the bucket
        display (Union[Unset, ResultBucketsBucketsItemDisplay]): An optional field for additional display information
        filter_query (Union[Unset, str]): The filter query you can use to apply this facet
        label (Union[Unset, str]): The bucket label
    """

    count: Union[Unset, int] = UNSET
    display: Union[Unset, "ResultBucketsBucketsItemDisplay"] = UNSET
    filter_query: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        display: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.display, Unset):
            display = self.display.to_dict()

        filter_query = self.filter_query

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if display is not UNSET:
            field_dict["display"] = display
        if filter_query is not UNSET:
            field_dict["filterQuery"] = filter_query
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.result_buckets_buckets_item_display import ResultBucketsBucketsItemDisplay

        d = dict(src_dict)
        count = d.pop("count", UNSET)

        _display = d.pop("display", UNSET)
        display: Union[Unset, ResultBucketsBucketsItemDisplay]
        if isinstance(_display, Unset):
            display = UNSET
        else:
            display = ResultBucketsBucketsItemDisplay.from_dict(_display)

        filter_query = d.pop("filterQuery", UNSET)

        label = d.pop("label", UNSET)

        result_buckets_buckets_item = cls(
            count=count,
            display=display,
            filter_query=filter_query,
            label=label,
        )

        result_buckets_buckets_item.additional_properties = d
        return result_buckets_buckets_item

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
