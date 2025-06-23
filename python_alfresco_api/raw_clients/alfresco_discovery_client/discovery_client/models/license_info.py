import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entitlements_info import EntitlementsInfo


T = TypeVar("T", bound="LicenseInfo")


@_attrs_define
class LicenseInfo:
    """
    Attributes:
        expires_at (datetime.datetime):
        holder (str):
        issued_at (datetime.datetime):
        mode (str):
        remaining_days (int):
        entitlements (Union[Unset, EntitlementsInfo]):
    """

    expires_at: datetime.datetime
    holder: str
    issued_at: datetime.datetime
    mode: str
    remaining_days: int
    entitlements: Union[Unset, "EntitlementsInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at = self.expires_at.isoformat()

        holder = self.holder

        issued_at = self.issued_at.isoformat()

        mode = self.mode

        remaining_days = self.remaining_days

        entitlements: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entitlements, Unset):
            entitlements = self.entitlements.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expiresAt": expires_at,
                "holder": holder,
                "issuedAt": issued_at,
                "mode": mode,
                "remainingDays": remaining_days,
            }
        )
        if entitlements is not UNSET:
            field_dict["entitlements"] = entitlements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entitlements_info import EntitlementsInfo

        d = dict(src_dict)
        expires_at = isoparse(d.pop("expiresAt"))

        holder = d.pop("holder")

        issued_at = isoparse(d.pop("issuedAt"))

        mode = d.pop("mode")

        remaining_days = d.pop("remainingDays")

        _entitlements = d.pop("entitlements", UNSET)
        entitlements: Union[Unset, EntitlementsInfo]
        if isinstance(_entitlements, Unset):
            entitlements = UNSET
        else:
            entitlements = EntitlementsInfo.from_dict(_entitlements)

        license_info = cls(
            expires_at=expires_at,
            holder=holder,
            issued_at=issued_at,
            mode=mode,
            remaining_days=remaining_days,
            entitlements=entitlements,
        )

        license_info.additional_properties = d
        return license_info

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
