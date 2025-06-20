# NodeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Node**](Node.md) |  | 

## Example

```python
from alfresco_core_client.models.node_entry import NodeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NodeEntry from a JSON string
node_entry_instance = NodeEntry.from_json(json)
# print the JSON string representation of the object
print(NodeEntry.to_json())

# convert the object into a dict
node_entry_dict = node_entry_instance.to_dict()
# create an instance of NodeEntry from a dict
node_entry_from_dict = NodeEntry.from_dict(node_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


