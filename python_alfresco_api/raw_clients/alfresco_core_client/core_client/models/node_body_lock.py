from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.node_body_lock_lifetime import NodeBodyLockLifetime
from ..models.node_body_lock_type import NodeBodyLockType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeBodyLock")


@_attrs_define
class NodeBodyLock:
    """
    Attributes:
        lifetime (Union[Unset, NodeBodyLockLifetime]):  Default: NodeBodyLockLifetime.PERSISTENT.
        time_to_expire (Union[Unset, int]):
        type_ (Union[Unset, NodeBodyLockType]):  Default: NodeBodyLockType.ALLOW_OWNER_CHANGES.
    """

    lifetime: Union[Unset, NodeBodyLockLifetime] = NodeBodyLockLifetime.PERSISTENT
    time_to_expire: Union[Unset, int] = UNSET
    type_: Union[Unset, NodeBodyLockType] = NodeBodyLockType.ALLOW_OWNER_CHANGES
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lifetime: Union[Unset, str] = UNSET
        if not isinstance(self.lifetime, Unset):
            lifetime = self.lifetime.value

        time_to_expire = self.time_to_expire

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lifetime is not UNSET:
            field_dict["lifetime"] = lifetime
        if time_to_expire is not UNSET:
            field_dict["timeToExpire"] = time_to_expire
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _lifetime = d.pop("lifetime", UNSET)
        lifetime: Union[Unset, NodeBodyLockLifetime]
        if isinstance(_lifetime, Unset):
            lifetime = UNSET
        else:
            lifetime = NodeBodyLockLifetime(_lifetime)

        time_to_expire = d.pop("timeToExpire", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, NodeBodyLockType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NodeBodyLockType(_type_)

        node_body_lock = cls(
            lifetime=lifetime,
            time_to_expire=time_to_expire,
            type_=type_,
        )

        node_body_lock.additional_properties = d
        return node_body_lock

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
