# ProcessDefinitionPagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[ProcessDefinitionEntry]**](ProcessDefinitionEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.process_definition_paging_list import ProcessDefinitionPagingList

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessDefinitionPagingList from a JSON string
process_definition_paging_list_instance = ProcessDefinitionPagingList.from_json(json)
# print the JSON string representation of the object
print(ProcessDefinitionPagingList.to_json())

# convert the object into a dict
process_definition_paging_list_dict = process_definition_paging_list_instance.to_dict()
# create an instance of ProcessDefinitionPagingList from a dict
process_definition_paging_list_from_dict = ProcessDefinitionPagingList.from_dict(process_definition_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


