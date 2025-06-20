# ActionDefinitionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**ActionDefinition**](ActionDefinition.md) |  | 

## Example

```python
from alfresco_core_client.models.action_definition_entry import ActionDefinitionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDefinitionEntry from a JSON string
action_definition_entry_instance = ActionDefinitionEntry.from_json(json)
# print the JSON string representation of the object
print(ActionDefinitionEntry.to_json())

# convert the object into a dict
action_definition_entry_dict = action_definition_entry_instance.to_dict()
# create an instance of ActionDefinitionEntry from a dict
action_definition_entry_from_dict = ActionDefinitionEntry.from_dict(action_definition_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


