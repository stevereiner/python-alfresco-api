# TaskPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**TaskPagingList**](TaskPagingList.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.task_paging import TaskPaging

# TODO update the JSON string below
json = "{}"
# create an instance of TaskPaging from a JSON string
task_paging_instance = TaskPaging.from_json(json)
# print the JSON string representation of the object
print(TaskPaging.to_json())

# convert the object into a dict
task_paging_dict = task_paging_instance.to_dict()
# create an instance of TaskPaging from a dict
task_paging_from_dict = TaskPaging.from_dict(task_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


