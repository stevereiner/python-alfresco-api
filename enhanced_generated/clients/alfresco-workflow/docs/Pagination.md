# Pagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of objects in the entries array.  | [optional] 
**has_more_items** | **bool** | A boolean value which is **true** if there are more entities in the collection beyond those in this response. A true value means a request with a larger value for the **skipCount** or the **maxItems** parameter will return more entities.  | [optional] 
**max_items** | **int** | The value of the **maxItems** parameter used to generate this list, or if there was no **maxItems** parameter the default value, 10  | [optional] 
**skip_count** | **int** | An integer describing how many entities exist in the collection before those included in this list.  | [optional] 
**total_items** | **int** | An integer describing the total number of entities in the collection. The API might not be able to determine this value, in which case this property will not be present.  | [optional] 

## Example

```python
from alfresco_workflow_client.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print(Pagination.to_json())

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_from_dict = Pagination.from_dict(pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


