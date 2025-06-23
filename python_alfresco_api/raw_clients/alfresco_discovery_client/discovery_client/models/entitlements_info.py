from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntitlementsInfo")


@_attrs_define
class EntitlementsInfo:
    """
    Attributes:
        is_cluster_enabled (Union[Unset, bool]):  Default: False.
        is_cryptodoc_enabled (Union[Unset, bool]):  Default: False.
        max_docs (Union[Unset, int]):
        max_users (Union[Unset, int]):
    """

    is_cluster_enabled: Union[Unset, bool] = False
    is_cryptodoc_enabled: Union[Unset, bool] = False
    max_docs: Union[Unset, int] = UNSET
    max_users: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_cluster_enabled = self.is_cluster_enabled

        is_cryptodoc_enabled = self.is_cryptodoc_enabled

        max_docs = self.max_docs

        max_users = self.max_users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_cluster_enabled is not UNSET:
            field_dict["isClusterEnabled"] = is_cluster_enabled
        if is_cryptodoc_enabled is not UNSET:
            field_dict["isCryptodocEnabled"] = is_cryptodoc_enabled
        if max_docs is not UNSET:
            field_dict["maxDocs"] = max_docs
        if max_users is not UNSET:
            field_dict["maxUsers"] = max_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_cluster_enabled = d.pop("isClusterEnabled", UNSET)

        is_cryptodoc_enabled = d.pop("isCryptodocEnabled", UNSET)

        max_docs = d.pop("maxDocs", UNSET)

        max_users = d.pop("maxUsers", UNSET)

        entitlements_info = cls(
            is_cluster_enabled=is_cluster_enabled,
            is_cryptodoc_enabled=is_cryptodoc_enabled,
            max_docs=max_docs,
            max_users=max_users,
        )

        entitlements_info.additional_properties = d
        return entitlements_info

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
