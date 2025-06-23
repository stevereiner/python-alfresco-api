from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditApp")


@_attrs_define
class AuditApp:
    """
    Attributes:
        id (str):
        is_enabled (Union[Unset, bool]):  Default: True.
        max_entry_id (Union[Unset, int]):
        min_entry_id (Union[Unset, int]):
        name (Union[Unset, str]):
    """

    id: str
    is_enabled: Union[Unset, bool] = True
    max_entry_id: Union[Unset, int] = UNSET
    min_entry_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_enabled = self.is_enabled

        max_entry_id = self.max_entry_id

        min_entry_id = self.min_entry_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if is_enabled is not UNSET:
            field_dict["isEnabled"] = is_enabled
        if max_entry_id is not UNSET:
            field_dict["maxEntryId"] = max_entry_id
        if min_entry_id is not UNSET:
            field_dict["minEntryId"] = min_entry_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        is_enabled = d.pop("isEnabled", UNSET)

        max_entry_id = d.pop("maxEntryId", UNSET)

        min_entry_id = d.pop("minEntryId", UNSET)

        name = d.pop("name", UNSET)

        audit_app = cls(
            id=id,
            is_enabled=is_enabled,
            max_entry_id=max_entry_id,
            min_entry_id=min_entry_id,
            name=name,
        )

        audit_app.additional_properties = d
        return audit_app

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
