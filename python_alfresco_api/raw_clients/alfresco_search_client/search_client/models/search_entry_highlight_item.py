from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchEntryHighlightItem")


@_attrs_define
class SearchEntryHighlightItem:
    """
    Attributes:
        field (Union[Unset, str]): The field where a match occured (one of the fields defined on the request)
        snippets (Union[Unset, list[str]]): Any number of snippets for the specified field highlighting the matching
            text
    """

    field: Union[Unset, str] = UNSET
    snippets: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        snippets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.snippets, Unset):
            snippets = self.snippets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if snippets is not UNSET:
            field_dict["snippets"] = snippets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field", UNSET)

        snippets = cast(list[str], d.pop("snippets", UNSET))

        search_entry_highlight_item = cls(
            field=field,
            snippets=snippets,
        )

        search_entry_highlight_item.additional_properties = d
        return search_entry_highlight_item

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
