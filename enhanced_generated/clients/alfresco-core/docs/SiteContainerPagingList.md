# SiteContainerPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SiteContainerEntry]**](SiteContainerEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.site_container_paging_list import SiteContainerPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SiteContainerPagingList from a JSON string
site_container_paging_list_instance = SiteContainerPagingList.from_json(json)
# print the JSON string representation of the object
print(SiteContainerPagingList.to_json())

# convert the object into a dict
site_container_paging_list_dict = site_container_paging_list_instance.to_dict()
# create an instance of SiteContainerPagingList from a dict
site_container_paging_list_from_dict = SiteContainerPagingList.from_dict(site_container_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


