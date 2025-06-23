import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_entry_values import AuditEntryValues
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="AuditEntry")


@_attrs_define
class AuditEntry:
    """
    Attributes:
        audit_application_id (str):
        created_at (datetime.datetime):
        created_by_user (UserInfo):
        id (str):
        values (Union[Unset, AuditEntryValues]):
    """

    audit_application_id: str
    created_at: datetime.datetime
    created_by_user: "UserInfo"
    id: str
    values: Union[Unset, "AuditEntryValues"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audit_application_id = self.audit_application_id

        created_at = self.created_at.isoformat()

        created_by_user = self.created_by_user.to_dict()

        id = self.id

        values: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auditApplicationId": audit_application_id,
                "createdAt": created_at,
                "createdByUser": created_by_user,
                "id": id,
            }
        )
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_entry_values import AuditEntryValues
        from ..models.user_info import UserInfo

        d = dict(src_dict)
        audit_application_id = d.pop("auditApplicationId")

        created_at = isoparse(d.pop("createdAt"))

        created_by_user = UserInfo.from_dict(d.pop("createdByUser"))

        id = d.pop("id")

        _values = d.pop("values", UNSET)
        values: Union[Unset, AuditEntryValues]
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = AuditEntryValues.from_dict(_values)

        audit_entry = cls(
            audit_application_id=audit_application_id,
            created_at=created_at,
            created_by_user=created_by_user,
            id=id,
            values=values,
        )

        audit_entry.additional_properties = d
        return audit_entry

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
