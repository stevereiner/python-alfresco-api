# ActionBodyExec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_definition_id** | **str** |  | 
**params** | **object** |  | [optional] 
**target_id** | **str** | The entity upon which to execute the action, typically a node ID or similar. | [optional] 

## Example

```python
from alfresco_core_client.models.action_body_exec import ActionBodyExec

# TODO update the JSON string below
json = "{}"
# create an instance of ActionBodyExec from a JSON string
action_body_exec_instance = ActionBodyExec.from_json(json)
# print the JSON string representation of the object
print(ActionBodyExec.to_json())

# convert the object into a dict
action_body_exec_dict = action_body_exec_instance.to_dict()
# create an instance of ActionBodyExec from a dict
action_body_exec_from_dict = ActionBodyExec.from_dict(action_body_exec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


