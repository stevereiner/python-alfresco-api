# VariablePagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[VariableEntry]**](VariableEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.variable_paging_list import VariablePagingList

# TODO update the JSON string below
json = "{}"
# create an instance of VariablePagingList from a JSON string
variable_paging_list_instance = VariablePagingList.from_json(json)
# print the JSON string representation of the object
print(VariablePagingList.to_json())

# convert the object into a dict
variable_paging_list_dict = variable_paging_list_instance.to_dict()
# create an instance of VariablePagingList from a dict
variable_paging_list_from_dict = VariablePagingList.from_dict(variable_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


