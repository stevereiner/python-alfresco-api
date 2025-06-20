# DeletedNodeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**DeletedNode**](DeletedNode.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.deleted_node_entry import DeletedNodeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedNodeEntry from a JSON string
deleted_node_entry_instance = DeletedNodeEntry.from_json(json)
# print the JSON string representation of the object
print(DeletedNodeEntry.to_json())

# convert the object into a dict
deleted_node_entry_dict = deleted_node_entry_instance.to_dict()
# create an instance of DeletedNodeEntry from a dict
deleted_node_entry_from_dict = DeletedNodeEntry.from_dict(deleted_node_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


