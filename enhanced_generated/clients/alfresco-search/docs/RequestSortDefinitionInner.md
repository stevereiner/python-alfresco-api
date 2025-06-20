# RequestSortDefinitionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ascending** | **bool** | The sort order. (The ordering of nulls is determined by the SOLR configuration) | [optional] [default to False]
**var_field** | **str** | The name of the field | [optional] 
**type** | **str** | How to order - using a field, when position of the document in the index, score/relevence. | [optional] [default to 'FIELD']

## Example

```python
from alfresco_search_client.models.request_sort_definition_inner import RequestSortDefinitionInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestSortDefinitionInner from a JSON string
request_sort_definition_inner_instance = RequestSortDefinitionInner.from_json(json)
# print the JSON string representation of the object
print(RequestSortDefinitionInner.to_json())

# convert the object into a dict
request_sort_definition_inner_dict = request_sort_definition_inner_instance.to_dict()
# create an instance of RequestSortDefinitionInner from a dict
request_sort_definition_inner_from_dict = RequestSortDefinitionInner.from_dict(request_sort_definition_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


