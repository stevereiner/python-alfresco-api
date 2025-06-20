# ActionParameterDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_label** | **str** |  | [optional] 
**mandatory** | **bool** |  | [optional] 
**multi_valued** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.action_parameter_definition import ActionParameterDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of ActionParameterDefinition from a JSON string
action_parameter_definition_instance = ActionParameterDefinition.from_json(json)
# print the JSON string representation of the object
print(ActionParameterDefinition.to_json())

# convert the object into a dict
action_parameter_definition_dict = action_parameter_definition_instance.to_dict()
# create an instance of ActionParameterDefinition from a dict
action_parameter_definition_from_dict = ActionParameterDefinition.from_dict(action_parameter_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


