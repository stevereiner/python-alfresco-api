from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.result_set_context import ResultSetContext
    from ..models.result_set_row_entry import ResultSetRowEntry


T = TypeVar("T", bound="ResultSetPagingList")


@_attrs_define
class ResultSetPagingList:
    """
    Attributes:
        context (Union[Unset, ResultSetContext]): Context that applies to the whole result set
        entries (Union[Unset, list['ResultSetRowEntry']]):
        pagination (Union[Unset, Pagination]):
    """

    context: Union[Unset, "ResultSetContext"] = UNSET
    entries: Union[Unset, list["ResultSetRowEntry"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        context: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if context is not UNSET:
            field_dict["context"] = context
        if entries is not UNSET:
            field_dict["entries"] = entries
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.result_set_context import ResultSetContext
        from ..models.result_set_row_entry import ResultSetRowEntry

        d = dict(src_dict)
        _context = d.pop("context", UNSET)
        context: Union[Unset, ResultSetContext]
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = ResultSetContext.from_dict(_context)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = ResultSetRowEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        result_set_paging_list = cls(
            context=context,
            entries=entries,
            pagination=pagination,
        )

        result_set_paging_list.additional_properties = d
        return result_set_paging_list

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
