# RepositoryEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | [**RepositoryInfo**](RepositoryInfo.md) |  | 

## Example

```python
from alfresco_discovery_client.models.repository_entry import RepositoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryEntry from a JSON string
repository_entry_instance = RepositoryEntry.from_json(json)
# print the JSON string representation of the object
print(RepositoryEntry.to_json())

# convert the object into a dict
repository_entry_dict = repository_entry_instance.to_dict()
# create an instance of RepositoryEntry from a dict
repository_entry_from_dict = RepositoryEntry.from_dict(repository_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


