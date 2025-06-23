from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseConsistency")


@_attrs_define
class ResponseConsistency:
    """The consistency state of the index used to execute the query

    Attributes:
        last_tx_id (Union[Unset, int]): The id of the last indexed transaction
    """

    last_tx_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_tx_id = self.last_tx_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_tx_id is not UNSET:
            field_dict["lastTxId"] = last_tx_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        last_tx_id = d.pop("lastTxId", UNSET)

        response_consistency = cls(
            last_tx_id=last_tx_id,
        )

        response_consistency.additional_properties = d
        return response_consistency

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
