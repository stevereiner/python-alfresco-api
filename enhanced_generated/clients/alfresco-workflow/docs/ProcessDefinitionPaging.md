# ProcessDefinitionPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ProcessDefinitionPagingList**](ProcessDefinitionPagingList.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.process_definition_paging import ProcessDefinitionPaging

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessDefinitionPaging from a JSON string
process_definition_paging_instance = ProcessDefinitionPaging.from_json(json)
# print the JSON string representation of the object
print(ProcessDefinitionPaging.to_json())

# convert the object into a dict
process_definition_paging_dict = process_definition_paging_instance.to_dict()
# create an instance of ProcessDefinitionPaging from a dict
process_definition_paging_from_dict = ProcessDefinitionPaging.from_dict(process_definition_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


