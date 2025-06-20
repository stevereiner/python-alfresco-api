# GroupMemberEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**GroupMember**](GroupMember.md) |  | 

## Example

```python
from alfresco_core_client.models.group_member_entry import GroupMemberEntry

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberEntry from a JSON string
group_member_entry_instance = GroupMemberEntry.from_json(json)
# print the JSON string representation of the object
print(GroupMemberEntry.to_json())

# convert the object into a dict
group_member_entry_dict = group_member_entry_instance.to_dict()
# create an instance of GroupMemberEntry from a dict
group_member_entry_from_dict = GroupMemberEntry.from_dict(group_member_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


