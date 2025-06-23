import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_state import TaskState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.variable import Variable


T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    """A task describes one task for a human user.

    Attributes:
        id (str): The unique id of this task
        activity_definition_id (Union[Unset, str]): The activity id of this task
        assignee (Union[Unset, str]): The id of the user who is currently assigned this task
        description (Union[Unset, str]): The description of this task
        due_at (Union[Unset, datetime.datetime]): The date time this task is due
        duration_in_ms (Union[Unset, int]): The duration of this task
        ended_at (Union[Unset, datetime.datetime]): The date time this task started
        form_resource_key (Union[Unset, str]): The key of the form for this task
        name (Union[Unset, str]): The text name of this task
        owner (Union[Unset, str]): The id of the user who owns this task
        priority (Union[Unset, int]): The numeric priority of this task
        process_definition_id (Union[Unset, str]): The unique identity of the owning process definition
        process_id (Union[Unset, str]): The containing process's unique id
        started_at (Union[Unset, datetime.datetime]): The date time this task started
        state (Union[Unset, TaskState]): The state of this task
        variables (Union[Unset, list['Variable']]): An array of variables for this task
    """

    id: str
    activity_definition_id: Union[Unset, str] = UNSET
    assignee: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    due_at: Union[Unset, datetime.datetime] = UNSET
    duration_in_ms: Union[Unset, int] = UNSET
    ended_at: Union[Unset, datetime.datetime] = UNSET
    form_resource_key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    owner: Union[Unset, str] = UNSET
    priority: Union[Unset, int] = UNSET
    process_definition_id: Union[Unset, str] = UNSET
    process_id: Union[Unset, str] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    state: Union[Unset, TaskState] = UNSET
    variables: Union[Unset, list["Variable"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        activity_definition_id = self.activity_definition_id

        assignee = self.assignee

        description = self.description

        due_at: Union[Unset, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat()

        duration_in_ms = self.duration_in_ms

        ended_at: Union[Unset, str] = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        form_resource_key = self.form_resource_key

        name = self.name

        owner = self.owner

        priority = self.priority

        process_definition_id = self.process_definition_id

        process_id = self.process_id

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

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
        field_dict.update(
            {
                "id": id,
            }
        )
        if activity_definition_id is not UNSET:
            field_dict["activityDefinitionId"] = activity_definition_id
        if assignee is not UNSET:
            field_dict["assignee"] = assignee
        if description is not UNSET:
            field_dict["description"] = description
        if due_at is not UNSET:
            field_dict["dueAt"] = due_at
        if duration_in_ms is not UNSET:
            field_dict["durationInMs"] = duration_in_ms
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if form_resource_key is not UNSET:
            field_dict["formResourceKey"] = form_resource_key
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if priority is not UNSET:
            field_dict["priority"] = priority
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if process_id is not UNSET:
            field_dict["processId"] = process_id
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if state is not UNSET:
            field_dict["state"] = state
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variable import Variable

        d = dict(src_dict)
        id = d.pop("id")

        activity_definition_id = d.pop("activityDefinitionId", UNSET)

        assignee = d.pop("assignee", UNSET)

        description = d.pop("description", UNSET)

        _due_at = d.pop("dueAt", UNSET)
        due_at: Union[Unset, datetime.datetime]
        if isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = isoparse(_due_at)

        duration_in_ms = d.pop("durationInMs", UNSET)

        _ended_at = d.pop("endedAt", UNSET)
        ended_at: Union[Unset, datetime.datetime]
        if isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = isoparse(_ended_at)

        form_resource_key = d.pop("formResourceKey", UNSET)

        name = d.pop("name", UNSET)

        owner = d.pop("owner", UNSET)

        priority = d.pop("priority", UNSET)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        process_id = d.pop("processId", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _state = d.pop("state", UNSET)
        state: Union[Unset, TaskState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = TaskState(_state)

        variables = []
        _variables = d.pop("variables", UNSET)
        for variables_item_data in _variables or []:
            variables_item = Variable.from_dict(variables_item_data)

            variables.append(variables_item)

        task = cls(
            id=id,
            activity_definition_id=activity_definition_id,
            assignee=assignee,
            description=description,
            due_at=due_at,
            duration_in_ms=duration_in_ms,
            ended_at=ended_at,
            form_resource_key=form_resource_key,
            name=name,
            owner=owner,
            priority=priority,
            process_definition_id=process_definition_id,
            process_id=process_id,
            started_at=started_at,
            state=state,
            variables=variables,
        )

        task.additional_properties = d
        return task

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
