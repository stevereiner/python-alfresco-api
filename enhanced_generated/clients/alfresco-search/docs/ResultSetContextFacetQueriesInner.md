# ResultSetContextFacetQueriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**filter_query** | **str** | The filter query you can use to apply this facet | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from alfresco_search_client.models.result_set_context_facet_queries_inner import ResultSetContextFacetQueriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSetContextFacetQueriesInner from a JSON string
result_set_context_facet_queries_inner_instance = ResultSetContextFacetQueriesInner.from_json(json)
# print the JSON string representation of the object
print(ResultSetContextFacetQueriesInner.to_json())

# convert the object into a dict
result_set_context_facet_queries_inner_dict = result_set_context_facet_queries_inner_instance.to_dict()
# create an instance of ResultSetContextFacetQueriesInner from a dict
result_set_context_facet_queries_inner_from_dict = ResultSetContextFacetQueriesInner.from_dict(result_set_context_facet_queries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


