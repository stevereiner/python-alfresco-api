# ActionDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicable_types** | **List[str]** | QNames of the types this action applies to | 
**description** | **str** | describes the action definition, e.g. \&quot;This will move the matched item to another space.\&quot; | [optional] 
**id** | **str** | Identifier of the action definition — used for example when executing an action | 
**name** | **str** | name of the action definition, e.g. \&quot;move\&quot; | [optional] 
**parameter_definitions** | [**List[ActionParameterDefinition]**](ActionParameterDefinition.md) |  | [optional] 
**title** | **str** | title of the action definition, e.g. \&quot;Move\&quot; | [optional] 
**track_status** | **bool** | whether the basic action definition supports action tracking or not | 

## Example

```python
from alfresco_core_client.models.action_definition import ActionDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDefinition from a JSON string
action_definition_instance = ActionDefinition.from_json(json)
# print the JSON string representation of the object
print(ActionDefinition.to_json())

# convert the object into a dict
action_definition_dict = action_definition_instance.to_dict()
# create an instance of ActionDefinition from a dict
action_definition_from_dict = ActionDefinition.from_dict(action_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


