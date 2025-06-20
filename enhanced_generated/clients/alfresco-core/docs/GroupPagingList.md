# GroupPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[GroupEntry]**](GroupEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.group_paging_list import GroupPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPagingList from a JSON string
group_paging_list_instance = GroupPagingList.from_json(json)
# print the JSON string representation of the object
print(GroupPagingList.to_json())

# convert the object into a dict
group_paging_list_dict = group_paging_list_instance.to_dict()
# create an instance of GroupPagingList from a dict
group_paging_list_from_dict = GroupPagingList.from_dict(group_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


