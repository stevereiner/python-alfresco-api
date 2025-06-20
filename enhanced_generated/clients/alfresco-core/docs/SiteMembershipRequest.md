# SiteMembershipRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**message** | **str** |  | [optional] 
**site** | [**Site**](Site.md) |  | 

## Example

```python
from alfresco_core_client.models.site_membership_request import SiteMembershipRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequest from a JSON string
site_membership_request_instance = SiteMembershipRequest.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipRequest.to_json())

# convert the object into a dict
site_membership_request_dict = site_membership_request_instance.to_dict()
# create an instance of SiteMembershipRequest from a dict
site_membership_request_from_dict = SiteMembershipRequest.from_dict(site_membership_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


