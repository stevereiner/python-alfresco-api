# SiteMembershipApprovalBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.site_membership_approval_body import SiteMembershipApprovalBody

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipApprovalBody from a JSON string
site_membership_approval_body_instance = SiteMembershipApprovalBody.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipApprovalBody.to_json())

# convert the object into a dict
site_membership_approval_body_dict = site_membership_approval_body_instance.to_dict()
# create an instance of SiteMembershipApprovalBody from a dict
site_membership_approval_body_from_dict = SiteMembershipApprovalBody.from_dict(site_membership_approval_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


