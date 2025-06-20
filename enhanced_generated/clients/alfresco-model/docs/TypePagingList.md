# TypePagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[TypeEntry]**](TypeEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_model_client.models.type_paging_list import TypePagingList

# TODO update the JSON string below
json = "{}"
# create an instance of TypePagingList from a JSON string
type_paging_list_instance = TypePagingList.from_json(json)
# print the JSON string representation of the object
print(TypePagingList.to_json())

# convert the object into a dict
type_paging_list_dict = type_paging_list_instance.to_dict()
# create an instance of TypePagingList from a dict
type_paging_list_from_dict = TypePagingList.from_dict(type_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


