from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.generic_facet_response import GenericFacetResponse
    from ..models.response_consistency import ResponseConsistency
    from ..models.result_buckets import ResultBuckets
    from ..models.result_set_context_facet_queries_item import ResultSetContextFacetQueriesItem
    from ..models.result_set_context_spellcheck_item import ResultSetContextSpellcheckItem
    from ..models.search_request import SearchRequest


T = TypeVar("T", bound="ResultSetContext")


@_attrs_define
class ResultSetContext:
    """Context that applies to the whole result set

    Attributes:
        consistency (Union[Unset, ResponseConsistency]): The consistency state of the index used to execute the query
        facet_queries (Union[Unset, list['ResultSetContextFacetQueriesItem']]): The counts from facet queries
        facets (Union[Unset, list['GenericFacetResponse']]): The faceted response
        facets_fields (Union[Unset, list['ResultBuckets']]): The counts from field facets
        request (Union[Unset, SearchRequest]):
        spellcheck (Union[Unset, list['ResultSetContextSpellcheckItem']]): Suggested corrections

            If zero results were found for the original query then a single entry of type "searchInsteadFor" will be
            returned.
            If alternatives were found that return more results than the original query they are returned as "didYouMean"
            options.
            The highest quality suggestion is first.
    """

    consistency: Union[Unset, "ResponseConsistency"] = UNSET
    facet_queries: Union[Unset, list["ResultSetContextFacetQueriesItem"]] = UNSET
    facets: Union[Unset, list["GenericFacetResponse"]] = UNSET
    facets_fields: Union[Unset, list["ResultBuckets"]] = UNSET
    request: Union[Unset, "SearchRequest"] = UNSET
    spellcheck: Union[Unset, list["ResultSetContextSpellcheckItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        consistency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.consistency, Unset):
            consistency = self.consistency.to_dict()

        facet_queries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.facet_queries, Unset):
            facet_queries = []
            for facet_queries_item_data in self.facet_queries:
                facet_queries_item = facet_queries_item_data.to_dict()
                facet_queries.append(facet_queries_item)

        facets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.facets, Unset):
            facets = []
            for facets_item_data in self.facets:
                facets_item = facets_item_data.to_dict()
                facets.append(facets_item)

        facets_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.facets_fields, Unset):
            facets_fields = []
            for facets_fields_item_data in self.facets_fields:
                facets_fields_item = facets_fields_item_data.to_dict()
                facets_fields.append(facets_fields_item)

        request: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.request, Unset):
            request = self.request.to_dict()

        spellcheck: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.spellcheck, Unset):
            spellcheck = []
            for spellcheck_item_data in self.spellcheck:
                spellcheck_item = spellcheck_item_data.to_dict()
                spellcheck.append(spellcheck_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if consistency is not UNSET:
            field_dict["consistency"] = consistency
        if facet_queries is not UNSET:
            field_dict["facetQueries"] = facet_queries
        if facets is not UNSET:
            field_dict["facets"] = facets
        if facets_fields is not UNSET:
            field_dict["facetsFields"] = facets_fields
        if request is not UNSET:
            field_dict["request"] = request
        if spellcheck is not UNSET:
            field_dict["spellcheck"] = spellcheck

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.generic_facet_response import GenericFacetResponse
        from ..models.response_consistency import ResponseConsistency
        from ..models.result_buckets import ResultBuckets
        from ..models.result_set_context_facet_queries_item import ResultSetContextFacetQueriesItem
        from ..models.result_set_context_spellcheck_item import ResultSetContextSpellcheckItem
        from ..models.search_request import SearchRequest

        d = dict(src_dict)
        _consistency = d.pop("consistency", UNSET)
        consistency: Union[Unset, ResponseConsistency]
        if isinstance(_consistency, Unset):
            consistency = UNSET
        else:
            consistency = ResponseConsistency.from_dict(_consistency)

        facet_queries = []
        _facet_queries = d.pop("facetQueries", UNSET)
        for facet_queries_item_data in _facet_queries or []:
            facet_queries_item = ResultSetContextFacetQueriesItem.from_dict(facet_queries_item_data)

            facet_queries.append(facet_queries_item)

        facets = []
        _facets = d.pop("facets", UNSET)
        for facets_item_data in _facets or []:
            facets_item = GenericFacetResponse.from_dict(facets_item_data)

            facets.append(facets_item)

        facets_fields = []
        _facets_fields = d.pop("facetsFields", UNSET)
        for facets_fields_item_data in _facets_fields or []:
            facets_fields_item = ResultBuckets.from_dict(facets_fields_item_data)

            facets_fields.append(facets_fields_item)

        _request = d.pop("request", UNSET)
        request: Union[Unset, SearchRequest]
        if isinstance(_request, Unset):
            request = UNSET
        else:
            request = SearchRequest.from_dict(_request)

        spellcheck = []
        _spellcheck = d.pop("spellcheck", UNSET)
        for spellcheck_item_data in _spellcheck or []:
            spellcheck_item = ResultSetContextSpellcheckItem.from_dict(spellcheck_item_data)

            spellcheck.append(spellcheck_item)

        result_set_context = cls(
            consistency=consistency,
            facet_queries=facet_queries,
            facets=facets,
            facets_fields=facets_fields,
            request=request,
            spellcheck=spellcheck,
        )

        result_set_context.additional_properties = d
        return result_set_context

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
