# TagPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[TagEntry]**](TagEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.tag_paging_list import TagPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of TagPagingList from a JSON string
tag_paging_list_instance = TagPagingList.from_json(json)
# print the JSON string representation of the object
print(TagPagingList.to_json())

# convert the object into a dict
tag_paging_list_dict = tag_paging_list_instance.to_dict()
# create an instance of TagPagingList from a dict
tag_paging_list_from_dict = TagPagingList.from_dict(tag_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


