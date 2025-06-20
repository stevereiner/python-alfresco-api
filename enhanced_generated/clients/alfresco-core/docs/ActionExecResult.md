# ActionExecResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the action pending execution | 

## Example

```python
from alfresco_core_client.models.action_exec_result import ActionExecResult

# TODO update the JSON string below
json = "{}"
# create an instance of ActionExecResult from a JSON string
action_exec_result_instance = ActionExecResult.from_json(json)
# print the JSON string representation of the object
print(ActionExecResult.to_json())

# convert the object into a dict
action_exec_result_dict = action_exec_result_instance.to_dict()
# create an instance of ActionExecResult from a dict
action_exec_result_from_dict = ActionExecResult.from_dict(action_exec_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


