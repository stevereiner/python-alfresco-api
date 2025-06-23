from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_body_update_properties import NodeBodyUpdateProperties
    from ..models.permissions_body import PermissionsBody


T = TypeVar("T", bound="NodeBodyUpdate")


@_attrs_define
class NodeBodyUpdate:
    r"""
    Attributes:
        aspect_names (Union[Unset, list[str]]):
        name (Union[Unset, str]): The name must not contain spaces or the following special characters: * " < > \ / ? :
            and |.
            The character . must not be used at the end of the name.
        node_type (Union[Unset, str]):
        permissions (Union[Unset, PermissionsBody]):
        properties (Union[Unset, NodeBodyUpdateProperties]):
    """

    aspect_names: Union[Unset, list[str]] = UNSET
    name: Union[Unset, str] = UNSET
    node_type: Union[Unset, str] = UNSET
    permissions: Union[Unset, "PermissionsBody"] = UNSET
    properties: Union[Unset, "NodeBodyUpdateProperties"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aspect_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aspect_names, Unset):
            aspect_names = self.aspect_names

        name = self.name

        node_type = self.node_type

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_names is not UNSET:
            field_dict["aspectNames"] = aspect_names
        if name is not UNSET:
            field_dict["name"] = name
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_body_update_properties import NodeBodyUpdateProperties
        from ..models.permissions_body import PermissionsBody

        d = dict(src_dict)
        aspect_names = cast(list[str], d.pop("aspectNames", UNSET))

        name = d.pop("name", UNSET)

        node_type = d.pop("nodeType", UNSET)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, PermissionsBody]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = PermissionsBody.from_dict(_permissions)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, NodeBodyUpdateProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = NodeBodyUpdateProperties.from_dict(_properties)

        node_body_update = cls(
            aspect_names=aspect_names,
            name=name,
            node_type=node_type,
            permissions=permissions,
            properties=properties,
        )

        node_body_update.additional_properties = d
        return node_body_update

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
