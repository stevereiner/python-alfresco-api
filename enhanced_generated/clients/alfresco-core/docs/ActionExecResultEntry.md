# ActionExecResultEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**ActionExecResult**](ActionExecResult.md) |  | 

## Example

```python
from alfresco_core_client.models.action_exec_result_entry import ActionExecResultEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ActionExecResultEntry from a JSON string
action_exec_result_entry_instance = ActionExecResultEntry.from_json(json)
# print the JSON string representation of the object
print(ActionExecResultEntry.to_json())

# convert the object into a dict
action_exec_result_entry_dict = action_exec_result_entry_instance.to_dict()
# create an instance of ActionExecResultEntry from a dict
action_exec_result_entry_from_dict = ActionExecResultEntry.from_dict(action_exec_result_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


