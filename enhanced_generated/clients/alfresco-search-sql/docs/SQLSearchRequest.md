# SQLSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_queries** | **List[str]** |  | [optional] 
**format** | **str** |  | [optional] 
**include_metadata** | **bool** |  | [optional] 
**locales** | **List[str]** |  | [optional] 
**stmt** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from alfresco_search_sql_client.models.sql_search_request import SQLSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SQLSearchRequest from a JSON string
sql_search_request_instance = SQLSearchRequest.from_json(json)
# print the JSON string representation of the object
print(SQLSearchRequest.to_json())

# convert the object into a dict
sql_search_request_dict = sql_search_request_instance.to_dict()
# create an instance of SQLSearchRequest from a dict
sql_search_request_from_dict = SQLSearchRequest.from_dict(sql_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


