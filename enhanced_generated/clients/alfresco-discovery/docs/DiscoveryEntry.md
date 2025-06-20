# DiscoveryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**RepositoryEntry**](RepositoryEntry.md) |  | 

## Example

```python
from alfresco_discovery_client.models.discovery_entry import DiscoveryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveryEntry from a JSON string
discovery_entry_instance = DiscoveryEntry.from_json(json)
# print the JSON string representation of the object
print(DiscoveryEntry.to_json())

# convert the object into a dict
discovery_entry_dict = discovery_entry_instance.to_dict()
# create an instance of DiscoveryEntry from a dict
discovery_entry_from_dict = DiscoveryEntry.from_dict(discovery_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


