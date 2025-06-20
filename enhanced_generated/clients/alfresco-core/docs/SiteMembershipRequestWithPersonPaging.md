# SiteMembershipRequestWithPersonPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**SiteMembershipRequestWithPersonPagingList**](SiteMembershipRequestWithPersonPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.site_membership_request_with_person_paging import SiteMembershipRequestWithPersonPaging

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequestWithPersonPaging from a JSON string
site_membership_request_with_person_paging_instance = SiteMembershipRequestWithPersonPaging.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipRequestWithPersonPaging.to_json())

# convert the object into a dict
site_membership_request_with_person_paging_dict = site_membership_request_with_person_paging_instance.to_dict()
# create an instance of SiteMembershipRequestWithPersonPaging from a dict
site_membership_request_with_person_paging_from_dict = SiteMembershipRequestWithPersonPaging.from_dict(site_membership_request_with_person_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


