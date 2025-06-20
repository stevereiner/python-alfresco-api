# RatingPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**RatingPagingList**](RatingPagingList.md) |  | 

## Example

```python
from alfresco_core_client.models.rating_paging import RatingPaging

# TODO update the JSON string below
json = "{}"
# create an instance of RatingPaging from a JSON string
rating_paging_instance = RatingPaging.from_json(json)
# print the JSON string representation of the object
print(RatingPaging.to_json())

# convert the object into a dict
rating_paging_dict = rating_paging_instance.to_dict()
# create an instance of RatingPaging from a dict
rating_paging_from_dict = RatingPaging.from_dict(rating_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


