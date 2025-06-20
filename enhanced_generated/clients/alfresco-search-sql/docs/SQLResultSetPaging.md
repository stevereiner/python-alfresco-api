# SQLResultSetPaging

Query results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**SQLResultSetPagingList**](SQLResultSetPagingList.md) |  | [optional] 

## Example

```python
from alfresco_search_sql_client.models.sql_result_set_paging import SQLResultSetPaging

# TODO update the JSON string below
json = "{}"
# create an instance of SQLResultSetPaging from a JSON string
sql_result_set_paging_instance = SQLResultSetPaging.from_json(json)
# print the JSON string representation of the object
print(SQLResultSetPaging.to_json())

# convert the object into a dict
sql_result_set_paging_dict = sql_result_set_paging_instance.to_dict()
# create an instance of SQLResultSetPaging from a dict
sql_result_set_paging_from_dict = SQLResultSetPaging.from_dict(sql_result_set_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


