# RequestQuery

Query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The query language in which the query is written. | [optional] [default to 'afts']
**query** | **str** | The query which may have been generated in some way from the userQuery | 
**user_query** | **str** | The exact search request typed in by the user | [optional] 

## Example

```python
from alfresco_search_client.models.request_query import RequestQuery

# TODO update the JSON string below
json = "{}"
# create an instance of RequestQuery from a JSON string
request_query_instance = RequestQuery.from_json(json)
# print the JSON string representation of the object
print(RequestQuery.to_json())

# convert the object into a dict
request_query_dict = request_query_instance.to_dict()
# create an instance of RequestQuery from a dict
request_query_from_dict = RequestQuery.from_dict(request_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


