# FavoriteSiteEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**FavoriteSite**](FavoriteSite.md) |  | 

## Example

```python
from alfresco_core_client.models.favorite_site_entry import FavoriteSiteEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteSiteEntry from a JSON string
favorite_site_entry_instance = FavoriteSiteEntry.from_json(json)
# print the JSON string representation of the object
print(FavoriteSiteEntry.to_json())

# convert the object into a dict
favorite_site_entry_dict = favorite_site_entry_instance.to_dict()
# create an instance of FavoriteSiteEntry from a dict
favorite_site_entry_from_dict = FavoriteSiteEntry.from_dict(favorite_site_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


