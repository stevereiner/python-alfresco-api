# GroupMembershipBodyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**member_type** | **str** |  | 

## Example

```python
from alfresco_core_client.models.group_membership_body_create import GroupMembershipBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembershipBodyCreate from a JSON string
group_membership_body_create_instance = GroupMembershipBodyCreate.from_json(json)
# print the JSON string representation of the object
print(GroupMembershipBodyCreate.to_json())

# convert the object into a dict
group_membership_body_create_dict = group_membership_body_create_instance.to_dict()
# create an instance of GroupMembershipBodyCreate from a dict
group_membership_body_create_from_dict = GroupMembershipBodyCreate.from_dict(group_membership_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


