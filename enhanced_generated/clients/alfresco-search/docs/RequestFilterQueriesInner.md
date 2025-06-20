# RequestFilterQueriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The filter query expression. For multi-select facets selected facets must be order together  | [optional] 
**tags** | **List[str]** | Tags used exclude the filters from facet evaluation for multi-select facet support | [optional] 

## Example

```python
from alfresco_search_client.models.request_filter_queries_inner import RequestFilterQueriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestFilterQueriesInner from a JSON string
request_filter_queries_inner_instance = RequestFilterQueriesInner.from_json(json)
# print the JSON string representation of the object
print(RequestFilterQueriesInner.to_json())

# convert the object into a dict
request_filter_queries_inner_dict = request_filter_queries_inner_instance.to_dict()
# create an instance of RequestFilterQueriesInner from a dict
request_filter_queries_inner_from_dict = RequestFilterQueriesInner.from_dict(request_filter_queries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


