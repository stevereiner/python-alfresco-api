from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.request_include_item import RequestIncludeItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.request_defaults import RequestDefaults
    from ..models.request_facet_fields import RequestFacetFields
    from ..models.request_facet_intervals import RequestFacetIntervals
    from ..models.request_facet_queries_item import RequestFacetQueriesItem
    from ..models.request_filter_queries_item import RequestFilterQueriesItem
    from ..models.request_highlight import RequestHighlight
    from ..models.request_limits import RequestLimits
    from ..models.request_localization import RequestLocalization
    from ..models.request_pagination import RequestPagination
    from ..models.request_pivot import RequestPivot
    from ..models.request_query import RequestQuery
    from ..models.request_range import RequestRange
    from ..models.request_scope import RequestScope
    from ..models.request_sort_definition_item import RequestSortDefinitionItem
    from ..models.request_spellcheck import RequestSpellcheck
    from ..models.request_stats import RequestStats
    from ..models.request_templates_item import RequestTemplatesItem


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """
    Attributes:
        query (RequestQuery): Query.
        defaults (Union[Unset, RequestDefaults]): Common query defaults
        facet_fields (Union[Unset, RequestFacetFields]): Simple facet fields to include
            The Properties reflect the global properties related to field facts in SOLR.
            They are descripbed in detail by the SOLR documentation
        facet_intervals (Union[Unset, RequestFacetIntervals]): Facet Intervals
        facet_queries (Union[Unset, list['RequestFacetQueriesItem']]): Facet queries to include
        fields (Union[Unset, list[str]]): A list of field names.
            You can use this parameter to restrict the fields returned within a response if, for example, you want to save
            on overall bandwidth.
            The list applies to a returned individual entity or entries within a collection.
            If the **include** parameter is used aswell then the fields specified in the **include** parameter are returned
            in addition to those specified in the **fields** parameter.
        filter_queries (Union[Unset, list['RequestFilterQueriesItem']]): Filter Queries. Constraints that apply to the
            results set but do not affect the score of each entry.
        highlight (Union[Unset, RequestHighlight]): Request that highlight fragments to be added to result set rows
            The properties reflect SOLR highlighting parameters.
        include (Union[Unset, list[RequestIncludeItem]]): Returns additional information about the node. The following
            optional fields can be requested:
             * properties
             * aspectNames
             * path
             * isLink
             * allowableOperations
             * association
        include_request (Union[Unset, bool]): When true, include the original request in the response Default: False.
        limits (Union[Unset, RequestLimits]): Limit the time and resources used for query execution
        localization (Union[Unset, RequestLocalization]): Localization settings
        paging (Union[Unset, RequestPagination]):
        pivots (Union[Unset, list['RequestPivot']]):
        ranges (Union[Unset, list['RequestRange']]):
        scope (Union[Unset, RequestScope]): Scope
        sort (Union[Unset, list['RequestSortDefinitionItem']]): How to sort the rows? An array of sort specifications.
            The array order defines the ordering precedence.
        spellcheck (Union[Unset, RequestSpellcheck]): Request that spellcheck fragments to be added to result set rows
            The properties reflect SOLR spellcheck parameters.
        stats (Union[Unset, list['RequestStats']]):
        templates (Union[Unset, list['RequestTemplatesItem']]): Templates usewd for query expansion.
            A template called "WOOF" defined as "%(cm:name cm:title)" allows
            WOOF:example
            to generate
            cm:name:example cm:name:example
    """

    query: "RequestQuery"
    defaults: Union[Unset, "RequestDefaults"] = UNSET
    facet_fields: Union[Unset, "RequestFacetFields"] = UNSET
    facet_intervals: Union[Unset, "RequestFacetIntervals"] = UNSET
    facet_queries: Union[Unset, list["RequestFacetQueriesItem"]] = UNSET
    fields: Union[Unset, list[str]] = UNSET
    filter_queries: Union[Unset, list["RequestFilterQueriesItem"]] = UNSET
    highlight: Union[Unset, "RequestHighlight"] = UNSET
    include: Union[Unset, list[RequestIncludeItem]] = UNSET
    include_request: Union[Unset, bool] = False
    limits: Union[Unset, "RequestLimits"] = UNSET
    localization: Union[Unset, "RequestLocalization"] = UNSET
    paging: Union[Unset, "RequestPagination"] = UNSET
    pivots: Union[Unset, list["RequestPivot"]] = UNSET
    ranges: Union[Unset, list["RequestRange"]] = UNSET
    scope: Union[Unset, "RequestScope"] = UNSET
    sort: Union[Unset, list["RequestSortDefinitionItem"]] = UNSET
    spellcheck: Union[Unset, "RequestSpellcheck"] = UNSET
    stats: Union[Unset, list["RequestStats"]] = UNSET
    templates: Union[Unset, list["RequestTemplatesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query.to_dict()

        defaults: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()

        facet_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.facet_fields, Unset):
            facet_fields = self.facet_fields.to_dict()

        facet_intervals: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.facet_intervals, Unset):
            facet_intervals = self.facet_intervals.to_dict()

        facet_queries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.facet_queries, Unset):
            facet_queries = []
            for componentsschemas_request_facet_queries_item_data in self.facet_queries:
                componentsschemas_request_facet_queries_item = (
                    componentsschemas_request_facet_queries_item_data.to_dict()
                )
                facet_queries.append(componentsschemas_request_facet_queries_item)

        fields: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields

        filter_queries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.filter_queries, Unset):
            filter_queries = []
            for componentsschemas_request_filter_queries_item_data in self.filter_queries:
                componentsschemas_request_filter_queries_item = (
                    componentsschemas_request_filter_queries_item_data.to_dict()
                )
                filter_queries.append(componentsschemas_request_filter_queries_item)

        highlight: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.highlight, Unset):
            highlight = self.highlight.to_dict()

        include: Union[Unset, list[str]] = UNSET
        if not isinstance(self.include, Unset):
            include = []
            for componentsschemas_request_include_item_data in self.include:
                componentsschemas_request_include_item = componentsschemas_request_include_item_data.value
                include.append(componentsschemas_request_include_item)

        include_request = self.include_request

        limits: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        localization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.localization, Unset):
            localization = self.localization.to_dict()

        paging: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.paging, Unset):
            paging = self.paging.to_dict()

        pivots: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pivots, Unset):
            pivots = []
            for pivots_item_data in self.pivots:
                pivots_item = pivots_item_data.to_dict()
                pivots.append(pivots_item)

        ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        scope: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        sort: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = []
            for componentsschemas_request_sort_definition_item_data in self.sort:
                componentsschemas_request_sort_definition_item = (
                    componentsschemas_request_sort_definition_item_data.to_dict()
                )
                sort.append(componentsschemas_request_sort_definition_item)

        spellcheck: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spellcheck, Unset):
            spellcheck = self.spellcheck.to_dict()

        stats: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.templates, Unset):
            templates = []
            for componentsschemas_request_templates_item_data in self.templates:
                componentsschemas_request_templates_item = componentsschemas_request_templates_item_data.to_dict()
                templates.append(componentsschemas_request_templates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if defaults is not UNSET:
            field_dict["defaults"] = defaults
        if facet_fields is not UNSET:
            field_dict["facetFields"] = facet_fields
        if facet_intervals is not UNSET:
            field_dict["facetIntervals"] = facet_intervals
        if facet_queries is not UNSET:
            field_dict["facetQueries"] = facet_queries
        if fields is not UNSET:
            field_dict["fields"] = fields
        if filter_queries is not UNSET:
            field_dict["filterQueries"] = filter_queries
        if highlight is not UNSET:
            field_dict["highlight"] = highlight
        if include is not UNSET:
            field_dict["include"] = include
        if include_request is not UNSET:
            field_dict["includeRequest"] = include_request
        if limits is not UNSET:
            field_dict["limits"] = limits
        if localization is not UNSET:
            field_dict["localization"] = localization
        if paging is not UNSET:
            field_dict["paging"] = paging
        if pivots is not UNSET:
            field_dict["pivots"] = pivots
        if ranges is not UNSET:
            field_dict["ranges"] = ranges
        if scope is not UNSET:
            field_dict["scope"] = scope
        if sort is not UNSET:
            field_dict["sort"] = sort
        if spellcheck is not UNSET:
            field_dict["spellcheck"] = spellcheck
        if stats is not UNSET:
            field_dict["stats"] = stats
        if templates is not UNSET:
            field_dict["templates"] = templates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.request_defaults import RequestDefaults
        from ..models.request_facet_fields import RequestFacetFields
        from ..models.request_facet_intervals import RequestFacetIntervals
        from ..models.request_facet_queries_item import RequestFacetQueriesItem
        from ..models.request_filter_queries_item import RequestFilterQueriesItem
        from ..models.request_highlight import RequestHighlight
        from ..models.request_limits import RequestLimits
        from ..models.request_localization import RequestLocalization
        from ..models.request_pagination import RequestPagination
        from ..models.request_pivot import RequestPivot
        from ..models.request_query import RequestQuery
        from ..models.request_range import RequestRange
        from ..models.request_scope import RequestScope
        from ..models.request_sort_definition_item import RequestSortDefinitionItem
        from ..models.request_spellcheck import RequestSpellcheck
        from ..models.request_stats import RequestStats
        from ..models.request_templates_item import RequestTemplatesItem

        d = dict(src_dict)
        query = RequestQuery.from_dict(d.pop("query"))

        _defaults = d.pop("defaults", UNSET)
        defaults: Union[Unset, RequestDefaults]
        if isinstance(_defaults, Unset):
            defaults = UNSET
        else:
            defaults = RequestDefaults.from_dict(_defaults)

        _facet_fields = d.pop("facetFields", UNSET)
        facet_fields: Union[Unset, RequestFacetFields]
        if isinstance(_facet_fields, Unset):
            facet_fields = UNSET
        else:
            facet_fields = RequestFacetFields.from_dict(_facet_fields)

        _facet_intervals = d.pop("facetIntervals", UNSET)
        facet_intervals: Union[Unset, RequestFacetIntervals]
        if isinstance(_facet_intervals, Unset):
            facet_intervals = UNSET
        else:
            facet_intervals = RequestFacetIntervals.from_dict(_facet_intervals)

        facet_queries = []
        _facet_queries = d.pop("facetQueries", UNSET)
        for componentsschemas_request_facet_queries_item_data in _facet_queries or []:
            componentsschemas_request_facet_queries_item = RequestFacetQueriesItem.from_dict(
                componentsschemas_request_facet_queries_item_data
            )

            facet_queries.append(componentsschemas_request_facet_queries_item)

        fields = cast(list[str], d.pop("fields", UNSET))

        filter_queries = []
        _filter_queries = d.pop("filterQueries", UNSET)
        for componentsschemas_request_filter_queries_item_data in _filter_queries or []:
            componentsschemas_request_filter_queries_item = RequestFilterQueriesItem.from_dict(
                componentsschemas_request_filter_queries_item_data
            )

            filter_queries.append(componentsschemas_request_filter_queries_item)

        _highlight = d.pop("highlight", UNSET)
        highlight: Union[Unset, RequestHighlight]
        if isinstance(_highlight, Unset):
            highlight = UNSET
        else:
            highlight = RequestHighlight.from_dict(_highlight)

        include = []
        _include = d.pop("include", UNSET)
        for componentsschemas_request_include_item_data in _include or []:
            componentsschemas_request_include_item = RequestIncludeItem(componentsschemas_request_include_item_data)

            include.append(componentsschemas_request_include_item)

        include_request = d.pop("includeRequest", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: Union[Unset, RequestLimits]
        if isinstance(_limits, Unset):
            limits = UNSET
        else:
            limits = RequestLimits.from_dict(_limits)

        _localization = d.pop("localization", UNSET)
        localization: Union[Unset, RequestLocalization]
        if isinstance(_localization, Unset):
            localization = UNSET
        else:
            localization = RequestLocalization.from_dict(_localization)

        _paging = d.pop("paging", UNSET)
        paging: Union[Unset, RequestPagination]
        if isinstance(_paging, Unset):
            paging = UNSET
        else:
            paging = RequestPagination.from_dict(_paging)

        pivots = []
        _pivots = d.pop("pivots", UNSET)
        for pivots_item_data in _pivots or []:
            pivots_item = RequestPivot.from_dict(pivots_item_data)

            pivots.append(pivots_item)

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = RequestRange.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, RequestScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = RequestScope.from_dict(_scope)

        sort = []
        _sort = d.pop("sort", UNSET)
        for componentsschemas_request_sort_definition_item_data in _sort or []:
            componentsschemas_request_sort_definition_item = RequestSortDefinitionItem.from_dict(
                componentsschemas_request_sort_definition_item_data
            )

            sort.append(componentsschemas_request_sort_definition_item)

        _spellcheck = d.pop("spellcheck", UNSET)
        spellcheck: Union[Unset, RequestSpellcheck]
        if isinstance(_spellcheck, Unset):
            spellcheck = UNSET
        else:
            spellcheck = RequestSpellcheck.from_dict(_spellcheck)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = RequestStats.from_dict(stats_item_data)

            stats.append(stats_item)

        templates = []
        _templates = d.pop("templates", UNSET)
        for componentsschemas_request_templates_item_data in _templates or []:
            componentsschemas_request_templates_item = RequestTemplatesItem.from_dict(
                componentsschemas_request_templates_item_data
            )

            templates.append(componentsschemas_request_templates_item)

        search_request = cls(
            query=query,
            defaults=defaults,
            facet_fields=facet_fields,
            facet_intervals=facet_intervals,
            facet_queries=facet_queries,
            fields=fields,
            filter_queries=filter_queries,
            highlight=highlight,
            include=include,
            include_request=include_request,
            limits=limits,
            localization=localization,
            paging=paging,
            pivots=pivots,
            ranges=ranges,
            scope=scope,
            sort=sort,
            spellcheck=spellcheck,
            stats=stats,
            templates=templates,
        )

        search_request.additional_properties = d
        return search_request

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
