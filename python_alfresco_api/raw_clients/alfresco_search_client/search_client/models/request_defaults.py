from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_defaults_default_fts_field_operator import RequestDefaultsDefaultFTSFieldOperator
from ..models.request_defaults_default_fts_operator import RequestDefaultsDefaultFTSOperator
from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestDefaults")


@_attrs_define
class RequestDefaults:
    """Common query defaults

    Attributes:
        default_fts_field_operator (Union[Unset, RequestDefaultsDefaultFTSFieldOperator]): The default way to combine
            query parts in field query groups when AND or OR is not explicitly stated - includes ! - +
            FIELD:(one two three)
             Default: RequestDefaultsDefaultFTSFieldOperator.AND.
        default_fts_operator (Union[Unset, RequestDefaultsDefaultFTSOperator]): The default way to combine query parts
            when AND or OR is not explicitly stated - includes ! - +
            one two three
            (one two three)
             Default: RequestDefaultsDefaultFTSOperator.AND.
        default_field_name (Union[Unset, str]):  Default: 'TEXT'.
        namespace (Union[Unset, str]): The default name space to use if one is not provided Default: 'cm'.
        text_attributes (Union[Unset, list[str]]): A list of query fields/properties used to expand TEXT: queries.
            The default is cm:content.
            You could include all content properties using d:content or list all individual content properties or types.
            As more terms are included the query size, complexity, memory impact and query time will increase.
    """

    default_fts_field_operator: Union[Unset, RequestDefaultsDefaultFTSFieldOperator] = (
        RequestDefaultsDefaultFTSFieldOperator.AND
    )
    default_fts_operator: Union[Unset, RequestDefaultsDefaultFTSOperator] = RequestDefaultsDefaultFTSOperator.AND
    default_field_name: Union[Unset, str] = "TEXT"
    namespace: Union[Unset, str] = "cm"
    text_attributes: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_fts_field_operator: Union[Unset, str] = UNSET
        if not isinstance(self.default_fts_field_operator, Unset):
            default_fts_field_operator = self.default_fts_field_operator.value

        default_fts_operator: Union[Unset, str] = UNSET
        if not isinstance(self.default_fts_operator, Unset):
            default_fts_operator = self.default_fts_operator.value

        default_field_name = self.default_field_name

        namespace = self.namespace

        text_attributes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.text_attributes, Unset):
            text_attributes = self.text_attributes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_fts_field_operator is not UNSET:
            field_dict["defaultFTSFieldOperator"] = default_fts_field_operator
        if default_fts_operator is not UNSET:
            field_dict["defaultFTSOperator"] = default_fts_operator
        if default_field_name is not UNSET:
            field_dict["defaultFieldName"] = default_field_name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if text_attributes is not UNSET:
            field_dict["textAttributes"] = text_attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _default_fts_field_operator = d.pop("defaultFTSFieldOperator", UNSET)
        default_fts_field_operator: Union[Unset, RequestDefaultsDefaultFTSFieldOperator]
        if isinstance(_default_fts_field_operator, Unset):
            default_fts_field_operator = UNSET
        else:
            default_fts_field_operator = RequestDefaultsDefaultFTSFieldOperator(_default_fts_field_operator)

        _default_fts_operator = d.pop("defaultFTSOperator", UNSET)
        default_fts_operator: Union[Unset, RequestDefaultsDefaultFTSOperator]
        if isinstance(_default_fts_operator, Unset):
            default_fts_operator = UNSET
        else:
            default_fts_operator = RequestDefaultsDefaultFTSOperator(_default_fts_operator)

        default_field_name = d.pop("defaultFieldName", UNSET)

        namespace = d.pop("namespace", UNSET)

        text_attributes = cast(list[str], d.pop("textAttributes", UNSET))

        request_defaults = cls(
            default_fts_field_operator=default_fts_field_operator,
            default_fts_operator=default_fts_operator,
            default_field_name=default_field_name,
            namespace=namespace,
            text_attributes=text_attributes,
        )

        request_defaults.additional_properties = d
        return request_defaults

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
