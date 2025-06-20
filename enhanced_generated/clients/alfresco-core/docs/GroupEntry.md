# GroupEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Group**](Group.md) |  | 

## Example

```python
from alfresco_core_client.models.group_entry import GroupEntry

# TODO update the JSON string below
json = "{}"
# create an instance of GroupEntry from a JSON string
group_entry_instance = GroupEntry.from_json(json)
# print the JSON string representation of the object
print(GroupEntry.to_json())

# convert the object into a dict
group_entry_dict = group_entry_instance.to_dict()
# create an instance of GroupEntry from a dict
group_entry_from_dict = GroupEntry.from_dict(group_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


