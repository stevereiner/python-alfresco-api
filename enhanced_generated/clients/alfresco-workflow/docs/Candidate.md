# Candidate

A candidate item. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_id** | **str** |  | [optional] 
**candidate_type** | **str** |  | [optional] 

## Example

```python
from alfresco_workflow_client.models.candidate import Candidate

# TODO update the JSON string below
json = "{}"
# create an instance of Candidate from a JSON string
candidate_instance = Candidate.from_json(json)
# print the JSON string representation of the object
print(Candidate.to_json())

# convert the object into a dict
candidate_dict = candidate_instance.to_dict()
# create an instance of Candidate from a dict
candidate_from_dict = Candidate.from_dict(candidate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


