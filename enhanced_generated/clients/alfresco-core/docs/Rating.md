# Rating

A person can rate an item of content by liking it. They can also remove their like of an item of content. API methods exist to get a list of ratings and to add a new rating. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate** | [**RatingAggregate**](RatingAggregate.md) |  | 
**id** | **str** |  | 
**my_rating** | **str** | The rating. The type is specific to the rating scheme, boolean for the likes and an integer for the fiveStar. | [optional] 
**rated_at** | **datetime** |  | [optional] 

## Example

```python
from alfresco_core_client.models.rating import Rating

# TODO update the JSON string below
json = "{}"
# create an instance of Rating from a JSON string
rating_instance = Rating.from_json(json)
# print the JSON string representation of the object
print(Rating.to_json())

# convert the object into a dict
rating_dict = rating_instance.to_dict()
# create an instance of Rating from a dict
rating_from_dict = Rating.from_dict(rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


