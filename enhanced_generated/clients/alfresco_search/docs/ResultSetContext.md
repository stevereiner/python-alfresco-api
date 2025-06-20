# ResultSetContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consistency** | [**ResponseConsistency**](ResponseConsistency.md) |  | [optional] 
**facet_queries** | [**list[ResultSetContextFacetQueries]**](ResultSetContextFacetQueries.md) | The counts from facet queries | [optional] 
**facets** | [**list[GenericFacetResponse]**](GenericFacetResponse.md) | The faceted response | [optional] 
**facets_fields** | [**list[ResultBuckets]**](ResultBuckets.md) | The counts from field facets | [optional] 
**request** | [**SearchRequest**](SearchRequest.md) |  | [optional] 
**spellcheck** | [**list[ResultSetContextSpellcheck]**](ResultSetContextSpellcheck.md) | Suggested corrections  If zero results were found for the original query then a single entry of type \&quot;searchInsteadFor\&quot; will be returned. If alternatives were found that return more results than the original query they are returned as \&quot;didYouMean\&quot; options. The highest quality suggestion is first.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

