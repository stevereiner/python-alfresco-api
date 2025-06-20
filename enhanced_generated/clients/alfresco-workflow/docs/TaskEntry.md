# TaskEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Task**](Task.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.task_entry import TaskEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TaskEntry from a JSON string
task_entry_instance = TaskEntry.from_json(json)
# print the JSON string representation of the object
print(TaskEntry.to_json())

# convert the object into a dict
task_entry_dict = task_entry_instance.to_dict()
# create an instance of TaskEntry from a dict
task_entry_from_dict = TaskEntry.from_dict(task_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


