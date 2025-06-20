# ProcessBodyVariable

A set of process variables of differing types. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bpm_assignee** | **str** |  | [optional] 
**bpm_send_e_mail_notifications** | **bool** |  | [optional] 
**bpm_workflow_priority** | **int** |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.process_body_variable import ProcessBodyVariable

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessBodyVariable from a JSON string
process_body_variable_instance = ProcessBodyVariable.from_json(json)
# print the JSON string representation of the object
print(ProcessBodyVariable.to_json())

# convert the object into a dict
process_body_variable_dict = process_body_variable_instance.to_dict()
# create an instance of ProcessBodyVariable from a dict
process_body_variable_from_dict = ProcessBodyVariable.from_dict(process_body_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


