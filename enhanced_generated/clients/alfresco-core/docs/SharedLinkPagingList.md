# SharedLinkPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SharedLinkEntry]**](SharedLinkEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.shared_link_paging_list import SharedLinkPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SharedLinkPagingList from a JSON string
shared_link_paging_list_instance = SharedLinkPagingList.from_json(json)
# print the JSON string representation of the object
print(SharedLinkPagingList.to_json())

# convert the object into a dict
shared_link_paging_list_dict = shared_link_paging_list_instance.to_dict()
# create an instance of SharedLinkPagingList from a dict
shared_link_paging_list_from_dict = SharedLinkPagingList.from_dict(shared_link_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


