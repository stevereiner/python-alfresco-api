import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_body_state import TaskBodyState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.variable import Variable


T = TypeVar("T", bound="TaskBody")


@_attrs_define
class TaskBody:
    """Input body to update a specific task.

    Attributes:
        description (Union[Unset, str]): The description of this task
        due_at (Union[Unset, datetime.datetime]): The date time this task is due
        name (Union[Unset, str]): The text name of this task
        owner (Union[Unset, str]): The id of the user who owns this task
        priority (Union[Unset, int]): The numeric priority of this task
        state (Union[Unset, TaskBodyState]): The state of this task
        variables (Union[Unset, list['Variable']]): An array of variables for this task
    """

    description: Union[Unset, str] = UNSET
    due_at: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    state: Union[Unset, TaskBodyState] = UNSET
    variables: Union[Unset, list["Variable"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        due_at: Union[Unset, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat()

        name = self.name

        owner = self.owner

        priority = self.priority

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        variables: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if priority is not UNSET:
            field_dict["priority"] = priority
        if state is not UNSET:
            field_dict["state"] = state
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variable import Variable

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _due_at = d.pop("dueAt", UNSET)
        due_at: Union[Unset, datetime.datetime]
        if isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = isoparse(_due_at)

        name = d.pop("name", UNSET)

        owner = d.pop("owner", UNSET)

        priority = d.pop("priority", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, TaskBodyState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = TaskBodyState(_state)

        variables = []
        _variables = d.pop("variables", UNSET)
        for variables_item_data in _variables or []:
            variables_item = Variable.from_dict(variables_item_data)

            variables.append(variables_item)

        task_body = cls(
            description=description,
            due_at=due_at,
            name=name,
            owner=owner,
            priority=priority,
            state=state,
            variables=variables,
        )

        task_body.additional_properties = d
        return task_body

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
