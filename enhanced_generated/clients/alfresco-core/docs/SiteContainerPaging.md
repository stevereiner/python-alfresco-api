# SiteContainerPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**SiteContainerPagingList**](SiteContainerPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.site_container_paging import SiteContainerPaging

# TODO update the JSON string below
json = "{}"
# create an instance of SiteContainerPaging from a JSON string
site_container_paging_instance = SiteContainerPaging.from_json(json)
# print the JSON string representation of the object
print(SiteContainerPaging.to_json())

# convert the object into a dict
site_container_paging_dict = site_container_paging_instance.to_dict()
# create an instance of SiteContainerPaging from a dict
site_container_paging_from_dict = SiteContainerPaging.from_dict(site_container_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


