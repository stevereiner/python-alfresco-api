# SiteMembershipRequestEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**SiteMembershipRequest**](SiteMembershipRequest.md) |  | 

## Example

```python
from alfresco_core_client.models.site_membership_request_entry import SiteMembershipRequestEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequestEntry from a JSON string
site_membership_request_entry_instance = SiteMembershipRequestEntry.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipRequestEntry.to_json())

# convert the object into a dict
site_membership_request_entry_dict = site_membership_request_entry_instance.to_dict()
# create an instance of SiteMembershipRequestEntry from a dict
site_membership_request_entry_from_dict = SiteMembershipRequestEntry.from_dict(site_membership_request_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


