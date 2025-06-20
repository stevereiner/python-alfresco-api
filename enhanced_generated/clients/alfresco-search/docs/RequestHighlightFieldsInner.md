# RequestHighlightFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The name of the field to highlight. | [optional] 
**fragment_size** | **int** |  | [optional] 
**merge_contiguous** | **bool** |  | [optional] 
**postfix** | **str** |  | [optional] 
**prefix** | **str** |  | [optional] 
**snippet_count** | **int** |  | [optional] 

## Example

```python
from alfresco_search_client.models.request_highlight_fields_inner import RequestHighlightFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestHighlightFieldsInner from a JSON string
request_highlight_fields_inner_instance = RequestHighlightFieldsInner.from_json(json)
# print the JSON string representation of the object
print(RequestHighlightFieldsInner.to_json())

# convert the object into a dict
request_highlight_fields_inner_dict = request_highlight_fields_inner_instance.to_dict()
# create an instance of RequestHighlightFieldsInner from a dict
request_highlight_fields_inner_from_dict = RequestHighlightFieldsInner.from_dict(request_highlight_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


