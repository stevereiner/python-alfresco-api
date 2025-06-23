from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.site_body_update_visibility import SiteBodyUpdateVisibility
from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteBodyUpdate")


@_attrs_define
class SiteBodyUpdate:
    """
    Attributes:
        description (Union[Unset, str]):
        title (Union[Unset, str]):
        visibility (Union[Unset, SiteBodyUpdateVisibility]):
    """

    description: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    visibility: Union[Unset, SiteBodyUpdateVisibility] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        title = self.title

        visibility: Union[Unset, str] = UNSET
        if not isinstance(self.visibility, Unset):
            visibility = self.visibility.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if title is not UNSET:
            field_dict["title"] = title
        if visibility is not UNSET:
            field_dict["visibility"] = visibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        title = d.pop("title", UNSET)

        _visibility = d.pop("visibility", UNSET)
        visibility: Union[Unset, SiteBodyUpdateVisibility]
        if isinstance(_visibility, Unset):
            visibility = UNSET
        else:
            visibility = SiteBodyUpdateVisibility(_visibility)

        site_body_update = cls(
            description=description,
            title=title,
            visibility=visibility,
        )

        site_body_update.additional_properties = d
        return site_body_update

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
