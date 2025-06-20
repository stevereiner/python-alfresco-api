# SiteMemberEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**SiteMember**](SiteMember.md) |  | 

## Example

```python
from alfresco_core_client.models.site_member_entry import SiteMemberEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMemberEntry from a JSON string
site_member_entry_instance = SiteMemberEntry.from_json(json)
# print the JSON string representation of the object
print(SiteMemberEntry.to_json())

# convert the object into a dict
site_member_entry_dict = site_member_entry_instance.to_dict()
# create an instance of SiteMemberEntry from a dict
site_member_entry_from_dict = SiteMemberEntry.from_dict(site_member_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


