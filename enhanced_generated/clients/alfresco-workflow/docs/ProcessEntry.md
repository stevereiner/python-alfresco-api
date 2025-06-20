# ProcessEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Process**](Process.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.process_entry import ProcessEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessEntry from a JSON string
process_entry_instance = ProcessEntry.from_json(json)
# print the JSON string representation of the object
print(ProcessEntry.to_json())

# convert the object into a dict
process_entry_dict = process_entry_instance.to_dict()
# create an instance of ProcessEntry from a dict
process_entry_from_dict = ProcessEntry.from_dict(process_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


