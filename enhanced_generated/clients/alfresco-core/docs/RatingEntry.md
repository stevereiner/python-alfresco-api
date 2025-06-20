# RatingEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Rating**](Rating.md) |  | 

## Example

```python
from alfresco_core_client.models.rating_entry import RatingEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RatingEntry from a JSON string
rating_entry_instance = RatingEntry.from_json(json)
# print the JSON string representation of the object
print(RatingEntry.to_json())

# convert the object into a dict
rating_entry_dict = rating_entry_instance.to_dict()
# create an instance of RatingEntry from a dict
rating_entry_from_dict = RatingEntry.from_dict(rating_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


