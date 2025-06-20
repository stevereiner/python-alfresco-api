# CandidatePagingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[CandidateEntry]**](CandidateEntry.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.candidate_paging_list import CandidatePagingList

# TODO update the JSON string below
json = "{}"
# create an instance of CandidatePagingList from a JSON string
candidate_paging_list_instance = CandidatePagingList.from_json(json)
# print the JSON string representation of the object
print(CandidatePagingList.to_json())

# convert the object into a dict
candidate_paging_list_dict = candidate_paging_list_instance.to_dict()
# create an instance of CandidatePagingList from a dict
candidate_paging_list_from_dict = CandidatePagingList.from_dict(candidate_paging_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


