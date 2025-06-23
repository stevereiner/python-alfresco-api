from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_facet_field import RequestFacetField


T = TypeVar("T", bound="RequestFacetFields")


@_attrs_define
class RequestFacetFields:
    """Simple facet fields to include
    The Properties reflect the global properties related to field facts in SOLR.
    They are descripbed in detail by the SOLR documentation

        Attributes:
            facets (Union[Unset, list['RequestFacetField']]): Define specifc fields on which to facet (adds SOLR facet.field
                and f.<field>.facet.* options)
    """

    facets: Union[Unset, list["RequestFacetField"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.facets, Unset):
            facets = []
            for facets_item_data in self.facets:
                facets_item = facets_item_data.to_dict()
                facets.append(facets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if facets is not UNSET:
            field_dict["facets"] = facets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_facet_field import RequestFacetField

        d = dict(src_dict)
        facets = []
        _facets = d.pop("facets", UNSET)
        for facets_item_data in _facets or []:
            facets_item = RequestFacetField.from_dict(facets_item_data)

            facets.append(facets_item)

        request_facet_fields = cls(
            facets=facets,
        )

        request_facet_fields.additional_properties = d
        return request_facet_fields

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
