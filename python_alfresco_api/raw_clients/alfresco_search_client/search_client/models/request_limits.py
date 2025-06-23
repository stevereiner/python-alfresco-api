from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestLimits")


@_attrs_define
class RequestLimits:
    """Limit the time and resources used for query execution

    Attributes:
        permission_evaluation_count (Union[Unset, int]): Maximum count of post query permission evaluations Default:
            2000.
        permission_evaluation_time (Union[Unset, int]): Maximum time for post query permission evaluation Default:
            20000.
    """

    permission_evaluation_count: Union[Unset, int] = 2000
    permission_evaluation_time: Union[Unset, int] = 20000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permission_evaluation_count = self.permission_evaluation_count

        permission_evaluation_time = self.permission_evaluation_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if permission_evaluation_count is not UNSET:
            field_dict["permissionEvaluationCount"] = permission_evaluation_count
        if permission_evaluation_time is not UNSET:
            field_dict["permissionEvaluationTime"] = permission_evaluation_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permission_evaluation_count = d.pop("permissionEvaluationCount", UNSET)

        permission_evaluation_time = d.pop("permissionEvaluationTime", UNSET)

        request_limits = cls(
            permission_evaluation_count=permission_evaluation_count,
            permission_evaluation_time=permission_evaluation_time,
        )

        request_limits.additional_properties = d
        return request_limits

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
