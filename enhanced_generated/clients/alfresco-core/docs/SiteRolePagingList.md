# SiteRolePagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SiteRoleEntry]**](SiteRoleEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.site_role_paging_list import SiteRolePagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SiteRolePagingList from a JSON string
site_role_paging_list_instance = SiteRolePagingList.from_json(json)
# print the JSON string representation of the object
print(SiteRolePagingList.to_json())

# convert the object into a dict
site_role_paging_list_dict = site_role_paging_list_instance.to_dict()
# create an instance of SiteRolePagingList from a dict
site_role_paging_list_from_dict = SiteRolePagingList.from_dict(site_role_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


