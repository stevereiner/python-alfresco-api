from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_body_exec_params import ActionBodyExecParams


T = TypeVar("T", bound="ActionBodyExec")


@_attrs_define
class ActionBodyExec:
    """
    Attributes:
        action_definition_id (str):
        params (Union[Unset, ActionBodyExecParams]):
        target_id (Union[Unset, str]): The entity upon which to execute the action, typically a node ID or similar.
    """

    action_definition_id: str
    params: Union[Unset, "ActionBodyExecParams"] = UNSET
    target_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_definition_id = self.action_definition_id

        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        target_id = self.target_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actionDefinitionId": action_definition_id,
            }
        )
        if params is not UNSET:
            field_dict["params"] = params
        if target_id is not UNSET:
            field_dict["targetId"] = target_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_body_exec_params import ActionBodyExecParams

        d = dict(src_dict)
        action_definition_id = d.pop("actionDefinitionId")

        _params = d.pop("params", UNSET)
        params: Union[Unset, ActionBodyExecParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ActionBodyExecParams.from_dict(_params)

        target_id = d.pop("targetId", UNSET)

        action_body_exec = cls(
            action_definition_id=action_definition_id,
            params=params,
            target_id=target_id,
        )

        action_body_exec.additional_properties = d
        return action_body_exec

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
