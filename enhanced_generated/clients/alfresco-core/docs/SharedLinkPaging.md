# SharedLinkPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**SharedLinkPagingList**](SharedLinkPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.shared_link_paging import SharedLinkPaging

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLinkPaging from a JSON string
shared_link_paging_instance = SharedLinkPaging.from_json(json)
# print the JSON string representation of the object
print(SharedLinkPaging.to_json())

# convert the object into a dict
shared_link_paging_dict = shared_link_paging_instance.to_dict()
# create an instance of SharedLinkPaging from a dict
shared_link_paging_from_dict = SharedLinkPaging.from_dict(shared_link_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


