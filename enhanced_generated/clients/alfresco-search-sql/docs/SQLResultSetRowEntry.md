# SQLResultSetRowEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from alfresco_search_sql_client.models.sql_result_set_row_entry import SQLResultSetRowEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SQLResultSetRowEntry from a JSON string
sql_result_set_row_entry_instance = SQLResultSetRowEntry.from_json(json)
# print the JSON string representation of the object
print(SQLResultSetRowEntry.to_json())

# convert the object into a dict
sql_result_set_row_entry_dict = sql_result_set_row_entry_instance.to_dict()
# create an instance of SQLResultSetRowEntry from a dict
sql_result_set_row_entry_from_dict = SQLResultSetRowEntry.from_dict(sql_result_set_row_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


