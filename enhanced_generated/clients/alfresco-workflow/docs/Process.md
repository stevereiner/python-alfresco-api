# Process

A process describes a running instance of a process definition.  When a new deployment includes a process definition that is already deployed with the same key, the newly deployed process definition will be considered a new version of the same process definition. By default processes will keep running in the process definition they are started in. But new processes can be started in the latest version of a process definition by using the processDefinitionKey parameter.  In non-network deployments, administrators can see all processes and perform all operations on tasks. In network deployments, network administrators can see processes in their network and perform all operations on tasks in their network. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_key** | **str** | The business key | [optional] 
**delete_reason** | **str** | The reason this process was canceled | [optional] 
**duration_in_ms** | **int** | The duration of this process | [optional] 
**end_activity_definition_id** | **str** | The id of the last activity in the process | [optional] 
**ended_at** | **datetime** | The date time this process started | [optional] 
**id** | **str** | The unique id of this process | 
**process_definition_id** | **str** | The unique identity of the owning process definition | [optional] 
**start_activity_definition_id** | **str** | The id of the first activity in the process | [optional] 
**start_user_id** | **str** | The id of the user who started the process | [optional] 
**started_at** | **datetime** | The date time this process started | [optional] 

## Example

```python
from alfresco_workflow_client.models.process import Process

# TODO update the JSON string below
json = "{}"
# create an instance of Process from a JSON string
process_instance = Process.from_json(json)
# print the JSON string representation of the object
print(Process.to_json())

# convert the object into a dict
process_dict = process_instance.to_dict()
# create an instance of Process from a dict
process_from_dict = Process.from_dict(process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


