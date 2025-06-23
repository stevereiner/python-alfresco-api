from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.variable import Variable


T = TypeVar("T", bound="VariableEntry")


@_attrs_define
class VariableEntry:
    """
    Attributes:
        entry (Union[Unset, Variable]): A task variable.
    """

    entry: Union[Unset, "Variable"] = UNSET
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
        from ..models.variable import Variable

        d = dict(src_dict)
        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, Variable]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = Variable.from_dict(_entry)

        variable_entry = cls(
            entry=entry,
        )

        variable_entry.additional_properties = d
        return variable_entry

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
