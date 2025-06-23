from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TaskFormModel")


@_attrs_define
class TaskFormModel:
    """A task form model item.

    Attributes:
        allowed_values (Union[Unset, list[str]]): An array of allowed values for this item
        data_type (Union[Unset, str]):
        default_value (Union[Unset, str]):
        name (Union[Unset, str]):
        qualified_name (Union[Unset, str]):
        required (Union[Unset, bool]):
        title (Union[Unset, str]):
    """

    allowed_values: Union[Unset, list[str]] = UNSET
    data_type: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    qualified_name: Union[Unset, str] = UNSET
    required: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowed_values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowed_values, Unset):
            allowed_values = self.allowed_values

        data_type = self.data_type

        default_value = self.default_value

        name = self.name

        qualified_name = self.qualified_name

        required = self.required

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowed_values is not UNSET:
            field_dict["allowedValues"] = allowed_values
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if name is not UNSET:
            field_dict["name"] = name
        if qualified_name is not UNSET:
            field_dict["qualifiedName"] = qualified_name
        if required is not UNSET:
            field_dict["required"] = required
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_values = cast(list[str], d.pop("allowedValues", UNSET))

        data_type = d.pop("dataType", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        name = d.pop("name", UNSET)

        qualified_name = d.pop("qualifiedName", UNSET)

        required = d.pop("required", UNSET)

        title = d.pop("title", UNSET)

        task_form_model = cls(
            allowed_values=allowed_values,
            data_type=data_type,
            default_value=default_value,
            name=name,
            qualified_name=qualified_name,
            required=required,
            title=title,
        )

        task_form_model.additional_properties = d
        return task_form_model

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
