# RequestScope

Scope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | **str** | The locations to include in the query  | [optional] 

## Example

```python
from alfresco_search_client.models.request_scope import RequestScope

# TODO update the JSON string below
json = "{}"
# create an instance of RequestScope from a JSON string
request_scope_instance = RequestScope.from_json(json)
# print the JSON string representation of the object
print(RequestScope.to_json())

# convert the object into a dict
request_scope_dict = request_scope_instance.to_dict()
# create an instance of RequestScope from a dict
request_scope_from_dict = RequestScope.from_dict(request_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


