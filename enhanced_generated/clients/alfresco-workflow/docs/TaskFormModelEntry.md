# TaskFormModelEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**TaskFormModel**](TaskFormModel.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.task_form_model_entry import TaskFormModelEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFormModelEntry from a JSON string
task_form_model_entry_instance = TaskFormModelEntry.from_json(json)
# print the JSON string representation of the object
print(TaskFormModelEntry.to_json())

# convert the object into a dict
task_form_model_entry_dict = task_form_model_entry_instance.to_dict()
# create an instance of TaskFormModelEntry from a dict
task_form_model_entry_from_dict = TaskFormModelEntry.from_dict(task_form_model_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


