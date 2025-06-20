# SiteContainerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**SiteContainer**](SiteContainer.md) |  | 

## Example

```python
from alfresco_core_client.models.site_container_entry import SiteContainerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SiteContainerEntry from a JSON string
site_container_entry_instance = SiteContainerEntry.from_json(json)
# print the JSON string representation of the object
print(SiteContainerEntry.to_json())

# convert the object into a dict
site_container_entry_dict = site_container_entry_instance.to_dict()
# create an instance of SiteContainerEntry from a dict
site_container_entry_from_dict = SiteContainerEntry.from_dict(site_container_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


