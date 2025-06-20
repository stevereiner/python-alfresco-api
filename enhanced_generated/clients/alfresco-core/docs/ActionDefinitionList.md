# ActionDefinitionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ActionDefinitionListList**](ActionDefinitionListList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.action_definition_list import ActionDefinitionList

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDefinitionList from a JSON string
action_definition_list_instance = ActionDefinitionList.from_json(json)
# print the JSON string representation of the object
print(ActionDefinitionList.to_json())

# convert the object into a dict
action_definition_list_dict = action_definition_list_instance.to_dict()
# create an instance of ActionDefinitionList from a dict
action_definition_list_from_dict = ActionDefinitionList.from_dict(action_definition_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


