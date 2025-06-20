# TaskFormModel

A task form model item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_values** | **List[str]** | An array of allowed values for this item | [optional] 
**data_type** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**qualified_name** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.task_form_model import TaskFormModel

# TODO update the JSON string below
json = "{}"
# create an instance of TaskFormModel from a JSON string
task_form_model_instance = TaskFormModel.from_json(json)
# print the JSON string representation of the object
print(TaskFormModel.to_json())

# convert the object into a dict
task_form_model_dict = task_form_model_instance.to_dict()
# create an instance of TaskFormModel from a dict
task_form_model_from_dict = TaskFormModel.from_dict(task_form_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


