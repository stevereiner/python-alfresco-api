from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestPivot")


@_attrs_define
class RequestPivot:
    """A list of pivots.

    Example:
        {'key': 'MyKey', 'pivots': [{'key': 'AnotherKey', 'pivots': []}]}

    Attributes:
        key (Union[Unset, str]): A key corresponding to a matching field facet label or stats.
        pivots (Union[Unset, list['RequestPivot']]):
    """

    key: Union[Unset, str] = UNSET
    pivots: Union[Unset, list["RequestPivot"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        pivots: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pivots, Unset):
            pivots = []
            for pivots_item_data in self.pivots:
                pivots_item = pivots_item_data.to_dict()
                pivots.append(pivots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if pivots is not UNSET:
            field_dict["pivots"] = pivots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        pivots = []
        _pivots = d.pop("pivots", UNSET)
        for pivots_item_data in _pivots or []:
            pivots_item = RequestPivot.from_dict(pivots_item_data)

            pivots.append(pivots_item)

        request_pivot = cls(
            key=key,
            pivots=pivots,
        )

        request_pivot.additional_properties = d
        return request_pivot

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
