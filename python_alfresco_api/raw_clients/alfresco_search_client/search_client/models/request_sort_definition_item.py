from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_sort_definition_item_type import RequestSortDefinitionItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestSortDefinitionItem")


@_attrs_define
class RequestSortDefinitionItem:
    """
    Attributes:
        ascending (Union[Unset, bool]): The sort order. (The ordering of nulls is determined by the SOLR configuration)
            Default: False.
        field (Union[Unset, str]): The name of the field
        type_ (Union[Unset, RequestSortDefinitionItemType]): How to order - using a field, when position of the document
            in the index, score/relevence. Default: RequestSortDefinitionItemType.FIELD.
    """

    ascending: Union[Unset, bool] = False
    field: Union[Unset, str] = UNSET
    type_: Union[Unset, RequestSortDefinitionItemType] = RequestSortDefinitionItemType.FIELD
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ascending = self.ascending

        field = self.field

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ascending is not UNSET:
            field_dict["ascending"] = ascending
        if field is not UNSET:
            field_dict["field"] = field
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ascending = d.pop("ascending", UNSET)

        field = d.pop("field", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, RequestSortDefinitionItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RequestSortDefinitionItemType(_type_)

        request_sort_definition_item = cls(
            ascending=ascending,
            field=field,
            type_=type_,
        )

        request_sort_definition_item.additional_properties = d
        return request_sort_definition_item

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
