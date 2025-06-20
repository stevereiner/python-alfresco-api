# ItemPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ItemPagingList**](ItemPagingList.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.item_paging import ItemPaging

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPaging from a JSON string
item_paging_instance = ItemPaging.from_json(json)
# print the JSON string representation of the object
print(ItemPaging.to_json())

# convert the object into a dict
item_paging_dict = item_paging_instance.to_dict()
# create an instance of ItemPaging from a dict
item_paging_from_dict = ItemPaging.from_dict(item_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


