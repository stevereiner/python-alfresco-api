import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DirectAccessUrlBodyCreate")


@_attrs_define
class DirectAccessUrlBodyCreate:
    """
    Attributes:
        expires_at (Union[Unset, datetime.datetime]):
        valid_for (Union[Unset, int]): The length of time in seconds that the url is valid for.
    """

    expires_at: Union[Unset, datetime.datetime] = UNSET
    valid_for: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        valid_for = self.valid_for

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if valid_for is not UNSET:
            field_dict["validFor"] = valid_for

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        valid_for = d.pop("validFor", UNSET)

        direct_access_url_body_create = cls(
            expires_at=expires_at,
            valid_for=valid_for,
        )

        direct_access_url_body_create.additional_properties = d
        return direct_access_url_body_create

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
