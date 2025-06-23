from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_scope_locations import RequestScopeLocations
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestScope")


@_attrs_define
class RequestScope:
    """Scope

    Attributes:
        locations (Union[Unset, RequestScopeLocations]): The locations to include in the query
    """

    locations: Union[Unset, RequestScopeLocations] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        locations: Union[Unset, str] = UNSET
        if not isinstance(self.locations, Unset):
            locations = self.locations.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _locations = d.pop("locations", UNSET)
        locations: Union[Unset, RequestScopeLocations]
        if isinstance(_locations, Unset):
            locations = UNSET
        else:
            locations = RequestScopeLocations(_locations)

        request_scope = cls(
            locations=locations,
        )

        request_scope.additional_properties = d
        return request_scope

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
