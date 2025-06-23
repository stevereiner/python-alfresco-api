from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.download_status import DownloadStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Download")


@_attrs_define
class Download:
    """
    Attributes:
        bytes_added (Union[Unset, int]): number of bytes added so far in the zip Default: 0.
        files_added (Union[Unset, int]): number of files added so far in the zip Default: 0.
        id (Union[Unset, str]): the id of the download node
        status (Union[Unset, DownloadStatus]): the current status of the download node creation Default:
            DownloadStatus.PENDING.
        total_bytes (Union[Unset, int]): the total number of bytes to be added in the zip Default: 0.
        total_files (Union[Unset, int]): the total number of files to be added in the zip Default: 0.
    """

    bytes_added: Union[Unset, int] = 0
    files_added: Union[Unset, int] = 0
    id: Union[Unset, str] = UNSET
    status: Union[Unset, DownloadStatus] = DownloadStatus.PENDING
    total_bytes: Union[Unset, int] = 0
    total_files: Union[Unset, int] = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_added = self.bytes_added

        files_added = self.files_added

        id = self.id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        total_bytes = self.total_bytes

        total_files = self.total_files

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bytes_added is not UNSET:
            field_dict["bytesAdded"] = bytes_added
        if files_added is not UNSET:
            field_dict["filesAdded"] = files_added
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if total_bytes is not UNSET:
            field_dict["totalBytes"] = total_bytes
        if total_files is not UNSET:
            field_dict["totalFiles"] = total_files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bytes_added = d.pop("bytesAdded", UNSET)

        files_added = d.pop("filesAdded", UNSET)

        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DownloadStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DownloadStatus(_status)

        total_bytes = d.pop("totalBytes", UNSET)

        total_files = d.pop("totalFiles", UNSET)

        download = cls(
            bytes_added=bytes_added,
            files_added=files_added,
            id=id,
            status=status,
            total_bytes=total_bytes,
            total_files=total_files,
        )

        download.additional_properties = d
        return download

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
