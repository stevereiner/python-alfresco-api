# GroupMemberPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**GroupMemberPagingList**](GroupMemberPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.group_member_paging import GroupMemberPaging

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberPaging from a JSON string
group_member_paging_instance = GroupMemberPaging.from_json(json)
# print the JSON string representation of the object
print(GroupMemberPaging.to_json())

# convert the object into a dict
group_member_paging_dict = group_member_paging_instance.to_dict()
# create an instance of GroupMemberPaging from a dict
group_member_paging_from_dict = GroupMemberPaging.from_dict(group_member_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


