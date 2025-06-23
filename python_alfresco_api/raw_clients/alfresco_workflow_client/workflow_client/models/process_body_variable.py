from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessBodyVariable")


@_attrs_define
class ProcessBodyVariable:
    """A set of process variables of differing types.

    Attributes:
        bpm_assignee (Union[Unset, str]):
        bpm_send_e_mail_notifications (Union[Unset, bool]):
        bpm_workflow_priority (Union[Unset, int]):
    """

    bpm_assignee: Union[Unset, str] = UNSET
    bpm_send_e_mail_notifications: Union[Unset, bool] = UNSET
    bpm_workflow_priority: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bpm_assignee = self.bpm_assignee

        bpm_send_e_mail_notifications = self.bpm_send_e_mail_notifications

        bpm_workflow_priority = self.bpm_workflow_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bpm_assignee is not UNSET:
            field_dict["bpm_assignee"] = bpm_assignee
        if bpm_send_e_mail_notifications is not UNSET:
            field_dict["bpm_sendEMailNotifications"] = bpm_send_e_mail_notifications
        if bpm_workflow_priority is not UNSET:
            field_dict["bpm_workflowPriority"] = bpm_workflow_priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bpm_assignee = d.pop("bpm_assignee", UNSET)

        bpm_send_e_mail_notifications = d.pop("bpm_sendEMailNotifications", UNSET)

        bpm_workflow_priority = d.pop("bpm_workflowPriority", UNSET)

        process_body_variable = cls(
            bpm_assignee=bpm_assignee,
            bpm_send_e_mail_notifications=bpm_send_e_mail_notifications,
            bpm_workflow_priority=bpm_workflow_priority,
        )

        process_body_variable.additional_properties = d
        return process_body_variable

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
