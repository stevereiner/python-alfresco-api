# VariableBody

An input process variable. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **int** |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.variable_body import VariableBody

# TODO update the JSON string below
json = "{}"
# create an instance of VariableBody from a JSON string
variable_body_instance = VariableBody.from_json(json)
# print the JSON string representation of the object
print(VariableBody.to_json())

# convert the object into a dict
variable_body_dict = variable_body_instance.to_dict()
# create an instance of VariableBody from a dict
variable_body_from_dict = VariableBody.from_dict(variable_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


