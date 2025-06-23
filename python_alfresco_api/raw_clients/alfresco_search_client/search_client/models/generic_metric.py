from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generic_metric_value import GenericMetricValue


T = TypeVar("T", bound="GenericMetric")


@_attrs_define
class GenericMetric:
    """A metric used in faceting

    Attributes:
        type_ (Union[Unset, str]): The type of metric, e.g. count
        value (Union[Unset, GenericMetricValue]): The metric value, e.g. {"count": 34}
    """

    type_: Union[Unset, str] = UNSET
    value: Union[Unset, "GenericMetricValue"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        value: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generic_metric_value import GenericMetricValue

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, GenericMetricValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = GenericMetricValue.from_dict(_value)

        generic_metric = cls(
            type_=type_,
            value=value,
        )

        generic_metric.additional_properties = d
        return generic_metric

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
