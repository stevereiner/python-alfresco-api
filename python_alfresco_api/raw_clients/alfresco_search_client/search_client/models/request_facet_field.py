from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_facet_field_method import RequestFacetFieldMethod
from ..models.request_facet_field_sort import RequestFacetFieldSort
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestFacetField")


@_attrs_define
class RequestFacetField:
    """A simple facet field

    Attributes:
        exclude_filters (Union[Unset, list[str]]): Filter Queries with tags listed here will not be included in facet
            counts.
            This is used for multi-select facetting.
        facet_enum_cache_min_df (Union[Unset, int]):
        field (Union[Unset, str]): The facet field
        label (Union[Unset, str]): A label to include in place of the facet field
        limit (Union[Unset, int]):
        method (Union[Unset, RequestFacetFieldMethod]):
        mincount (Union[Unset, int]): The minimum count required for a facet field to be included in the response.
            Default: 1.
        missing (Union[Unset, bool]): When true, count results that match the query but which have no facet value for
            the field (in addition to the Term-based constraints). Default: False.
        offset (Union[Unset, int]):
        prefix (Union[Unset, str]): Restricts the possible constraints to only indexed values with a specified prefix.
        sort (Union[Unset, RequestFacetFieldSort]):
    """

    exclude_filters: Union[Unset, list[str]] = UNSET
    facet_enum_cache_min_df: Union[Unset, int] = UNSET
    field: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    limit: Union[Unset, int] = UNSET
    method: Union[Unset, RequestFacetFieldMethod] = UNSET
    mincount: Union[Unset, int] = 1
    missing: Union[Unset, bool] = False
    offset: Union[Unset, int] = UNSET
    prefix: Union[Unset, str] = UNSET
    sort: Union[Unset, RequestFacetFieldSort] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude_filters: Union[Unset, list[str]] = UNSET
        if not isinstance(self.exclude_filters, Unset):
            exclude_filters = self.exclude_filters

        facet_enum_cache_min_df = self.facet_enum_cache_min_df

        field = self.field

        label = self.label

        limit = self.limit

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        mincount = self.mincount

        missing = self.missing

        offset = self.offset

        prefix = self.prefix

        sort: Union[Unset, str] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude_filters is not UNSET:
            field_dict["excludeFilters"] = exclude_filters
        if facet_enum_cache_min_df is not UNSET:
            field_dict["facetEnumCacheMinDf"] = facet_enum_cache_min_df
        if field is not UNSET:
            field_dict["field"] = field
        if label is not UNSET:
            field_dict["label"] = label
        if limit is not UNSET:
            field_dict["limit"] = limit
        if method is not UNSET:
            field_dict["method"] = method
        if mincount is not UNSET:
            field_dict["mincount"] = mincount
        if missing is not UNSET:
            field_dict["missing"] = missing
        if offset is not UNSET:
            field_dict["offset"] = offset
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exclude_filters = cast(list[str], d.pop("excludeFilters", UNSET))

        facet_enum_cache_min_df = d.pop("facetEnumCacheMinDf", UNSET)

        field = d.pop("field", UNSET)

        label = d.pop("label", UNSET)

        limit = d.pop("limit", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, RequestFacetFieldMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = RequestFacetFieldMethod(_method)

        mincount = d.pop("mincount", UNSET)

        missing = d.pop("missing", UNSET)

        offset = d.pop("offset", UNSET)

        prefix = d.pop("prefix", UNSET)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, RequestFacetFieldSort]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = RequestFacetFieldSort(_sort)

        request_facet_field = cls(
            exclude_filters=exclude_filters,
            facet_enum_cache_min_df=facet_enum_cache_min_df,
            field=field,
            label=label,
            limit=limit,
            method=method,
            mincount=mincount,
            missing=missing,
            offset=offset,
            prefix=prefix,
            sort=sort,
        )

        request_facet_field.additional_properties = d
        return request_facet_field

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
