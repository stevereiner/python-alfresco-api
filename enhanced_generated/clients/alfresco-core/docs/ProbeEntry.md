# ProbeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**ProbeEntryEntry**](ProbeEntryEntry.md) |  | 

## Example

```python
from alfresco_core_client.models.probe_entry import ProbeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeEntry from a JSON string
probe_entry_instance = ProbeEntry.from_json(json)
# print the JSON string representation of the object
print(ProbeEntry.to_json())

# convert the object into a dict
probe_entry_dict = probe_entry_instance.to_dict()
# create an instance of ProbeEntry from a dict
probe_entry_from_dict = ProbeEntry.from_dict(probe_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


