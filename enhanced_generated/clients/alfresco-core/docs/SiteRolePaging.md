# SiteRolePaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**SiteRolePagingList**](SiteRolePagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.site_role_paging import SiteRolePaging

# TODO update the JSON string below
json = "{}"
# create an instance of SiteRolePaging from a JSON string
site_role_paging_instance = SiteRolePaging.from_json(json)
# print the JSON string representation of the object
print(SiteRolePaging.to_json())

# convert the object into a dict
site_role_paging_dict = site_role_paging_instance.to_dict()
# create an instance of SiteRolePaging from a dict
site_role_paging_from_dict = SiteRolePaging.from_dict(site_role_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


