# SiteMembershipBodyUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | 

## Example

```python
from alfresco_core_client.models.site_membership_body_update import SiteMembershipBodyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipBodyUpdate from a JSON string
site_membership_body_update_instance = SiteMembershipBodyUpdate.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipBodyUpdate.to_json())

# convert the object into a dict
site_membership_body_update_dict = site_membership_body_update_instance.to_dict()
# create an instance of SiteMembershipBodyUpdate from a dict
site_membership_body_update_from_dict = SiteMembershipBodyUpdate.from_dict(site_membership_body_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


