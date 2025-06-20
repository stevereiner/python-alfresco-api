# NodeAssociationPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**NodeAssociationPagingList**](NodeAssociationPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_association_paging import NodeAssociationPaging

# TODO update the JSON string below
json = "{}"
# create an instance of NodeAssociationPaging from a JSON string
node_association_paging_instance = NodeAssociationPaging.from_json(json)
# print the JSON string representation of the object
print(NodeAssociationPaging.to_json())

# convert the object into a dict
node_association_paging_dict = node_association_paging_instance.to_dict()
# create an instance of NodeAssociationPaging from a dict
node_association_paging_from_dict = NodeAssociationPaging.from_dict(node_association_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


