# Task

A task describes one task for a human user. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_definition_id** | **str** | The activity id of this task | [optional] 
**assignee** | **str** | The id of the user who is currently assigned this task | [optional] 
**description** | **str** | The description of this task | [optional] 
**due_at** | **datetime** | The date time this task is due | [optional] 
**duration_in_ms** | **int** | The duration of this task | [optional] 
**ended_at** | **datetime** | The date time this task started | [optional] 
**form_resource_key** | **str** | The key of the form for this task | [optional] 
**id** | **str** | The unique id of this task | 
**name** | **str** | The text name of this task | [optional] 
**owner** | **str** | The id of the user who owns this task | [optional] 
**priority** | **int** | The numeric priority of this task | [optional] 
**process_definition_id** | **str** | The unique identity of the owning process definition | [optional] 
**process_id** | **str** | The containing process&#39;s unique id | [optional] 
**started_at** | **datetime** | The date time this task started | [optional] 
**state** | **str** | The state of this task | [optional] 
**variables** | [**List[Variable]**](Variable.md) | An array of variables for this task | [optional] 

## Example

```python
from alfresco_workflow_client.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


