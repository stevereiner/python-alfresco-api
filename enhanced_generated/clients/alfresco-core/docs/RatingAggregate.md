# RatingAggregate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **int** |  | [optional] 
**number_of_ratings** | **int** |  | [optional] 

## Example

```python
from alfresco_core_client.models.rating_aggregate import RatingAggregate

# TODO update the JSON string below
json = "{}"
# create an instance of RatingAggregate from a JSON string
rating_aggregate_instance = RatingAggregate.from_json(json)
# print the JSON string representation of the object
print(RatingAggregate.to_json())

# convert the object into a dict
rating_aggregate_dict = rating_aggregate_instance.to_dict()
# create an instance of RatingAggregate from a dict
rating_aggregate_from_dict = RatingAggregate.from_dict(rating_aggregate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


