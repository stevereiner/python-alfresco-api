from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_entry_highlight_item import SearchEntryHighlightItem


T = TypeVar("T", bound="SearchEntry")


@_attrs_define
class SearchEntry:
    """
    Attributes:
        highlight (Union[Unset, list['SearchEntryHighlightItem']]): Highlight fragments if requested and available. A
            match can happen in any of the requested field.
        score (Union[Unset, float]): The score for this row
    """

    highlight: Union[Unset, list["SearchEntryHighlightItem"]] = UNSET
    score: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        highlight: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.highlight, Unset):
            highlight = []
            for highlight_item_data in self.highlight:
                highlight_item = highlight_item_data.to_dict()
                highlight.append(highlight_item)

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if highlight is not UNSET:
            field_dict["highlight"] = highlight
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_entry_highlight_item import SearchEntryHighlightItem

        d = dict(src_dict)
        highlight = []
        _highlight = d.pop("highlight", UNSET)
        for highlight_item_data in _highlight or []:
            highlight_item = SearchEntryHighlightItem.from_dict(highlight_item_data)

            highlight.append(highlight_item)

        score = d.pop("score", UNSET)

        search_entry = cls(
            highlight=highlight,
            score=score,
        )

        search_entry.additional_properties = d
        return search_entry

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
