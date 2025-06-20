# RequestFacetField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_filters** | **list[str]** | Filter Queries with tags listed here will not be included in facet counts. This is used for multi-select facetting.  | [optional] 
**facet_enum_cache_min_df** | **int** |  | [optional] 
**field** | **str** | The facet field | [optional] 
**label** | **str** | A label to include in place of the facet field | [optional] 
**limit** | **int** |  | [optional] 
**method** | **str** |  | [optional] 
**mincount** | **int** | The minimum count required for a facet field to be included in the response. | [optional] 
**missing** | **bool** | When true, count results that match the query but which have no facet value for the field (in addition to the Term-based constraints). | [optional] [default to False]
**offset** | **int** |  | [optional] 
**prefix** | **str** | Restricts the possible constraints to only indexed values with a specified prefix. | [optional] 
**sort** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

