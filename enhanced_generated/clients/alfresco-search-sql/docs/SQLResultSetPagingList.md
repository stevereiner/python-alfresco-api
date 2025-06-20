# SQLResultSetPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SQLResultSetRowEntry]**](SQLResultSetRowEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_search_sql_client.models.sql_result_set_paging_list import SQLResultSetPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of SQLResultSetPagingList from a JSON string
sql_result_set_paging_list_instance = SQLResultSetPagingList.from_json(json)
# print the JSON string representation of the object
print(SQLResultSetPagingList.to_json())

# convert the object into a dict
sql_result_set_paging_list_dict = sql_result_set_paging_list_instance.to_dict()
# create an instance of SQLResultSetPagingList from a dict
sql_result_set_paging_list_from_dict = SQLResultSetPagingList.from_dict(sql_result_set_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


