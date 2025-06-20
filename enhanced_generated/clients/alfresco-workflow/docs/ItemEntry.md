# ItemEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Item**](Item.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.item_entry import ItemEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ItemEntry from a JSON string
item_entry_instance = ItemEntry.from_json(json)
# print the JSON string representation of the object
print(ItemEntry.to_json())

# convert the object into a dict
item_entry_dict = item_entry_instance.to_dict()
# create an instance of ItemEntry from a dict
item_entry_from_dict = ItemEntry.from_dict(item_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


