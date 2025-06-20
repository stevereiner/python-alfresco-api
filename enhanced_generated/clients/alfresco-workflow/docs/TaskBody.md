# TaskBody

Input body to update a specific task. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of this task | [optional] 
**due_at** | **datetime** | The date time this task is due | [optional] 
**name** | **str** | The text name of this task | [optional] 
**owner** | **str** | The id of the user who owns this task | [optional] 
**priority** | **int** | The numeric priority of this task | [optional] 
**state** | **str** | The state of this task | [optional] 
**variables** | [**List[Variable]**](Variable.md) | An array of variables for this task | [optional] 

## Example

```python
from alfresco_workflow_client.models.task_body import TaskBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaskBody from a JSON string
task_body_instance = TaskBody.from_json(json)
# print the JSON string representation of the object
print(TaskBody.to_json())

# convert the object into a dict
task_body_dict = task_body_instance.to_dict()
# create an instance of TaskBody from a dict
task_body_from_dict = TaskBody.from_dict(task_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


