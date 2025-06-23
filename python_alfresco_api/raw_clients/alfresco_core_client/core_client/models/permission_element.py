from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.permission_element_access_status import PermissionElementAccessStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PermissionElement")


@_attrs_define
class PermissionElement:
    """
    Attributes:
        access_status (Union[Unset, PermissionElementAccessStatus]):  Default: PermissionElementAccessStatus.ALLOWED.
        authority_id (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    access_status: Union[Unset, PermissionElementAccessStatus] = PermissionElementAccessStatus.ALLOWED
    authority_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_status: Union[Unset, str] = UNSET
        if not isinstance(self.access_status, Unset):
            access_status = self.access_status.value

        authority_id = self.authority_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_status is not UNSET:
            field_dict["accessStatus"] = access_status
        if authority_id is not UNSET:
            field_dict["authorityId"] = authority_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _access_status = d.pop("accessStatus", UNSET)
        access_status: Union[Unset, PermissionElementAccessStatus]
        if isinstance(_access_status, Unset):
            access_status = UNSET
        else:
            access_status = PermissionElementAccessStatus(_access_status)

        authority_id = d.pop("authorityId", UNSET)

        name = d.pop("name", UNSET)

        permission_element = cls(
            access_status=access_status,
            authority_id=authority_id,
            name=name,
        )

        permission_element.additional_properties = d
        return permission_element

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
