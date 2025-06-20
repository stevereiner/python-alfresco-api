# FavoritePaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**FavoritePagingList**](FavoritePagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.favorite_paging import FavoritePaging

# TODO update the JSON string below
json = "{}"
# create an instance of FavoritePaging from a JSON string
favorite_paging_instance = FavoritePaging.from_json(json)
# print the JSON string representation of the object
print(FavoritePaging.to_json())

# convert the object into a dict
favorite_paging_dict = favorite_paging_instance.to_dict()
# create an instance of FavoritePaging from a dict
favorite_paging_from_dict = FavoritePaging.from_dict(favorite_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


