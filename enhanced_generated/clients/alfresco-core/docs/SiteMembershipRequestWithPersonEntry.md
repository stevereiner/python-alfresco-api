# SiteMembershipRequestWithPersonEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**SiteMembershipRequestWithPerson**](SiteMembershipRequestWithPerson.md) |  | 

## Example

```python
from alfresco_core_client.models.site_membership_request_with_person_entry import SiteMembershipRequestWithPersonEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequestWithPersonEntry from a JSON string
site_membership_request_with_person_entry_instance = SiteMembershipRequestWithPersonEntry.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipRequestWithPersonEntry.to_json())

# convert the object into a dict
site_membership_request_with_person_entry_dict = site_membership_request_with_person_entry_instance.to_dict()
# create an instance of SiteMembershipRequestWithPersonEntry from a dict
site_membership_request_with_person_entry_from_dict = SiteMembershipRequestWithPersonEntry.from_dict(site_membership_request_with_person_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


