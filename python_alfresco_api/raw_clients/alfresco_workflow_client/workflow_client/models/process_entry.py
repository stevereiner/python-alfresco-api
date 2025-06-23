from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process import Process


T = TypeVar("T", bound="ProcessEntry")


@_attrs_define
class ProcessEntry:
    """
    Attributes:
        entry (Union[Unset, Process]): A process describes a running instance of a process definition.

            When a new deployment includes a process definition that is already
            deployed with the same key, the newly deployed process definition will be
            considered a new version of the same process definition. By default
            processes will keep running in the process definition they are started in.
            But new processes can be started in the latest version of a process
            definition by using the processDefinitionKey parameter.

            In non-network deployments, administrators can see all processes and
            perform all operations on tasks. In network deployments, network
            administrators can see processes in their network and perform all
            operations on tasks in their network.
    """

    entry: Union[Unset, "Process"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process import Process

        d = dict(src_dict)
        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, Process]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = Process.from_dict(_entry)

        process_entry = cls(
            entry=entry,
        )

        process_entry.additional_properties = d
        return process_entry

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
