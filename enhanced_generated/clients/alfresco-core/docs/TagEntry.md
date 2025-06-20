# TagEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Tag**](Tag.md) |  | 

## Example

```python
from alfresco_core_client.models.tag_entry import TagEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TagEntry from a JSON string
tag_entry_instance = TagEntry.from_json(json)
# print the JSON string representation of the object
print(TagEntry.to_json())

# convert the object into a dict
tag_entry_dict = tag_entry_instance.to_dict()
# create an instance of TagEntry from a dict
tag_entry_from_dict = TagEntry.from_dict(tag_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


