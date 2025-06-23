from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Model")


@_attrs_define
class Model:
    """
    Attributes:
        id (str):
        author (Union[Unset, str]):
        description (Union[Unset, str]):
        namespace_prefix (Union[Unset, str]):
        namespace_uri (Union[Unset, str]):
    """

    id: str
    author: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    namespace_prefix: Union[Unset, str] = UNSET
    namespace_uri: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        author = self.author

        description = self.description

        namespace_prefix = self.namespace_prefix

        namespace_uri = self.namespace_uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if author is not UNSET:
            field_dict["author"] = author
        if description is not UNSET:
            field_dict["description"] = description
        if namespace_prefix is not UNSET:
            field_dict["namespacePrefix"] = namespace_prefix
        if namespace_uri is not UNSET:
            field_dict["namespaceUri"] = namespace_uri

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        author = d.pop("author", UNSET)

        description = d.pop("description", UNSET)

        namespace_prefix = d.pop("namespacePrefix", UNSET)

        namespace_uri = d.pop("namespaceUri", UNSET)

        model = cls(
            id=id,
            author=author,
            description=description,
            namespace_prefix=namespace_prefix,
            namespace_uri=namespace_uri,
        )

        model.additional_properties = d
        return model

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
