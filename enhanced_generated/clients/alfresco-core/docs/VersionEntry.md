# VersionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Version**](Version.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.version_entry import VersionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of VersionEntry from a JSON string
version_entry_instance = VersionEntry.from_json(json)
# print the JSON string representation of the object
print(VersionEntry.to_json())

# convert the object into a dict
version_entry_dict = version_entry_instance.to_dict()
# create an instance of VersionEntry from a dict
version_entry_from_dict = VersionEntry.from_dict(version_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


