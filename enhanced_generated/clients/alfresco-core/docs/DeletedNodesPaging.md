# DeletedNodesPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**DeletedNodesPagingList**](DeletedNodesPagingList.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.deleted_nodes_paging import DeletedNodesPaging

# TODO update the JSON string below
json = "{}"
# create an instance of DeletedNodesPaging from a JSON string
deleted_nodes_paging_instance = DeletedNodesPaging.from_json(json)
# print the JSON string representation of the object
print(DeletedNodesPaging.to_json())

# convert the object into a dict
deleted_nodes_paging_dict = deleted_nodes_paging_instance.to_dict()
# create an instance of DeletedNodesPaging from a dict
deleted_nodes_paging_from_dict = DeletedNodesPaging.from_dict(deleted_nodes_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


