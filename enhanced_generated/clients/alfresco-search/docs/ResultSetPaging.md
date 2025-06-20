# ResultSetPaging

Query results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ResultSetPagingList**](ResultSetPagingList.md) |  | [optional] 

## Example

```python
from alfresco_search_client.models.result_set_paging import ResultSetPaging

# TODO update the JSON string below
json = "{}"
# create an instance of ResultSetPaging from a JSON string
result_set_paging_instance = ResultSetPaging.from_json(json)
# print the JSON string representation of the object
print(ResultSetPaging.to_json())

# convert the object into a dict
result_set_paging_dict = result_set_paging_instance.to_dict()
# create an instance of ResultSetPaging from a dict
result_set_paging_from_dict = ResultSetPaging.from_dict(result_set_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


