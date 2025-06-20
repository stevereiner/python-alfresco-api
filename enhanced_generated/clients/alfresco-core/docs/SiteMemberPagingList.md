# SiteMemberPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SiteMemberEntry]**](SiteMemberEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.site_member_paging_list import SiteMemberPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMemberPagingList from a JSON string
site_member_paging_list_instance = SiteMemberPagingList.from_json(json)
# print the JSON string representation of the object
print(SiteMemberPagingList.to_json())

# convert the object into a dict
site_member_paging_list_dict = site_member_paging_list_instance.to_dict()
# create an instance of SiteMemberPagingList from a dict
site_member_paging_list_from_dict = SiteMemberPagingList.from_dict(site_member_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


