# ProcessBody

required to start a process. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_definition_key** | **str** |  | [optional] 
**variables** | [**ProcessBodyVariable**](ProcessBodyVariable.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.process_body import ProcessBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessBody from a JSON string
process_body_instance = ProcessBody.from_json(json)
# print the JSON string representation of the object
print(ProcessBody.to_json())

# convert the object into a dict
process_body_dict = process_body_instance.to_dict()
# create an instance of ProcessBody from a dict
process_body_from_dict = ProcessBody.from_dict(process_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


