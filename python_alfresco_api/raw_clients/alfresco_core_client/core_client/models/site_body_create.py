from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.site_body_create_visibility import SiteBodyCreateVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteBodyCreate")


@_attrs_define
class SiteBodyCreate:
    """
    Attributes:
        title (str):
        visibility (SiteBodyCreateVisibility):  Default: SiteBodyCreateVisibility.PUBLIC.
        description (Union[Unset, str]):
        id (Union[Unset, str]):
    """

    title: str
    visibility: SiteBodyCreateVisibility = SiteBodyCreateVisibility.PUBLIC
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        visibility = self.visibility.value

        description = self.description

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "visibility": visibility,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        visibility = SiteBodyCreateVisibility(d.pop("visibility"))

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        site_body_create = cls(
            title=title,
            visibility=visibility,
            description=description,
            id=id,
        )

        site_body_create.additional_properties = d
        return site_body_create

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
