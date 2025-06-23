from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        count (Union[Unset, int]): The number of objects in the entries array.
        has_more_items (Union[Unset, bool]): A boolean value which is **true** if there are more entities in the
            collection
            beyond those in this response. A true value means a request with a larger value
            for the **skipCount** or the **maxItems** parameter will return more entities.
        max_items (Union[Unset, int]): The value of the **maxItems** parameter used to generate this list,
            or if there was no **maxItems** parameter the default value, 10
        skip_count (Union[Unset, int]): An integer describing how many entities exist in the collection before
            those included in this list.
        total_items (Union[Unset, int]): An integer describing the total number of entities in the collection.
            The API might not be able to determine this value,
            in which case this property will not be present.
    """

    count: Union[Unset, int] = UNSET
    has_more_items: Union[Unset, bool] = UNSET
    max_items: Union[Unset, int] = UNSET
    skip_count: Union[Unset, int] = UNSET
    total_items: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        count = self.count

        has_more_items = self.has_more_items

        max_items = self.max_items

        skip_count = self.skip_count

        total_items = self.total_items

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if has_more_items is not UNSET:
            field_dict["hasMoreItems"] = has_more_items
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if skip_count is not UNSET:
            field_dict["skipCount"] = skip_count
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        has_more_items = d.pop("hasMoreItems", UNSET)

        max_items = d.pop("maxItems", UNSET)

        skip_count = d.pop("skipCount", UNSET)

        total_items = d.pop("totalItems", UNSET)

        pagination = cls(
            count=count,
            has_more_items=has_more_items,
            max_items=max_items,
            skip_count=skip_count,
            total_items=total_items,
        )

        pagination.additional_properties = d
        return pagination

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
