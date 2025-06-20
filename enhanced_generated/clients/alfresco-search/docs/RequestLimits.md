# RequestLimits

Limit the time and resources used for query execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission_evaluation_count** | **int** | Maximum count of post query permission evaluations | [optional] [default to 2000]
**permission_evaluation_time** | **int** | Maximum time for post query permission evaluation | [optional] [default to 20000]

## Example

```python
from alfresco_search_client.models.request_limits import RequestLimits

# TODO update the JSON string below
json = "{}"
# create an instance of RequestLimits from a JSON string
request_limits_instance = RequestLimits.from_json(json)
# print the JSON string representation of the object
print(RequestLimits.to_json())

# convert the object into a dict
request_limits_dict = request_limits_instance.to_dict()
# create an instance of RequestLimits from a dict
request_limits_from_dict = RequestLimits.from_dict(request_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


