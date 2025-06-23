import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_info import ContentInfo
    from ..models.user_info import UserInfo
    from ..models.version_properties import VersionProperties


T = TypeVar("T", bound="Version")


@_attrs_define
class Version:
    r"""
    Attributes:
        id (str):
        is_file (bool):
        is_folder (bool):
        modified_at (datetime.datetime):
        modified_by_user (UserInfo):
        name (str): The name must not contain spaces or the following special characters: * " < > \ / ? : and |.
            The character . must not be used at the end of the name.
        node_type (str):
        aspect_names (Union[Unset, list[str]]):
        content (Union[Unset, ContentInfo]):
        properties (Union[Unset, VersionProperties]):
        version_comment (Union[Unset, str]):
    """

    id: str
    is_file: bool
    is_folder: bool
    modified_at: datetime.datetime
    modified_by_user: "UserInfo"
    name: str
    node_type: str
    aspect_names: Union[Unset, list[str]] = UNSET
    content: Union[Unset, "ContentInfo"] = UNSET
    properties: Union[Unset, "VersionProperties"] = UNSET
    version_comment: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_file = self.is_file

        is_folder = self.is_folder

        modified_at = self.modified_at.isoformat()

        modified_by_user = self.modified_by_user.to_dict()

        name = self.name

        node_type = self.node_type

        aspect_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aspect_names, Unset):
            aspect_names = self.aspect_names

        content: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        version_comment = self.version_comment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isFile": is_file,
                "isFolder": is_folder,
                "modifiedAt": modified_at,
                "modifiedByUser": modified_by_user,
                "name": name,
                "nodeType": node_type,
            }
        )
        if aspect_names is not UNSET:
            field_dict["aspectNames"] = aspect_names
        if content is not UNSET:
            field_dict["content"] = content
        if properties is not UNSET:
            field_dict["properties"] = properties
        if version_comment is not UNSET:
            field_dict["versionComment"] = version_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_info import ContentInfo
        from ..models.user_info import UserInfo
        from ..models.version_properties import VersionProperties

        d = dict(src_dict)
        id = d.pop("id")

        is_file = d.pop("isFile")

        is_folder = d.pop("isFolder")

        modified_at = isoparse(d.pop("modifiedAt"))

        modified_by_user = UserInfo.from_dict(d.pop("modifiedByUser"))

        name = d.pop("name")

        node_type = d.pop("nodeType")

        aspect_names = cast(list[str], d.pop("aspectNames", UNSET))

        _content = d.pop("content", UNSET)
        content: Union[Unset, ContentInfo]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ContentInfo.from_dict(_content)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, VersionProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = VersionProperties.from_dict(_properties)

        version_comment = d.pop("versionComment", UNSET)

        version = cls(
            id=id,
            is_file=is_file,
            is_folder=is_folder,
            modified_at=modified_at,
            modified_by_user=modified_by_user,
            name=name,
            node_type=node_type,
            aspect_names=aspect_names,
            content=content,
            properties=properties,
            version_comment=version_comment,
        )

        version.additional_properties = d
        return version

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
