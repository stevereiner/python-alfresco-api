# VariableEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Variable**](Variable.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.variable_entry import VariableEntry

# TODO update the JSON string below
json = "{}"
# create an instance of VariableEntry from a JSON string
variable_entry_instance = VariableEntry.from_json(json)
# print the JSON string representation of the object
print(VariableEntry.to_json())

# convert the object into a dict
variable_entry_dict = variable_entry_instance.to_dict()
# create an instance of VariableEntry from a dict
variable_entry_from_dict = VariableEntry.from_dict(variable_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


