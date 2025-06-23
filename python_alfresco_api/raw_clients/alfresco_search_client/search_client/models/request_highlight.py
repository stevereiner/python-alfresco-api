from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_highlight_fields_item import RequestHighlightFieldsItem


T = TypeVar("T", bound="RequestHighlight")


@_attrs_define
class RequestHighlight:
    """Request that highlight fragments to be added to result set rows
    The properties reflect SOLR highlighting parameters.

        Attributes:
            fields (Union[Unset, list['RequestHighlightFieldsItem']]): The fields to highlight and field specific
                configuration properties for each field
            fragment_size (Union[Unset, int]): The character length of each snippet.
            max_analyzed_chars (Union[Unset, int]): The number of characters to be considered for highlighting. Matches
                after this count will not be shown.
            merge_contiguous (Union[Unset, bool]): If fragments over lap they can be  merged into one larger fragment
            postfix (Union[Unset, str]): The string used to mark the end of a highlight in a fragment.
            prefix (Union[Unset, str]): The string used to mark the start of a highlight in a fragment.
            snippet_count (Union[Unset, int]): The maximum number of distinct highlight snippets to return for each
                highlight field.
            use_phrase_highlighter (Union[Unset, bool]): Should phrases be identified.
    """

    fields: Union[Unset, list["RequestHighlightFieldsItem"]] = UNSET
    fragment_size: Union[Unset, int] = UNSET
    max_analyzed_chars: Union[Unset, int] = UNSET
    merge_contiguous: Union[Unset, bool] = UNSET
    postfix: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    snippet_count: Union[Unset, int] = UNSET
    use_phrase_highlighter: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        fragment_size = self.fragment_size

        max_analyzed_chars = self.max_analyzed_chars

        merge_contiguous = self.merge_contiguous

        postfix = self.postfix

        prefix = self.prefix

        snippet_count = self.snippet_count

        use_phrase_highlighter = self.use_phrase_highlighter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields
        if fragment_size is not UNSET:
            field_dict["fragmentSize"] = fragment_size
        if max_analyzed_chars is not UNSET:
            field_dict["maxAnalyzedChars"] = max_analyzed_chars
        if merge_contiguous is not UNSET:
            field_dict["mergeContiguous"] = merge_contiguous
        if postfix is not UNSET:
            field_dict["postfix"] = postfix
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if snippet_count is not UNSET:
            field_dict["snippetCount"] = snippet_count
        if use_phrase_highlighter is not UNSET:
            field_dict["usePhraseHighlighter"] = use_phrase_highlighter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_highlight_fields_item import RequestHighlightFieldsItem

        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = RequestHighlightFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        fragment_size = d.pop("fragmentSize", UNSET)

        max_analyzed_chars = d.pop("maxAnalyzedChars", UNSET)

        merge_contiguous = d.pop("mergeContiguous", UNSET)

        postfix = d.pop("postfix", UNSET)

        prefix = d.pop("prefix", UNSET)

        snippet_count = d.pop("snippetCount", UNSET)

        use_phrase_highlighter = d.pop("usePhraseHighlighter", UNSET)

        request_highlight = cls(
            fields=fields,
            fragment_size=fragment_size,
            max_analyzed_chars=max_analyzed_chars,
            merge_contiguous=merge_contiguous,
            postfix=postfix,
            prefix=prefix,
            snippet_count=snippet_count,
            use_phrase_highlighter=use_phrase_highlighter,
        )

        request_highlight.additional_properties = d
        return request_highlight

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
