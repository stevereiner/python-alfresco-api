# SiteGroupPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**SiteGroupPagingList**](SiteGroupPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.site_group_paging import SiteGroupPaging

# TODO update the JSON string below
json = "{}"
# create an instance of SiteGroupPaging from a JSON string
site_group_paging_instance = SiteGroupPaging.from_json(json)
# print the JSON string representation of the object
print(SiteGroupPaging.to_json())

# convert the object into a dict
site_group_paging_dict = site_group_paging_instance.to_dict()
# create an instance of SiteGroupPaging from a dict
site_group_paging_from_dict = SiteGroupPaging.from_dict(site_group_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


