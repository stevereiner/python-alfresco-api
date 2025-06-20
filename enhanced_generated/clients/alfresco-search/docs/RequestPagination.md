# RequestPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_items** | **int** | The maximum number of items to return in the query results | [optional] [default to 100]
**skip_count** | **int** | The number of items to skip from the start of the query set | [optional] [default to 0]

## Example

```python
from alfresco_search_client.models.request_pagination import RequestPagination

# TODO update the JSON string below
json = "{}"
# create an instance of RequestPagination from a JSON string
request_pagination_instance = RequestPagination.from_json(json)
# print the JSON string representation of the object
print(RequestPagination.to_json())

# convert the object into a dict
request_pagination_dict = request_pagination_instance.to_dict()
# create an instance of RequestPagination from a dict
request_pagination_from_dict = RequestPagination.from_dict(request_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


