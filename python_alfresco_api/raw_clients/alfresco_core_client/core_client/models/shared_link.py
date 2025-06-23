import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_info import ContentInfo
    from ..models.path_info import PathInfo
    from ..models.shared_link_properties import SharedLinkProperties
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="SharedLink")


@_attrs_define
class SharedLink:
    r"""
    Attributes:
        allowable_operations (Union[Unset, list[str]]): The allowable operations for the Quickshare link itself. See
            allowableOperationsOnTarget for the
            allowable operations pertaining to the linked content node.
        allowable_operations_on_target (Union[Unset, list[str]]): The allowable operations for the content node being
            shared.
        aspect_names (Union[Unset, list[str]]):
        content (Union[Unset, ContentInfo]):
        description (Union[Unset, str]):
        expires_at (Union[Unset, datetime.datetime]):
        id (Union[Unset, str]):
        is_favorite (Union[Unset, bool]):
        modified_at (Union[Unset, datetime.datetime]):
        modified_by_user (Union[Unset, UserInfo]):
        name (Union[Unset, str]): The name must not contain spaces or the following special characters: * " < > \ / ? :
            and |.
            The character . must not be used at the end of the name.
        node_id (Union[Unset, str]):
        path (Union[Unset, PathInfo]):
        properties (Union[Unset, SharedLinkProperties]): A subset of the target node's properties, system properties and
            properties already available in the SharedLink are excluded.
        shared_by_user (Union[Unset, UserInfo]):
        title (Union[Unset, str]):
    """

    allowable_operations: Union[Unset, list[str]] = UNSET
    allowable_operations_on_target: Union[Unset, list[str]] = UNSET
    aspect_names: Union[Unset, list[str]] = UNSET
    content: Union[Unset, "ContentInfo"] = UNSET
    description: Union[Unset, str] = UNSET
    expires_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    is_favorite: Union[Unset, bool] = UNSET
    modified_at: Union[Unset, datetime.datetime] = UNSET
    modified_by_user: Union[Unset, "UserInfo"] = UNSET
    name: Union[Unset, str] = UNSET
    node_id: Union[Unset, str] = UNSET
    path: Union[Unset, "PathInfo"] = UNSET
    properties: Union[Unset, "SharedLinkProperties"] = UNSET
    shared_by_user: Union[Unset, "UserInfo"] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allowable_operations: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowable_operations, Unset):
            allowable_operations = self.allowable_operations

        allowable_operations_on_target: Union[Unset, list[str]] = UNSET
        if not isinstance(self.allowable_operations_on_target, Unset):
            allowable_operations_on_target = self.allowable_operations_on_target

        aspect_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aspect_names, Unset):
            aspect_names = self.aspect_names

        content: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        description = self.description

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        id = self.id

        is_favorite = self.is_favorite

        modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by_user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.modified_by_user, Unset):
            modified_by_user = self.modified_by_user.to_dict()

        name = self.name

        node_id = self.node_id

        path: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        shared_by_user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.shared_by_user, Unset):
            shared_by_user = self.shared_by_user.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allowable_operations is not UNSET:
            field_dict["allowableOperations"] = allowable_operations
        if allowable_operations_on_target is not UNSET:
            field_dict["allowableOperationsOnTarget"] = allowable_operations_on_target
        if aspect_names is not UNSET:
            field_dict["aspectNames"] = aspect_names
        if content is not UNSET:
            field_dict["content"] = content
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if is_favorite is not UNSET:
            field_dict["isFavorite"] = is_favorite
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by_user is not UNSET:
            field_dict["modifiedByUser"] = modified_by_user
        if name is not UNSET:
            field_dict["name"] = name
        if node_id is not UNSET:
            field_dict["nodeId"] = node_id
        if path is not UNSET:
            field_dict["path"] = path
        if properties is not UNSET:
            field_dict["properties"] = properties
        if shared_by_user is not UNSET:
            field_dict["sharedByUser"] = shared_by_user
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_info import ContentInfo
        from ..models.path_info import PathInfo
        from ..models.shared_link_properties import SharedLinkProperties
        from ..models.user_info import UserInfo

        d = dict(src_dict)
        allowable_operations = cast(list[str], d.pop("allowableOperations", UNSET))

        allowable_operations_on_target = cast(list[str], d.pop("allowableOperationsOnTarget", UNSET))

        aspect_names = cast(list[str], d.pop("aspectNames", UNSET))

        _content = d.pop("content", UNSET)
        content: Union[Unset, ContentInfo]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ContentInfo.from_dict(_content)

        description = d.pop("description", UNSET)

        _expires_at = d.pop("expiresAt", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        id = d.pop("id", UNSET)

        is_favorite = d.pop("isFavorite", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: Union[Unset, datetime.datetime]
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        _modified_by_user = d.pop("modifiedByUser", UNSET)
        modified_by_user: Union[Unset, UserInfo]
        if isinstance(_modified_by_user, Unset):
            modified_by_user = UNSET
        else:
            modified_by_user = UserInfo.from_dict(_modified_by_user)

        name = d.pop("name", UNSET)

        node_id = d.pop("nodeId", UNSET)

        _path = d.pop("path", UNSET)
        path: Union[Unset, PathInfo]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = PathInfo.from_dict(_path)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, SharedLinkProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = SharedLinkProperties.from_dict(_properties)

        _shared_by_user = d.pop("sharedByUser", UNSET)
        shared_by_user: Union[Unset, UserInfo]
        if isinstance(_shared_by_user, Unset):
            shared_by_user = UNSET
        else:
            shared_by_user = UserInfo.from_dict(_shared_by_user)

        title = d.pop("title", UNSET)

        shared_link = cls(
            allowable_operations=allowable_operations,
            allowable_operations_on_target=allowable_operations_on_target,
            aspect_names=aspect_names,
            content=content,
            description=description,
            expires_at=expires_at,
            id=id,
            is_favorite=is_favorite,
            modified_at=modified_at,
            modified_by_user=modified_by_user,
            name=name,
            node_id=node_id,
            path=path,
            properties=properties,
            shared_by_user=shared_by_user,
            title=title,
        )

        shared_link.additional_properties = d
        return shared_link

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
