from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.docs_item import DocsItem


T = TypeVar("T", bound="SolrResultSet")


@_attrs_define
class SolrResultSet:
    """SQL results in Solr formatting

    Attributes:
        result_set (Union[Unset, list['DocsItem']]): Array of documents returned by the query, note that this is a Solr
            convention.
    """

    result_set: Union[Unset, list["DocsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result_set: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.result_set, Unset):
            result_set = []
            for componentsschemasdocs_item_data in self.result_set:
                componentsschemasdocs_item = componentsschemasdocs_item_data.to_dict()
                result_set.append(componentsschemasdocs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result_set is not UNSET:
            field_dict["result-set"] = result_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.docs_item import DocsItem

        d = dict(src_dict)
        result_set = []
        _result_set = d.pop("result-set", UNSET)
        for componentsschemasdocs_item_data in _result_set or []:
            componentsschemasdocs_item = DocsItem.from_dict(componentsschemasdocs_item_data)

            result_set.append(componentsschemasdocs_item)

        solr_result_set = cls(
            result_set=result_set,
        )

        solr_result_set.additional_properties = d
        return solr_result_set

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
