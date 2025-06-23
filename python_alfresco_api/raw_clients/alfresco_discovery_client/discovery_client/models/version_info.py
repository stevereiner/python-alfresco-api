from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VersionInfo")


@_attrs_define
class VersionInfo:
    """
    Attributes:
        display (str):
        hotfix (str):
        label (str):
        major (str):
        minor (str):
        patch (str):
        schema (int):
    """

    display: str
    hotfix: str
    label: str
    major: str
    minor: str
    patch: str
    schema: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display = self.display

        hotfix = self.hotfix

        label = self.label

        major = self.major

        minor = self.minor

        patch = self.patch

        schema = self.schema

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display": display,
                "hotfix": hotfix,
                "label": label,
                "major": major,
                "minor": minor,
                "patch": patch,
                "schema": schema,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display = d.pop("display")

        hotfix = d.pop("hotfix")

        label = d.pop("label")

        major = d.pop("major")

        minor = d.pop("minor")

        patch = d.pop("patch")

        schema = d.pop("schema")

        version_info = cls(
            display=display,
            hotfix=hotfix,
            label=label,
            major=major,
            minor=minor,
            patch=patch,
            schema=schema,
        )

        version_info.additional_properties = d
        return version_info

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
