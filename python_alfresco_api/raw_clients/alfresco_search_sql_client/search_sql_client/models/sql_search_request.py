from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SQLSearchRequest")


@_attrs_define
class SQLSearchRequest:
    """
    Attributes:
        filter_queries (Union[Unset, list[str]]):
        format_ (Union[Unset, str]):
        include_metadata (Union[Unset, bool]):
        locales (Union[Unset, list[str]]):
        stmt (Union[Unset, str]):
        timezone (Union[Unset, str]):
    """

    filter_queries: Union[Unset, list[str]] = UNSET
    format_: Union[Unset, str] = UNSET
    include_metadata: Union[Unset, bool] = UNSET
    locales: Union[Unset, list[str]] = UNSET
    stmt: Union[Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_queries: Union[Unset, list[str]] = UNSET
        if not isinstance(self.filter_queries, Unset):
            filter_queries = self.filter_queries

        format_ = self.format_

        include_metadata = self.include_metadata

        locales: Union[Unset, list[str]] = UNSET
        if not isinstance(self.locales, Unset):
            locales = self.locales

        stmt = self.stmt

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_queries is not UNSET:
            field_dict["filterQueries"] = filter_queries
        if format_ is not UNSET:
            field_dict["format"] = format_
        if include_metadata is not UNSET:
            field_dict["includeMetadata"] = include_metadata
        if locales is not UNSET:
            field_dict["locales"] = locales
        if stmt is not UNSET:
            field_dict["stmt"] = stmt
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        filter_queries = cast(list[str], d.pop("filterQueries", UNSET))

        format_ = d.pop("format", UNSET)

        include_metadata = d.pop("includeMetadata", UNSET)

        locales = cast(list[str], d.pop("locales", UNSET))

        stmt = d.pop("stmt", UNSET)

        timezone = d.pop("timezone", UNSET)

        sql_search_request = cls(
            filter_queries=filter_queries,
            format_=format_,
            include_metadata=include_metadata,
            locales=locales,
            stmt=stmt,
            timezone=timezone,
        )

        sql_search_request.additional_properties = d
        return sql_search_request

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
