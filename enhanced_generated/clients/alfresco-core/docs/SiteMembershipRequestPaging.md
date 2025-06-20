# SiteMembershipRequestPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**SiteMembershipRequestPagingList**](SiteMembershipRequestPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.site_membership_request_paging import SiteMembershipRequestPaging

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMembershipRequestPaging from a JSON string
site_membership_request_paging_instance = SiteMembershipRequestPaging.from_json(json)
# print the JSON string representation of the object
print(SiteMembershipRequestPaging.to_json())

# convert the object into a dict
site_membership_request_paging_dict = site_membership_request_paging_instance.to_dict()
# create an instance of SiteMembershipRequestPaging from a dict
site_membership_request_paging_from_dict = SiteMembershipRequestPaging.from_dict(site_membership_request_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


