# ProcessPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**ProcessPagingList**](ProcessPagingList.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.process_paging import ProcessPaging

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessPaging from a JSON string
process_paging_instance = ProcessPaging.from_json(json)
# print the JSON string representation of the object
print(ProcessPaging.to_json())

# convert the object into a dict
process_paging_dict = process_paging_instance.to_dict()
# create an instance of ProcessPaging from a dict
process_paging_from_dict = ProcessPaging.from_dict(process_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


