from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatusInfo")


@_attrs_define
class StatusInfo:
    """
    Attributes:
        is_audit_enabled (bool):
        is_quick_share_enabled (bool):
        is_read_only (bool):  Default: False.
        is_thumbnail_generation_enabled (bool):
    """

    is_audit_enabled: bool
    is_quick_share_enabled: bool
    is_thumbnail_generation_enabled: bool
    is_read_only: bool = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_audit_enabled = self.is_audit_enabled

        is_quick_share_enabled = self.is_quick_share_enabled

        is_read_only = self.is_read_only

        is_thumbnail_generation_enabled = self.is_thumbnail_generation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isAuditEnabled": is_audit_enabled,
                "isQuickShareEnabled": is_quick_share_enabled,
                "isReadOnly": is_read_only,
                "isThumbnailGenerationEnabled": is_thumbnail_generation_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_audit_enabled = d.pop("isAuditEnabled")

        is_quick_share_enabled = d.pop("isQuickShareEnabled")

        is_read_only = d.pop("isReadOnly")

        is_thumbnail_generation_enabled = d.pop("isThumbnailGenerationEnabled")

        status_info = cls(
            is_audit_enabled=is_audit_enabled,
            is_quick_share_enabled=is_quick_share_enabled,
            is_read_only=is_read_only,
            is_thumbnail_generation_enabled=is_thumbnail_generation_enabled,
        )

        status_info.additional_properties = d
        return status_info

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
