# NodeAssociationPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[NodeAssociationEntry]**](NodeAssociationEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**source** | [**Node**](Node.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_association_paging_list import NodeAssociationPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAssociationPagingList from a JSON string
node_association_paging_list_instance = NodeAssociationPagingList.from_json(json)
# print the JSON string representation of the object
print(NodeAssociationPagingList.to_json())

# convert the object into a dict
node_association_paging_list_dict = node_association_paging_list_instance.to_dict()
# create an instance of NodeAssociationPagingList from a dict
node_association_paging_list_from_dict = NodeAssociationPagingList.from_dict(node_association_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


