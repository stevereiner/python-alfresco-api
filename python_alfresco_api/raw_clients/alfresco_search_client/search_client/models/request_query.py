from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_query_language import RequestQueryLanguage
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestQuery")


@_attrs_define
class RequestQuery:
    """Query.

    Attributes:
        query (str): The query which may have been generated in some way from the userQuery
        language (Union[Unset, RequestQueryLanguage]): The query language in which the query is written. Default:
            RequestQueryLanguage.AFTS.
        user_query (Union[Unset, str]): The exact search request typed in by the user
    """

    query: str
    language: Union[Unset, RequestQueryLanguage] = RequestQueryLanguage.AFTS
    user_query: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        language: Union[Unset, str] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.value

        user_query = self.user_query

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if language is not UNSET:
            field_dict["language"] = language
        if user_query is not UNSET:
            field_dict["userQuery"] = user_query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        _language = d.pop("language", UNSET)
        language: Union[Unset, RequestQueryLanguage]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = RequestQueryLanguage(_language)

        user_query = d.pop("userQuery", UNSET)

        request_query = cls(
            query=query,
            language=language,
            user_query=user_query,
        )

        request_query.additional_properties = d
        return request_query

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
