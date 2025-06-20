# NodePagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[NodeEntry]**](NodeEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**source** | [**Node**](Node.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_paging_list import NodePagingList

# TODO update the JSON string below
json = "{}"
# create an instance of NodePagingList from a JSON string
node_paging_list_instance = NodePagingList.from_json(json)
# print the JSON string representation of the object
print(NodePagingList.to_json())

# convert the object into a dict
node_paging_list_dict = node_paging_list_instance.to_dict()
# create an instance of NodePagingList from a dict
node_paging_list_from_dict = NodePagingList.from_dict(node_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


