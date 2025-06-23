from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.result_buckets_buckets_item import ResultBucketsBucketsItem


T = TypeVar("T", bound="ResultBuckets")


@_attrs_define
class ResultBuckets:
    """
    Attributes:
        buckets (Union[Unset, list['ResultBucketsBucketsItem']]): An array of buckets and values
        label (Union[Unset, str]): The field name or its explicit label, if provided on the request
    """

    buckets: Union[Unset, list["ResultBucketsBucketsItem"]] = UNSET
    label: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buckets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.result_buckets_buckets_item import ResultBucketsBucketsItem

        d = dict(src_dict)
        buckets = []
        _buckets = d.pop("buckets", UNSET)
        for buckets_item_data in _buckets or []:
            buckets_item = ResultBucketsBucketsItem.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        label = d.pop("label", UNSET)

        result_buckets = cls(
            buckets=buckets,
            label=label,
        )

        result_buckets.additional_properties = d
        return result_buckets

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
