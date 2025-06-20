# FavoritePagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[FavoriteEntry]**](FavoriteEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.favorite_paging_list import FavoritePagingList

# TODO update the JSON string below
json = "{}"
# create an instance of FavoritePagingList from a JSON string
favorite_paging_list_instance = FavoritePagingList.from_json(json)
# print the JSON string representation of the object
print(FavoritePagingList.to_json())

# convert the object into a dict
favorite_paging_list_dict = favorite_paging_list_instance.to_dict()
# create an instance of FavoritePagingList from a dict
favorite_paging_list_from_dict = FavoritePagingList.from_dict(favorite_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


