from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node import Node
    from ..models.node_association_entry import NodeAssociationEntry
    from ..models.pagination import Pagination


T = TypeVar("T", bound="NodeAssociationPagingList")


@_attrs_define
class NodeAssociationPagingList:
    """
    Attributes:
        entries (Union[Unset, list['NodeAssociationEntry']]):
        pagination (Union[Unset, Pagination]):
        source (Union[Unset, Node]):
    """

    entries: Union[Unset, list["NodeAssociationEntry"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    source: Union[Unset, "Node"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entries is not UNSET:
            field_dict["entries"] = entries
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node import Node
        from ..models.node_association_entry import NodeAssociationEntry
        from ..models.pagination import Pagination

        d = dict(src_dict)
        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in _entries or []:
            entries_item = NodeAssociationEntry.from_dict(entries_item_data)

            entries.append(entries_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        _source = d.pop("source", UNSET)
        source: Union[Unset, Node]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = Node.from_dict(_source)

        node_association_paging_list = cls(
            entries=entries,
            pagination=pagination,
            source=source,
        )

        node_association_paging_list.additional_properties = d
        return node_association_paging_list

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
