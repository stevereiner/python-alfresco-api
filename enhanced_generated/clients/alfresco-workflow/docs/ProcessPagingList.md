# ProcessPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ProcessEntry]**](ProcessEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.process_paging_list import ProcessPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessPagingList from a JSON string
process_paging_list_instance = ProcessPagingList.from_json(json)
# print the JSON string representation of the object
print(ProcessPagingList.to_json())

# convert the object into a dict
process_paging_list_dict = process_paging_list_instance.to_dict()
# create an instance of ProcessPagingList from a dict
process_paging_list_from_dict = ProcessPagingList.from_dict(process_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


