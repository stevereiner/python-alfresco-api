from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestPagination")


@_attrs_define
class RequestPagination:
    """
    Attributes:
        max_items (Union[Unset, int]): The maximum number of items to return in the query results Default: 100.
        skip_count (Union[Unset, int]): The number of items to skip from the start of the query set Default: 0.
    """

    max_items: Union[Unset, int] = 100
    skip_count: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_items = self.max_items

        skip_count = self.skip_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_items is not UNSET:
            field_dict["maxItems"] = max_items
        if skip_count is not UNSET:
            field_dict["skipCount"] = skip_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_items = d.pop("maxItems", UNSET)

        skip_count = d.pop("skipCount", UNSET)

        request_pagination = cls(
            max_items=max_items,
            skip_count=skip_count,
        )

        request_pagination.additional_properties = d
        return request_pagination

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
