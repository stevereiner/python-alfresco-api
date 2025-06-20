# NodeChildAssociationPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[NodeChildAssociationEntry]**](NodeChildAssociationEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**source** | [**Node**](Node.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_child_association_paging_list import NodeChildAssociationPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of NodeChildAssociationPagingList from a JSON string
node_child_association_paging_list_instance = NodeChildAssociationPagingList.from_json(json)
# print the JSON string representation of the object
print(NodeChildAssociationPagingList.to_json())

# convert the object into a dict
node_child_association_paging_list_dict = node_child_association_paging_list_instance.to_dict()
# create an instance of NodeChildAssociationPagingList from a dict
node_child_association_paging_list_from_dict = NodeChildAssociationPagingList.from_dict(node_child_association_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


