# SiteMembershipRequestWithPersonPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SiteMembershipRequestWithPersonEntry]**](SiteMembershipRequestWithPersonEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.site_membership_request_with_person_paging_list import SiteMembershipRequestWithPersonPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequestWithPersonPagingList from a JSON string
site_membership_request_with_person_paging_list_instance = SiteMembershipRequestWithPersonPagingList.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipRequestWithPersonPagingList.to_json())

# convert the object into a dict
site_membership_request_with_person_paging_list_dict = site_membership_request_with_person_paging_list_instance.to_dict()
# create an instance of SiteMembershipRequestWithPersonPagingList from a dict
site_membership_request_with_person_paging_list_from_dict = SiteMembershipRequestWithPersonPagingList.from_dict(site_membership_request_with_person_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


