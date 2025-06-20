# SiteMembershipBodyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**role** | **str** |  | 

## Example

```python
from alfresco_core_client.models.site_membership_body_create import SiteMembershipBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipBodyCreate from a JSON string
site_membership_body_create_instance = SiteMembershipBodyCreate.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipBodyCreate.to_json())

# convert the object into a dict
site_membership_body_create_dict = site_membership_body_create_instance.to_dict()
# create an instance of SiteMembershipBodyCreate from a dict
site_membership_body_create_from_dict = SiteMembershipBodyCreate.from_dict(site_membership_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


