# SiteRoleEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**SiteRole**](SiteRole.md) |  | 

## Example

```python
from alfresco_core_client.models.site_role_entry import SiteRoleEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SiteRoleEntry from a JSON string
site_role_entry_instance = SiteRoleEntry.from_json(json)
# print the JSON string representation of the object
print(SiteRoleEntry.to_json())

# convert the object into a dict
site_role_entry_dict = site_role_entry_instance.to_dict()
# create an instance of SiteRoleEntry from a dict
site_role_entry_from_dict = SiteRoleEntry.from_dict(site_role_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


