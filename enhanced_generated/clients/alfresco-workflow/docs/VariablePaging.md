# VariablePaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**VariablePagingList**](VariablePagingList.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.variable_paging import VariablePaging

# TODO update the JSON string below
json = "{}"
# create an instance of VariablePaging from a JSON string
variable_paging_instance = VariablePaging.from_json(json)
# print the JSON string representation of the object
print(VariablePaging.to_json())

# convert the object into a dict
variable_paging_dict = variable_paging_instance.to_dict()
# create an instance of VariablePaging from a dict
variable_paging_from_dict = VariablePaging.from_dict(variable_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


