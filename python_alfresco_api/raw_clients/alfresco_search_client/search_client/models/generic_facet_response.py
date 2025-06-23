from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generic_bucket import GenericBucket


T = TypeVar("T", bound="GenericFacetResponse")


@_attrs_define
class GenericFacetResponse:
    """
    Attributes:
        buckets (Union[Unset, list['GenericBucket']]): An array of buckets and values
        label (Union[Unset, str]): The field name or its explicit label, if provided on the request
        type_ (Union[Unset, str]): The facet type, eg. interval, range, pivot, stats
    """

    buckets: Union[Unset, list["GenericBucket"]] = UNSET
    label: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buckets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        label = self.label

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buckets is not UNSET:
            field_dict["buckets"] = buckets
        if label is not UNSET:
            field_dict["label"] = label
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generic_bucket import GenericBucket

        d = dict(src_dict)
        buckets = []
        _buckets = d.pop("buckets", UNSET)
        for buckets_item_data in _buckets or []:
            buckets_item = GenericBucket.from_dict(buckets_item_data)

            buckets.append(buckets_item)

        label = d.pop("label", UNSET)

        type_ = d.pop("type", UNSET)

        generic_facet_response = cls(
            buckets=buckets,
            label=label,
            type_=type_,
        )

        generic_facet_response.additional_properties = d
        return generic_facet_response

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
