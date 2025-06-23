from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_facet_set import RequestFacetSet


T = TypeVar("T", bound="RequestFacetIntervalsIntervalsItem")


@_attrs_define
class RequestFacetIntervalsIntervalsItem:
    """
    Attributes:
        field (Union[Unset, str]): The field to facet on
        label (Union[Unset, str]): A label to use to identify the field facet
        sets (Union[Unset, list['RequestFacetSet']]): Sets the intervals for all fields.
    """

    field: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    sets: Union[Unset, list["RequestFacetSet"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        label = self.label

        sets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sets, Unset):
            sets = []
            for sets_item_data in self.sets:
                sets_item = sets_item_data.to_dict()
                sets.append(sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if label is not UNSET:
            field_dict["label"] = label
        if sets is not UNSET:
            field_dict["sets"] = sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_facet_set import RequestFacetSet

        d = dict(src_dict)
        field = d.pop("field", UNSET)

        label = d.pop("label", UNSET)

        sets = []
        _sets = d.pop("sets", UNSET)
        for sets_item_data in _sets or []:
            sets_item = RequestFacetSet.from_dict(sets_item_data)

            sets.append(sets_item)

        request_facet_intervals_intervals_item = cls(
            field=field,
            label=label,
            sets=sets,
        )

        request_facet_intervals_intervals_item.additional_properties = d
        return request_facet_intervals_intervals_item

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
