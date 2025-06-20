# CandidateEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Candidate**](Candidate.md) |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.candidate_entry import CandidateEntry

# TODO update the JSON string below
json = "{}"
# create an instance of CandidateEntry from a JSON string
candidate_entry_instance = CandidateEntry.from_json(json)
# print the JSON string representation of the object
print(CandidateEntry.to_json())

# convert the object into a dict
candidate_entry_dict = candidate_entry_instance.to_dict()
# create an instance of CandidateEntry from a dict
candidate_entry_from_dict = CandidateEntry.from_dict(candidate_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


