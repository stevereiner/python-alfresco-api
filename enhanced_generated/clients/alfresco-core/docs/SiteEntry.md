# SiteEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Site**](Site.md) |  | 

## Example

```python
from alfresco_core_client.models.site_entry import SiteEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SiteEntry from a JSON string
site_entry_instance = SiteEntry.from_json(json)
# print the JSON string representation of the object
print(SiteEntry.to_json())

# convert the object into a dict
site_entry_dict = site_entry_instance.to_dict()
# create an instance of SiteEntry from a dict
site_entry_from_dict = SiteEntry.from_dict(site_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


