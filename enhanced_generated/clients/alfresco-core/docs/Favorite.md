# Favorite

A favorite describes an Alfresco entity that a person has marked as a favorite. The target can be a site, file or folder. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time the object was made a favorite. | [optional] 
**properties** | **object** | A subset of the target favorite properties, system properties and properties already available in the target are excluded. | [optional] 
**target** | **object** |  | 
**target_guid** | **str** | The guid of the object that is a favorite. | 

## Example

```python
from alfresco_core_client.models.favorite import Favorite

# TODO update the JSON string below
json = "{}"
# create an instance of Favorite from a JSON string
favorite_instance = Favorite.from_json(json)
# print the JSON string representation of the object
print(Favorite.to_json())

# convert the object into a dict
favorite_dict = favorite_instance.to_dict()
# create an instance of Favorite from a dict
favorite_from_dict = Favorite.from_dict(favorite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


