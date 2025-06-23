from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_parameter_definition import ActionParameterDefinition


T = TypeVar("T", bound="ActionDefinition")


@_attrs_define
class ActionDefinition:
    """
    Attributes:
        applicable_types (list[str]): QNames of the types this action applies to
        id (str): Identifier of the action definition — used for example when executing an action
        track_status (bool): whether the basic action definition supports action tracking or not
        description (Union[Unset, str]): describes the action definition, e.g. "This will move the matched item to
            another space."
        name (Union[Unset, str]): name of the action definition, e.g. "move"
        parameter_definitions (Union[Unset, list['ActionParameterDefinition']]):
        title (Union[Unset, str]): title of the action definition, e.g. "Move"
    """

    applicable_types: list[str]
    id: str
    track_status: bool
    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    parameter_definitions: Union[Unset, list["ActionParameterDefinition"]] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applicable_types = self.applicable_types

        id = self.id

        track_status = self.track_status

        description = self.description

        name = self.name

        parameter_definitions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.parameter_definitions, Unset):
            parameter_definitions = []
            for parameter_definitions_item_data in self.parameter_definitions:
                parameter_definitions_item = parameter_definitions_item_data.to_dict()
                parameter_definitions.append(parameter_definitions_item)

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applicableTypes": applicable_types,
                "id": id,
                "trackStatus": track_status,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if parameter_definitions is not UNSET:
            field_dict["parameterDefinitions"] = parameter_definitions
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_parameter_definition import ActionParameterDefinition

        d = dict(src_dict)
        applicable_types = cast(list[str], d.pop("applicableTypes"))

        id = d.pop("id")

        track_status = d.pop("trackStatus")

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        parameter_definitions = []
        _parameter_definitions = d.pop("parameterDefinitions", UNSET)
        for parameter_definitions_item_data in _parameter_definitions or []:
            parameter_definitions_item = ActionParameterDefinition.from_dict(parameter_definitions_item_data)

            parameter_definitions.append(parameter_definitions_item)

        title = d.pop("title", UNSET)

        action_definition = cls(
            applicable_types=applicable_types,
            id=id,
            track_status=track_status,
            description=description,
            name=name,
            parameter_definitions=parameter_definitions,
            title=title,
        )

        action_definition.additional_properties = d
        return action_definition

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
