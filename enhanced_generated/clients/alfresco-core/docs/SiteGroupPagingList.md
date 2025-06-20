# SiteGroupPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SiteGroupEntry]**](SiteGroupEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.site_group_paging_list import SiteGroupPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SiteGroupPagingList from a JSON string
site_group_paging_list_instance = SiteGroupPagingList.from_json(json)
# print the JSON string representation of the object
print(SiteGroupPagingList.to_json())

# convert the object into a dict
site_group_paging_list_dict = site_group_paging_list_instance.to_dict()
# create an instance of SiteGroupPagingList from a dict
site_group_paging_list_from_dict = SiteGroupPagingList.from_dict(site_group_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


