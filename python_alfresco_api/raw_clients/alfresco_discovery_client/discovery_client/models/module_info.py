import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModuleInfo")


@_attrs_define
class ModuleInfo:
    """
    Attributes:
        description (Union[Unset, str]):
        id (Union[Unset, str]):
        install_date (Union[Unset, datetime.datetime]):
        install_state (Union[Unset, str]):
        title (Union[Unset, str]):
        version (Union[Unset, str]):
        version_max (Union[Unset, str]):
        version_min (Union[Unset, str]):
    """

    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    install_date: Union[Unset, datetime.datetime] = UNSET
    install_state: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    version_max: Union[Unset, str] = UNSET
    version_min: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        id = self.id

        install_date: Union[Unset, str] = UNSET
        if not isinstance(self.install_date, Unset):
            install_date = self.install_date.isoformat()

        install_state = self.install_state

        title = self.title

        version = self.version

        version_max = self.version_max

        version_min = self.version_min

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if install_date is not UNSET:
            field_dict["installDate"] = install_date
        if install_state is not UNSET:
            field_dict["installState"] = install_state
        if title is not UNSET:
            field_dict["title"] = title
        if version is not UNSET:
            field_dict["version"] = version
        if version_max is not UNSET:
            field_dict["versionMax"] = version_max
        if version_min is not UNSET:
            field_dict["versionMin"] = version_min

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _install_date = d.pop("installDate", UNSET)
        install_date: Union[Unset, datetime.datetime]
        if isinstance(_install_date, Unset):
            install_date = UNSET
        else:
            install_date = isoparse(_install_date)

        install_state = d.pop("installState", UNSET)

        title = d.pop("title", UNSET)

        version = d.pop("version", UNSET)

        version_max = d.pop("versionMax", UNSET)

        version_min = d.pop("versionMin", UNSET)

        module_info = cls(
            description=description,
            id=id,
            install_date=install_date,
            install_state=install_state,
            title=title,
            version=version,
            version_max=version_max,
            version_min=version_min,
        )

        module_info.additional_properties = d
        return module_info

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
