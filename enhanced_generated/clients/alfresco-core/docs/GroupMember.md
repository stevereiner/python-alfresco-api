# GroupMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | **str** |  | 
**member_type** | **str** |  | 

## Example

```python
from alfresco_core_client.models.group_member import GroupMember

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMember from a JSON string
group_member_instance = GroupMember.from_json(json)
# print the JSON string representation of the object
print(GroupMember.to_json())

# convert the object into a dict
group_member_dict = group_member_instance.to_dict()
# create an instance of GroupMember from a dict
group_member_from_dict = GroupMember.from_dict(group_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


