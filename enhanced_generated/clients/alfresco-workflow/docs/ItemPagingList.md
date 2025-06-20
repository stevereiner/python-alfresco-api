# ItemPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ItemEntry]**](ItemEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.item_paging_list import ItemPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPagingList from a JSON string
item_paging_list_instance = ItemPagingList.from_json(json)
# print the JSON string representation of the object
print(ItemPagingList.to_json())

# convert the object into a dict
item_paging_list_dict = item_paging_list_instance.to_dict()
# create an instance of ItemPagingList from a dict
item_paging_list_from_dict = ItemPagingList.from_dict(item_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


