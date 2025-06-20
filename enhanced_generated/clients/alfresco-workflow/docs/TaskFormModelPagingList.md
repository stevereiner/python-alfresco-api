# TaskFormModelPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[TaskFormModelEntry]**](TaskFormModelEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.task_form_model_paging_list import TaskFormModelPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFormModelPagingList from a JSON string
task_form_model_paging_list_instance = TaskFormModelPagingList.from_json(json)
# print the JSON string representation of the object
print(TaskFormModelPagingList.to_json())

# convert the object into a dict
task_form_model_paging_list_dict = task_form_model_paging_list_instance.to_dict()
# create an instance of TaskFormModelPagingList from a dict
task_form_model_paging_list_from_dict = TaskFormModelPagingList.from_dict(task_form_model_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


