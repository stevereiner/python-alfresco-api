from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionParameterDefinition")


@_attrs_define
class ActionParameterDefinition:
    """
    Attributes:
        display_label (Union[Unset, str]):
        mandatory (Union[Unset, bool]):
        multi_valued (Union[Unset, bool]):
        name (Union[Unset, str]):
        type_ (Union[Unset, str]):
    """

    display_label: Union[Unset, str] = UNSET
    mandatory: Union[Unset, bool] = UNSET
    multi_valued: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_label = self.display_label

        mandatory = self.mandatory

        multi_valued = self.multi_valued

        name = self.name

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_label is not UNSET:
            field_dict["displayLabel"] = display_label
        if mandatory is not UNSET:
            field_dict["mandatory"] = mandatory
        if multi_valued is not UNSET:
            field_dict["multiValued"] = multi_valued
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_label = d.pop("displayLabel", UNSET)

        mandatory = d.pop("mandatory", UNSET)

        multi_valued = d.pop("multiValued", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        action_parameter_definition = cls(
            display_label=display_label,
            mandatory=mandatory,
            multi_valued=multi_valued,
            name=name,
            type_=type_,
        )

        action_parameter_definition.additional_properties = d
        return action_parameter_definition

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
