# CandidatePaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | [**CandidatePagingList**](CandidatePagingList.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.candidate_paging import CandidatePaging

# TODO update the JSON string below
json = "{}"
# create an instance of CandidatePaging from a JSON string
candidate_paging_instance = CandidatePaging.from_json(json)
# print the JSON string representation of the object
print(CandidatePaging.to_json())

# convert the object into a dict
candidate_paging_dict = candidate_paging_instance.to_dict()
# create an instance of CandidatePaging from a dict
candidate_paging_from_dict = CandidatePaging.from_dict(candidate_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


