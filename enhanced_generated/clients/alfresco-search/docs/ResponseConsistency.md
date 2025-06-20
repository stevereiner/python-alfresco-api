# ResponseConsistency

The consistency state of the index used to execute the query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_tx_id** | **int** | The id of the last indexed transaction | [optional] 

## Example

```python
from alfresco_search_client.models.response_consistency import ResponseConsistency

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseConsistency from a JSON string
response_consistency_instance = ResponseConsistency.from_json(json)
# print the JSON string representation of the object
print(ResponseConsistency.to_json())

# convert the object into a dict
response_consistency_dict = response_consistency_instance.to_dict()
# create an instance of ResponseConsistency from a dict
response_consistency_from_dict = ResponseConsistency.from_dict(response_consistency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


