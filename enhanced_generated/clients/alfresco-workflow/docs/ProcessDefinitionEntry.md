# ProcessDefinitionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**ProcessDefinition**](ProcessDefinition.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.process_definition_entry import ProcessDefinitionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessDefinitionEntry from a JSON string
process_definition_entry_instance = ProcessDefinitionEntry.from_json(json)
# print the JSON string representation of the object
print(ProcessDefinitionEntry.to_json())

# convert the object into a dict
process_definition_entry_dict = process_definition_entry_instance.to_dict()
# create an instance of ProcessDefinitionEntry from a dict
process_definition_entry_from_dict = ProcessDefinitionEntry.from_dict(process_definition_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


