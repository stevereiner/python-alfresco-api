# GroupBodyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | **str** |  | 
**parent_ids** | **List[str]** |  | [optional] 

## Example

```python
from alfresco_core_client.models.group_body_create import GroupBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupBodyCreate from a JSON string
group_body_create_instance = GroupBodyCreate.from_json(json)
# print the JSON string representation of the object
print(GroupBodyCreate.to_json())

# convert the object into a dict
group_body_create_dict = group_body_create_instance.to_dict()
# create an instance of GroupBodyCreate from a dict
group_body_create_from_dict = GroupBodyCreate.from_dict(group_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


