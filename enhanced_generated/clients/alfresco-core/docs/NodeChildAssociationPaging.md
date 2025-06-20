# NodeChildAssociationPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**NodeChildAssociationPagingList**](NodeChildAssociationPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_child_association_paging import NodeChildAssociationPaging

# TODO update the JSON string below
json = "{}"
# create an instance of NodeChildAssociationPaging from a JSON string
node_child_association_paging_instance = NodeChildAssociationPaging.from_json(json)
# print the JSON string representation of the object
print(NodeChildAssociationPaging.to_json())

# convert the object into a dict
node_child_association_paging_dict = node_child_association_paging_instance.to_dict()
# create an instance of NodeChildAssociationPaging from a dict
node_child_association_paging_from_dict = NodeChildAssociationPaging.from_dict(node_child_association_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


