# GroupMemberPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[GroupMemberEntry]**](GroupMemberEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.group_member_paging_list import GroupMemberPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberPagingList from a JSON string
group_member_paging_list_instance = GroupMemberPagingList.from_json(json)
# print the JSON string representation of the object
print(GroupMemberPagingList.to_json())

# convert the object into a dict
group_member_paging_list_dict = group_member_paging_list_instance.to_dict()
# create an instance of GroupMemberPagingList from a dict
group_member_paging_list_from_dict = GroupMemberPagingList.from_dict(group_member_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


