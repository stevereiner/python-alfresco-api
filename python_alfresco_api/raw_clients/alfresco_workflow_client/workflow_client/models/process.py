import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Process")


@_attrs_define
class Process:
    """A process describes a running instance of a process definition.

    When a new deployment includes a process definition that is already
    deployed with the same key, the newly deployed process definition will be
    considered a new version of the same process definition. By default
    processes will keep running in the process definition they are started in.
    But new processes can be started in the latest version of a process
    definition by using the processDefinitionKey parameter.

    In non-network deployments, administrators can see all processes and
    perform all operations on tasks. In network deployments, network
    administrators can see processes in their network and perform all
    operations on tasks in their network.

        Attributes:
            id (str): The unique id of this process
            business_key (Union[Unset, str]): The business key
            delete_reason (Union[Unset, str]): The reason this process was canceled
            duration_in_ms (Union[Unset, int]): The duration of this process
            end_activity_definition_id (Union[Unset, str]): The id of the last activity in the process
            ended_at (Union[Unset, datetime.datetime]): The date time this process started
            process_definition_id (Union[Unset, str]): The unique identity of the owning process definition
            start_activity_definition_id (Union[Unset, str]): The id of the first activity in the process
            start_user_id (Union[Unset, str]): The id of the user who started the process
            started_at (Union[Unset, datetime.datetime]): The date time this process started
    """

    id: str
    business_key: Union[Unset, str] = UNSET
    delete_reason: Union[Unset, str] = UNSET
    duration_in_ms: Union[Unset, int] = UNSET
    end_activity_definition_id: Union[Unset, str] = UNSET
    ended_at: Union[Unset, datetime.datetime] = UNSET
    process_definition_id: Union[Unset, str] = UNSET
    start_activity_definition_id: Union[Unset, str] = UNSET
    start_user_id: Union[Unset, str] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        business_key = self.business_key

        delete_reason = self.delete_reason

        duration_in_ms = self.duration_in_ms

        end_activity_definition_id = self.end_activity_definition_id

        ended_at: Union[Unset, str] = UNSET
        if not isinstance(self.ended_at, Unset):
            ended_at = self.ended_at.isoformat()

        process_definition_id = self.process_definition_id

        start_activity_definition_id = self.start_activity_definition_id

        start_user_id = self.start_user_id

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if business_key is not UNSET:
            field_dict["businessKey"] = business_key
        if delete_reason is not UNSET:
            field_dict["deleteReason"] = delete_reason
        if duration_in_ms is not UNSET:
            field_dict["durationInMs"] = duration_in_ms
        if end_activity_definition_id is not UNSET:
            field_dict["endActivityDefinitionId"] = end_activity_definition_id
        if ended_at is not UNSET:
            field_dict["endedAt"] = ended_at
        if process_definition_id is not UNSET:
            field_dict["processDefinitionId"] = process_definition_id
        if start_activity_definition_id is not UNSET:
            field_dict["startActivityDefinitionId"] = start_activity_definition_id
        if start_user_id is not UNSET:
            field_dict["startUserId"] = start_user_id
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        business_key = d.pop("businessKey", UNSET)

        delete_reason = d.pop("deleteReason", UNSET)

        duration_in_ms = d.pop("durationInMs", UNSET)

        end_activity_definition_id = d.pop("endActivityDefinitionId", UNSET)

        _ended_at = d.pop("endedAt", UNSET)
        ended_at: Union[Unset, datetime.datetime]
        if isinstance(_ended_at, Unset):
            ended_at = UNSET
        else:
            ended_at = isoparse(_ended_at)

        process_definition_id = d.pop("processDefinitionId", UNSET)

        start_activity_definition_id = d.pop("startActivityDefinitionId", UNSET)

        start_user_id = d.pop("startUserId", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        process = cls(
            id=id,
            business_key=business_key,
            delete_reason=delete_reason,
            duration_in_ms=duration_in_ms,
            end_activity_definition_id=end_activity_definition_id,
            ended_at=ended_at,
            process_definition_id=process_definition_id,
            start_activity_definition_id=start_activity_definition_id,
            start_user_id=start_user_id,
            started_at=started_at,
        )

        process.additional_properties = d
        return process

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
