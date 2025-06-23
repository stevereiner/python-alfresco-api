from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rendition_status import RenditionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_info import ContentInfo


T = TypeVar("T", bound="Rendition")


@_attrs_define
class Rendition:
    """
    Attributes:
        content (Union[Unset, ContentInfo]):
        id (Union[Unset, str]):
        status (Union[Unset, RenditionStatus]):
    """

    content: Union[Unset, "ContentInfo"] = UNSET
    id: Union[Unset, str] = UNSET
    status: Union[Unset, RenditionStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        id = self.id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_info import ContentInfo

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: Union[Unset, ContentInfo]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = ContentInfo.from_dict(_content)

        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RenditionStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RenditionStatus(_status)

        rendition = cls(
            content=content,
            id=id,
            status=status,
        )

        rendition.additional_properties = d
        return rendition

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
