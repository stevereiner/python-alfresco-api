# SitePaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**SitePagingList**](SitePagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.site_paging import SitePaging

# TODO update the JSON string below
json = "{}"
# create an instance of SitePaging from a JSON string
site_paging_instance = SitePaging.from_json(json)
# print the JSON string representation of the object
print(SitePaging.to_json())

# convert the object into a dict
site_paging_dict = site_paging_instance.to_dict()
# create an instance of SitePaging from a dict
site_paging_from_dict = SitePaging.from_dict(site_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


