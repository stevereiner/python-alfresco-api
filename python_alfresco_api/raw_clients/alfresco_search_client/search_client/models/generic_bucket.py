from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generic_bucket_bucket_info import GenericBucketBucketInfo
    from ..models.generic_bucket_display import GenericBucketDisplay
    from ..models.generic_bucket_facets_item import GenericBucketFacetsItem
    from ..models.generic_metric import GenericMetric


T = TypeVar("T", bound="GenericBucket")


@_attrs_define
class GenericBucket:
    """A bucket of facet results

    Attributes:
        bucket_info (Union[Unset, GenericBucketBucketInfo]): Additional information of nested facet
        display (Union[Unset, GenericBucketDisplay]): An optional field for additional display information
        facets (Union[Unset, list['GenericBucketFacetsItem']]): Additional list of nested facets
        filter_query (Union[Unset, str]): The filter query you can use to apply this facet
        label (Union[Unset, str]): The bucket label
        metrics (Union[Unset, list['GenericMetric']]): An array of buckets and values
    """

    bucket_info: Union[Unset, "GenericBucketBucketInfo"] = UNSET
    display: Union[Unset, "GenericBucketDisplay"] = UNSET
    facets: Union[Unset, list["GenericBucketFacetsItem"]] = UNSET
    filter_query: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    metrics: Union[Unset, list["GenericMetric"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bucket_info, Unset):
            bucket_info = self.bucket_info.to_dict()

        display: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.display, Unset):
            display = self.display.to_dict()

        facets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.facets, Unset):
            facets = []
            for facets_item_data in self.facets:
                facets_item = facets_item_data.to_dict()
                facets.append(facets_item)

        filter_query = self.filter_query

        label = self.label

        metrics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = []
            for metrics_item_data in self.metrics:
                metrics_item = metrics_item_data.to_dict()
                metrics.append(metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_info is not UNSET:
            field_dict["bucketInfo"] = bucket_info
        if display is not UNSET:
            field_dict["display"] = display
        if facets is not UNSET:
            field_dict["facets"] = facets
        if filter_query is not UNSET:
            field_dict["filterQuery"] = filter_query
        if label is not UNSET:
            field_dict["label"] = label
        if metrics is not UNSET:
            field_dict["metrics"] = metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generic_bucket_bucket_info import GenericBucketBucketInfo
        from ..models.generic_bucket_display import GenericBucketDisplay
        from ..models.generic_bucket_facets_item import GenericBucketFacetsItem
        from ..models.generic_metric import GenericMetric

        d = dict(src_dict)
        _bucket_info = d.pop("bucketInfo", UNSET)
        bucket_info: Union[Unset, GenericBucketBucketInfo]
        if isinstance(_bucket_info, Unset):
            bucket_info = UNSET
        else:
            bucket_info = GenericBucketBucketInfo.from_dict(_bucket_info)

        _display = d.pop("display", UNSET)
        display: Union[Unset, GenericBucketDisplay]
        if isinstance(_display, Unset):
            display = UNSET
        else:
            display = GenericBucketDisplay.from_dict(_display)

        facets = []
        _facets = d.pop("facets", UNSET)
        for facets_item_data in _facets or []:
            facets_item = GenericBucketFacetsItem.from_dict(facets_item_data)

            facets.append(facets_item)

        filter_query = d.pop("filterQuery", UNSET)

        label = d.pop("label", UNSET)

        metrics = []
        _metrics = d.pop("metrics", UNSET)
        for metrics_item_data in _metrics or []:
            metrics_item = GenericMetric.from_dict(metrics_item_data)

            metrics.append(metrics_item)

        generic_bucket = cls(
            bucket_info=bucket_info,
            display=display,
            facets=facets,
            filter_query=filter_query,
            label=label,
            metrics=metrics,
        )

        generic_bucket.additional_properties = d
        return generic_bucket

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
