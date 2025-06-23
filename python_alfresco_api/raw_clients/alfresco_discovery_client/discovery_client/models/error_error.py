from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorError")


@_attrs_define
class ErrorError:
    """
    Attributes:
        brief_summary (Union[Unset, str]):
        description_url (Union[Unset, str]):
        error_key (Union[Unset, str]):
        log_id (Union[Unset, str]):
        stack_trace (Union[Unset, str]):
        status_code (Union[Unset, int]):
    """

    brief_summary: Union[Unset, str] = UNSET
    description_url: Union[Unset, str] = UNSET
    error_key: Union[Unset, str] = UNSET
    log_id: Union[Unset, str] = UNSET
    stack_trace: Union[Unset, str] = UNSET
    status_code: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brief_summary = self.brief_summary

        description_url = self.description_url

        error_key = self.error_key

        log_id = self.log_id

        stack_trace = self.stack_trace

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brief_summary is not UNSET:
            field_dict["briefSummary"] = brief_summary
        if description_url is not UNSET:
            field_dict["descriptionURL"] = description_url
        if error_key is not UNSET:
            field_dict["errorKey"] = error_key
        if log_id is not UNSET:
            field_dict["logId"] = log_id
        if stack_trace is not UNSET:
            field_dict["stackTrace"] = stack_trace
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brief_summary = d.pop("briefSummary", UNSET)

        description_url = d.pop("descriptionURL", UNSET)

        error_key = d.pop("errorKey", UNSET)

        log_id = d.pop("logId", UNSET)

        stack_trace = d.pop("stackTrace", UNSET)

        status_code = d.pop("statusCode", UNSET)

        error_error = cls(
            brief_summary=brief_summary,
            description_url=description_url,
            error_key=error_key,
            log_id=log_id,
            stack_trace=stack_trace,
            status_code=status_code,
        )

        error_error.additional_properties = d
        return error_error

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
