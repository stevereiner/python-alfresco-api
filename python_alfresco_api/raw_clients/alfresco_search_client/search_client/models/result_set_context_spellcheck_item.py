from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.result_set_context_spellcheck_item_type import ResultSetContextSpellcheckItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResultSetContextSpellcheckItem")


@_attrs_define
class ResultSetContextSpellcheckItem:
    """
    Attributes:
        suggestion (Union[Unset, list[str]]): A suggested alternative query
        type_ (Union[Unset, ResultSetContextSpellcheckItemType]):
    """

    suggestion: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, ResultSetContextSpellcheckItemType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suggestion: Union[Unset, list[str]] = UNSET
        if not isinstance(self.suggestion, Unset):
            suggestion = self.suggestion

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if suggestion is not UNSET:
            field_dict["suggestion"] = suggestion
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        suggestion = cast(list[str], d.pop("suggestion", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ResultSetContextSpellcheckItemType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ResultSetContextSpellcheckItemType(_type_)

        result_set_context_spellcheck_item = cls(
            suggestion=suggestion,
            type_=type_,
        )

        result_set_context_spellcheck_item.additional_properties = d
        return result_set_context_spellcheck_item

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
