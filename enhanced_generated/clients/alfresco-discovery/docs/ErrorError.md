# ErrorError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brief_summary** | **str** |  | [optional] 
**description_url** | **str** |  | [optional] 
**error_key** | **str** |  | [optional] 
**log_id** | **str** |  | [optional] 
**stack_trace** | **str** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from alfresco_discovery_client.models.error_error import ErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorError from a JSON string
error_error_instance = ErrorError.from_json(json)
# print the JSON string representation of the object
print(ErrorError.to_json())

# convert the object into a dict
error_error_dict = error_error_instance.to_dict()
# create an instance of ErrorError from a dict
error_error_from_dict = ErrorError.from_dict(error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


