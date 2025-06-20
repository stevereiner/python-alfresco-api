# RatingPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[RatingEntry]**](RatingEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_core_client.models.rating_paging_list import RatingPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of RatingPagingList from a JSON string
rating_paging_list_instance = RatingPagingList.from_json(json)
# print the JSON string representation of the object
print(RatingPagingList.to_json())

# convert the object into a dict
rating_paging_list_dict = rating_paging_list_instance.to_dict()
# create an instance of RatingPagingList from a dict
rating_paging_list_from_dict = RatingPagingList.from_dict(rating_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


