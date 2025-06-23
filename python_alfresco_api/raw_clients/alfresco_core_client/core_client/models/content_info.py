from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContentInfo")


@_attrs_define
class ContentInfo:
    """
    Attributes:
        mime_type (str):
        encoding (Union[Unset, str]):
        mime_type_name (Union[Unset, str]):
        size_in_bytes (Union[Unset, int]):
    """

    mime_type: str
    encoding: Union[Unset, str] = UNSET
    mime_type_name: Union[Unset, str] = UNSET
    size_in_bytes: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mime_type = self.mime_type

        encoding = self.encoding

        mime_type_name = self.mime_type_name

        size_in_bytes = self.size_in_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mimeType": mime_type,
            }
        )
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if mime_type_name is not UNSET:
            field_dict["mimeTypeName"] = mime_type_name
        if size_in_bytes is not UNSET:
            field_dict["sizeInBytes"] = size_in_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mime_type = d.pop("mimeType")

        encoding = d.pop("encoding", UNSET)

        mime_type_name = d.pop("mimeTypeName", UNSET)

        size_in_bytes = d.pop("sizeInBytes", UNSET)

        content_info = cls(
            mime_type=mime_type,
            encoding=encoding,
            mime_type_name=mime_type_name,
            size_in_bytes=size_in_bytes,
        )

        content_info.additional_properties = d
        return content_info

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
