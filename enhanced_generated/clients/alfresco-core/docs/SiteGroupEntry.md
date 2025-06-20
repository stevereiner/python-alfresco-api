# SiteGroupEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**SiteGroup**](SiteGroup.md) |  | 

## Example

```python
from alfresco_core_client.models.site_group_entry import SiteGroupEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SiteGroupEntry from a JSON string
site_group_entry_instance = SiteGroupEntry.from_json(json)
# print the JSON string representation of the object
print(SiteGroupEntry.to_json())

# convert the object into a dict
site_group_entry_dict = site_group_entry_instance.to_dict()
# create an instance of SiteGroupEntry from a dict
site_group_entry_from_dict = SiteGroupEntry.from_dict(site_group_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


