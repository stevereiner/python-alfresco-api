from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_body_variable import ProcessBodyVariable


T = TypeVar("T", bound="ProcessBody")


@_attrs_define
class ProcessBody:
    """required to start a process.

    Attributes:
        process_definition_key (Union[Unset, str]):
        variables (Union[Unset, ProcessBodyVariable]): A set of process variables of differing types.
    """

    process_definition_key: Union[Unset, str] = UNSET
    variables: Union[Unset, "ProcessBodyVariable"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_definition_key = self.process_definition_key

        variables: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = self.variables.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process_definition_key is not UNSET:
            field_dict["processDefinitionKey"] = process_definition_key
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_body_variable import ProcessBodyVariable

        d = dict(src_dict)
        process_definition_key = d.pop("processDefinitionKey", UNSET)

        _variables = d.pop("variables", UNSET)
        variables: Union[Unset, ProcessBodyVariable]
        if isinstance(_variables, Unset):
            variables = UNSET
        else:
            variables = ProcessBodyVariable.from_dict(_variables)

        process_body = cls(
            process_definition_key=process_definition_key,
            variables=variables,
        )

        process_body.additional_properties = d
        return process_body

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
