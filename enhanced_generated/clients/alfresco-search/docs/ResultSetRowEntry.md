# ResultSetRowEntry

A row in the result set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**ResultNode**](ResultNode.md) |  | 

## Example

```python
from alfresco_search_client.models.result_set_row_entry import ResultSetRowEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSetRowEntry from a JSON string
result_set_row_entry_instance = ResultSetRowEntry.from_json(json)
# print the JSON string representation of the object
print(ResultSetRowEntry.to_json())

# convert the object into a dict
result_set_row_entry_dict = result_set_row_entry_instance.to_dict()
# create an instance of ResultSetRowEntry from a dict
result_set_row_entry_from_dict = ResultSetRowEntry.from_dict(result_set_row_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


