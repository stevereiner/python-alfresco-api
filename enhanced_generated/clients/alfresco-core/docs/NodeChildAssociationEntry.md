# NodeChildAssociationEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**NodeChildAssociation**](NodeChildAssociation.md) |  | 

## Example

```python
from alfresco_core_client.models.node_child_association_entry import NodeChildAssociationEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NodeChildAssociationEntry from a JSON string
node_child_association_entry_instance = NodeChildAssociationEntry.from_json(json)
# print the JSON string representation of the object
print(NodeChildAssociationEntry.to_json())

# convert the object into a dict
node_child_association_entry_dict = node_child_association_entry_instance.to_dict()
# create an instance of NodeChildAssociationEntry from a dict
node_child_association_entry_from_dict = NodeChildAssociationEntry.from_dict(node_child_association_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


