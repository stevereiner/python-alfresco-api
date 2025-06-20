# SharedLinkEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**SharedLink**](SharedLink.md) |  | 

## Example

```python
from alfresco_core_client.models.shared_link_entry import SharedLinkEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLinkEntry from a JSON string
shared_link_entry_instance = SharedLinkEntry.from_json(json)
# print the JSON string representation of the object
print(SharedLinkEntry.to_json())

# convert the object into a dict
shared_link_entry_dict = shared_link_entry_instance.to_dict()
# create an instance of SharedLinkEntry from a dict
shared_link_entry_from_dict = SharedLinkEntry.from_dict(shared_link_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


