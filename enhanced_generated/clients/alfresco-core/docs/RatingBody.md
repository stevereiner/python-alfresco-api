# RatingBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The rating scheme type. Possible values are likes and fiveStar. | [default to 'likes']
**my_rating** | **str** | The rating. The type is specific to the rating scheme, boolean for the likes and an integer for the fiveStar | 

## Example

```python
from alfresco_core_client.models.rating_body import RatingBody

# TODO update the JSON string below
json = "{}"
# create an instance of RatingBody from a JSON string
rating_body_instance = RatingBody.from_json(json)
# print the JSON string representation of the object
print(RatingBody.to_json())

# convert the object into a dict
rating_body_dict = rating_body_instance.to_dict()
# create an instance of RatingBody from a dict
rating_body_from_dict = RatingBody.from_dict(rating_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


