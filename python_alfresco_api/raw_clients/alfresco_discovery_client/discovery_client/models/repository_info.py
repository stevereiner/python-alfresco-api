from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_info import LicenseInfo
    from ..models.module_info import ModuleInfo
    from ..models.status_info import StatusInfo
    from ..models.version_info import VersionInfo


T = TypeVar("T", bound="RepositoryInfo")


@_attrs_define
class RepositoryInfo:
    """
    Attributes:
        edition (str):
        id (str):
        status (StatusInfo):
        version (VersionInfo):
        license_ (Union[Unset, LicenseInfo]):
        modules (Union[Unset, list['ModuleInfo']]):
    """

    edition: str
    id: str
    status: "StatusInfo"
    version: "VersionInfo"
    license_: Union[Unset, "LicenseInfo"] = UNSET
    modules: Union[Unset, list["ModuleInfo"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        edition = self.edition

        id = self.id

        status = self.status.to_dict()

        version = self.version.to_dict()

        license_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.license_, Unset):
            license_ = self.license_.to_dict()

        modules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.modules, Unset):
            modules = []
            for modules_item_data in self.modules:
                modules_item = modules_item_data.to_dict()
                modules.append(modules_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edition": edition,
                "id": id,
                "status": status,
                "version": version,
            }
        )
        if license_ is not UNSET:
            field_dict["license"] = license_
        if modules is not UNSET:
            field_dict["modules"] = modules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.license_info import LicenseInfo
        from ..models.module_info import ModuleInfo
        from ..models.status_info import StatusInfo
        from ..models.version_info import VersionInfo

        d = dict(src_dict)
        edition = d.pop("edition")

        id = d.pop("id")

        status = StatusInfo.from_dict(d.pop("status"))

        version = VersionInfo.from_dict(d.pop("version"))

        _license_ = d.pop("license", UNSET)
        license_: Union[Unset, LicenseInfo]
        if isinstance(_license_, Unset):
            license_ = UNSET
        else:
            license_ = LicenseInfo.from_dict(_license_)

        modules = []
        _modules = d.pop("modules", UNSET)
        for modules_item_data in _modules or []:
            modules_item = ModuleInfo.from_dict(modules_item_data)

            modules.append(modules_item)

        repository_info = cls(
            edition=edition,
            id=id,
            status=status,
            version=version,
            license_=license_,
            modules=modules,
        )

        repository_info.additional_properties = d
        return repository_info

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
