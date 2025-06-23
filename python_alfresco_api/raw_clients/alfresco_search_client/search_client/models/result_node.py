import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_info import ContentInfo
    from ..models.node_properties import NodeProperties
    from ..models.path_info import PathInfo
    from ..models.search_entry import SearchEntry
    from ..models.user_info import UserInfo


T = TypeVar("T", bound="ResultNode")


@_attrs_define
class ResultNode:
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
        is_link (Union[Unset, bool]):
        is_locked (Union[Unset, bool]):  Default: False.
        parent_id (Union[Unset, str]):
        path (Union[Unset, PathInfo]):
        properties (Union[Unset, NodeProperties]):
        archived_at (Union[Unset, datetime.datetime]):
        archived_by_user (Union[Unset, UserInfo]):
        search (Union[Unset, SearchEntry]):
        version_comment (Union[Unset, str]):
        version_label (Union[Unset, str]):
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
    is_link: Union[Unset, bool] = UNSET
    is_locked: Union[Unset, bool] = False
    parent_id: Union[Unset, str] = UNSET
    path: Union[Unset, "PathInfo"] = UNSET
    properties: Union[Unset, "NodeProperties"] = UNSET
    archived_at: Union[Unset, datetime.datetime] = UNSET
    archived_by_user: Union[Unset, "UserInfo"] = UNSET
    search: Union[Unset, "SearchEntry"] = UNSET
    version_comment: Union[Unset, str] = UNSET
    version_label: Union[Unset, str] = UNSET
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

        is_link = self.is_link

        is_locked = self.is_locked

        parent_id = self.parent_id

        path: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.path, Unset):
            path = self.path.to_dict()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        archived_at: Union[Unset, str] = UNSET
        if not isinstance(self.archived_at, Unset):
            archived_at = self.archived_at.isoformat()

        archived_by_user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.archived_by_user, Unset):
            archived_by_user = self.archived_by_user.to_dict()

        search: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.search, Unset):
            search = self.search.to_dict()

        version_comment = self.version_comment

        version_label = self.version_label

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
        if is_link is not UNSET:
            field_dict["isLink"] = is_link
        if is_locked is not UNSET:
            field_dict["isLocked"] = is_locked
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if path is not UNSET:
            field_dict["path"] = path
        if properties is not UNSET:
            field_dict["properties"] = properties
        if archived_at is not UNSET:
            field_dict["archivedAt"] = archived_at
        if archived_by_user is not UNSET:
            field_dict["archivedByUser"] = archived_by_user
        if search is not UNSET:
            field_dict["search"] = search
        if version_comment is not UNSET:
            field_dict["versionComment"] = version_comment
        if version_label is not UNSET:
            field_dict["versionLabel"] = version_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_info import ContentInfo
        from ..models.node_properties import NodeProperties
        from ..models.path_info import PathInfo
        from ..models.search_entry import SearchEntry
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

        is_link = d.pop("isLink", UNSET)

        is_locked = d.pop("isLocked", UNSET)

        parent_id = d.pop("parentId", UNSET)

        _path = d.pop("path", UNSET)
        path: Union[Unset, PathInfo]
        if isinstance(_path, Unset):
            path = UNSET
        else:
            path = PathInfo.from_dict(_path)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, NodeProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = NodeProperties.from_dict(_properties)

        _archived_at = d.pop("archivedAt", UNSET)
        archived_at: Union[Unset, datetime.datetime]
        if isinstance(_archived_at, Unset):
            archived_at = UNSET
        else:
            archived_at = isoparse(_archived_at)

        _archived_by_user = d.pop("archivedByUser", UNSET)
        archived_by_user: Union[Unset, UserInfo]
        if isinstance(_archived_by_user, Unset):
            archived_by_user = UNSET
        else:
            archived_by_user = UserInfo.from_dict(_archived_by_user)

        _search = d.pop("search", UNSET)
        search: Union[Unset, SearchEntry]
        if isinstance(_search, Unset):
            search = UNSET
        else:
            search = SearchEntry.from_dict(_search)

        version_comment = d.pop("versionComment", UNSET)

        version_label = d.pop("versionLabel", UNSET)

        result_node = cls(
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
            is_link=is_link,
            is_locked=is_locked,
            parent_id=parent_id,
            path=path,
            properties=properties,
            archived_at=archived_at,
            archived_by_user=archived_by_user,
            search=search,
            version_comment=version_comment,
            version_label=version_label,
        )

        result_node.additional_properties = d
        return result_node

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
