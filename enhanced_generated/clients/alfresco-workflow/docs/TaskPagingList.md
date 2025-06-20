# TaskPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[TaskEntry]**](TaskEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.task_paging_list import TaskPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPagingList from a JSON string
task_paging_list_instance = TaskPagingList.from_json(json)
# print the JSON string representation of the object
print(TaskPagingList.to_json())

# convert the object into a dict
task_paging_list_dict = task_paging_list_instance.to_dict()
# create an instance of TaskPagingList from a dict
task_paging_list_from_dict = TaskPagingList.from_dict(task_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


