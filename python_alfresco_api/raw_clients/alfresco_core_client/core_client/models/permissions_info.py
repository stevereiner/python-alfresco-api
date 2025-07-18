from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.permission_element import PermissionElement


T = TypeVar("T", bound="PermissionsInfo")


@_attrs_define
class PermissionsInfo:
    """
    Attributes:
        inherited (Union[Unset, list['PermissionElement']]):
        is_inheritance_enabled (Union[Unset, bool]):
        locally_set (Union[Unset, list['PermissionElement']]):
        settable (Union[Unset, list[str]]):
    """

    inherited: Union[Unset, list["PermissionElement"]] = UNSET
    is_inheritance_enabled: Union[Unset, bool] = UNSET
    locally_set: Union[Unset, list["PermissionElement"]] = UNSET
    settable: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inherited: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.inherited, Unset):
            inherited = []
            for inherited_item_data in self.inherited:
                inherited_item = inherited_item_data.to_dict()
                inherited.append(inherited_item)

        is_inheritance_enabled = self.is_inheritance_enabled

        locally_set: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locally_set, Unset):
            locally_set = []
            for locally_set_item_data in self.locally_set:
                locally_set_item = locally_set_item_data.to_dict()
                locally_set.append(locally_set_item)

        settable: Union[Unset, list[str]] = UNSET
        if not isinstance(self.settable, Unset):
            settable = self.settable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inherited is not UNSET:
            field_dict["inherited"] = inherited
        if is_inheritance_enabled is not UNSET:
            field_dict["isInheritanceEnabled"] = is_inheritance_enabled
        if locally_set is not UNSET:
            field_dict["locallySet"] = locally_set
        if settable is not UNSET:
            field_dict["settable"] = settable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_element import PermissionElement

        d = dict(src_dict)
        inherited = []
        _inherited = d.pop("inherited", UNSET)
        for inherited_item_data in _inherited or []:
            inherited_item = PermissionElement.from_dict(inherited_item_data)

            inherited.append(inherited_item)

        is_inheritance_enabled = d.pop("isInheritanceEnabled", UNSET)

        locally_set = []
        _locally_set = d.pop("locallySet", UNSET)
        for locally_set_item_data in _locally_set or []:
            locally_set_item = PermissionElement.from_dict(locally_set_item_data)

            locally_set.append(locally_set_item)

        settable = cast(list[str], d.pop("settable", UNSET))

        permissions_info = cls(
            inherited=inherited,
            is_inheritance_enabled=is_inheritance_enabled,
            locally_set=locally_set,
            settable=settable,
        )

        permissions_info.additional_properties = d
        return permissions_info

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
