from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestHighlightFieldsItem")


@_attrs_define
class RequestHighlightFieldsItem:
    """
    Attributes:
        field (Union[Unset, str]): The name of the field to highlight.
        fragment_size (Union[Unset, int]):
        merge_contiguous (Union[Unset, bool]):
        postfix (Union[Unset, str]):
        prefix (Union[Unset, str]):
        snippet_count (Union[Unset, int]):
    """

    field: Union[Unset, str] = UNSET
    fragment_size: Union[Unset, int] = UNSET
    merge_contiguous: Union[Unset, bool] = UNSET
    postfix: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    snippet_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        fragment_size = self.fragment_size

        merge_contiguous = self.merge_contiguous

        postfix = self.postfix

        prefix = self.prefix

        snippet_count = self.snippet_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if fragment_size is not UNSET:
            field_dict["fragmentSize"] = fragment_size
        if merge_contiguous is not UNSET:
            field_dict["mergeContiguous"] = merge_contiguous
        if postfix is not UNSET:
            field_dict["postfix"] = postfix
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if snippet_count is not UNSET:
            field_dict["snippetCount"] = snippet_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field", UNSET)

        fragment_size = d.pop("fragmentSize", UNSET)

        merge_contiguous = d.pop("mergeContiguous", UNSET)

        postfix = d.pop("postfix", UNSET)

        prefix = d.pop("prefix", UNSET)

        snippet_count = d.pop("snippetCount", UNSET)

        request_highlight_fields_item = cls(
            field=field,
            fragment_size=fragment_size,
            merge_contiguous=merge_contiguous,
            postfix=postfix,
            prefix=prefix,
            snippet_count=snippet_count,
        )

        request_highlight_fields_item.additional_properties = d
        return request_highlight_fields_item

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
