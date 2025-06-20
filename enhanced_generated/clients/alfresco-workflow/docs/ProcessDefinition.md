# ProcessDefinition

A process definition is a description of an execution flow in terms of activities. New processes are created and started for a process definition. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category to which this process definition belongs | [optional] 
**deployment_id** | **str** | The deployment of which this process definition is a part | [optional] 
**description** | **str** | The description of this process definition | [optional] 
**graphic_notation_defined** | **bool** |  | [optional] 
**id** | **str** | The unique id of this process definition | 
**key** | **str** | The key of this process definition | [optional] 
**name** | **str** | The name of this process definition | [optional] 
**start_form_resource_key** | **str** | The start form key | [optional] 
**title** | **str** | The title of this process definition | [optional] 

## Example

```python
from alfresco_workflow_client.models.process_definition import ProcessDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessDefinition from a JSON string
process_definition_instance = ProcessDefinition.from_json(json)
# print the JSON string representation of the object
print(ProcessDefinition.to_json())

# convert the object into a dict
process_definition_dict = process_definition_instance.to_dict()
# create an instance of ProcessDefinition from a dict
process_definition_from_dict = ProcessDefinition.from_dict(process_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


