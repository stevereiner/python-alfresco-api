# NodePaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**NodePagingList**](NodePagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.node_paging import NodePaging

# TODO update the JSON string below
json = "{}"
# create an instance of NodePaging from a JSON string
node_paging_instance = NodePaging.from_json(json)
# print the JSON string representation of the object
print(NodePaging.to_json())

# convert the object into a dict
node_paging_dict = node_paging_instance.to_dict()
# create an instance of NodePaging from a dict
node_paging_from_dict = NodePaging.from_dict(node_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


