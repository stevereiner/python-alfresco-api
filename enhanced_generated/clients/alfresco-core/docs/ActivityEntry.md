# ActivityEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Activity**](Activity.md) |  | 

## Example

```python
from alfresco_core_client.models.activity_entry import ActivityEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityEntry from a JSON string
activity_entry_instance = ActivityEntry.from_json(json)
# print the JSON string representation of the object
print(ActivityEntry.to_json())

# convert the object into a dict
activity_entry_dict = activity_entry_instance.to_dict()
# create an instance of ActivityEntry from a dict
activity_entry_from_dict = ActivityEntry.from_dict(activity_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


