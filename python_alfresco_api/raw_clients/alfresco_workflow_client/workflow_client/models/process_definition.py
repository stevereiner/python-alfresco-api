from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessDefinition")


@_attrs_define
class ProcessDefinition:
    """A process definition is a description of an execution flow in terms of
    activities. New processes are created and started for a process
    definition.

        Attributes:
            id (str): The unique id of this process definition
            category (Union[Unset, str]): The category to which this process definition belongs
            deployment_id (Union[Unset, str]): The deployment of which this process definition is a part
            description (Union[Unset, str]): The description of this process definition
            graphic_notation_defined (Union[Unset, bool]):
            key (Union[Unset, str]): The key of this process definition
            name (Union[Unset, str]): The name of this process definition
            start_form_resource_key (Union[Unset, str]): The start form key
            title (Union[Unset, str]): The title of this process definition
    """

    id: str
    category: Union[Unset, str] = UNSET
    deployment_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    graphic_notation_defined: Union[Unset, bool] = UNSET
    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    start_form_resource_key: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        deployment_id = self.deployment_id

        description = self.description

        graphic_notation_defined = self.graphic_notation_defined

        key = self.key

        name = self.name

        start_form_resource_key = self.start_form_resource_key

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if deployment_id is not UNSET:
            field_dict["deploymentId"] = deployment_id
        if description is not UNSET:
            field_dict["description"] = description
        if graphic_notation_defined is not UNSET:
            field_dict["graphicNotationDefined"] = graphic_notation_defined
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name
        if start_form_resource_key is not UNSET:
            field_dict["startFormResourceKey"] = start_form_resource_key
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        category = d.pop("category", UNSET)

        deployment_id = d.pop("deploymentId", UNSET)

        description = d.pop("description", UNSET)

        graphic_notation_defined = d.pop("graphicNotationDefined", UNSET)

        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        start_form_resource_key = d.pop("startFormResourceKey", UNSET)

        title = d.pop("title", UNSET)

        process_definition = cls(
            id=id,
            category=category,
            deployment_id=deployment_id,
            description=description,
            graphic_notation_defined=graphic_notation_defined,
            key=key,
            name=name,
            start_form_resource_key=start_form_resource_key,
            title=title,
        )

        process_definition.additional_properties = d
        return process_definition

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
