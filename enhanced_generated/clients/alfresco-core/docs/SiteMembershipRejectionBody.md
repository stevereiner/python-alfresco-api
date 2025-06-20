# SiteMembershipRejectionBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.site_membership_rejection_body import SiteMembershipRejectionBody

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRejectionBody from a JSON string
site_membership_rejection_body_instance = SiteMembershipRejectionBody.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipRejectionBody.to_json())

# convert the object into a dict
site_membership_rejection_body_dict = site_membership_rejection_body_instance.to_dict()
# create an instance of SiteMembershipRejectionBody from a dict
site_membership_rejection_body_from_dict = SiteMembershipRejectionBody.from_dict(site_membership_rejection_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


