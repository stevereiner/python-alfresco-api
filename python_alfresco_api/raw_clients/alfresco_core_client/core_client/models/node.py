import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_info import ContentInfo
    from ..models.definition import Definition
    from ..models.node_properties import NodeProperties
    from ..models.path_info import PathInfo
    from ..models.permissions_info import PermissionsInfo
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="Node")


@_attrs_define
class Node:
    r"""
    Attributes:
        created_at (datetime.datetime):
        created_by_user (UserInfo):
        id (str):
        is_file (bool):
        is_folder (bool):
        modified_at (datetime.datetime):
        modified_by_user (UserInfo):
        name (str): The name must not contain spaces or the following special characters: * " < > \ / ? : and |.
            The character . must not be used at the end of the name.
        node_type (str):
        allowable_operations (Union[Unset, list[str]]):
        aspect_names (Union[Unset, list[str]]):
        content (Union[Unset, ContentInfo]):
        definition (Union[Unset, Definition]):
        is_favorite (Union[Unset, bool]):
        is_link (Union[Unset, bool]):
        is_locked (Union[Unset, bool]):  Default: False.
        parent_id (Union[Unset, str]):
        path (Union[Unset, PathInfo]):
        permissions (Union[Unset, PermissionsInfo]):
        properties (Union[Unset, NodeProperties]):
    """

    created_at: datetime.datetime
    created_by_user: "UserInfo"
    id: str
    is_file: bool
    is_folder: bool
    modified_at: datetime.datetime
    modified_by_user: "UserInfo"
    name: str
    node_type: str
    allowable_operations: Union[Unset, list[str]] = UNSET
    aspect_names: Union[Unset, list[str]] = UNSET
    content: Union[Unset, "ContentInfo"] = UNSET
    definition: Union[Unset, "Definition"] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    is_link: Union[Unset, bool] = UNSET
    is_locked: Union[Unset, bool] = False
    parent_id: Union[Unset, str] = UNSET
    path: Union[Unset, "PathInfo"] = UNSET
    permissions: Union[Unset, "PermissionsInfo"] = UNSET
    properties: Union[Unset, "NodeProperties"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by_user = self.created_by_user.to_dict()

        id = self.id

        is_file = self.is_file

        is_folder = self.is_folder

        modified_at = self.modified_at.isoformat()

        modified_by_user = self.modified_by_user.to_dict()

        name = self.name

        node_type = self.node_type

        allowable_operations: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowable_operations, Unset):
            allowable_operations = self.allowable_operations

        aspect_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aspect_names, Unset):
            aspect_names = self.aspect_names

        content: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        definition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

        is_favorite = self.is_favorite

        is_link = self.is_link

        is_locked = self.is_locked

        parent_id = self.parent_id

        path: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "createdByUser": created_by_user,
                "id": id,
                "isFile": is_file,
                "isFolder": is_folder,
                "modifiedAt": modified_at,
                "modifiedByUser": modified_by_user,
                "name": name,
                "nodeType": node_type,
            }
        )
        if allowable_operations is not UNSET:
            field_dict["allowableOperations"] = allowable_operations
        if aspect_names is not UNSET:
            field_dict["aspectNames"] = aspect_names
        if content is not UNSET:
            field_dict["content"] = content
        if definition is not UNSET:
            field_dict["definition"] = definition
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if is_link is not UNSET:
            field_dict["isLink"] = is_link
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if path is not UNSET:
            field_dict["path"] = path
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_info import ContentInfo
        from ..models.definition import Definition
        from ..models.node_properties import NodeProperties
        from ..models.path_info import PathInfo
        from ..models.permissions_info import PermissionsInfo
        from ..models.user_info import UserInfo

        d = dict(src_dict)
        created_at = isoparse(d.pop("createdAt"))

        created_by_user = UserInfo.from_dict(d.pop("createdByUser"))

        id = d.pop("id")

        is_file = d.pop("isFile")

        is_folder = d.pop("isFolder")

        modified_at = isoparse(d.pop("modifiedAt"))

        modified_by_user = UserInfo.from_dict(d.pop("modifiedByUser"))

        name = d.pop("name")

        node_type = d.pop("nodeType")

        allowable_operations = cast(list[str], d.pop("allowableOperations", UNSET))

        aspect_names = cast(list[str], d.pop("aspectNames", UNSET))

        _content = d.pop("content", UNSET)
        content: Union[Unset, ContentInfo]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ContentInfo.from_dict(_content)

        _definition = d.pop("definition", UNSET)
        definition: Union[Unset, Definition]
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = Definition.from_dict(_definition)

        is_favorite = d.pop("isFavorite", UNSET)

        is_link = d.pop("isLink", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        parent_id = d.pop("parentId", UNSET)

        _path = d.pop("path", UNSET)
        path: Union[Unset, PathInfo]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = PathInfo.from_dict(_path)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, PermissionsInfo]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = PermissionsInfo.from_dict(_permissions)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, NodeProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = NodeProperties.from_dict(_properties)

        node = cls(
            created_at=created_at,
            created_by_user=created_by_user,
            id=id,
            is_file=is_file,
            is_folder=is_folder,
            modified_at=modified_at,
            modified_by_user=modified_by_user,
            name=name,
            node_type=node_type,
            allowable_operations=allowable_operations,
            aspect_names=aspect_names,
            content=content,
            definition=definition,
            is_favorite=is_favorite,
            is_link=is_link,
            is_locked=is_locked,
            parent_id=parent_id,
            path=path,
            permissions=permissions,
            properties=properties,
        )

        node.additional_properties = d
        return node

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
