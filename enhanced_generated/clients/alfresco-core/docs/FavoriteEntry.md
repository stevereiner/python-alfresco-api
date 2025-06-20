# FavoriteEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Favorite**](Favorite.md) |  | 

## Example

```python
from alfresco_core_client.models.favorite_entry import FavoriteEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteEntry from a JSON string
favorite_entry_instance = FavoriteEntry.from_json(json)
# print the JSON string representation of the object
print(FavoriteEntry.to_json())

# convert the object into a dict
favorite_entry_dict = favorite_entry_instance.to_dict()
# create an instance of FavoriteEntry from a dict
favorite_entry_from_dict = FavoriteEntry.from_dict(favorite_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


