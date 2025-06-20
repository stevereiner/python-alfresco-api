# SiteMemberPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**SiteMemberPagingList**](SiteMemberPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.site_member_paging import SiteMemberPaging

# TODO update the JSON string below
json = "{}"
# create an instance of SiteMemberPaging from a JSON string
site_member_paging_instance = SiteMemberPaging.from_json(json)
# print the JSON string representation of the object
print(SiteMemberPaging.to_json())

# convert the object into a dict
site_member_paging_dict = site_member_paging_instance.to_dict()
# create an instance of SiteMemberPaging from a dict
site_member_paging_from_dict = SiteMemberPaging.from_dict(site_member_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


