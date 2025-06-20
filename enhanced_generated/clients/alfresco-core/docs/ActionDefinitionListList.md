# ActionDefinitionListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ActionDefinition]**](ActionDefinition.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.action_definition_list_list import ActionDefinitionListList

# TODO update the JSON string below
json = "{}"
# create an instance of ActionDefinitionListList from a JSON string
action_definition_list_list_instance = ActionDefinitionListList.from_json(json)
# print the JSON string representation of the object
print(ActionDefinitionListList.to_json())

# convert the object into a dict
action_definition_list_list_dict = action_definition_list_list_instance.to_dict()
# create an instance of ActionDefinitionListList from a dict
action_definition_list_list_from_dict = ActionDefinitionListList.from_dict(action_definition_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


